# Dollar Dynamics: Analyzing the Relationship Between USD Strength and U.S. Export Competitiveness

## Contributors
Prajeeta Dahal  
Shannon Choi  

---


## Summary

This project investigates the relationship between the strength of the United States Dollar (USD) and the competitiveness of U.S. exports. Specifically, we examine whether changes in the Real Trade Weighted U.S. Dollar Index (RTWEXBGS) are associated with changes in Real Exports of Goods and Services (EXPGS), and whether any such relationship has shifted in the post-2020 economy.

The economic background behind this research question is grounded in the concept of Exchange Rate Pass-Through: when the U.S. Dollar appreciates against trading-partner currencies, U.S.-produced goods become more expensive for foreign buyers, which should, in theory, reduce demand for American exports. However, amid heightened supply-chain disruptions, pandemic-driven demand shocks, and shifting global trade patterns, this mechanism is less certain, which motivated us to explore the data.

Our primary research question is: To what degree does a 5% increase in the Real Trade Weighted U.S. Dollar Index correlate with a decline in Real Exports over the following two fiscal quarters, and has this relationship shifted in the post-2020 economy?

We chose to work with data sourced from the Federal Reserve Economic Data (FRED) repository because it offers trustworthy, high-quality, and publicly accessible economic data. The Real Trade Weighted U.S. Dollar Index (RTWEXBGS) is published monthly by the Board of Governors of the Federal Reserve System and measures the inflation-adjusted value of the USD against a broad basket of trading-partner currencies. The Real Exports of Goods and Services (EXPGS) series is published quarterly by the U.S. Bureau of Economic Analysis (BEA) and captures the total inflation-adjusted value of all goods and services the U.S. sells abroad.

A central technical challenge in this project was reconciling the two datasets' different temporal granularities. The Dollar Index (RTWEXBGS) is reported monthly while Export data (EXPGS) is reported quarterly. We resolved this through a downsampling transformation in Python Pandas, computing the mean of the monthly Dollar Index values within each calendar quarter to produce a single quarterly observation. Both datasets were then aligned using a standardized quarterly period index before being merged via an inner join.

We used lag structures to better understand whether the relationship between currency strength and exports operates with a delay. We conducted correlation analysis between percentage changes in the dollar index and export values across different lag structures: constructed lagged versions of the export variable (lags 0 through 4 quarters), to test the hypothesis that USD appreciation has a delayed negative effect on export performance.

We found that the strongest negative correlation between USD change and export change appeared at lag 0 (r ≈ −0.47), indicating that USD appreciation and export decline do tend to occur in the same quarter rather than with a two-quarter delay. Correlations at longer lags were weak and inconsistent. When we split the sample into pre- and post-2020 periods, both sub-periods showed weak positive correlations (0.18 and 0.32, respectively), suggesting that structural economic shifts following the COVID-19 pandemic may have altered the traditional exchange-rate–trade relationship. The absence of a strong, persistent negative relationship challenges the convention that USD strength is a reliable leading indicator of export decline, and points toward the importance of other omitted confounding variables such as foreign GDP growth, trade tariffs, and global shipping costs.

## Summary of Individual Contributions

Prajeeta Dahal: I implemented the FRED API data acquisition scripts to retrieve the required datasets and performed data integration, including resampling the weekly dollar index into quarterly averages for alignment with export data. I conducted the correlation and lag analysis to evaluate the relationship between USD strength and exports under different model specifications. Additionally, I developed a reproducible workflow in Google Colab to ensure the analysis can be easily rerun and verified. I also contributed to documentation and report writing, and assisted in interpreting results and refining the overall analytical approach. I also developed and uploaded the profile quality, data dictionary, LISCENSE, uploaded the READMEmd file, and created the final project release tag. In the README.Md file, I helped write and summarize the sections on findings, challenges, future work, visualizations, reproducing steps, and the citations. 

Shannon Choi: I conducted a data quality assessment and looked for any missing values and inconsistencies in the data. Additionally, I debugged merge and lag alignment issues and developed a reproducible workflow in Google Colab. Finally, I also contributed to the documentation and report writing, while assisting in interpreting the results and refining our analysis. I specifically uploaded the IS477_Project_Code-2.py file, requirements.txt, metadata.json, IS477_Final_Project_Code.ipynb, and merged_dataset.csv files to the repository. In the README.md file, I wrote the data profile for RTWEXBGS and EXPGS datasets and also the data quality assessment for each. I added the findings on USD strength and export correlation and the challenges encountered.

