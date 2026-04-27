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
