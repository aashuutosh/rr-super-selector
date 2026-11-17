import pandas as pd
import numpy as np

# Load tagged data
bbb = pd.read_pickle('C:/Users/ADMIN/.gemini/antigravity/brain/4b0fe19f-3d16-4370-8aff-b5a2fb22e3dc/scratch/bbb_pressure_tagged.pkl')

def z(series):
    std = series.std()
    return (series - series.mean()) / (std if std > 1e-9 else 1.0)

# ============================================================
# 1. BATTING RATING FORMULATION
# ============================================================
# Overall
total_bat = bbb.groupby(['striker_id', 'striker_name']).agg(
    total_balls=('runs', 'count'),
    total_runs=('runs', 'sum'),
    total_fours=('is_four', 'sum'),
    total_sixes=('is_six', 'sum'),
    total_outs=('is_wicket', 'sum'),
    total_dots=('runs', lambda x: (x == 0).sum()),
    matches=('match_id', 'nunique')
).reset_index()
total_bat['sr_total'] = (total_bat['total_runs'] / total_bat['total_balls'] * 100).round(2)
total_bat['avg_total'] = (total_bat['total_runs'] / total_bat['total_outs'].replace(0, np.nan)).round(2)

# Pressure
press_bat = bbb[bbb['is_pressure'] == 1].groupby(['striker_id', 'striker_name']).agg(
    press_balls=('runs', 'count'),
    press_runs=('runs', 'sum'),
    press_fours=('is_four', 'sum'),
    press_sixes=('is_six', 'sum'),
    press_outs=('is_wicket', 'sum'),
    press_dots=('runs', lambda x: (x == 0).sum()),
    press_matches=('match_id', 'nunique')
).reset_index()
press_bat['sr_press'] = (press_bat['press_runs'] / press_bat['press_balls'] * 100).round(2)
press_bat['avg_press'] = (press_bat['press_runs'] / press_bat['press_outs'].replace(0, np.nan)).fillna(press_bat['press_runs']).round(2)
press_bat['bndry_pct_press'] = ((press_bat['press_fours'] + press_bat['press_sixes']) / press_bat['press_balls'] * 100).round(2)
press_bat['dot_pct_press'] = (press_bat['press_dots'] / press_bat['press_balls'] * 100).round(2)

# Non-pressure (Baseline)
base_bat = bbb[bbb['is_pressure'] == 0].groupby(['striker_id', 'striker_name']).agg(
    base_balls=('runs', 'count'),
    base_runs=('runs', 'sum'),
    base_fours=('is_four', 'sum'),
    base_sixes=('is_six', 'sum'),
    base_outs=('is_wicket', 'sum'),
    base_dots=('runs', lambda x: (x == 0).sum())
).reset_index()
base_bat['sr_base'] = (base_bat['base_runs'] / base_bat['base_balls'] * 100).round(2)
base_bat['avg_base'] = (base_bat['base_runs'] / base_bat['base_outs'].replace(0, np.nan)).fillna(base_bat['base_runs']).round(2)
base_bat['bndry_pct_base'] = ((base_bat['base_fours'] + base_bat['base_sixes']) / base_bat['base_balls'] * 100).round(2)

# Consistency: per-innings coefficient of variation in pressure situations
press_innings = bbb[bbb['is_pressure'] == 1].groupby(['match_id', 'striker_id', 'striker_name'])['runs'].sum().reset_index()
consist_bat = press_innings.groupby(['striker_id', 'striker_name']).agg(
    innings_count=('runs', 'count'),
    mean_press_runs=('runs', 'mean'),
    std_press_runs=('runs', 'std')
).reset_index()
consist_bat['cv_press'] = (consist_bat['std_press_runs'] / consist_bat['mean_press_runs'].replace(0, np.nan)).fillna(1.0).round(3)

# Merge batting
b_all = total_bat.merge(press_bat, on=['striker_id', 'striker_name'], how='inner')
b_all = b_all.merge(base_bat, on=['striker_id', 'striker_name'], how='left')
b_all = b_all.merge(consist_bat[['striker_id', 'striker_name', 'cv_press']], on=['striker_id', 'striker_name'], how='left')

# Filter qualified batters
b_qual = b_all[(b_all['press_balls'] >= 60) & (b_all['total_balls'] >= 180)].copy()

# Elevation deltas
b_qual['delta_sr'] = b_qual['sr_press'] - b_qual['sr_base']
b_qual['delta_bndry'] = b_qual['bndry_pct_press'] - b_qual['bndry_pct_base']
b_qual['log_volume'] = np.log(b_qual['press_balls'])

# Calculate Batting Pressure Score (BPS)
b_qual['z_sr_press'] = z(b_qual['sr_press'])
b_qual['z_avg_press'] = z(b_qual['avg_press'].clip(upper=75)) # clip extreme outlier averages from not-outs
b_qual['z_delta_sr'] = z(b_qual['delta_sr'])
b_qual['z_delta_bndry'] = z(b_qual['delta_bndry'])
b_qual['z_volume'] = z(b_qual['log_volume'])
b_qual['z_consist'] = -z(b_qual['cv_press'].fillna(1.0))

