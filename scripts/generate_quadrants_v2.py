import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.family'] = 'Segoe UI'

SCRATCH = 'C:/Users/ADMIN/.gemini/antigravity/brain/4b0fe19f-3d16-4370-8aff-b5a2fb22e3dc/scratch/'

# Exact Official Top 10 Batters
batters = [
    {"rank": 1, "name": "Shashank Singh", "short": "Shashank", "base": 108.3, "delta": 67.7, "press": 176.0, "quad": "Q2: Crisis Accelerator"},
    {"rank": 2, "name": "Ashutosh Sharma", "short": "Ashutosh", "base": 96.9, "delta": 72.0, "press": 168.9, "quad": "Q2: Crisis Accelerator"},
    {"rank": 3, "name": "Najibullah Zadran", "short": "Najibullah", "base": 86.0, "delta": 69.4, "press": 155.3, "quad": "Q2: Crisis Accelerator"},
    {"rank": 4, "name": "Donovan Ferreira", "short": "Ferreira", "base": 120.0, "delta": 58.6, "press": 178.6, "quad": "Q1/Q2 Elite"},
    {"rank": 5, "name": "Naman Dhir", "short": "Naman Dhir", "base": 147.7, "delta": 42.0, "press": 189.7, "quad": "Q1: Elite Clutch Ace"},
    {"rank": 6, "name": "Tom Banton", "short": "Banton", "base": 137.5, "delta": 38.6, "press": 176.1, "quad": "Q1: Elite Clutch Ace"},
    {"rank": 7, "name": "Tristan Stubbs", "short": "Stubbs", "base": 122.3, "delta": 37.1, "press": 159.3, "quad": "Q1: Elite Clutch Ace"},
    {"rank": 8, "name": "Tim David", "short": "Tim David", "base": 154.6, "delta": 22.1, "press": 176.7, "quad": "Q1: Elite Clutch Ace"},
    {"rank": 9, "name": "Suryakumar Yadav", "short": "SKY", "base": 156.7, "delta": 13.8, "press": 170.5, "quad": "Q1: Elite Clutch Ace"},
    {"rank": 10, "name": "Shreyas Iyer", "short": "Shreyas", "base": 137.6, "delta": 33.2, "press": 170.9, "quad": "Q1: Elite Clutch Ace"}
]

# Exact Official Top 10 Bowlers
bowlers = [
    {"rank": 1, "name": "Rashid Khan", "short": "Rashid", "base": 7.55, "delta": 0.17, "press": 7.38, "quad": "Q1: Elite Run Choker"},
    {"rank": 2, "name": "Arshdeep Singh", "short": "Arshdeep", "base": 8.59, "delta": -0.29, "press": 8.88, "quad": "Q4: Death Wicket Spearhead"},
    {"rank": 3, "name": "Matheesha Pathirana", "short": "Pathirana", "base": 8.24, "delta": 0.30, "press": 7.94, "quad": "Q2: Clutch Restrictor"},
    {"rank": 4, "name": "Jasprit Bumrah", "short": "Bumrah", "base": 7.17, "delta": 0.03, "press": 7.14, "quad": "Q1: Elite Run Choker"},
    {"rank": 5, "name": "Akeal Hosein", "short": "Akeal Hosein", "base": 7.89, "delta": 1.80, "press": 6.09, "quad": "Q1: Elite Run Choker"},
    {"rank": 6, "name": "Mitchell Santner", "short": "Santner", "base": 7.62, "delta": 0.98, "press": 6.64, "quad": "Q1: Elite Run Choker"},
    {"rank": 7, "name": "Hasan Mahmud", "short": "Hasan Mahmud", "base": 8.34, "delta": 1.63, "press": 6.71, "quad": "Q2: Clutch Restrictor"},
    {"rank": 8, "name": "Varun Chakravarthy", "short": "Chakravarthy", "base": 7.88, "delta": -0.17, "press": 8.05, "quad": "Q3: Strike Attacker"},
    {"rank": 9, "name": "Wanindu Hasaranga", "short": "Hasaranga", "base": 7.93, "delta": -0.17, "press": 8.10, "quad": "Q3: Strike Attacker"},
    {"rank": 10, "name": "Yuzvendra Chahal", "short": "Chahal", "base": 8.25, "delta": -0.27, "press": 8.52, "quad": "Q3: Strike Attacker"}
]

