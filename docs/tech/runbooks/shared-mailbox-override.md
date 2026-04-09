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
Add a new entry to the `"overrides"` array:

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

## Important Notes

- The `offices` value must match the **exact restaurant name** as configured in the system
- Multiple offices can be assigned to one user (see `fredrik@` example with Solli + Torggata)
- A user can have multiple override entries (see `minna.kiira-nymark@` with Mikonkatu + Kamppi)
- Always include a `reason` — this is the audit trail for why the override exists
- Reference INC ticket numbers when the override is triggered by a support request

## TODO
- [ ] Document how to **remove** a user override
- [ ] Document the `validFrom` / `validTo` fields — are they functional or reserved for future use?
- [ ] Document which automation runbook reads this variable and how it applies the overrides
- [ ] Document the restaurant name matching logic (where does the automation get the list of valid office names?)
- [ ] Add this runbook to Confluence as the authoritative version
