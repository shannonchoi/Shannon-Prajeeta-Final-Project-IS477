# IS477 Final Project: USD Strength vs. U.S. Export Competitiveness
# Authors: Prajeeta Dahal, Shannon Choi
#
# This script acquires data from the FRED API, integrates and cleans the datasets,
# runs correlation and lag analysis, saves output files, and prints a SHA-256
# checksum of the merged dataset for reproducibility verification.
#
# Run: pip install fredapi pandas matplotlib
# Then set your FRED API key below before running.

# ── 0. Install (uncomment if running in Colab) ────────────────────────────────
# !pip install fredapi

# ── 1. Imports ────────────────────────────────────────────────────────────────
import hashlib
import os
import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

# ── 2. Configuration ──────────────────────────────────────────────────────────
# Replace with your own free FRED API key from https://fred.stlouisfed.org/docs/api/api_key.html
FRED_API_KEY = 'YOUR_API_KEY_HERE'

# Output directory — will be created if it doesn't exist
OUTPUT_DIR = 'outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── 3. Data Acquisition ───────────────────────────────────────────────────────
print("Acquiring data from FRED API...")
fred = Fred(api_key=FRED_API_KEY)

# Real Trade Weighted USD Index (monthly)
dollar = fred.get_series('RTWEXBGS')
dollar = dollar.to_frame(name='RTWEXBGS')
dollar.index = pd.to_datetime(dollar.index)

# Real Exports of Goods and Services (quarterly)
exports = fred.get_series('EXPGS')
exports = exports.to_frame(name='EXPGS')
exports.index = pd.to_datetime(exports.index)

print(f"  RTWEXBGS: {len(dollar)} monthly observations")
print(f"  EXPGS:    {len(exports)} quarterly observations")

# ── 4. Data Integration ───────────────────────────────────────────────────────
print("\nIntegrating datasets...")

# Downsample monthly Dollar Index to quarterly averages
dollar_q = dollar.resample('Q').mean()
dollar_q.index = dollar_q.index.to_period('Q')

# Convert exports to quarterly PeriodIndex (resolves timestamp mismatch)
exports.index = exports.index.to_period('Q')

# Create 2-quarter lag on exports (original hypothesis)
exports['EXPGS_lag2'] = exports['EXPGS'].shift(2)

# Inner join on aligned quarterly PeriodIndex
merged = pd.merge(dollar_q, exports, left_index=True, right_index=True, how='inner')
print(f"  Merged shape: {merged.shape}")

# ── 5. Data Cleaning & Transformation ─────────────────────────────────────────
print("\nApplying transformations...")

# Percentage change to address non-stationarity
merged['usd_pct']     = merged['RTWEXBGS'].pct_change()
merged['exports_pct'] = merged['EXPGS_lag2'].pct_change()

# Drop NaNs introduced by shift() and pct_change()
merged = merged.dropna()
print(f"  Clean merged shape (after dropna): {merged.shape}")

# ── 6. Save Merged Dataset ────────────────────────────────────────────────────
csv_path = os.path.join(OUTPUT_DIR, 'merged_dataset.csv')
merged.to_csv(csv_path)
print(f"\nSaved merged dataset to: {csv_path}")

# SHA-256 integrity check
with open(csv_path, 'rb') as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()
print(f"  SHA-256 checksum: {file_hash}")
print("  (Save this checksum to verify the file hasn't changed when reproducing results.)")

# ── 7. Analysis: Baseline Correlation ─────────────────────────────────────────
print("\n── Baseline Correlation (lag-2 specification) ──")
baseline_corr = merged['usd_pct'].corr(merged['exports_pct'])
print(f"  Pearson r (USD % change vs. 2Q-lagged exports % change): {baseline_corr:.4f}")

# ── 8. Analysis: Lag 0–4 Correlations ─────────────────────────────────────────
print("\n── Lag Analysis (lags 0–4 quarters) ──")
lag_results = {}
for i in range(5):
    lagged_exports = merged['EXPGS'].shift(i).pct_change()
    # Align index with usd_pct
    combined = pd.concat([merged['usd_pct'], lagged_exports], axis=1).dropna()
    combined.columns = ['usd_pct', f'exports_lag{i}']
    r = combined['usd_pct'].corr(combined[f'exports_lag{i}'])
    lag_results[i] = r
    print(f"  Lag {i}: r = {r:.4f}")

# ── 9. Analysis: Pre- and Post-2020 ───────────────────────────────────────────
print("\n── Pre/Post-2020 Analysis (no lag, percentage change) ──")
pre_2020  = merged[merged.index < '2020Q1']
post_2020 = merged[merged.index >= '2020Q1']

pre_corr  = pre_2020['usd_pct'].corr(pre_2020['exports_pct'])
post_corr = post_2020['usd_pct'].corr(post_2020['exports_pct'])
print(f"  Pre-2020  r: {pre_corr:.4f}  ({len(pre_2020)} quarters)")
print(f"  Post-2020 r: {post_corr:.4f}  ({len(post_2020)} quarters)")

# ── 10. Visualization: Scatter Plot ───────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(merged['usd_pct'], merged['exports_pct'], alpha=0.6, edgecolors='none')
ax.set_xlabel('USD % Change (Quarterly)')
ax.set_ylabel('Exports % Change (Lagged 2 Quarters)')
ax.set_title('USD Strength vs. U.S. Exports (2-Quarter Lag)')
ax.axhline(0, color='gray', linewidth=0.8, linestyle='--')
ax.axvline(0, color='gray', linewidth=0.8, linestyle='--')
plt.tight_layout()

plot_path = os.path.join(OUTPUT_DIR, 'usd_vs_exports_scatter.png')
plt.savefig(plot_path, dpi=150)
plt.show()
print(f"\nSaved scatter plot to: {plot_path}")

print("\n── Analysis complete. All outputs saved to the 'outputs/' folder. ──")
