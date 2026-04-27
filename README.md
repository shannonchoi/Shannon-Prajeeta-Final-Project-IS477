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