# Colors
RR_PINK  = '#E8305A'
RR_BLUE  = '#1B365D'
RR_GOLD  = '#F59E0B'
BG_DARK  = '#0B132B'
BG_MID   = '#16223F'
TEXT_W   = '#FFFFFF'
WHITE    = '#FFFFFF'
ACCENT_GREEN = '#10B981'
ACCENT_CYAN  = '#06B6D4'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))
fig.patch.set_facecolor(BG_DARK)
fig.suptitle('CLUTCH DELTA QUADRANT ANALYSIS — EXACT PLAYER POINT MAPPING',
             color=TEXT_W, fontsize=18, fontweight='bold', y=0.98)

# ================================================================
# LEFT CHART: BATTERS (Base SR vs Delta SR)
# ================================================================
ax1.set_facecolor(BG_MID)
ax1.set_xlim(70, 175)
ax1.set_ylim(-10, 85)

# Colored Quadrant Background Zones
# Median dividing lines: X = 125 (Base SR), Y = 25 (Delta SR)
ax1.axvspan(125, 175, 25, 85, color='#10B981', alpha=0.10) # Q1: Top-Right (Green)
ax1.axvspan(70, 125, 25, 85, color='#06B6D4', alpha=0.10)  # Q2: Top-Left (Cyan)
ax1.axvspan(125, 175, -10, 25, color='#F59E0B', alpha=0.08) # Q3: Bottom-Right (Amber)
ax1.axvspan(70, 125, -10, 25, color='#64748B', alpha=0.08)  # Q4: Bottom-Left (Gray)

# Dividing lines
ax1.axvline(125, color=RR_GOLD, linestyle='--', linewidth=1.2, alpha=0.7)
ax1.axhline(25, color=RR_GOLD, linestyle='--', linewidth=1.2, alpha=0.7)
ax1.axhline(0, color='white', linestyle=':', linewidth=0.8, alpha=0.4)

# Quadrant Zone Labels (Watermarks)
ax1.text(150, 78, 'QUADRANT I: ELITE CLUTCH ACES\n(High Base & High Elevation)',
         color='#34D399', fontsize=9, fontweight='bold', ha='center', va='top', alpha=0.9,
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_DARK, edgecolor='#10B981', alpha=0.8))

ax1.text(97, 78, 'QUADRANT II: CRISIS ACCELERATORS\n(Explosive Delta under Pressure)',
         color='#38BDF8', fontsize=9, fontweight='bold', ha='center', va='top', alpha=0.9,
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_DARK, edgecolor='#06B6D4', alpha=0.8))

ax1.text(150, 3, 'QUADRANT III: DECELERATORS\n(High Base, Drops in Pressure)',
         color='#FBBF24', fontsize=8.5, fontweight='bold', ha='center', va='bottom', alpha=0.7)

ax1.text(97, 3, 'QUADRANT IV: LOW LEVERAGE\n(Low Base, Low Elevation)',
         color='#94A3B8', fontsize=8.5, fontweight='bold', ha='center', va='bottom', alpha=0.7)

# Background qualified batters (scatter)
all_bat_qual = pd.read_csv(SCRATCH + 'top_batters_eligible.csv')
ax1.scatter(all_bat_qual['sr_base'], all_bat_qual['delta_sr'], color='#94A3B8', alpha=0.25, s=40, label='Other Qualified Batters')