---

## Data Profile

### Dataset 1: Real Trade Weighted U.S. Dollar Index (RTWEXBGS)

#### Source and Provenance

This dataset is retrieved from the Federal Reserve Economic Data (FRED) repository, a premier macroeconomic database maintained by the Federal Reserve Bank of St. Louis. The underlying data is produced by the Board of Governors of the Federal Reserve System (U.S.), the central banking authority of the United States. FRED is widely regarded as one of the most authoritative and reliable sources of U.S. macroeconomic data and is used extensively by academic researchers, government agencies, and financial institutions. The dataset is publicly accessible and freely available with an API key.

#### Format and Frequency

The data is a monthly time-series, with each observation representing the index value for a given month. Coverage spans from January 2006 to the February 2026, providing 243 rows of data.

#### Description and Variables

| Variable | Description |
|----------|------------|
| observation_date | Timestamp of observation (monthly, first day of each month) |
| RTWEXBGS | Inflation-adjusted USD strength index value relative to a broad basket of major trading partners |

#### Location in Repository

Shannon-Prajeeta-Final-Project-IS477 / Final Project / Datasets / RTWEXBGS.csv  
https://github.com/shannonchoi/Shannon-Prajeeta-Final-Project-IS477/blob/478155394cb4824b266b9b5f68e3eacc933fa61e/Final%20Project/Datasets/RTWEXBGS.csv

#### Ethical and Legal Constraints

The RTWEXBGS dataset is published by a U.S. federal government agency and is in the public domain. There are no redistribution restrictions. The primary ethical consideration is responsible use of the FRED API: our scripts include standard request handling to avoid excessive load on FRED's servers, in keeping with FRED's terms of service.

---

### Dataset 2: Real Exports of Goods and Services (EXPGS)

#### Source and Provenance

This dataset is also retrieved from FRED but is produced by the U.S. Bureau of Economic Analysis (BEA), the primary federal agency responsible for calculating U.S. Gross Domestic Product (GDP) and the National Income and Product Accounts (NIPA). The BEA applies rigorous federal standards for statistical accuracy. The EXPGS series is a component of GDP and is considered one of the definitive measures of U.S. international trade activity. It is subject to periodic revisions by the BEA, which is a known limitation for the most recent data points.

#### Format and Frequency

The data is a quarterly time-series. Each observation represents the total inflation-adjusted exports for a given quarter. Coverage spans from 1947 to October 2025, providing 320 quarterly observations.

#### Description and Variables

| Variable | Description |
|----------|------------|
| observation_date | Timestamp of observation (quarterly) |
| EXPGS | Inflation-adjusted total exports in billions of chained 2017 dollars |

#### Location in Repository

Shannon-Prajeeta-Final-Project-IS477 / Final Project / Datasets / EXPGS.csv  
https://github.com/shannonchoi/Shannon-Prajeeta-Final-Project-IS477/blob/9084cbd746440a5a627705ca98b97fece1c1796a/Final%20Project/Datasets/EXPGS.csv

#### Ethical and Legal Constraints

The EXPGS dataset is produced by a U.S. federal government agency and is in the public domain. No redistribution restrictions apply. The same API rate-limiting considerations apply as noted above.

---
## Dataset Integration and Relationship to Research Questions

Both datasets share a common temporal dimension, the observation_date, which serves as the integration key. The datasets are complementary by design: RTWEXBGS captures the independent variable (USD strength), and EXPGS captures the dependent variable (U.S. export volume). Together they allow us to test the theoretical Exchange Rate Pass-Through mechanism.

The primary integration challenge is the difference in reporting frequency (monthly vs. quarterly). We address this through downsampling: the monthly Dollar Index is aggregated to quarterly averages, giving each quarter a single representative USD index value that can be aligned with the corresponding export figure. After downsampling and temporal alignment, the merged dataset covers the period from 2006 Q1 through 2025 Q4, yielding approximately 80 rows of quarterly observations after dropping rows with missing values created by the lag transformation.

### Relationship to Research Questions

The primary research question (does USD appreciation correlate with a decline in exports two quarters later?) is directly addressed by computing the Pearson correlation between quarterly percentage changes in RTWEXBGS and lagged quarterly percentage changes in EXPGS.

The secondary question (has this relationship shifted post-2020?) is addressed by splitting the merged dataset at 2020Q1 and computing correlations within each sub-period.

