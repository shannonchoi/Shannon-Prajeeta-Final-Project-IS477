# Data Dictionary

This document describes the variables in each dataset used in this project, as well as the variables created during data integration and analysis.

---

## Dataset 1: Real Trade Weighted U.S. Dollar Index (RTWEXBGS)

**Source:** Federal Reserve Bank of St. Louis (FRED)  
**Original Producer:** Board of Governors of the Federal Reserve System (US)  
**Frequency:** Monthly  
**Format:** Time-series, CSV-compatible via FRED API  
**License:** Public domain (U.S. federal government)  
**FRED URL:** https://fred.stlouisfed.org/series/RTWEXBGS

| Variable | Type | Description | Units | Notes |
|---|---|---|---|---|
| observation_date | datetime | Date of the observation | Monthly (first of month) | Retrieved as Pandas DatetimeIndex |
| RTWEXBGS | float | Inflation-adjusted U.S. Dollar index value relative to a broad basket of major trading-partner currencies | Index (base period = January 2006) | "Real" = adjusted for consumer price inflation differences between the U.S. and trading partners. Higher value = stronger USD. |

---

## Dataset 2: Real Exports of Goods and Services (EXPGS)

**Source:** Federal Reserve Bank of St. Louis (FRED)  
**Original Producer:** U.S. Bureau of Economic Analysis (BEA)  
**Frequency:** Quarterly  
**Format:** Time-series, CSV-compatible via FRED API  
**License:** Public domain (U.S. federal government)  
**FRED URL:** https://fred.stlouisfed.org/series/EXPGS

| Variable | Type | Description | Units | Notes |
|---|---|---|---|---|
| observation_date | datetime | Date of the observation | Quarterly | Retrieved as Pandas DatetimeIndex; converted to PeriodIndex during processing |
| EXPGS | float | Total inflation-adjusted value of all U.S. goods and services sold to foreign buyers | Billions of chained 2017 U.S. dollars | Subject to periodic revision by BEA; most recent 2–4 quarters may be revised |

---

## Merged / Derived Dataset (created in IS477_Project_Code.py)

After integration and transformation, the following variables exist in the merged DataFrame used for analysis:

| Variable | Type | Description | Source | Notes |
|---|---|---|---|---|
| RTWEXBGS | float | Quarterly average of the monthly Dollar Index | Derived from RTWEXBGS via `.resample('Q').mean()` | Represents average USD strength across all months in a given quarter |
| EXPGS | float | Quarterly real exports value | EXPGS | Raw level value retained for lag construction |
| EXPGS_lag2 | float | EXPGS shifted forward by 2 quarters | Derived via `.shift(2)` | Used in initial lag-2 hypothesis test |
| usd_pct | float | Quarter-over-quarter percentage change in RTWEXBGS | Derived via `.pct_change()` | Used in all correlation calculations; removes non-stationarity |
| exports_pct | float | Quarter-over-quarter percentage change in EXPGS_lag2 | Derived via `.pct_change()` | Used in baseline correlation |
| lag_1 through lag_4 | float | EXPGS shifted by 1–4 quarters respectively | Derived via `.shift(n)` | Used in extended lag analysis |

---

## Notes on Integration

- Both datasets were converted to a quarterly `PeriodIndex` (e.g., "2020Q1") before merging to resolve timestamp format mismatches.
- The merge was performed as an **inner join** on the quarterly period index, retaining only quarters present in both datasets.
- All rows with `NaN` values (introduced by `.shift()` and `.pct_change()`) were removed with `.dropna()` before correlation analysis.
- Final merged dataset covers approximately 1973 Q1 – 2024 Q4 (~200 quarterly observations after cleaning).
