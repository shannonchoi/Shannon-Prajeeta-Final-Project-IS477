# Status Report: USD Strength vs. U.S. Exports

## Overview

This report provides an update on the progress of our project analyzing the relationship between the Real Trade Weighted U.S. Dollar Index (RTWEXBGS) and Real Exports of Goods and Services (EXPGS). Our primary objective is to evaluate how changes in the strength of the U.S. dollar influence export performance.

Since starting the analysis, we expanded our scope to include lag effects and changes in this relationship in the post-2020 economy, in addition to the overall correlation.

Since the submission of our initial project plan, we have successfully completed data acquisition, integration, and preliminary analysis. We have also refined our methodology to address issues related to time-series alignment and lag structure. The project has progressed from planning into active analysis, with findings revealing that the relationship between exchange rates and exports is more complex than originally hypothesized.

---

## Progress on Project Tasks

### Data Acquisition (Completed)

We retrieved both datasets from the Federal Reserve Economic Data (FRED) API using Python and the `fredapi` library:

- **RTWEXBGS** (weekly frequency)  
- **EXPGS** (quarterly frequency)

The data was stored as Pandas DataFrames to ensure reproducibility and workflow automation.

---

### Data Integration (Completed)

A key challenge was aligning datasets due to differences in temporal granularity and timestamp formats:

- Dollar index data was weekly and required resampling to quarterly averages  
- Export data was already quarterly but used different timestamp conventions  

Initially, merging resulted in an empty DataFrame due to misaligned date indices (quarter-end vs. quarter-start). This issue was resolved by converting both datasets to a standardized quarterly `PeriodIndex`.

After fixing alignment, the datasets were successfully merged using an inner join.

---

### Data Transformation (Completed)

To prepare the data for analysis:

- Applied **percentage change transformations** to address non-stationarity  
- Created **lag variables (0–4 quarters)** to test delayed effects  

---

## Preliminary Analysis

### Baseline Correlation (No Lag)

We first examined the contemporaneous relationship between the dollar index and exports using percentage changes.

- **Correlation (no lag): r ≈ 0.22**

This indicates a weak positive relationship, which does not align with the initial hypothesis that a stronger dollar reduces exports. The weak magnitude suggests that exchange rate movements alone are not strong predictors of export performance.
---

### Lag Analysis Results

| Lag (Quarters) | Correlation |
|---------------|------------|
| 0             | -0.47      |
| 1             | 0.05       |
| 2             | 0.24       |
| 3             | 0.19       |
| 4             | 0.03       |

The strongest relationship occurs at **lag 0 (r ≈ -0.47)**, indicating that increases in USD strength are associated with decreases in exports within the same quarter.

However, correlations at longer lags are weak and inconsistent, suggesting that delayed effects are less reliable and likely influenced by other macroeconomic factors.

---

### Pre- and Post-2020 Analysis (Completed)

To evaluate structural changes, we split the dataset:

- **Pre-2020 correlation:** 0.18  
- **Post-2020 correlation:** 0.32  

Both indicate weak positive relationships, with a modest increase after 2020. This suggests the USD–export relationship may have shifted due to global economic changes such as supply chain disruptions and policy shifts.

---

## Updated Timeline

| Phase       | Task                              | Status        | Updated Completion |
|------------|----------------------------------|--------------|-------------------|
| Acquisition | FRED API data retrieval          | Completed     | March 15          |
| Integration | Resampling and merging datasets  | Completed     | March 20          |
| Quality     | Data validation and cleaning     | Completed     | April 7           |
| Analysis    | Correlation and lag analysis     | Completed     | April 5           |
| Reporting   | Status report drafting           | In Progress   | April 6           |
| Reporting   | Status report submission         | In Progress   | April 14          |
| Final       | Full analysis and report         | Not Started   | May 3             |

---