# Data Quality

## Quality Assessment Overview

We conducted a systematic data quality assessment of both datasets following acquisition from the FRED API. Our assessment focused on four dimensions: completeness, consistency, accuracy, and timeliness.

### RTWEXBGS Quality Assessment

**Completeness:** After retrieving the full RTWEXBGS series programmatically, we inspected the resulting Pandas DataFrame for missing values (NaN). There were none.

**Consistency:** The series is internally consistent. The index is computed using a fixed methodology maintained by the Federal Reserve Board, and no structural breaks in the data-collection methodology are documented.

**Accuracy:** As a product of the U.S. Federal Reserve, the data meets rigorous institutional accuracy standards. No outliers were identified during quality assessment that could not be attributed to known macroeconomic events. These movements are genuine economic signals, not data errors.

**Timeliness:** The series is updated monthly with minimal lag (typically within a few days of the reference month). The most recent values are considered preliminary until confirmed in subsequent releases, but historical values are stable.

### EXPGS Quality Assessment

**Completeness:** The EXPGS series contained no missing quarterly observations across the full historical range. All expected quarters from 1947 Q1 through the most recent available period were present.

**Consistency:** The BEA periodically revises EXPGS estimates, sometimes substantially, as more complete source data becomes available. This means that the most recent 2–4 quarterly observations are subject to revision. For our analysis, which emphasizes historical relationships and does not rely on the most recent data point in isolation, this poses minimal risk.

**Accuracy:** The BEA is the authoritative source for national accounts data in the United States. The EXPGS figures are considered the gold standard for measuring U.S. export activity. No data accuracy issues were identified.

**Timeliness:** Quarterly data is typically released approximately one month after the reference quarter's end, with subsequent revisions over the following year. Our analysis uses the one available at the time of data acquisition.

### Post-Integration Quality Assessment

After merging the two datasets, we performed an additional quality check on the merged DataFrame:

- **Shape verification:** We confirmed the merged DataFrame had the expected number of rows (80 quarterly observations).
- **No spurious NaNs introduced by the merge:** The inner join on the period index ensured that only time periods present in both datasets were retained, eliminating any mismatch-induced missing values.
- **Lag-induced NaN handling:** The creation of lagged export variables (`shift()`) introduces NaN values at the beginning of the time series. These rows were explicitly dropped using `dropna()` before computing any correlations. (cleaned df has 79 rows)
- **Non-stationarity check:** Visual inspection of the raw RTWEXBGS and EXPGS time series confirmed the presence of long-run trends in both variables, confirming the need for percentage-change transformation before correlation analysis.

---
## Data Cleaning

### Overview

Because both datasets were sourced from high-quality, institutionally maintained repositories, the cleaning requirements were relatively modest but also important for ensuring the validity of our statistical analysis. The following cleaning steps were applied.

---

### Step 1: Temporal Index Standardization

**Issue:** After retrieving the datasets from the FRED API, the two DataFrames used different timestamp conventions. The Dollar Index used monthly timestamps (first day of each month), while the Export data used quarter-end timestamps. When we first attempted a direct merge on the date index, the result was an empty DataFrame with no timestamps matched exactly because one set ended on quarter-end dates and the other on monthly dates.

**Operation:** We converted both DataFrames to a standardized quarterly PeriodIndex using Pandas' `.to_period('Q')` method. For the Dollar Index, this was applied after downsampling to quarterly averages; for the Export data, it was applied directly. A PeriodIndex represents a quarter as a period (e.g., 2020Q1) rather than a specific timestamp, making it a better format and enabling a clean merge.

**Justification:** This is the best solution for merging time series of different frequencies because it takes away the specific timestamp anchor and works with the calendar period.

---

### Step 2: Downsampling from Monthly to Quarterly

**Issue:** RTWEXBGS is reported monthly, while EXPGS is reported quarterly. Analysis requires observations at the same temporal resolution.

**Operation:** We applied `.resample('Q').mean()` to the monthly Dollar Index DataFrame, computing the mean index value across all months falling within each calendar quarter. This produced a single quarterly representative value for the Dollar Index.

**Justification:** Using the mean (vs the quarter-end or quarter-start value) is appropriate because it represents the average currency conditions experienced throughout the quarter, which is more relevant to how exporters actually experience exchange rate fluctuations than a single snapshot at the quarter's end.

---

### Step 3: Lag Variable Construction