b_qual['BPS'] = (
    b_qual['z_sr_press'] * 0.25 +
    b_qual['z_avg_press'] * 0.15 +
    b_qual['z_delta_sr'] * 0.25 +
    b_qual['z_delta_bndry'] * 0.10 +
    b_qual['z_volume'] * 0.15 +
    b_qual['z_consist'] * 0.10
).round(3)

top10_batters = b_qual.sort_values('BPS', ascending=False).reset_index(drop=True)
print("=== TOP 15 BATTERS UNDER PRESSURE (BPS) ===")
cols_bat = ['striker_name', 'press_balls', 'sr_base', 'sr_press', 'delta_sr', 'avg_press', 'press_sixes', 'cv_press', 'BPS']
print(top10_batters[cols_bat].head(15).to_string())

# ============================================================
# 2. BOWLING RATING FORMULATION
# ============================================================
total_bowl = bbb.groupby(['bowler_id', 'bowler_name']).agg(
    total_balls=('runs', 'count'),
    total_runs_conceded=('total_ball_runs', 'sum'),
    total_wkts=('is_wicket', 'sum'),
    total_dots=('runs', lambda x: (x == 0).sum()),
    matches=('match_id', 'nunique')
).reset_index()
total_bowl['econ_total'] = (total_bowl['total_runs_conceded'] / total_bowl['total_balls'] * 6).round(2)

press_bowl = bbb[bbb['is_pressure'] == 1].groupby(['bowler_id', 'bowler_name']).agg(
    press_balls=('runs', 'count'),
    press_runs_conceded=('total_ball_runs', 'sum'),
    press_wkts=('is_wicket', 'sum'),
    press_dots=('runs', lambda x: (x == 0).sum()),
    press_matches=('match_id', 'nunique')
).reset_index()
press_bowl['econ_press'] = (press_bowl['press_runs_conceded'] / press_bowl['press_balls'] * 6).round(2)
press_bowl['sr_press'] = (press_bowl['press_balls'] / press_bowl['press_wkts'].replace(0, np.nan)).fillna(99.0).round(2)
press_bowl['dot_pct_press'] = (press_bowl['press_dots'] / press_bowl['press_balls'] * 100).round(2)

base_bowl = bbb[bbb['is_pressure'] == 0].groupby(['bowler_id', 'bowler_name']).agg(
    base_balls=('runs', 'count'),
    base_runs_conceded=('total_ball_runs', 'sum'),
    base_wkts=('is_wicket', 'sum')
).reset_index()
base_bowl['econ_base'] = (base_bowl['base_runs_conceded'] / base_bowl['base_balls'] * 6).round(2)

# Merge bowling
bw_all = total_bowl.merge(press_bowl, on=['bowler_id', 'bowler_name'], how='inner')
bw_all = bw_all.merge(base_bowl, on=['bowler_id', 'bowler_name'], how='left')

# Filter qualified bowlers
bw_qual = bw_all[(bw_all['press_balls'] >= 60) & (bw_all['total_balls'] >= 180)].copy()

# Relative tightening: positive delta_econ means bowler was MORE economical under pressure than base
bw_qual['delta_econ'] = bw_qual['econ_base'] - bw_qual['econ_press']
bw_qual['log_volume'] = np.log(bw_qual['press_balls'])

# Calculate Bowling Pressure Score (BPS_bowl)
bw_qual['z_econ_press'] = -z(bw_qual['econ_press']) # lower is better
bw_qual['z_wkts_press'] = z(bw_qual['press_wkts'])
bw_qual['z_delta_econ'] = z(bw_qual['delta_econ']) # positive is better
bw_qual['z_dot_pct'] = z(bw_qual['dot_pct_press'])
bw_qual['z_sr_press'] = -z(bw_qual['sr_press'].clip(upper=40)) # lower balls/wicket is better
bw_qual['z_volume'] = z(bw_qual['log_volume'])

bw_qual['BPS_bowl'] = (
    bw_qual['z_econ_press'] * 0.25 +
    bw_qual['z_wkts_press'] * 0.20 +
    bw_qual['z_delta_econ'] * 0.15 +
    bw_qual['z_dot_pct'] * 0.15 +
    bw_qual['z_sr_press'] * 0.15 +
    bw_qual['z_volume'] * 0.10
).round(3)

top10_bowlers = bw_qual.sort_values('BPS_bowl', ascending=False).reset_index(drop=True)
print("\n=== TOP 15 BOWLERS UNDER PRESSURE (BPS_bowl) ===")
cols_bowl = ['bowler_name', 'press_balls', 'econ_base', 'econ_press', 'delta_econ', 'press_wkts', 'sr_press', 'dot_pct_press', 'BPS_bowl']
print(top10_bowlers[cols_bowl].head(15).to_string())

# Save both rankings
top10_batters.to_csv('C:/Users/ADMIN/.gemini/antigravity/brain/4b0fe19f-3d16-4370-8aff-b5a2fb22e3dc/scratch/ranked_batters_final.csv', index=False)
top10_bowlers.to_csv('C:/Users/ADMIN/.gemini/antigravity/brain/4b0fe19f-3d16-4370-8aff-b5a2fb22e3dc/scratch/ranked_bowlers_final.csv', index=False)
print("\nFinal rankings saved successfully.")
