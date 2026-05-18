# ICON Company - Financial Ratio Analysis (Phase 2)

## Company: Industrial Engineering and Architecture Company for Construction and Development "ICON" (S.A.E.)

## Period: Nine months ended 30 September 2025

---

## Data Source

All numbers are extracted from:
**"# ICOM income Statement.md"** located in `Phase-1/` folder, which contains the official ICON consolidated financial statements reviewed by PricewaterhouseCoopers.

The source statements used are (page numbers refer to the original annual report structure):

1. **Page 3 — Statement of Financial Position (Balance Sheet):** "Interim condensed consolidated statement of financial position – At 30 September 2025" — contains all asset, liability, and equity figures
2. **Page 4 — Statement of Profit or Loss (Income Statement):** "Interim condensed consolidated statement of profit or loss – For the nine-months period ended 30 September 2025" — contains revenue, expenses, and profit figures
3. **Page 5 — Statement of Comprehensive Income** — used to cross-check total comprehensive income
4. **Page 6 — Statement of Changes in Equity** — used to cross-check equity movements
5. **Pages 8–64 — Notes to Financial Statements** — Note 11 for share capital (par value EGP 4/share)

---

## Key Financial Data Used (with Source Tracing)

| # | Item | Amount (EGP) | Page | Exact Line Item in Source |
| --- | --- | ---: | :---: | --- |
| 1 | Current Assets | 5,264,516,290 | **P.3** | **"Total current assets"** row, column "30 September 2025" — subtotal of Inventory + Trade and notes receivables + Debtors and other debit balances + Due from related parties + Cash and cash equivalents |
| 2 | Inventory | 1,660,578,087 | **P.3** | **"Inventory"** row under Current Assets section, column "30 September 2025" |
| 3 | Cash and Cash Equivalents | 96,041,078 | **P.3** | **"Cash and cash equivalents"** row under Current Assets section, column "30 September 2025" |
| 4 | Total Assets | 7,193,300,999 | **P.3** | **"Total assets"** row, column "30 September 2025" — equals Non-current (1,928,784,709) + Current (5,264,516,290) |
| 5 | Current Liabilities | 3,896,382,062 | **P.3** | **"Total current liabilities"** row, column "30 September 2025" |
| 6 | Total Liabilities | 4,116,020,259 | **P.3** | **"Total liabilities"** row, column "30 September 2025" — equals Non-current (219,638,197) + Current (3,896,382,062) |
| 7 | Total Equity | 3,077,280,740 | **P.3** | **"Total equity"** row, column "30 September 2025" — Parent equity + Non-controlling interests |
| 8 | Total Equity attributable to Parent | 2,469,275,417 | **P.3** | **"Total equity attributable to the Parent Company"** row, column "30 September 2025" — used for ROE/BVPS (excludes NCI) |
| 9 | Revenue | 5,337,752,819 | **P.4** | **"Revenue from contracts with customers"** row, column "Nine months ended 30 Sep 2025" |
| 10 | Cost of Revenue | 3,382,179,943 | **P.4** | **"Cost of revenue"** row (shown as negative), column "Nine months ended 30 Sep 2025" |
| 11 | Gross Profit | 1,955,572,876 | **P.4** | **"Gross profit"** row, column "Nine months ended 30 Sep 2025" — Revenue minus Cost of Revenue |
| 12 | Operating Profit (EBIT) | 1,150,114,103 | **P.4** | **"Operating profit"** row, column "Nine months ended 30 Sep 2025" — after all operating expenses, before finance costs and tax |
| 13 | Finance Costs (Interest) | 430,403,477 | **P.4** | **"Finance costs"** row (shown as negative), column "Nine months ended 30 Sep 2025" |
| 14 | Net Profit | 525,949,599 | **P.4** | **"Profit for the period"** row, column "Nine months ended 30 Sep 2025" — bottom line after tax |
| 15 | Earnings for common stockholders | 391,100,694 | **P.4** | **"Shareholders of the Parent Company"** under "Distributed as follows", column "Nine months ended 30 Sep 2025" — excludes NCI (134,848,905) |
| 16 | Number of Shares Outstanding | 145,500,000 | **P.3 + Notes** | Issued capital EGP 582,000,000 (P.3) ÷ Par value EGP 4/share (Note 11, P.8–64) = 145,500,000 shares. Cross-verified: 391,100,694 ÷ 145,500,000 = 2.69 matches reported EPS on P.4 |

---

## First: Liquidity Ratios

### 1. Current Ratio

**Where the numbers come from:**

