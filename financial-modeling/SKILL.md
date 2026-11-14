---
# ═══════════════════════════════════════════════════════════════════════════════
# CHATGPT OFFICE SKILL - Financial Modeling
# ═══════════════════════════════════════════════════════════════════════════════

name: financial-modeling
description: "Build integrated financial models with 3-statement projections. Create income statement, balance sheet, and cash flow models with proper linkages."
version: "1.0.0"
author: wealchu
license: MIT

category: finance
tags:
  - financial-modeling
  - three-statement
  - forecasting
  - income-statement
  - balance-sheet
department: Finance/FP&A

models:
  recommended:
    - gpt-6-astra
  compatible:
    - gpt-6-astra

mcp:
  server: office-mcp
  tools:
    - read_xlsx
    - create_xlsx
    - apply_formula
    - create_chart

capabilities:
  - three_statement_modeling
  - revenue_forecasting
  - expense_modeling
  - working_capital_projections
  - debt_schedule_modeling

languages:
  - en
  - zh

related_skills:
  - dcf-valuation
  - stock-analysis
  - data-analysis
---

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

# Financial Modeling Skill

## Overview

I help you build integrated 3-statement financial models that link Income Statement, Balance Sheet, and Cash Flow Statement. These models are essential for valuation, budgeting, and strategic planning.

**What I can do:**
- Build income statement projections
- Create balance sheet forecasts
- Generate cash flow statements
- Model working capital requirements
- Build debt schedules and interest calculations
- Create scenario analysis (base/bull/bear cases)

**What I cannot do:**
- Access real-time financial data
- Guarantee projection accuracy
- Provide accounting advice
- Replace professional financial analysis

---

## How to Use Me

### Step 1: Provide Historical Data

I need 2-3 years of:
- Income statement (revenue, COGS, operating expenses)
- Balance sheet (assets, liabilities, equity)
- Cash flow statement (optional but helpful)

### Step 2: Define Projection Assumptions

Key drivers:
- Revenue growth rate
- Gross margin
- Operating expense ratios
- Capex as % of revenue
- Working capital days (DSO, DIO, DPO)

### Step 3: Choose Model Scope

- **Basic**: Income statement only
- **Standard**: Income statement + balance sheet
- **Full**: Complete 3-statement model with cash flow

---

## Model Architecture

### Three-Statement Linkages

```
┌─────────────────────────────────────────────────────────────┐
│                    INCOME STATEMENT                         │
│  Revenue → Gross Profit → Operating Income → Net Income     │
└─────────────────────────┬───────────────────────────────────┘
                          │
        Net Income flows to Retained Earnings
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    BALANCE SHEET                            │
│  Assets = Liabilities + Equity                              │
│  (Must balance via Cash as plug)                            │
└─────────────────────────┬───────────────────────────────────┘
                          │
        Changes in B/S items drive CF Statement
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  CASH FLOW STATEMENT                        │
│  Operating CF + Investing CF + Financing CF = Δ Cash        │
│  Ending Cash flows back to Balance Sheet                    │
└─────────────────────────────────────────────────────────────┘
```

### Key Formulas

#### Income Statement Drivers
```
Revenue = Prior Year × (1 + Growth Rate)
COGS = Revenue × (1 - Gross Margin %)
Gross Profit = Revenue - COGS
SG&A = Revenue × SG&A %
EBITDA = Gross Profit - SG&A
D&A = Prior PP&E × D&A Rate OR Revenue × D&A %
EBIT = EBITDA - D&A
Interest = Avg Debt × Interest Rate
EBT = EBIT - Interest
Taxes = EBT × Tax Rate
Net Income = EBT - Taxes
```

#### Balance Sheet Drivers
```
Accounts Receivable = Revenue × (DSO / 365)
Inventory = COGS × (DIO / 365)
Accounts Payable = COGS × (DPO / 365)
PP&E = Prior PP&E + Capex - D&A
Retained Earnings = Prior RE + Net Income - Dividends
Cash = Total Liabilities + Equity - Other Assets (plug)
```

#### Cash Flow Statement
```
Operating Cash Flow:
  Net Income
  + D&A (non-cash)
  - Increase in AR
  - Increase in Inventory
  + Increase in AP
  = Cash from Operations

Investing Cash Flow:
  - Capex
  = Cash from Investing

Financing Cash Flow:
  + Debt Issuance
  - Debt Repayment
  - Dividends
  = Cash from Financing

Net Change in Cash = CFO + CFI + CFF
```