**Issue:** Our research hypothesis represents a delayed effect, meaning that we theorized the changes in the Dollar Index to impact exports with a lag of one to two quarters, as it takes time for exchange rate movements to flow through to actual trade volumes.

**Operation:** We created lagged versions of the EXPGS series using Pandas' `.shift(n)` method for lag values of 0 through 4 quarters. Each lagged variable was added as a new column before analysis.

**Justification:** Lag construction is a standard technique in macroeconomic time-series analysis for testing hypotheses about delayed transmission mechanisms.

---

### Step 4: Percentage Change Transformation

**Issue:** Both the RTWEXBGS and EXPGS series exhibit strong upward long-run trends. Computing Pearson correlations on the raw values of these trending series would produce high correlations driven by the shared upward trend rather than any genuine quarter-to-quarter relationship. This is the classic "spurious regression" problem in time-series econometrics.

**Operation:** We transformed both variables into quarter-over-quarter percentage changes using Pandas' `.pct_change()` method before computing any correlations.

**Justification:** Percentage change is the standard transformation for removing non-stationarity from macroeconomic time series because it converts level variables into growth-rate variables. This ensures that correlations reflect true contemporaneous or lagged co-movement between the variables, not just the shared trend.

---

### Step 5: Missing Value Removal

**Issue:** The lag and percentage change transformations introduce NaN values at the beginning of the time series (the first observation after shifting has no prior value to compute a change or lag from).

**Operation:** We called `.dropna()` on the merged DataFrame after all transformations were applied, removing rows with any missing values.

**Justification:** Pearson correlation cannot be computed on rows with NaN values. Removing these rows at the end of the transformation pipeline rather than at each intermediate step is efficient and ensures no valid observations are lost.

---

## Findings

### Baseline Correlation (No Lag)

We first examined the contemporaneous (no lag) relationship between quarterly percentage changes in USD strength and quarterly percentage changes in export value. The Pearson correlation was r ≈ 0.22, indicating a weak positive relationship. This result counters our initial hypothesis that if USD appreciation directly suppresses exports, we would expect a negative correlation. The weakness in this baseline correlation suggests that the Dollar Index alone is not a strong contemporaneous predictor of export performance.

### Lag Analysis

To investigate whether the relationship operates with a delay, we computed correlations between USD percentage change and lagged export percentage change for lags of 0 through 4 quarters. The results were as follows:

| Lag (Quarters) | Pearson r |
|----------------|-----------|
| 0              | −0.47     |
| 1              | 0.05      |
| 2              | 0.24      |
| 3              | 0.19      |
| 4              | 0.03      |

The strongest result was at lag 0 (r ≈ −0.47): a moderate negative correlation, indicating that quarters in which the USD appreciates tend to be the same quarters in which export growth slows or turns negative. This is consistent with the Exchange Rate Pass-Through theory operating within the same quarter, maybe even reflecting that some export contracts are priced in real time and that large changes in currency value have an immediate impact on demand.

Correlations at lags 1 through 4 were weak and inconsistent (near zero or positive), contradicting our initial two-quarter-lag hypothesis. This suggests that the delayed impact of USD strength on exports is not a stable or reliable empirical pattern at the aggregate national level over this time period, or at least when measured in percentage-change terms.

### Pre- and Post-2020 Analysis

To evaluate whether pandemic-era structural shifts altered the relationship, we split the sample at 2020 Q1:

- **Pre-2020 correlation** (percentage changes, no lag): r ≈ 0.18 — weak positive
- **Post-2020 correlation** (percentage changes, no lag): r ≈ 0.32 — weak positive

Both sub-periods show weak positive correlations, meaning that the moderate negative relationship observed at lag 0 in the full sample is not stable across time periods when examined this way. The modest increase in positive correlation post-2020 is consistent with the idea that during and after the pandemic, export volumes were driven more by extraordinary demand and supply-chain factors than by currency conditions. A dollar that was strong coincided with strong U.S. economic performance that also attracted export demand, which may explain the positive weak association.

### Visualization

A scatter plot of USD quarterly percentage change (x-axis) versus two-quarter-lagged export percentage change (y-axis) was produced and confirmed the absence of a strong linear relationship at lag 2, consistent with the near-zero correlation at that lag.

https://github.com/shannonchoi/Shannon-Prajeeta-Final-Project-IS477/blob/57abfcb85d3297eae3867f2a0be21be94cbf9e31/Final%20Project/Artifacts/usd_vs_exports_scatter.png 

