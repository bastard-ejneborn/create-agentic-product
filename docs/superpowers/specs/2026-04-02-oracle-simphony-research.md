# Oracle Simphony Cloud — Integration Research

> Status: **Ready to build** — full API docs found, no OHIP access needed
> Date: 2026-04-02 (updated with BI API documentation)

## Summary

Found the **Business Intelligence API** documentation — a complete REST API with 50+ endpoints for querying Simphony transactional, operational, and labor data. This is accessible through **R&A Back Office** (not OHIP), making it much simpler to set up. API accounts are created directly in the R&A admin console.

**Source**: https://docs.oracle.com/en/industries/food-beverage/back-office/20.1/biapi/rest-endpoints.html

## API Overview

- **Base URL**: `https://{your-domain}.oracleindustry.com/bi/v1/{orgShortName}/`
- **Method**: All endpoints use POST
- **Auth**: OpenID Connect (OAuth 2.0 with PKCE)
- **Format**: JSON request and response
- **Date format**: `YYYY-MM-DD`
- **No pagination needed**: Returns all revenue centers for the location/date

## Authentication Flow

### Endpoints
| Purpose | URL |
|---------|-----|
| Authorize | `{HOST}/oidc-provider/v1/oauth2/authorize` |
| Sign in | `{HOST}/oidc-provider/v1/oauth2/signin` |
| Token | `{HOST}/oidc-provider/v1/oauth2/token` |

### Flow
1. Create API account in R&A Back Office → gets `client_id`
2. Generate PKCE code_verifier + code_challenge (SHA-256)
3. GET authorize endpoint with `client_id`, `scope=openid`, `code_challenge`
4. POST sign-in with `username`, `password`, `orgname` → get `auth_code`
5. POST token endpoint with `auth_code` + `code_verifier` → get tokens

### Token Lifetimes
| Token | Lifetime | Use |
|-------|----------|-----|
| `id_token` | 14 days | Bearer token for API calls |
| `refresh_token` | 28 days | Obtain new id_token |
| Password | 60 days | Must be reset |

### API Call Format
```bash
curl -X POST \
  -H "Authorization: Bearer <id_token>" \
  -H "Content-Type: application/json" \
  -d '{"locRef":"1234","busDt":"2026-04-01"}' \
  https://{domain}.oracleindustry.com/bi/v1/{orgShortName}/getOperationsDailyTotals
```

## All Available Endpoints (50+)

### Daily Aggregations
| Endpoint | Data |
|----------|------|
| `getOperationsDailyTotals` | Net sales, taxes, checks, guests, voids, discounts, service charges |
| `getMenuItemDailyTotals` | Sales per menu item |
| `getDiscountDailyTotals` | Discount totals by type |
| `getEmployeeDailyTotals` | Per-employee sales/performance |
| `getJobCodeDailyTotals` | Labor totals by job code |
| `getTenderMediaDailyTotals` | Payment method totals (cash, card, etc.) |
| `getTaxDailyTotals` | Tax collected by type |
| `getServiceChargeDailyTotals` | Service charge totals |
| `getOrderTypeDailyTotals` | Dine-in, takeout, delivery, etc. |
| `getOrderChannelDailyTotals` | Order channel breakdown |
| `getComboItemDailyTotals` | Combo/meal deal totals |
| `getControlDailyTotals` | Control totals |

### Quarter Hour Aggregations
Same categories as daily but in 15-minute intervals:
`getOperationsQuarterHourTotals`, `getMenuItemQuarterHourTotals`, `getDiscountQuarterHourTotals`, `getJobCodeQuarterHourTotals`, `getOrderTypeQuarterHourTotals`, `getServiceChargeQuarterHourTotals`, `getTenderMediaQuarterHourTotals`, `getComboItemQuarterHourTotals`

### Transactions
| Endpoint | Data |
|----------|------|
| `getGuestChecks` | Full guest check data with line items |
| `getNonSalesTransactions` | Non-sale activities |
| `getPOSJournalLogDetails` | POS journal entries |
| `getPOSWasteDetails` | Waste/spoilage tracking |
| `getSPIPaymentDetails` | Payment integration details |
| `getGuestCheckExtensibilityDetails` | Custom check data |
| `getGuestCheckLineItemExtDetails` | Custom line item data |

### Labor
| Endpoint | Data |
|----------|------|
| `getTimeCardDetails` | Clock in/out, hours worked |

### Cash Management
| Endpoint | Data |
|----------|------|
| `getCashManagementDetails` | Cash drops, pickups, adjustments |

### Kitchen Performance
| Endpoint | Data |
|----------|------|
| `getKDSDetails` | Kitchen display system timing |

### Fiscal
| Endpoint | Data |
|----------|------|
| `getFiscalInvoiceData` | Invoice transactions |
| `getFiscalInvoiceControlData` | Invoice control data |
| `getFiscalTotalData` | Fiscal totals |

