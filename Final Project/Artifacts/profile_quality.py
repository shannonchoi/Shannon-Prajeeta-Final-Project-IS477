# IS477 Final Project: Data Quality Profiling Script
# Authors: Prajeeta Dahal, Shannon Choi
#
# This script profiles the raw RTWEXBGS and EXPGS datasets before any
# integration or transformation. Run this independently to reproduce
# the data quality assessment documented in README.md.
#
# Run: pip install fredapi pandas
# Then set your FRED API key below.

# ── 0. Install (uncomment if running in Colab) ────────────────────────────────
# !pip install fredapi

# ── 1. Imports ────────────────────────────────────────────────────────────────
import pandas as pd
from fredapi import Fred

# ── 2. Configuration ──────────────────────────────────────────────────────────
FRED_API_KEY = 'YOUR_API_KEY_HERE'

# ── 3. Acquire Raw Data ───────────────────────────────────────────────────────
fred = Fred(api_key=FRED_API_KEY)

dollar  = fred.get_series('RTWEXBGS').to_frame(name='RTWEXBGS')
exports = fred.get_series('EXPGS').to_frame(name='EXPGS')

dollar.index  = pd.to_datetime(dollar.index)
exports.index = pd.to_datetime(exports.index)

# ── 4. Profile: RTWEXBGS ──────────────────────────────────────────────────────
print("=" * 55)
print("RTWEXBGS — Real Trade Weighted U.S. Dollar Index")
print("=" * 55)
print(f"Frequency:         Monthly")
print(f"Total observations:{len(dollar):>6}")
print(f"Date range:        {dollar.index.min().date()} → {dollar.index.max().date()}")
print(f"\nMissing values:    {dollar['RTWEXBGS'].isna().sum()}")
print(f"Missing %:         {dollar['RTWEXBGS'].isna().mean() * 100:.2f}%")
print(f"\nDescriptive statistics:")
print(dollar['RTWEXBGS'].describe().round(4).to_string())

# Flag potential outliers (values beyond 3 standard deviations from mean)
mean_d  = dollar['RTWEXBGS'].mean()
std_d   = dollar['RTWEXBGS'].std()
outliers_d = dollar[(dollar['RTWEXBGS'] < mean_d - 3*std_d) |
                    (dollar['RTWEXBGS'] > mean_d + 3*std_d)]
print(f"\nPotential outliers (>3 std devs from mean): {len(outliers_d)}")
if len(outliers_d) > 0:
    print(outliers_d)

# ── 5. Profile: EXPGS ─────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("EXPGS — Real Exports of Goods and Services")
print("=" * 55)
print(f"Frequency:         Quarterly")
print(f"Total observations:{len(exports):>6}")
print(f"Date range:        {exports.index.min().date()} → {exports.index.max().date()}")
print(f"\nMissing values:    {exports['EXPGS'].isna().sum()}")
print(f"Missing %:         {exports['EXPGS'].isna().mean() * 100:.2f}%")
print(f"\nDescriptive statistics:")
print(exports['EXPGS'].describe().round(4).to_string())

# Flag potential outliers
mean_e  = exports['EXPGS'].mean()
std_e   = exports['EXPGS'].std()
outliers_e = exports[(exports['EXPGS'] < mean_e - 3*std_e) |
                     (exports['EXPGS'] > mean_e + 3*std_e)]
print(f"\nPotential outliers (>3 std devs from mean): {len(outliers_e)}")
if len(outliers_e) > 0:
    print(outliers_e)

# ── 6. Check for duplicate dates ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("Duplicate Date Check")
print("=" * 55)
print(f"RTWEXBGS duplicate dates: {dollar.index.duplicated().sum()}")
print(f"EXPGS duplicate dates:    {exports.index.duplicated().sum()}")

print("\n── Quality profiling complete. ──")