- **Current Assets = 5,264,516,290** → **Page 3** (Balance Sheet), row "Total current assets", column 30 Sep 2025. This total includes: Inventory (1,660,578,087) + Trade and notes receivables (1,568,914,985) + Debtors and other debit balances (1,281,475,002) + Due from related parties (657,507,138) + Cash and cash equivalents (96,041,078).
- **Current Liabilities = 3,896,382,062** → **Page 3** (Balance Sheet), row "Total current liabilities", column 30 Sep 2025. This total includes: Provisions + Banks credit balances + Credit facilities + Bank borrowings + Trade and notes payable + Creditors and other credit balances + Due to related parties + Current income tax liability + Lease liabilities.

**Why these numbers:** The current ratio measures the company's ability to pay short-term obligations using short-term assets. We use the totals as reported because they already aggregate all items due within one year.

$$\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}} = \frac{5{,}264{,}516{,}290}{3{,}896{,}382{,}062} = 1.35$$

**Interpretation:** ICON has EGP 1.35 in current assets for every EGP 1.00 in current liabilities. The ratio is above 1, which means the company can cover its short-term obligations from its current assets.

---

### 2. Quick Ratio

**Where the numbers come from:**

- **Current Assets = 5,264,516,290** → **Page 3** (Balance Sheet), same as Current Ratio above.
- **Inventory = 1,660,578,087** → **Page 3** (Balance Sheet), row "Inventory" under Current Assets section, column 30 Sep 2025.
- **Current Liabilities = 3,896,382,062** → **Page 3** (Balance Sheet), same as Current Ratio above.

**Why these numbers:** The quick ratio removes Inventory from current assets because inventory is the least liquid current asset — in a construction/manufacturing company like ICON, inventory (raw materials, steel sections, sandwich panels etc.) cannot be converted to cash as quickly as receivables. Subtracting it gives a stricter liquidity test.

$$\text{Quick Ratio} = \frac{\text{Current Assets} - \text{Inventory}}{\text{Current Liabilities}} = \frac{5{,}264{,}516{,}290 - 1{,}660{,}578{,}087}{3{,}896{,}382{,}062} = \frac{3{,}603{,}938{,}203}{3{,}896{,}382{,}062} = 0.92$$

**Interpretation:** After removing inventory (the least liquid current asset), ICON has EGP 0.92 for every EGP 1.00 in current liabilities. This is slightly below 1, which indicates some pressure on short-term liquidity if the company cannot quickly sell its inventory.

---

### 3. Cash Ratio

**Where the numbers come from:**

- **Cash and Cash Equivalents = 96,041,078** → **Page 3** (Balance Sheet), row "Cash and cash equivalents" under Current Assets section, column 30 Sep 2025.
- **Current Liabilities = 3,896,382,062** → **Page 3** (Balance Sheet), same as above.

**Why these numbers:** The cash ratio is the most conservative liquidity test — it uses only cash and cash equivalents (bank balances and short-term deposits) because these are the only assets immediately available to pay debts without waiting to collect receivables or sell inventory.

$$\text{Cash Ratio} = \frac{\text{Cash \& Cash Equivalents}}{\text{Current Liabilities}} = \frac{96{,}041{,}078}{3{,}896{,}382{,}062} = 0.025$$

**Interpretation:** ICON has only 2.5 piasters (EGP 0.025) in cash for every EGP 1.00 in current liabilities. This is very low, meaning the company relies heavily on collecting receivables and selling inventory to meet short-term obligations rather than holding cash reserves.

---

## Second: Debt / Leverage Ratios

### 1. Debt Ratio

**Where the numbers come from:**

- **Total Liabilities = 4,116,020,259** → **Page 3** (Balance Sheet), row "Total liabilities", column 30 Sep 2025. This equals Total non-current liabilities (219,638,197) + Total current liabilities (3,896,382,062).
- **Total Assets = 7,193,300,999** → **Page 3** (Balance Sheet), row "Total assets", column 30 Sep 2025.

**Why these numbers:** The debt ratio shows what proportion of the company's assets is financed by creditors (all liabilities, both current and non-current). We use Total Liabilities (not just bank debt) because the formula measures all obligations.

$$\text{Debt Ratio} = \frac{\text{Total Liabilities}}{\text{Total Assets}} = \frac{4{,}116{,}020{,}259}{7{,}193{,}300{,}999} = 0.572 = 57.2\%$$

**Interpretation:** 57.2% of ICON's total assets are financed by debt. This indicates moderate to high leverage.

---

### 2. Debt-to-Equity Ratio

**Where the numbers come from:**