<img width="1200" height="750" alt="usd_vs_exports_scatter" src="https://github.com/user-attachments/assets/79a1d786-be53-4482-9778-d83e515f2c45" />


---
## Future Work

### Addressing Confounding Variables

The most important limitation of this project is that it has a bivariate scope of the data, meaning it only focuses on two variables. The reality is that the real-world relationship between currency strength and export performance is embedded in a complex web of macroeconomic conditions that our model doesn't capture. Future work should incorporate additional explanatory variables such as foreign GDP growth rates for major trading partners (a stronger partner economy can offset the price disadvantage of a strong dollar), global commodity prices (especially for agricultural and energy exports, which are priced in dollars regardless of currency fluctuations), U.S. tariff policy and retaliatory foreign tariffs, shipping and logistics costs, and global demand indices.

An addition would be to build a multivariate regression model that treats exports and currency strength as jointly determined variables in a system, rather than assuming its one-way causal relationship.

### Sector Disaggregation

Our analysis treats all U.S. exports as a single aggregate figure, but different sectors of the economy respond to currency movements in different ways. Aircraft manufacturers, agricultural commodity exporters, and technology service exporters face very different competitive dynamics. Future work could use sector-level BEA export data to test whether the Exchange Rate Pass-Through effect is stronger in goods-intensive sectors (where price competition is direct) than in high-value-added services (where U.S. competitive advantages may insulate exporters from currency effects).

### Improved Time-Series Methodology

Our use of percentage-change transformations was a reasonable first step, but a more rigorous approach would involve formal unit root tests to confirm stationarity, followed by causality tests to assess statistical evidence for causal directionality. Dynamic correlation analysis could also reveal how the relationship evolves over time more precisely than the simple pre/post-2020 split.

### Expanding the Post-2020 Window

Our post-2020 analysis was limited by a small number of post-pandemic quarters available at the time of analysis (approximately 16 quarters). As more data accumulates, the structural shift hypothesis can be tested with greater statistical power.

### Workflow and Reproducibility Improvements

While our project is reproducible via a documented Colab notebook and FRED API, future iterations could benefit from a more formal workflow management system such as Snakemake, which would enable strict dependency tracking between pipeline stages (acquisition to integration to cleaning to analysis to visualization). This would make the pipeline easier to audit and extend.

### Metadata and FAIR Compliance

This project already includes a machine-readable metadata record in Schema.org format (metadata.json). A future version could expand this with a persistent DOI via Zenodo to make the project fully citable as a research artifact.

---

## Challenges

### Temporal Misalignment and Empty Merge

The most significant technical challenge was the initial failure of the dataset merge. When we first attempted to join RTWEXBGS and EXPGS on their date indices after retrieving them from the FRED API, the resulting DataFrame was empty. The root cause was a mismatch in timestamp formats: the dollar index used monthly timestamps while the export data used quarter-end timestamps. Despite representing the same calendar quarters, these timestamps did not match exactly. The solution was converting both series to a PeriodIndex with quarterly granularity.

### Lag Direction and NaN Propagation

Our initial lag implementation produced unexpected NaN values across the entire DataFrame rather than only at the first few rows. After debugging, we identified that the lag was being applied before the temporal alignment step, which interacted poorly with the PeriodIndex conversion. Re-ordering the operations by first aligning and merging, then applying the lag solved the issue.

### Non-Stationarity and Spurious Correlation

An important challenge was recognizing that correlating the raw (level) values of RTWEXBGS and EXPGS would produce meaningless results. Both series trend upward over time, so any correlation between them in levels would be spurious. Understanding and correctly applying the percentage-change transformation required us to engage with macroeconomic time-series concepts that were initially outside our comfort zone.

### Weak and Counterintuitive Results

The biggest challenge was accepting results that contradicted our initial hypothesis. The absence of a strong two-quarter-lag negative correlation forced us to evaluate the limitations of bivariate analysis in macroeconomics. Rather than treating this as a failure, we framed it as a finding: the exchange rate pass-through mechanism at the aggregate national level is not as cleanly observable as theoretical models suggest, and confounding variables play a substantial role.

---

## Project Structure