# Plot Top 10 Batters with distinct badges and callouts
bat_offsets = [
    (12, 4),   # #1 Shashank
    (-75, 4),  # #2 Ashutosh
    (-75, -5), # #3 Najibullah
    (12, 3),   # #4 Ferreira
    (12, -2),  # #5 Naman Dhir
    (10, 5),   # #6 Banton
    (-60, 4),  # #7 Stubbs
    (12, 3),   # #8 Tim David
    (12, -6),  # #9 SKY
    (-65, -8)  # #10 Shreyas
]

for idx, b in enumerate(batters):
    x, y = b['base'], b['delta']
    # Outer gold halo
    ax1.scatter(x, y, color=RR_GOLD, s=260, zorder=5)
    # Inner pink dot
    ax1.scatter(x, y, color=RR_PINK, s=180, zorder=6)
    # Number badge inside dot
    ax1.text(x, y, str(b['rank']), color=WHITE, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=7)
    
    # Text callout box
    dx, dy = bat_offsets[idx]
    label_text = f"#{b['rank']} {b['short']}\n+{y:.1f} SR"
    ax1.annotate(
        label_text, (x, y),
        xytext=(x + dx*0.25, y + dy*0.4),
        color=WHITE, fontsize=8.5, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.25', facecolor='#1E293B', edgecolor=RR_GOLD if b['rank']<=3 else RR_PINK, linewidth=1),
        arrowprops=dict(arrowstyle='->', color=RR_GOLD, lw=1, shrinkA=3, shrinkB=3),
        zorder=8
    )

ax1.set_xlabel('Baseline (Non-Pressure) Strike Rate', color=TEXT_W, fontsize=12, fontweight='bold')
ax1.set_ylabel('Clutch &Delta; SR Elevation (Pressure SR - Base SR)', color=TEXT_W, fontsize=12, fontweight='bold')
ax1.set_title('BATTERS CLUTCH QUADRANT (Numbered #1 to #10)', color=RR_PINK, fontsize=13, fontweight='bold', pad=12)
ax1.tick_params(colors=TEXT_W)
for sp in ['top', 'right']: ax1.spines[sp].set_visible(False)
ax1.spines['left'].set_color(RR_PINK); ax1.spines['bottom'].set_color(RR_PINK)

# ================================================================
# RIGHT CHART: BOWLERS (Base Econ vs Delta Econ)
# ================================================================
ax2.set_facecolor(BG_MID)
ax2.set_xlim(6.8, 9.2)
ax2.set_ylim(-0.6, 2.2)

# Colored Quadrant Background Zones
# Median dividing lines: X = 8.0 (Base Econ), Y = 0.0 (Delta Econ)
ax2.axvspan(6.8, 8.0, 0.0, 2.2, color='#10B981', alpha=0.10) # Q1: Top-Left (Green) - Low Econ, Tightens!
ax2.axvspan(8.0, 9.2, 0.0, 2.2, color='#06B6D4', alpha=0.10) # Q2: Top-Right (Cyan) - Restrictor
ax2.axvspan(6.8, 8.0, -0.6, 0.0, color='#3B82F6', alpha=0.08) # Q3: Bottom-Left (Blue) - Attackers
ax2.axvspan(8.0, 9.2, -0.6, 0.0, color='#F43F5E', alpha=0.08) # Q4: Bottom-Right (Red) - High Econ Leak

# Dividing lines
ax2.axvline(8.0, color=RR_GOLD, linestyle='--', linewidth=1.2, alpha=0.7)
ax2.axhline(0.0, color=RR_GOLD, linestyle='--', linewidth=1.2, alpha=0.7)

# Quadrant Zone Labels (Watermarks)
ax2.text(7.4, 2.05, 'QUADRANT I: ELITE RUN CHOKERS\n(Low Base Econ & Tightens Further)',
         color='#34D399', fontsize=9, fontweight='bold', ha='center', va='top', alpha=0.9,
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_DARK, edgecolor='#10B981', alpha=0.8))

