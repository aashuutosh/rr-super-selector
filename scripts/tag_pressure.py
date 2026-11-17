import pandas as pd
import numpy as np

# Load data
print("Loading data...")
bbb = pd.read_csv('D:/Data Pack/ball_by_ball.csv')
matches = pd.read_csv('D:/Data Pack/matches.csv')
comps = pd.read_csv('D:/Data Pack/competitions.csv')

# Merge match & comp metadata
bbb = bbb.merge(matches[['match_id', 'comp_id', 'knock_out', 'win_team_id', 'result', 'revised_target']], on='match_id', how='left')
bbb = bbb.merge(comps[['comp_id', 'match_format', 'season', 'comp_name']], on='comp_id', how='left')

# Sort chronologically
bbb = bbb.sort_values(['match_id', 'innings', 'innings_ball_num']).reset_index(drop=True)

# Total runs on each delivery
bbb['total_ball_runs'] = bbb['runs'] + bbb['extras1_runs'] + bbb['extras_2_runs']
bbb['is_legal_ball'] = ~bbb['extras_type'].isin(['wide', 'Overstep'])

# Cumulative runs and wickets within each innings
bbb['cum_runs'] = bbb.groupby(['match_id', 'innings'])['total_ball_runs'].cumsum()
bbb['cum_wickets'] = bbb.groupby(['match_id', 'innings'])['is_wicket'].cumsum()

# Score and wickets before current delivery
bbb['score_before'] = bbb.groupby(['match_id', 'innings'])['cum_runs'].shift(1).fillna(0)
bbb['wickets_before'] = bbb.groupby(['match_id', 'innings'])['cum_wickets'].shift(1).fillna(0)

# Legal balls bowled and balls remaining
bbb['cum_legal_balls'] = bbb.groupby(['match_id', 'innings'])['is_legal_ball'].cumsum()
bbb['legal_balls_before'] = bbb.groupby(['match_id', 'innings'])['cum_legal_balls'].shift(1).fillna(0)
bbb['balls_remaining'] = np.maximum(0, 120 - bbb['legal_balls_before'])

# Innings 1 total score per match
inn1_totals = bbb[bbb['innings'] == 1].groupby('match_id')['total_ball_runs'].sum().reset_index().rename(columns={'total_ball_runs': 'inn1_total'})
bbb = bbb.merge(inn1_totals, on='match_id', how='left')

# Target for innings 2
bbb['target'] = np.where(bbb['revised_target'].notna(), bbb['revised_target'], bbb['inn1_total'] + 1)
bbb['runs_needed'] = np.where(bbb['innings'] == 2, np.maximum(0, bbb['target'] - bbb['score_before']), np.nan)
bbb['rrr'] = np.where((bbb['innings'] == 2) & (bbb['balls_remaining'] > 0), (bbb['runs_needed'] / bbb['balls_remaining']) * 6, np.nan)

# ============================================================
# COMPREHENSIVE DEFINITION OF PRESSURE SITUATION
# ============================================================
# 1. Death overs (overs 17-20) in both innings
#    (For Innings 2: game must still be live, i.e., runs_needed > 0 and rrr <= 24)
# 2. High-pressure chase (Innings 2, overs 11-16 with RRR >= 9.0 and RRR <= 20.0)
# 3. Collapse recovery (Overs 1-10 with wickets_before >= 3)
# 4. Knockout matches (overid >= 11 in knockout matches, or anytime wickets_before >= 2)

cond_death_inn1 = (bbb['innings'] == 1) & (bbb['overid'] >= 17)
cond_death_inn2 = (bbb['innings'] == 2) & (bbb['overid'] >= 17) & (bbb['runs_needed'] > 0) & (bbb['rrr'] <= 24)
cond_chase_pressure = (bbb['innings'] == 2) & (bbb['overid'].between(11, 16)) & (bbb['rrr'] >= 9.0) & (bbb['rrr'] <= 20.0)
cond_collapse = (bbb['overid'] <= 10) & (bbb['wickets_before'] >= 3)
cond_knockout = (bbb['knock_out'] == 1) & (bbb['overid'] >= 11)

bbb['is_pressure'] = (cond_death_inn1 | cond_death_inn2 | cond_chase_pressure | cond_collapse | cond_knockout).astype(int)

print(f"Total balls: {len(bbb)}")
print(f"Total pressure balls: {bbb['is_pressure'].sum()} ({bbb['is_pressure'].mean()*100:.1f}%)")
print(f"  - Death Inn 1: {cond_death_inn1.sum()}")
print(f"  - Death Inn 2 (live): {cond_death_inn2.sum()}")
print(f"  - Chase pressure (ov 11-16, RRR>=9): {cond_chase_pressure.sum()}")
print(f"  - Collapse recovery (ov <=10, wkts>=3): {cond_collapse.sum()}")
print(f"  - Knockout high stakes: {cond_knockout.sum()}")

# Save intermediate pickle
bbb.to_pickle('C:/Users/ADMIN/.gemini/antigravity/brain/4b0fe19f-3d16-4370-8aff-b5a2fb22e3dc/scratch/bbb_pressure_tagged.pkl')
print("Saved tagged pickle successfully.")