Final Project/
├── Artifacts/
│   ├── data_dictionary.md
│   ├── metadata.json
│   ├── profile_quality.py
│   ├── requirements.txt
│   └── usd_vs_exports_scatter.png
│
├── Code/
│   ├── IS477_Final_Project_Code.ipynb
│   └── IS477_RUN_Final_Project_Code.py
│
├── Datasets/
│   ├── RTWEXBGS.csv
│   ├── EXPGS.csv
│   └── merged_dataset.csv
│
├── Final Project Report/
│   └── README.md
│
├── Project Plan/
│
└── Status Report/

## Workflow Overview

1. Data Acquisition

   * Source: FRED or included CSV files
   * Files: `RTWEXBGS.csv`, `EXPGS.csv`

2. Data Integration & Cleaning

   * Script: `IS477_RUN_Final_Project_Code.py`
   * Output: `outputs/merged_dataset.csv`

3. Analysis & Visualization

   * Script: `IS477_RUN_Final_Project_Code.py`
   * Output: `outputs/usd_vs_exports_scatter.png`


## Reproducing

### Step 1: Clone the Repository

```bash
git clone https://github.com/shannonchoi/Shannon-Prajeeta-Final-Project-IS477.git
cd Shannon-Prajeeta-Final-Project-IS477
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Your FRED API Key

In the file (`IS477_RUN_Final_Project_Code.py`), locate the line:

```python
fred = Fred(api_key='YOUR_API_KEY_HERE')
```

Make sure to replace `'YOUR_API_KEY_HERE'` with your personal FRED API key after opening the notebook and before running the cell.

### Step 4: Run the Notebook

Open `IS477_RUN_Final_Project_Code.py` in Google Colab or Jupyter and run all cells in order. We uploaded the intended output in `IS477_Final_Project_Code.ipynb` for reference. The notebook is structured sequentially:

1. Install fredapi
2. Import libraries
3. Connect to FRED API
4. Acquire RTWEXBGS (monthly) and EXPGS (quarterly)
5. Resample RTWEXBGS to quarterly averages and convert both to PeriodIndex
6. Create lag variable (2-quarter lag on EXPGS) and perform inner join merge
7. Compute percentage changes for both variables
8. Drop missing values
9. Compute and print baseline Pearson correlation (lag 2)
10. Generate scatter plot (USD % Change vs. Lagged Exports % Change)
11. Split into pre-2020 / post-2020 subsets and compute sub-period correlations
12. Loop through lags 0–4, compute and print Pearson r for each

Alternatively, the raw data files (`RTWEXBGS.csv` and `EXPGS.csv`) are included in this repository and can be loaded directly without an API key if you modify the acquisition cells accordingly.

### Expected Outputs

- Printed correlation coefficient for lag-2 specification
- Scatter plot: USD % Change (x) vs. Exports % Change – Lagged 2Q (y)
- Printed pre-2020 and post-2020 correlation values
- Printed Pearson r values for lags 0 through 4

> **Note on Data Recency:** Because data is fetched live from the FRED API at runtime, results may differ marginally from those reported here if the BEA has revised recent EXPGS estimates since this report was written. The historical relationships (pre-2020) should be stable.

---

## References

1. Board of Governors of the Federal Reserve System (US). *Real Trade Weighted U.S. Dollar Index: Broad, Goods and Services* [RTWEXBGS]. Federal Reserve Bank of St. Louis, FRED Economic Data. https://fred.stlouisfed.org/series/RTWEXBGS
2. U.S. Bureau of Economic Analysis. *Real Exports of Goods and Services* [EXPGS]. Federal Reserve Bank of St. Louis, FRED Economic Data. https://fred.stlouisfed.org/series/EXPGS
3. McKinney, Wes. *Data Structures for Statistical Computing in Python.* Proceedings of the 9th Python in Science Conference, 2010. (pandas library)
4. Hunter, J.D. *Matplotlib: A 2D Graphics Environment.* Computing in Science & Engineering, Vol. 9, No. 3, pp. 90–95, 2007.
5. Federal Reserve Bank of St. Louis. *FRED API Documentation.* https://fred.stlouisfed.org/docs/api/fred/
6. Goldberg, L.S., & Knetter, M.M. *Goods Prices and Exchange Rates: What Have We Learned?* Journal of Economic Literature, 35(3), 1243–1272, 1997.
7. Campa, J.M., & Goldberg, L.S. *Exchange Rate Pass-Through into Import Prices.* The Review of Economics and Statistics, 87(4), 679–690, 2005.
8. fredapi Python library: https://github.com/mortada/fredapi