ax2.text(8.6, 2.05, 'QUADRANT II: CLUTCH RESTRICTORS\n(High Base, Dramatic Death Tightening)',
         color='#38BDF8', fontsize=9, fontweight='bold', ha='center', va='top', alpha=0.9,
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_DARK, edgecolor='#06B6D4', alpha=0.8))

ax2.text(7.4, -0.52, 'QUADRANT III: STRIKE ATTACKERS\n(Takes Wickets, Slight Econ Trade-off)',
         color='#60A5FA', fontsize=8.5, fontweight='bold', ha='center', va='bottom', alpha=0.8)

ax2.text(8.6, -0.52, 'QUADRANT IV: DEATH VOLUME ACES\n(Furnace Overs 18-20 / Wickets)',
         color='#FB7185', fontsize=8.5, fontweight='bold', ha='center', va='bottom', alpha=0.8)

# Background qualified bowlers (scatter)
all_bowl_qual = pd.read_csv(SCRATCH + 'top_bowlers_eligible.csv')
ax2.scatter(all_bowl_qual['econ_base'], all_bowl_qual['delta_econ'], color='#94A3B8', alpha=0.25, s=40, label='Other Qualified Bowlers')

# Plot Top 10 Bowlers with distinct badges and callouts
bowl_offsets = [
    (12, 10),   # #1 Rashid
    (12, -12),  # #2 Arshdeep
    (12, 8),    # #3 Pathirana
    (-75, 8),   # #4 Bumrah
    (10, -10),  # #5 Akeal
    (-65, 8),   # #6 Santner
    (12, -8),   # #7 Hasan Mahmud
    (-75, -10), # #8 Varun
    (12, 6),    # #9 Hasaranga
    (-65, -10)  # #10 Chahal
]

for idx, b in enumerate(bowlers):
    x, y = b['base'], b['delta']
    # Outer gold halo
    ax2.scatter(x, y, color=RR_GOLD, s=260, zorder=5)
    # Inner blue dot
    ax2.scatter(x, y, color='#2563EB', s=180, zorder=6)
    # Number badge inside dot
    ax2.text(x, y, str(b['rank']), color=WHITE, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=7)
    
    # Text callout box
    dx, dy = bowl_offsets[idx]
    tight_str = f"+{y:.2f}" if y > 0 else f"{y:.2f}"
    label_text = f"#{b['rank']} {b['short']}\n{tight_str} Econ"
    ax2.annotate(
        label_text, (x, y),
        xytext=(x + dx*0.0035, y + dy*0.035),
        color=WHITE, fontsize=8.5, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.25', facecolor='#1E293B', edgecolor=RR_GOLD if b['rank']<=4 else '#3B82F6', linewidth=1),
        arrowprops=dict(arrowstyle='->', color=RR_GOLD, lw=1, shrinkA=3, shrinkB=3),
        zorder=8
    )

ax2.set_xlabel('Baseline (Non-Pressure) Economy Rate', color=TEXT_W, fontsize=12, fontweight='bold')
ax2.set_ylabel('Clutch Tightening (Base Econ - Pressure Econ)', color=TEXT_W, fontsize=12, fontweight='bold')
ax2.set_title('BOWLERS CLUTCH QUADRANT (Numbered #1 to #10)', color='#38BDF8', fontsize=13, fontweight='bold', pad=12)
ax2.tick_params(colors=TEXT_W)
for sp in ['top', 'right']: ax2.spines[sp].set_visible(False)
ax2.spines['left'].set_color(RR_BLUE); ax2.spines['bottom'].set_color(RR_BLUE)

plt.tight_layout()
plt.savefig(SCRATCH + 'official_chart3_quadrants_v2.png', dpi=220, bbox_inches='tight', facecolor=BG_DARK)
plt.close()
print("✅ Official Chart 3 v2 generated successfully with crystal clear badges, quadrant zones, and direct pointers!")
