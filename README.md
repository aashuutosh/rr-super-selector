# Rajasthan Royals — SupeRR Selector Season 2: Round 1
### *Identifying the Most Reliable Players Under Pressure for the IPL 2027 Auction*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Rajasthan Royals](https://img.shields.io/badge/IPL-Rajasthan%20Royals-E8305A.svg)](https://rajasthanroyals.com)
[![Competition](https://img.shields.io/badge/Unstop-SupeRR%20Selector%20S2-blueviolet.svg)](https://unstop.com)
[![Status](https://img.shields.io/badge/Status-Round%201%20Submission%20Ready-success.svg)](#)

This repository contains the complete analytical framework, empirical data pipelines, machine learning pressure models, and interactive dashboard developed for **Rajasthan Royals SupeRR Selector Season 2 (Round 1)**.

---

## 🏆 Official Top 10 Submissions (Unstop Dropdowns)

### 🏏 Top 10 Batters Under Pressure (BPS Model)
Ranked by the multi-dimensional **Batting Pressure Score (BPS)**:

| Rank | Player Name | Nationality | Press Balls | Base SR | Press SR | Δ SR | Press Avg | BPS Score | Tactical Role |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Shashank Singh** | IND | 204 | 108.3 | **176.0** | **+67.7** | 63.4 | **2.054** | Indian Crisis Finisher |
| **2** | **Ashutosh Sharma** | IND | 305 | 96.9 | **168.9** | **+72.0** | 32.2 | **1.503** | Boundary Specialist (#7–8) |
| **3** | **Najibullah Zadran** | AFG | 123 | 86.0 | **155.3** | **+69.4** | 45.7 | **1.446** | Left-Hand Middle Floater |
| **4** | **Donovan Ferreira** | SA | 84 | 120.0 | **178.6** | **+58.6** | 33.3 | **1.301** | Dual WK / Finisher |
| **5** | **Naman Dhir** | IND | 87 | 147.7 | **189.7** | **+42.0** | 31.0 | **1.283** | Top-Order Accelerator |
| **6** | **Tom Banton** | ENG | 176 | 137.5 | **176.1** | **+38.6** | 51.5 | **1.268** | Aggressive Opener / WK |
| **7** | **Tristan Stubbs** | SA | 701 | 122.3 | **159.3** | **+37.1** | 43.0 | **1.194** | Middle-Order Game Changer |
| **8** | **Tim David** | AUS | 838 | 154.6 | **176.7** | **+22.1** | 37.3 | **1.095** | High-Volume Death Power |
| **9** | **Suryakumar Yadav** | IND | 927 | 156.7 | **170.5** | **+13.8** | 42.1 | **0.990** | 360° Benchmark Anchor |
| **10** | **Shreyas Iyer** | IND | 240 | 137.6 | **170.9** | **+33.2** | 31.8 | **0.988** | Playoff Knockout Captain |

---

### 🎳 Top 10 Bowlers Under Pressure (BPS_bowl Model)
Ranked by the multi-dimensional **Bowling Pressure Score (BPS_bowl)**:

| Rank | Player Name | Nationality | Press Balls | Base Econ | Press Econ | Tightening | Press Wkts | BPS_bowl | Tactical Role |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Rashid Khan** | AFG | 1,182 | 7.55 | **7.38** | **+0.17** | 83 | **1.497** | All-Phase Spin Maestro |
| **2** | **Arshdeep Singh** | IND | 1,223 | 8.59 | **8.88** | -0.29 | **99** | **1.409** | Death Overs 18–20 Spearhead |
| **3** | **Matheesha Pathirana** | SL | 688 | 8.24 | **7.94** | **+0.30** | 62 | **1.315** | Slingy Yorker Death Enforcer |
| **4** | **Jasprit Bumrah** | IND | 690 | 7.17 | **7.14** | **+0.03** | 56 | **1.189** | Universal Gold Standard |
| **5** | **Akeal Hosein** | WI | 378 | 7.89 | **6.09** | **+1.80** | 24 | **1.114** | Powerplay/Crisis Spin Lock |
| **6** | **Mitchell Santner** | NZ | 572 | 7.62 | **6.64** | **+0.98** | 36 | **1.095** | Middle-Overs Spin Restrictor |
| **7** | **Hasan Mahmud** | BAN | 168 | 8.34 | **6.71** | **+1.63** | 17 | **1.062** | Skiddy Death Pace Option |
| **8** | **Varun Chakravarthy** | IND | 848 | 7.88 | **8.05** | -0.17 | 58 | **1.060** | Mystery Spin Wicket Weapon |
| **9** | **Wanindu Hasaranga** | SL | 733 | 7.93 | **8.10** | -0.17 | 62 | **1.055** | Attacking Leg-Spin Option |
| **10** | **Yuzvendra Chahal** | IND | 946 | 8.25 | **8.52** | -0.27 | 72 | **0.931** | RR Wicket Legend (Flight/Dip) |

---

## 📊 Clutch Delta Quadrants: Point-by-Point Cross Reference

Every numbered point in the quadrant scatter plots (`charts/official_chart3_quadrants_v2.png`) directly maps to the official picks:

### Batters Quadrant (Left Scatter)
- **Quadrant I (Elite Clutch Aces):** High baseline strike rate (>125) and accelerates further under pressure.
  - `④` Donovan Ferreira (Base 120.0 → Press 178.6, **+58.6 ΔSR**)
  - `⑤` Naman Dhir (Base 147.7 → Press 189.7, **+42.0 ΔSR**)
  - `⑥` Tom Banton (Base 137.5 → Press 176.1, **+38.6 ΔSR**)
  - `⑦` Tristan Stubbs (Base 122.3 → Press 159.3, **+37.1 ΔSR**)
  - `⑧` Tim David (Base 154.6 → Press 176.7, **+22.1 ΔSR**)
  - `⑨` Suryakumar Yadav (Base 156.7 → Press 170.5, **+13.8 ΔSR**)
  - `⑩` Shreyas Iyer (Base 137.6 → Press 170.9, **+33.2 ΔSR**)
- **Quadrant II (Crisis Accelerators):** Moderate base strike rate (<125), but explodes in crisis/chase phases.
  - `①` Shashank Singh (Base 108.3 → Press 176.0, **+67.7 ΔSR**)
  - `②` Ashutosh Sharma (Base 96.9 → Press 168.9, **+72.0 ΔSR**)
  - `③` Najibullah Zadran (Base 86.0 → Press 155.3, **+69.4 ΔSR**)

### Bowlers Quadrant (Right Scatter)
- **Quadrant I (Elite Run Chokers):** Sub-8.0 baseline economy and tightens run-rate even further under pressure.
  - `①` Rashid Khan (7.55 → 7.38, **+0.17 Tightening**, 83 Wkts)
  - `④` Jasprit Bumrah (7.17 → 7.14, **+0.03 Tightening**, 56 Wkts)
  - `⑤` Akeal Hosein (7.89 → 6.09, **+1.80 Tightening**, 24 Wkts)
  - `⑥` Mitchell Santner (7.62 → 6.64, **+0.98 Tightening**, 36 Wkts)
- **Quadrant II (Clutch Restrictors):** Higher baseline economy, but executes extreme death over boundary choking.
  - `③` Matheesha Pathirana (8.24 → 7.94, **+0.30 Tightening**, 62 Wkts)
  - `⑦` Hasan Mahmud (8.34 → 6.71, **+1.63 Tightening**, 17 Wkts)
- **Quadrant III (Strike Attackers):** Attacking spinners who trade a slight run fraction (-0.17 to -0.27 Econ) to hunt key wickets.
  - `⑧` Varun Chakravarthy (7.88 → 8.05, 58 Wkts, 42.2% Dots)
  - `⑨` Wanindu Hasaranga (7.93 → 8.10, 62 Wkts, 11.8 SR)
  - `⑩` Yuzvendra Chahal (8.25 → 8.52, 72 Wkts, 946 Balls)
- **Quadrant IV (Death Spearhead):** Bowls the highest-risk furnace overs 18–20 where wickets outweigh raw economy.
  - `②` Arshdeep Singh (8.59 → 8.88, **99 Wickets** — tournament #1)

---

## 🎯 Rajasthan Royals — IPL 2027 Auction Roadmap

1. **Solve the 17–20 Death Overs Deficit:**
   - Pair **Arshdeep Singh** (left-arm swing & wide yorkers) with **Matheesha Pathirana** (slingy round-arm yorkers) to form an impenetrable death fortress.
2. **Unlock the Shashank–Ashutosh Value Steal:**
   - Instead of spending ₹15+ Cr on an overseas finisher, secure **Shashank Singh** and **Ashutosh Sharma** for ₹3–6 Cr each. Their domestic chemistry and +70 SR lift preserve purse for frontline bowlers.
3. **Fortify Jaipur with Spin Supremacy:**
   - Utilize Sawai Mansingh Stadium's large square boundaries by acquiring **Akeal Hosein** (6.09 pressure economy) or retaining **Yuzvendra Chahal** (72 pressure wickets).

---

## 💻 Repository Structure

```
├── RR_SupeRR_Selector_S2_Round1_Final.pdf  # Official 10-page Submission Report
├── dashboard.html                         # Standalone Interactive Web Dashboard
├── README.md                              # Complete Documentation
├── .gitignore                             # Ignored raw data and temporary files
│
├── charts/                                # Publication-ready Visualizations
│   ├── official_chart1_top10_batters.png
│   ├── official_chart2_top10_bowlers.png
│   ├── official_chart3_quadrants_v2.png  # Numbered Quadrants with Leader Lines
│   └── official_chart4_rr_roadmap.png
│
├── results/                               # Exported Ranked Datasets
│   ├── ranked_batters_final.csv
│   ├── ranked_bowlers_final.csv
│   ├── top_batters_eligible.csv
│   └── top_bowlers_eligible.csv
│
└── scripts/                               # Python Processing Pipelines
    ├── tag_pressure.py                    # 5-Dimensional Pressure Tagging Engine
    ├── compute_final_rankings.py          # BPS/BPS_bowl Z-Score Formulation
    ├── generate_quadrants_v2.py           # Quadrant Scatter Plot Generator
    └── generate_master_pdf_v4.py          # ReportLab 10-Page PDF Compiler
```

---

## 🚀 How to Run & View

### 1. Interactive Dashboard
Double-click or open `dashboard.html` in any modern web browser. It features:
- Filterable and searchable Top 10 Batters and Bowlers data tables.
- Interactive Chart.js scatter plots with hover tooltips and point identification.
- Rajasthan Royals IPL 2027 tiered auction roadmap.
- Complete mathematical methodology documentation.

### 2. Reproduce Analytics
```bash
# Clone the repository
git clone https://github.com/<your-username>/rr-super-selector.git
cd rr-super-selector

# Install dependencies
pip install pandas numpy matplotlib reportlab pypdf

# Run analytical pipeline
python scripts/tag_pressure.py
python scripts/compute_final_rankings.py
python scripts/generate_quadrants_v2.py
python scripts/generate_master_pdf_v4.py
```

---
**Submission Author:** Ashutosh Pratap Singh (`ashutoshps2020@gmail.com`)  
**Target:** Rajasthan Royals Analytics War Room (Kumar Sangakkara & Giles Lindsay)
