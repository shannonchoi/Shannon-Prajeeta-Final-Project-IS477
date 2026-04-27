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

Shannon-Prajeeta-Final-Project-IS477 / RTWEXBGS.csv  
https://github.com/shannonchoi/Shannon-Prajeeta-Final-Project-IS477/blob/46fb570fb34b9b9c2d303a20405bb63c517a299e/RTWEXBGS.csv  

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

Shannon-Prajeeta-Final-Project-IS477 / EXPGS.csv  
https://github.com/shannonchoi/Shannon-Prajeeta-Final-Project-IS477/blob/46fb570fb34b9b9c2d303a20405bb63c517a299e/EXPGS.csv  

#### Ethical and Legal Constraints

The EXPGS dataset is produced by a U.S. federal government agency and is in the public domain. No redistribution restrictions apply. The same API rate-limiting considerations apply as noted above.

---
## Dataset Integration and Relationship to Research Questions

Both datasets share a common temporal dimension, the observation_date, which serves as the integration key. The datasets are complementary by design: RTWEXBGS captures the independent variable (USD strength), and EXPGS captures the dependent variable (U.S. export volume). Together they allow us to test the theoretical Exchange Rate Pass-Through mechanism.

The primary integration challenge is the difference in reporting frequency (monthly vs. quarterly). We address this through downsampling: the monthly Dollar Index is aggregated to quarterly averages, giving each quarter a single representative USD index value that can be aligned with the corresponding export figure. After downsampling and temporal alignment, the merged dataset covers the period from 2026 Q1 through 2025 Q4, yielding approximately 80 rows of quarterly observations after dropping rows with missing values created by the lag transformation.

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