- **Total Liabilities = 4,116,020,259** → **Page 3** (Balance Sheet), same source as Debt Ratio above.
- **Total Equity = 3,077,280,740** → **Page 3** (Balance Sheet), row "Total equity", column 30 Sep 2025. This includes equity attributable to Parent (2,469,275,417) + Non-controlling interests (608,005,323).

**Why these numbers:** We use Total Equity (including non-controlling interests) because the denominator should match the scope of the numerator — Total Liabilities covers all creditors, so the equity side should cover all equity holders. This ratio shows the relative proportion of debt vs. equity financing.

$$\text{Debt/Equity} = \frac{\text{Total Liabilities}}{\text{Total Equity}} = \frac{4{,}116{,}020{,}259}{3{,}077{,}280{,}740} = 1.34$$

**Interpretation:** For every EGP 1.00 of equity, ICON has EGP 1.34 of liabilities. The company uses more debt than equity to finance its operations.

---

### 3. Equity Multiplier

**Where the numbers come from:**

- **Total Assets = 7,193,300,999** → **Page 3** (Balance Sheet), row "Total assets", column 30 Sep 2025.
- **Total Equity = 3,077,280,740** → **Page 3** (Balance Sheet), row "Total equity", column 30 Sep 2025.

**Why these numbers:** The equity multiplier shows how many EGP of assets are supported by each EGP of equity. We use Total Equity (including NCI) to be consistent with the balance sheet identity: Total Assets = Total Equity + Total Liabilities. Note: Equity Multiplier = 1 + Debt/Equity Ratio (2.34 ≈ 1 + 1.34).

$$\text{Equity Multiplier} = \frac{\text{Total Assets}}{\text{Total Equity}} = \frac{7{,}193{,}300{,}999}{3{,}077{,}280{,}740} = 2.34$$

**Interpretation:** For every EGP 1.00 of equity, ICON controls EGP 2.34 of assets. This confirms the company uses significant financial leverage.

---

### 4. Times Interest Earned Ratio

**Where the numbers come from:**

- **Operating Profit (EBIT) = 1,150,114,103** → **Page 4** (Income Statement), row "Operating profit", column "Nine months ended 30 Sep 2025". This line appears after all operating expenses (G&A, selling & marketing, other operating income/expenses, impairment losses) but before finance costs, financing income, and tax. It is the best available proxy for EBIT in these financial statements.
- **Finance Costs (Interest Expense) = 430,403,477** → **Page 4** (Income Statement), row "Finance costs" (shown as negative), column "Nine months ended 30 Sep 2025". This represents interest paid on credit facilities, bank borrowings, and lease liabilities.

**Why these numbers:** TIE measures how many times the company can cover its interest payments from operating earnings. We use "Operating profit" as EBIT because it is the profit generated from core operations before any financing decisions. We use "Finance costs" as interest expense because it is the total cost of borrowing.

$$\text{Times Interest Earned} = \frac{\text{Operating Profit (EBIT)}}{\text{Interest Expense}} = \frac{1{,}150{,}114{,}103}{430{,}403{,}477} = 2.67$$

**Interpretation:** ICON generates EGP 2.67 of operating profit for every EGP 1.00 of interest expense. While positive, this margin is not very high, indicating that a significant portion of operating income goes to servicing debt.

---

## Third: Profitability Ratios

### 1. Gross Profit Margin

**Where the numbers come from:**

- **Gross Profit = 1,955,572,876** → **Page 4** (Income Statement), row "Gross profit", column "Nine months ended 30 Sep 2025". Calculated as Revenue (5,337,752,819) minus Cost of Revenue (3,382,179,943).
- **Sales Revenue = 5,337,752,819** → **Page 4** (Income Statement), row "Revenue from contracts with customers", column "Nine months ended 30 Sep 2025".

**Why these numbers:** Gross profit margin measures the percentage of revenue remaining after direct production costs. "Revenue from contracts with customers" is the top-line sales figure, and "Cost of revenue" represents the direct costs of construction and manufacturing (materials, direct labor, subcontractors).

$$\text{Gross Profit Margin} = \frac{\text{Gross Profit}}{\text{Sales Revenue}} = \frac{1{,}955{,}572{,}876}{5{,}337{,}752{,}819} = 0.366 = 36.6\%$$

**Interpretation:** After subtracting direct costs, ICON retains 36.6 piasters from every EGP 1.00 of sales to cover operating expenses and generate profit.

---

### 2. Operating Profit Margin

**Where the numbers come from:**

