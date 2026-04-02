#!/usr/bin/env python3
"""
Oracle Simphony BI API — Authentication helper.
Handles OpenID Connect with PKCE flow and token refresh.
Stores tokens in a local file (gitignored).
"""

import base64
import hashlib
import json
import os
import secrets
import sys
import time

try:
    import requests
except ImportError:
    print("ERROR: requests package not installed. Run: pip install requests")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

TOKEN_FILE = os.path.join(os.path.dirname(__file__), ".tokens.json")

REQUIRED_ENV = {
    "SIMPHONY_AUTH_HOST": "Authentication server URL (e.g., https://yourdomain-idm.oracleindustry.com)",
    "SIMPHONY_CLIENT_ID": "Client ID from API account",
    "SIMPHONY_USERNAME": "API account username",
    "SIMPHONY_PASSWORD": "API account password",
    "SIMPHONY_ORG": "Organization short name",
}


def check_env():
    missing = []
    for key, desc in REQUIRED_ENV.items():
        if not os.getenv(key):
            missing.append(f"  {key} — {desc}")
    if missing:
        print("ERROR: Missing environment variables in .env:")
        for m in missing:
            print(m)
        sys.exit(1)


def generate_pkce():
    """Generate PKCE code_verifier and code_challenge."""
    code_verifier_bytes = secrets.token_bytes(32)
    code_verifier = base64.urlsafe_b64encode(code_verifier_bytes).rstrip(b"=").decode("ascii")

    challenge_digest = hashlib.sha256(code_verifier.encode("ascii")).digest()
    code_challenge = base64.urlsafe_b64encode(challenge_digest).rstrip(b"=").decode("ascii")

    return code_verifier, code_challenge


def authorize(auth_host, client_id, code_challenge):
    """Step 1: Get authorization cookies."""
    url = f"{auth_host}/oidc-provider/v1/oauth2/authorize"
    params = {
        "response_type": "code",
        "client_id": client_id,
        "scope": "openid",
        "redirect_uri": "apiaccount://callback",
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
    }
    session = requests.Session()
    resp = session.get(url, params=params, allow_redirects=False)
    if resp.status_code not in (200, 302):
        print(f"ERROR: Authorization failed with status {resp.status_code}")
        print(resp.text[:500])
        sys.exit(1)
    return session


def sign_in(session, auth_host, username, password, orgname):
    """Step 2: Sign in with API account credentials."""
    url = f"{auth_host}/oidc-provider/v1/oauth2/signin"
    data = {
        "username": username,
        "password": password,
        "orgname": orgname,
    }
    resp = session.post(url, data=data)
    if resp.status_code != 200:
        print(f"ERROR: Sign-in failed with status {resp.status_code}")
        print(resp.text[:500])
        sys.exit(1)

    result = resp.json()
    if not result.get("success"):
        print(f"ERROR: Sign-in failed: {result}")
        sys.exit(1)

    redirect_url = result.get("redirectUrl", "")
    if "code=" not in redirect_url:
        print(f"ERROR: No auth code in redirect: {redirect_url}")
        sys.exit(1)

    auth_code = redirect_url.split("code=")[1].split("&")[0]
    return auth_code


def get_tokens(auth_host, client_id, code_verifier, auth_code):
    """Step 3: Exchange auth code for tokens."""
    url = f"{auth_host}/oidc-provider/v1/oauth2/token"
    data = {
        "scope": "openid",
        "grant_type": "authorization_code",
        "client_id": client_id,
        "code_verifier": code_verifier,
        "code": auth_code,
        "redirect_uri": "apiaccount://callback",
    }
    resp = requests.post(url, data=data)
    if resp.status_code != 200:
        print(f"ERROR: Token request failed with status {resp.status_code}")
        print(resp.text[:500])
        sys.exit(1)

    tokens = resp.json()
    if "id_token" not in tokens:
        print(f"ERROR: No id_token in response: {tokens}")
        sys.exit(1)

    return tokens


def refresh_tokens(auth_host, client_id, refresh_token):
    """Refresh tokens using refresh_token."""
    url = f"{auth_host}/oidc-provider/v1/oauth2/token"
    data = {
        "scope": "openid",
        "grant_type": "refresh_token",
        "client_id": client_id,
        "refresh_token": refresh_token,
        "redirect_uri": "apiaccount://callback",
    }
    resp = requests.post(url, data=data)
    if resp.status_code != 200:
        print(f"ERROR: Token refresh failed with status {resp.status_code}")
        print(resp.text[:500])
        return None

    tokens = resp.json()
    if "id_token" not in tokens:
        print(f"ERROR: No id_token in refresh response: {tokens}")
        return None

    return tokens


def save_tokens(tokens):
    """Save tokens to local file."""
    token_data = {
        "id_token": tokens.get("id_token"),
        "refresh_token": tokens.get("refresh_token"),
        "expires_in": tokens.get("expires_in"),
        "saved_at": int(time.time()),
    }
    with open(TOKEN_FILE, "w") as f:
        json.dump(token_data, f, indent=2)
    print(f"Tokens saved to {TOKEN_FILE}")


