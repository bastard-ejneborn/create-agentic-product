# Runbook: Add User to Restaurant Shared Mailbox (Override)
> Status: **DRAFT** — needs full documentation
> Owner: André Ejneborn
> Last updated: 2026-04-09

## Purpose

Add a specific user (who is not part of the restaurant team) to a restaurant's shared mailbox. This is used when someone needs temporary or permanent access to a restaurant mailbox they don't normally have access to (e.g., covering for another location, district manager needing access, incident support).

## When to Use

- A user needs access to a restaurant mailbox they are not assigned to
- Temporary coverage (e.g., substitute RM for another location)
- District/Regional managers needing mailbox access for specific restaurants
- Support tickets requiring mailbox access (reference INC ticket number)

## Steps

### 1. Log in to Azure Portal
- Go to [portal.azure.com](https://portal.azure.com)
- Sign in with an admin account that has access to the Automation Account

### 2. Navigate to Automation Account
- Find the Automation Account: **`aa-bb-group-sync-prod`**
- Path: Azure Portal → Automation Accounts → `aa-bb-group-sync-prod`

### 3. Open the Variable
- Go to **Variables** (under Shared Resources)
- Open: **`SBX_MailboxOverridesJson`**

### 4. Edit the JSON

**To add a user** — add a new entry to the `"overrides"` array:

**To remove an override** — delete the entire JSON block for that user from the array. Save. The next hourly run will revoke the access automatically (since the user no longer appears in the desired state).

**Add entry format**:

```json
{
  "user": "firstname.lastname@bastardburgers.se",
  "offices": ["Restaurant Name"],
  "action": "add",
  "validFrom": "",
  "validTo": "",
  "reason": "Description of why access is needed (include INC ticket# if applicable)"
}
```

**Field reference:**
| Field | Description | Example |
|-------|-------------|---------|
| `user` | Email address of the user | `"minna.kiira-nymark@bastardburgers.se"` |
| `offices` | Array of restaurant names (can be multiple) | `["Solli", "Torggata"]` |
| `action` | Always `"add"` for granting access | `"add"` |
| `validFrom` | Start date (currently not used — leave empty) | `""` |
| `validTo` | End date (currently not used — leave empty) | `""` |
| `reason` | Why this override exists — include INC# if applicable | `"Bistår för närliggande enhet (Eskilstuna)"` |

### 5. Save
- Save the updated variable string

### 6. Wait for Automation
- The automation runs **every hour**
- The override will be applied at the next hourly run
- Verify access after ~1 hour

## Example: Current Overrides

```json
{
  "overrides": [
    {
      "user": "sebastian@bastardburgers.se",
      "offices": ["Eskilstuna"],
      "action": "add",
      "reason": "Bistår för närliggande enhet (Eskilstuna)"
    },
    {
      "user": "minna.kiira-nymark@bastardburgers.se",
      "offices": ["Mikonkatu"],
      "action": "add",
      "reason": "Behöver åtkomst till restaurang-brevlådan #INC-20977"
    },
    {
      "user": "minna.kiira-nymark@bastardburgers.se",
      "offices": ["Kamppi"],
      "action": "add",
      "reason": "Behöver åtkomst till restaurang-brevlådan under start"
    },
    {
      "user": "linda.estola@bastardburgers.se",
      "offices": ["Kamppi"],
      "action": "add",
      "reason": "Behöver åtkomst till restaurang-brevlådan #INC-23156"
    },
    {
      "user": "hannes@bastardburgers.se",
      "offices": ["Birger Jarlsgatan"],
      "action": "add",
      "reason": "Vikarierande RM för Birger Jarlsgatan"
    },
    {
      "user": "fred.page@bastardburgers.se",
      "offices": ["Gullmarsplan"],
      "action": "add",
      "reason": "Bistår för närliggande enhet (Gullmarsplan)"
    },
    {
      "user": "md.oliullah@bastardburgers.se",
      "offices": ["Karlstad City"],
      "action": "add",
      "reason": "Bistår för närliggande enhet (Karlstad City)"
    },
    {
      "user": "sakawat@bastardburgers.se",
      "offices": ["Karlstad"],
      "action": "add",
      "reason": "Bistår för närliggande enhet (Karlstad City)"
    },
    {
      "user": "ellinor.fagervall@bastardburgers.se",
      "offices": ["Luleå Shopping"],
      "action": "add",
      "reason": "Bistår för närliggande enhet (Luleå Shopping)"
    },
    {
      "user": "fredrik@bastardburgers.se",
      "offices": ["Solli", "Torggata"],
      "action": "add",
      "reason": "Bistår för närliggande enhet (Solli+Torggata)"
    },
    {
      "user": "abbas.tammelin@bastardburgers.se",
      "offices": ["Sofia"],
      "action": "add",
      "reason": "Bistår för närliggande enhet (Sofia)"
    }
  ]
}
```

## Automation Details

| Setting | Value |
|---------|-------|
| Automation Account | `aa-bb-group-sync-prod` |
| Runbook name | `UpdateSharedRestaurantMailboxes` |
| Variables read | `SBX_LocationToMailboxJson` (office→SMTP mapping), `SBX_MailboxOverridesJson` (overrides) |
| Schedule | Every hour |
| Auth | Managed Identity (system-assigned) — Microsoft Graph + Exchange Online |
| Tenant | `bastardburgerssweden.onmicrosoft.com` |
| Location | Azure Portal → Automation Accounts → `aa-bb-group-sync-prod` → Runbooks → `UpdateSharedRestaurantMailboxes` |

### How the Runbook Works

The `UpdateSharedRestaurantMailboxes` runbook performs **attribute-based delegation** to Exchange Online shared mailboxes. It grants **FullAccess + SendAs** permissions based on user attributes in Entra ID.

**Base rule** (automatic — no override needed):
```
IF   user.JobTitle ∈ {"Restaurant Manager", "Assistant restaurant manager"}
AND  user.Department = "Restaurants"
AND  user.OfficeLocation = <restaurant name>
THEN grant FullAccess + SendAs on the shared mailbox for that restaurant
```

This means RM and ARM automatically get access to their restaurant's shared mailbox based on their Entra ID profile — no manual action needed.

**Override rule** (the manual process documented above):
The `SBX_MailboxOverridesJson` variable adds exceptions to the base rule:
- `"action": "add"` — grant access to a user who doesn't match the base rule
- `"action": "exclude"` — revoke access from a user who would normally match
- `validFrom` / `validTo` — optional date-bounded overrides (functional — the runbook checks these dates)

**Processing flow**:
1. Connect to Microsoft Graph (Managed Identity) and Exchange Online
2. Query all users where Department="Restaurants" AND Title∈{RM, ARM} AND OfficeLocation is set
3. Build a plan: for each restaurant mailbox, list desired users (from base rule)
4. Apply overrides from `SBX_MailboxOverridesJson` (add/exclude, respecting date bounds)
5. Compare desired state vs. current permissions on each shared mailbox
6. Calculate delta: who to add, who to remove
7. Apply changes (FullAccess + SendAs) — or log only if DryRun mode
8. Output structured JSON logs per mailbox for audit

**Key behaviors**:
- **Declarative**: The runbook computes the full desired state and reconciles — it both adds AND removes permissions
- **Automapping**: Outlook automapping is enabled on FullAccess grants (mailbox auto-appears in Outlook)
- **System protection**: NT AUTHORITY\SELF and raw SIDs are never touched
- **DryRun mode**: Can be run with `-DryRun $true` to log what would change without applying
- **Single office mode**: Can be scoped to one restaurant with `-OnlyOffice "Restaurant Name"`

### Two Automation Variables

| Variable | Purpose | Format |
|----------|---------|--------|
| `SBX_LocationToMailboxJson` | Maps office/restaurant names to shared mailbox SMTP addresses | See full mapping below |
| `SBX_MailboxOverridesJson` | Manual overrides (add/exclude users) | See override JSON format above |

### Full Office → Mailbox Mapping (SBX_LocationToMailboxJson)

73 restaurants mapped:

| Office (OfficeLocation in Entra) | Shared Mailbox |
|----------------------------------|---------------|
| Alvik | alvik@bastardburgers.se |
| Barkarbystaden | barkarbystaden@bastardburgers.se |
| Birger Jarlsgatan | birgerjarlsgatan@bastardburgers.se |
| Birkastan | birkastan@bastardburgers.se |
| Boden | boden@bastardburgers.se |
| Borås | boras@bastardburgers.se |
| Emporia | emporia@bastardburgers.se |
| Eskilstuna | eskilstuna@bastardburgers.se |
| Etage | etage@bastardburgers.se |
| Falun | falun@bastardburgers.se |
| Farsta | farsta@bastardburgers.se |
| Frölunda | frolunda@bastardburgers.se |
| Gallerian | gallerian@bastardburgers.se |
| Grand Samarkand | grandsamarkand@bastardburgers.se |
| Gränby | granby@bastardburgers.se |
| Gullmarsplan | gullmarsplan@bastardburgers.se |
| Hagastaden | hagastaden@bastardburgers.se |
| Halmstad | halmstad@bastardburgers.se |
| Hammarby Sjöstad | hammarbysjostad@bastardburgers.se |
| Helsingborg | helsingborg@bastardburgers.se |
| Helsingborg City | helsingborgcity@bastardburgers.se |
| Helsingborg Väla | vala@bastardburgers.se |
| Helsinki Airport | helsinkiairport@bastardburgers.se |
| Hötorget | hotorget@bastardburgers.se |
| Jönköping | jonkoping@bastardburgers.se |
| Kalmar | kalmar@bastardburgers.se |
| Kamppi | kamppi@bastardburgers.**fi** |
| Karlskrona | karlskrona@bastardburgers.se |
| Karlstad | karlstad@bastardburgers.se |
| Karlstad City | karlstadcity@bastardburgers.se |
| Kungsholmen | kungsholmen@bastardburgers.se |
| Kungsmässan | kungsmassan@bastardburgers.se |
| Kungälv | kongahalla@bastardburgers.se |
| Liljeholmen | liljeholmen@bastardburgers.se |
| Linköping | linkoping@bastardburgers.se |
| Luleå | lulea@bastardburgers.se |
| Luleå Shopping | shopping@bastardburgers.se |
| Malmö | malmo@bastardburgers.se |
| Marieberg | marieberg@bastardburgers.se |
| Medborgarplatsen | medborgarplatsen@bastardburgers.se |
| Mikonkatu | mikonkatu@bastardburgers.se |
| Mobilia | mobilia@bastardburgers.se |
| Mölndal | molndal@bastardburgers.se |
| Norrköping | norrkoping@bastardburgers.se |
| Norrlandsgatan | norrlandsgatan@bastardburgers.se |
| Nova Lund | novalund@bastardburgers.se |
| Nyköping | nykoping@bastardburgers.se |
| Piteå | pitea@bastardburgers.se |
| Sickla | sickla@bastardburgers.se |
| Skellefteå | skelleftea@bastardburgers.se |
| Skövde | skovde@bastardburgers.se |
| Sofia | sofia@bastardburgers.se |
| Sollentuna | sollentuna@bastardburgers.se |
| Solli | solli@bastardburgers.se |
| Solna | solna@bastardburgers.se |
| St Paul | stpauls@bastardburgers.se |
| Sundsvall | sundsvall@bastardburgers.se |
| Södra Larmgatan | goteborgsodra@bastardburgers.se |
| Torggata | torggata@bastardburgers.se |
| Torp | torp@bastardburgers.se |
| Täby | taby@bastardburgers.se |
| Umeå | umea@bastardburgers.se |
| Uppsala | uppsala@bastardburgers.se |
| Varberg | varberg@bastardburgers.se |
| Vasastan | vasastan@bastardburgers.se |
| Värmdö | varmdo@bastardburgers.se |
| Väsby | vasby@bastardburgers.se |
| Västermalm | vastermalm@bastardburgers.se |
| Västerås | vasteras@bastardburgers.se |
| Växjö | vaxjo@bastardburgers.se |
| Örebro | orebro@bastardburgers.se |
| Östersund | ostersund@bastardburgers.se |
| Östra Hamngatan | goteborgostra@bastardburgers.se |

**Notes**:
- Kamppi uses **bastardburgers.fi** domain (Finland) — all others use bastardburgers.se
- Kungälv maps to `kongahalla@` (historical name)
- Luleå Shopping maps to `shopping@` (not `luleashopping@`)
- Helsingborg Väla maps to `vala@`
- Södra Larmgatan maps to `goteborgsodra@`
- Östra Hamngatan maps to `goteborgostra@`
- Helsinki Airport and Mikonkatu use bastardburgers.se (not .fi) — only Kamppi uses .fi

---

## Important Notes

- The `offices` value must match the **exact restaurant name** as configured in the system
- Multiple offices can be assigned to one user (see `fredrik@` example with Solli + Torggata)
- A user can have multiple override entries (see `minna.kiira-nymark@` with Mikonkatu + Kamppi)
- Always include a `reason` — this is the audit trail for why the override exists
- Reference INC ticket numbers when the override is triggered by a support request

## TODO
- [x] Document which automation runbook reads this variable and how it applies the overrides ✅
- [x] Document the `validFrom` / `validTo` fields — **they ARE functional** (runbook checks date bounds) ✅
- [x] Document how to remove a user override — **delete the JSON entry, save, auto-revoked next run** ✅
- [x] Document the `SBX_LocationToMailboxJson` variable contents ✅
- [ ] Add this runbook to Confluence as the authoritative version