- **Operating Profit = 1,150,114,103** → **Page 4** (Income Statement), row "Operating profit", column "Nine months ended 30 Sep 2025". This is calculated as: Gross Profit (1,955,572,876) minus G&A expenses (431,081,223) minus Selling & marketing expenses (209,574,721) plus Other operating income (64,524,708) minus Other operating expenses (48,071,611) minus Net impairment losses on financial assets (181,255,926).
- **Sales Revenue = 5,337,752,819** → **Page 4** (Income Statement), same as Gross Profit Margin above.

**Why these numbers:** Operating profit margin shows what percentage of revenue is left after all operating costs (not just direct costs). "Operating profit" is used because it captures the full operating performance before financing and tax effects.

$$\text{Operating Profit Margin} = \frac{\text{Operating Profit}}{\text{Sales Revenue}} = \frac{1{,}150{,}114{,}103}{5{,}337{,}752{,}819} = 0.215 = 21.5\%$$

**Interpretation:** After all operating expenses, ICON retains 21.5 piasters from every EGP 1.00 of sales as operating profit.

---

### 3. Net Profit Margin

**Where the numbers come from:**

- **Net Profit = 525,949,599** → **Page 4** (Income Statement), row "Profit for the period", column "Nine months ended 30 Sep 2025". This is the final bottom line after deducting finance costs (430,403,477), adding financing income (14,086,727), adding share in associates' profits (33,031,645), and deducting income tax (240,879,399).
- **Sales Revenue = 5,337,752,819** → **Page 4** (Income Statement), same as above.