---

## Output Format

```markdown
# Financial Model: [Company Name]

**Projection Period**: [Years]
**Base Year**: [Year]
**Currency**: [USD/CNY/etc.]

---

## Key Assumptions

| Driver | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|--------|--------|--------|--------|--------|--------|
| Revenue Growth | XX% | XX% | XX% | XX% | XX% |
| Gross Margin | XX% | XX% | XX% | XX% | XX% |
| SG&A % Revenue | XX% | XX% | XX% | XX% | XX% |
| Capex % Revenue | XX% | XX% | XX% | XX% | XX% |
| DSO (days) | XX | XX | XX | XX | XX |
| DIO (days) | XX | XX | XX | XX | XX |
| DPO (days) | XX | XX | XX | XX | XX |

---

## Income Statement Projection

| ($M) | Base | Y1 | Y2 | Y3 | Y4 | Y5 |
|------|------|-----|-----|-----|-----|-----|
| **Revenue** | | | | | | |
| Growth % | | | | | | |
| COGS | | | | | | |
| **Gross Profit** | | | | | | |
| Gross Margin % | | | | | | |
| SG&A | | | | | | |
| **EBITDA** | | | | | | |
| EBITDA Margin % | | | | | | |
| D&A | | | | | | |
| **EBIT** | | | | | | |
| Interest Expense | | | | | | |
| **EBT** | | | | | | |
| Taxes | | | | | | |
| **Net Income** | | | | | | |
| Net Margin % | | | | | | |

---

## Balance Sheet Projection

| ($M) | Base | Y1 | Y2 | Y3 | Y4 | Y5 |
|------|------|-----|-----|-----|-----|-----|
| **ASSETS** | | | | | | |
| Cash | | | | | | |
| Accounts Receivable | | | | | | |
| Inventory | | | | | | |
| **Current Assets** | | | | | | |
| PP&E (net) | | | | | | |
| Other Assets | | | | | | |
| **Total Assets** | | | | | | |
| | | | | | | |
| **LIABILITIES** | | | | | | |
| Accounts Payable | | | | | | |
| Short-term Debt | | | | | | |
| **Current Liabilities** | | | | | | |
| Long-term Debt | | | | | | |
| **Total Liabilities** | | | | | | |
| | | | | | | |
| **EQUITY** | | | | | | |
| Common Stock | | | | | | |
| Retained Earnings | | | | | | |
| **Total Equity** | | | | | | |
| **Total L + E** | | | | | | |

✓ Balance Check: Assets = Liabilities + Equity

---

## Cash Flow Statement

| ($M) | Y1 | Y2 | Y3 | Y4 | Y5 |
|------|-----|-----|-----|-----|-----|
| **Operating Activities** | | | | | |
| Net Income | | | | | |
| D&A | | | | | |
| Change in AR | | | | | |
| Change in Inventory | | | | | |
| Change in AP | | | | | |
| **Cash from Operations** | | | | | |
| | | | | | |
| **Investing Activities** | | | | | |
| Capex | | | | | |
| **Cash from Investing** | | | | | |
| | | | | | |
| **Financing Activities** | | | | | |
| Debt Changes | | | | | |
| Dividends | | | | | |
| **Cash from Financing** | | | | | |
| | | | | | |
| **Net Change in Cash** | | | | | |
| Beginning Cash | | | | | |
| **Ending Cash** | | | | | |

---

## Key Metrics Summary

| Metric | Base | Y1 | Y2 | Y3 | Y4 | Y5 |
|--------|------|-----|-----|-----|-----|-----|
| Revenue Growth | | | | | | |
| Gross Margin | | | | | | |
| EBITDA Margin | | | | | | |
| Net Margin | | | | | | |
| ROE | | | | | | |
| Debt/Equity | | | | | | |
| FCF | | | | | | |
```

---

## Tips for Better Results

1. **Provide clean historical data** in a consistent format
2. **Be specific about growth drivers** (volume vs price, organic vs acquisition)
3. **Specify industry context** for appropriate benchmarks
4. **Ask for scenario analysis** to understand range of outcomes
5. **Request sensitivity tables** for key assumptions

---

## Limitations

- Projections are only as good as the assumptions
- Cannot model complex corporate structures
- Does not account for one-time items automatically
- Simplified tax calculations
- Currency assumed constant (no FX modeling)

---

*Built by the ChatGPT Office Skills community. Contributions welcome!*