### Payment
| Endpoint | Data |
|----------|------|
| `getPaymentTransactions` | Payment transaction details |
| `getPaymentSettlements` | Settlement details |
| `getPaymentPayouts` | Payout details |
| `getPaymentPayoutSummary` | Payout summary |
| `getPaymentChargebacks` | Chargeback details |
| `getPaymentAccountDimensions` | Account details |
| `getPaymentAccountHolderDimensions` | Account holder info |

### POS Definitions (reference data)
| Endpoint | Data |
|----------|------|
| `getLocationDimensions` | All locations with references |
| `getRevenueCenterDimensions` | Revenue centers per location |
| `getMenuItemDimensions` | Menu item definitions |
| `getMenuItemPrices` | Menu item pricing |
| `getEmployeeDimensions` | Employee info |
| `getJobCodeDimensions` | Job codes |
| `getDiscountDimensions` | Discount definitions |
| `getOrderTypeDimensions` | Order type definitions |
| `getOrderChannelDimensions` | Order channel definitions |
| `getTenderMediaDimensions` | Payment method definitions |
| `getTaxDimensions` | Tax definitions |
| `getServiceChargeDimensions` | Service charge definitions |
| `getCashierDimensions` | Cashier info |
| `getReasonCodeDimensions` | Reason codes (voids, etc.) |
| `getCashManagementItemDimensions` | Cash management items |
| `getLatestBusDt` | Latest business date available |

## Response Example (Operations Daily Totals)

```json
{
  "locRef": "1234",
  "busDt": "2026-04-01",
  "revenueCenters": [
    {
      "rvcNum": 1,
      "netSlsTtl": 12450.50,
      "taxCollTtl": 1556.31,
      "chkCnt": 234,
      "gstCnt": 312,
      "vdCnt": 3,
      "vdTtl": 45.00,
      "itmDscTtl": 220.00,
      "chkClsdCnt": 230,
      "chkClsdTtl": 12200.50,
      "chkOpnCnt": 4,
      "chkOpnTtl": 250.00
    }
  ]
}
```

## Request Body Parameters

All endpoints accept:
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `locRef` | string | Yes | Location reference (store number) |
| `busDt` | string | Yes | Business date (YYYY-MM-DD) |
| `applicationName` | string | No | Your app name for tracking |
| `include` | string | No | Additional objects to include |
| `searchCriteria` | string | No | Filter results |

## Multi-Location

- Use `getLocationDimensions` to get all location references
- Then query each location by `locRef`
- Iterate across locations for enterprise-wide reports

## Proposed Skill Architecture

```
.claude/skills/simphony/
  SKILL.md                      ← Documentation
  scripts/
    simphony.py                 ← Main CLI (read-only POST only)
    simphony_auth.py            ← OAuth PKCE setup + token refresh
```

### Commands
```bash
# Setup: authenticate (one-time, tokens last 14 days)
python simphony_auth.py setup

# List all locations
python simphony.py locations

# Daily operations summary for a location
python simphony.py sales --location 1234 --date 2026-04-01

# Sales for date range (iterates days)
python simphony.py sales --location 1234 --since 7d

# Dashboard across all locations for a date
python simphony.py dashboard --date 2026-04-01

# Menu item performance (product mix)
python simphony.py pmix --location 1234 --date 2026-04-01

# Labor data
python simphony.py labor --location 1234 --date 2026-04-01

# Employee performance
python simphony.py employees --location 1234 --date 2026-04-01

# Payment breakdown
python simphony.py payments --location 1234 --date 2026-04-01

# Discount and void analysis
python simphony.py discounts --location 1234 --date 2026-04-01

# Guest checks (individual transactions)
python simphony.py checks --location 1234 --date 2026-04-01
```

### Dashboard Output
Aggregates across all locations for a date:
- Revenue per location + total
- Guest count per location
- Average check per location
- Discounts and voids (flags anomalies)
- Payment method breakdown
- Labor hours and cost
- Comparison between locations

## Setup Requirements

1. Create BI API account in R&A Back Office (Administration → System → API Accounts)
2. Select type: **Business Intelligence API**
3. Grant permissions: Sales & Operations, Employee Performance, Labor, Cash Management
4. Note the Client ID, set password
5. Note the Authentication Server URL and Application Server URL
6. Add to `.env`:
   ```
   SIMPHONY_HOST=https://yourdomain.oracleindustry.com
   SIMPHONY_AUTH_HOST=https://yourdomain-idm.oracleindustry.com
   SIMPHONY_CLIENT_ID=your-client-id
   SIMPHONY_USERNAME=your-api-username
   SIMPHONY_PASSWORD=your-api-password
   SIMPHONY_ORG=your-org-short-name
   ```

## Integration with Existing Skills

- **budget-tracker**: Compare restaurant revenue/costs against budgets
- **stakeholder-briefing**: Include real restaurant performance in board updates
- **meeting-prep**: Pull sales/labor data for management meetings
- **project-portfolio**: Correlate technology projects with restaurant performance
- **local-marketing**: Measure marketing impact on sales by location
- **freshservice**: Cross-reference IT issues with POS downtime impact