**Why these numbers:** Net profit margin uses the total "Profit for the period" (not just the parent's share) because this ratio measures overall company profitability relative to total revenue. The full net profit includes both parent and non-controlling interests' share.

$$\text{Net Profit Margin} = \frac{\text{Net Profit}}{\text{Total Sales Revenue}} = \frac{525{,}949{,}599}{5{,}337{,}752{,}819} = 0.0986 = 9.86\%$$

**Interpretation:** ICON keeps approximately 9.9 piasters of net profit from every EGP 1.00 of revenue after all expenses including interest and taxes.

---

### 4. Basic Earnings Power Ratio

**Where the numbers come from:**

- **EBIT = 1,150,114,103** → **Page 4** (Income Statement), row "Operating profit", column "Nine months ended 30 Sep 2025" (same as TIE ratio).
- **Total Assets = 7,193,300,999** → **Page 3** (Balance Sheet), row "Total assets", column 30 Sep 2025.

**Why these numbers:** BEP measures the raw earning power of the company's assets before any impact of financing structure or tax rates. By using Operating Profit (EBIT) and Total Assets, we see how efficiently the company uses all its assets to generate operating earnings, making it comparable across companies with different capital structures and tax situations.

$$\text{Basic Earnings Power} = \frac{\text{EBIT}}{\text{Total Assets}} = \frac{1{,}150{,}114{,}103}{7{,}193{,}300{,}999} = 0.160 = 16.0\%$$

**Interpretation:** ICON generates 16 piasters of operating profit for every EGP 1.00 of assets, regardless of how those assets are financed or taxed.

---

### 5. Earnings Per Share (EPS)

**Where the numbers come from:**

- **Earnings Available for Common Stockholders = 391,100,694** → **Page 4** (Income Statement), under "Distributed as follows:", row "Shareholders of the Parent Company", column "Nine months ended 30 Sep 2025". The total net profit of 525,949,599 is split between Parent shareholders (391,100,694) and Non-controlling interests (134,848,905). Only the parent's share belongs to common stockholders.
- **Number of Shares = 145,500,000** → Derived from **Page 3** (Balance Sheet): Issued and paid-up capital = EGP 582,000,000 (row "Issued and paid-up capital") ÷ Par value of EGP 4 per share (**Notes, Pages 8–64**, Note 11) = 145,500,000 shares. Cross-verified by **Page 4** (Income Statement) which reports "Basic and diluted earnings per share for the period" = 2.69 EGP/share, and 391,100,694 ÷ 145,500,000 = 2.69.

**Why these numbers:** EPS measures how much profit each common share earned. We use only the Parent's share of profit (not total net profit) because non-controlling interests represent minority shareholders in subsidiaries — they own shares in ICON's subsidiaries, not in ICON itself.

$$\text{EPS} = \frac{\text{Earnings Available for Common Stockholders}}{\text{Number of Common Shares Outstanding}} = \frac{391{,}100{,}694}{145{,}500{,}000} = 2.69 \text{ EGP/share}$$

**Interpretation:** Each common share earned EGP 2.69 during the nine-month period ended 30 September 2025.

---

### 6. Return on Assets (ROA)

**Where the numbers come from:**

- **Earnings Available for Common Stockholders = 391,100,694** → **Page 4** (Income Statement), same source as EPS (Parent's share of profit).
- **Total Assets = 7,193,300,999** → **Page 3** (Balance Sheet), row "Total assets", column 30 Sep 2025.

**Why these numbers:** ROA shows how effectively the company uses its total assets to generate profit for common stockholders. We use the Parent's share (391,100,694) rather than total net profit (525,949,599) to be consistent with the EPS perspective — measuring returns that belong to ICON's shareholders specifically.

$$\text{ROA} = \frac{\text{Earnings Available for Common Stockholders}}{\text{Total Assets}} = \frac{391{,}100{,}694}{7{,}193{,}300{,}999} = 0.0544 = 5.44\%$$

**Interpretation:** For every EGP 1.00 of total assets, ICON earned approximately 5.4 piasters for its common stockholders during the nine-month period.

---

### 7. Return on Equity (ROE)

**Where the numbers come from:**

- **Earnings Available for Common Stockholders = 391,100,694** → **Page 4** (Income Statement), same source as EPS (Parent's share of profit).
- **Stockholders' Equity = 2,469,275,417** → **Page 3** (Balance Sheet), row "Total equity attributable to the Parent Company", column 30 Sep 2025. This equals: Issued and paid-up capital (582,000,000) + Legal reserve (48,452,497) + Reserve of foreign entities translation (136,218,736) + Retained earnings (1,702,604,184).

**Why these numbers:** ROE measures the return generated on the equity invested by common stockholders. We use "Total equity attributable to the Parent Company" (2,469,275,417) and NOT "Total equity" (3,077,280,740) because we must match the numerator scope — since we use only the parent's share of earnings (391,100,694), we must use only the parent's equity. Non-controlling interests' equity (608,005,323) belongs to minority shareholders of subsidiaries, not to ICON's stockholders.

$$\text{ROE} = \frac{\text{Earnings Available for Common Stockholders}}{\text{Stockholders' Equity}} = \frac{391{,}100{,}694}{2{,}469{,}275{,}417} = 0.158 = 15.8\%$$

**Interpretation:** For every EGP 1.00 invested by shareholders, ICON generated approximately 15.8 piasters in profit during the nine-month period.

---

### 8. Book Value Per Share

**Where the numbers come from:**

- **Common Stock Equity = 2,469,275,417** → **Page 3** (Balance Sheet), row "Total equity attributable to the Parent Company", column 30 Sep 2025 (same as ROE denominator).
- **Number of Shares = 145,500,000** → same derivation as EPS: **Page 3** capital (582,000,000) ÷ par value EGP 4 (**Notes, Page 8–64**).

**Why these numbers:** BVPS shows the net asset value backing each common share. We use the Parent's equity (not total equity) because each ICON share represents a claim on the parent's equity only — non-controlling interests have claims on subsidiary equity, not on ICON's shares.

$$\text{Book Value Per Share} = \frac{\text{Common Stock Equity}}{\text{Number of Shares Outstanding}} = \frac{2{,}469{,}275{,}417}{145{,}500{,}000} = 16.97 \text{ EGP/share}$$

**Interpretation:** If the company were liquidated at book value, each common share would receive approximately EGP 16.97.

---

## Summary Table

| Ratio | Formula | Value |
| --- | --- | --- |
| **Liquidity** | | |
| Current Ratio | Current Assets / Current Liabilities | **1.35** |
| Quick Ratio | (Current Assets - Inventory) / Current Liabilities | **0.92** |
| Cash Ratio | Cash / Current Liabilities | **0.025** |
| **Leverage** | | |
| Debt Ratio | Total Liabilities / Total Assets | **57.2%** |
| Debt/Equity Ratio | Total Liabilities / Total Equity | **1.34** |
| Equity Multiplier | Total Assets / Total Equity | **2.34** |
| Times Interest Earned | EBIT / Interest Expense | **2.67x** |
| **Profitability** | | |
| Gross Profit Margin | Gross Profit / Sales | **36.6%** |
| Operating Profit Margin | Operating Profit / Sales | **21.5%** |
| Net Profit Margin | Net Profit / Sales | **9.86%** |
| Basic Earnings Power | EBIT / Total Assets | **16.0%** |
| EPS | Earnings for Common / Shares Outstanding | **EGP 2.69** |
| ROA | Earnings for Common / Total Assets | **5.44%** |
| ROE | Earnings for Common / Stockholders' Equity | **15.8%** |
| Book Value Per Share | Common Equity / Shares Outstanding | **EGP 16.97** |
