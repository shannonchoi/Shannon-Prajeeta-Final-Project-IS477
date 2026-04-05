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

## Changes to Project Plan
As we engaged deeply with the data and incorporated feedback from Milestone 2, we identified several necessary changes to our project plan regarding our methodology, technical constraints, and data definitions.

1. Variable Definition Refinement: To improve clarity about the datasets, we added explicit definitions for our key variables in each dataset to the plan:

Variables(columns) of the ‘Real Trade Weighted U.S. Dollar Index’(RTWEXBGS) Dataset:
- date (observation_date): Timestamp of observation. (weekly)
- RTWEXBGS: Index value representing inflation-adjusted USD strength relative to major trading partners.

Variables(columns) of the ‘Real Exports of Goods and Services’ (EXPGS) Dataset:
- date (observation_date): Timestamp of observation. (quarterly)
- EXPGS: Inflation-adjusted total exports (in billions of chained dollars).

2. Integration Methodology Update: We refined our explanation of how and on what column the datasets will be merged.
- Deleted: "We will integrate based on the 'observation_date' column in both datasets. The primary challenge in integrating these datasets is the difference in reporting frequency. The Dollar Index is updated weekly, while Export data is updated quarterly..." 
- Added: "The common feature between the two datasets is time, specifically the observation_date variable. This shared temporal dimension enables integration. We will integrate based on the 'observation_date' column in both datasets. The primary challenge in integrating these datasets is the difference in reporting frequency. The Dollar Index is updated weekly, while Export data is updated quarterly. To resolve this, we’ll use a downsampling transformation in Python Pandas. We’ll calculate the mean value of the weekly Dollar Index for each quarter, creating a new "Quarterly Average" series. We’ll create a lagged version of the Export dataset by shifting it by two quarters to test our hypothesis that currency fluctuations have a delayed impact on trade volume."

3. Addressing Analytical and Scope Limitations: We realized that raw time-series data presents statistical challenges and that our scope is very limited by the few variables available. We updated our "Gaps" section accordingly:
- Added: "Both RTWEXBGS and EXPGS are time-series data that may exhibit trends over time. Without transformation (e.g., first differencing or percentage change), correlation results may be misleading. This relates to time-series analysis concepts covered in class."
- Deleted: Our previous, vaguer statement regarding Course Content Gaps and Python workflow managers.
- Added: "Feature Limitation (Dataset Scope): Both datasets contain only a single primary measurement variable (index value and export value). The lack of additional explanatory variables limits the complexity of modeling and restricts analysis to bivariate relationships. Especially for related the later modules, we need to research tools like specific Python workflow managers to ensure our end-to-end process is fully automated and reproducible for the final submission."

## Challenges and Resolutions
Some of the challenges that we faced when working with our datasets are temporal misalignment, lag direction confusion, non-stationarity, and weak and inconsistent results. For temporal misalignment, the issue was that our merge procured an empty dataset due to Quarter-end vs. quarter-start timestamps, with our solution being that we converted both datasets to PeriodIndex (quarterly). For lag direction confusion, the issue was that our initial lag implementation produced NaN results and our solution was a corrected lag structure and verified alignment through debugging and inspection of intermediate outputs. For non-stationarity, the issue was raw time-series correlation risked spurious results and our solution was that we applied percentage change transformations before analysis. For weak and inconsistent results, the issue was that initial lag-2 correlation did not support our hypothesis and the solution was that we expanded our analysis to include multiple lags and time-period comparisons. 

## Summary of Individual Contributions
Prajeeta Dahal: 
I implemented the FRED API data acquisition scripts to retrieve the required datasets and performed data integration, including resampling the weekly dollar index into quarterly averages for alignment with export data. I conducted the correlation and lag analysis to evaluate the relationship between USD strength and exports under different model specifications. Additionally, I developed a reproducible workflow in Google Colab to ensure the analysis can be easily rerun and verified. I also contributed to documentation and report writing, and assisted in interpreting results and refining the overall analytical approach.

Shannon Choi:
I conducted a data quality assessment and identified missing values and inconsistencies during the cleaning process. Additionally, I debugged merge and lag alignment issues and developed a reproducible workflow in Google Colab. Finally, I also contributed to the documentation and report writing, while assisting in interpreting the results and refining our analysis.