def load_tokens():
    """Load tokens from local file."""
    if not os.path.exists(TOKEN_FILE):
        return None
    with open(TOKEN_FILE, "r") as f:
        return json.load(f)


def get_valid_token():
    """Get a valid id_token, refreshing if needed."""
    check_env()
    tokens = load_tokens()

    if not tokens:
        print("No saved tokens. Run: python simphony_auth.py setup")
        sys.exit(1)

    saved_at = tokens.get("saved_at", 0)
    expires_in = int(tokens.get("expires_in", 1209600))  # 14 days default
    age = int(time.time()) - saved_at

    # Refresh if older than 10 days (tokens last 14 days)
    if age > 10 * 86400:
        print("Token aging — refreshing...", file=sys.stderr)
        auth_host = os.getenv("SIMPHONY_AUTH_HOST")
        client_id = os.getenv("SIMPHONY_CLIENT_ID")
        new_tokens = refresh_tokens(auth_host, client_id, tokens["refresh_token"])
        if new_tokens:
            save_tokens(new_tokens)
            return new_tokens["id_token"]
        else:
            print("Refresh failed. Run: python simphony_auth.py setup")
            sys.exit(1)

    return tokens["id_token"]


def cmd_setup():
    """Full authentication flow."""
    check_env()
    auth_host = os.getenv("SIMPHONY_AUTH_HOST")
    client_id = os.getenv("SIMPHONY_CLIENT_ID")
    username = os.getenv("SIMPHONY_USERNAME")
    password = os.getenv("SIMPHONY_PASSWORD")
    orgname = os.getenv("SIMPHONY_ORG")

    print("Starting Simphony BI API authentication...")
    print(f"  Auth host: {auth_host}")
    print(f"  Client ID: {client_id[:8]}...")
    print(f"  Org: {orgname}")

    # PKCE
    code_verifier, code_challenge = generate_pkce()
    print("  Generated PKCE challenge")

    # Authorize
    session = authorize(auth_host, client_id, code_challenge)
    print("  Authorization successful")

    # Sign in
    auth_code = sign_in(session, auth_host, username, password, orgname)
    print("  Sign-in successful")

    # Get tokens
    tokens = get_tokens(auth_host, client_id, code_verifier, auth_code)
    print("  Tokens received")

    # Save
    save_tokens(tokens)
    expires_days = int(tokens.get("expires_in", 1209600)) // 86400
    print(f"\nSUCCESS: Authenticated. Token valid for {expires_days} days.")
    print("The token will auto-refresh when used by simphony.py.")


def cmd_refresh():
    """Refresh tokens manually."""
    check_env()
    tokens = load_tokens()
    if not tokens:
        print("No saved tokens. Run: python simphony_auth.py setup")
        sys.exit(1)

    auth_host = os.getenv("SIMPHONY_AUTH_HOST")
    client_id = os.getenv("SIMPHONY_CLIENT_ID")

    print("Refreshing tokens...")
    new_tokens = refresh_tokens(auth_host, client_id, tokens["refresh_token"])
    if new_tokens:
        save_tokens(new_tokens)
        print("SUCCESS: Tokens refreshed.")
    else:
        print("FAILED: Run setup again.")
        sys.exit(1)


def cmd_status():
    """Check token status."""
    tokens = load_tokens()
    if not tokens:
        print("Status: No tokens. Run: python simphony_auth.py setup")
        return

    saved_at = tokens.get("saved_at", 0)
    expires_in = int(tokens.get("expires_in", 1209600))
    age = int(time.time()) - saved_at
    remaining = expires_in - age

    if remaining <= 0:
        print("Status: EXPIRED. Run: python simphony_auth.py setup")
    elif remaining < 3 * 86400:
        print(f"Status: Expiring soon ({remaining // 86400} days left). Consider refreshing.")
    else:
        print(f"Status: Valid ({remaining // 86400} days remaining)")


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Simphony BI API authentication helper",
        epilog="""
Commands:
  setup    Full authentication flow (run first time or when tokens expire)
  refresh  Refresh tokens manually
  status   Check token status

Environment variables (in .env):
  SIMPHONY_AUTH_HOST  Authentication server URL
  SIMPHONY_CLIENT_ID  Client ID from API account
  SIMPHONY_USERNAME   API account username
  SIMPHONY_PASSWORD   API account password
  SIMPHONY_ORG        Organization short name
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("command", nargs="?", default="status",
                        choices=["setup", "refresh", "status"],
                        help="Command to run (default: status)")
    args = parser.parse_args()

    if args.command == "setup":
        cmd_setup()
    elif args.command == "refresh":
        cmd_refresh()
    else:
        cmd_status()


if __name__ == "__main__":
    main()
