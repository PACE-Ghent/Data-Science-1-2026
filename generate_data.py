"""
Generates the three (deliberately messy) datasets used throughout the
Dataverwerking I / Dataverwerking II / Datavisualisatie I lab series:

- data/athletes.csv    : one row per athlete (demographics)
- data/tests.csv       : physical test results across multiple test moments
- data/hr_session.csv  : heart rate + speed per second for one training session

Messiness that is baked in on purpose (see course prep notes):
- inconsistent spelling of "position" ("Forward", "forward ", "FWD", ...)
- sprint times that are sometimes stored in milliseconds instead of seconds
- missing values scattered across several columns
- one duplicate athlete (same person, appears twice in athletes.csv)
- comma-decimal numbers (European locale export) in the "weight_kg" column

Run: python generate_data.py
"""

import numpy as np
import pandas as pd
from pathlib import Path

RNG = np.random.default_rng(42)
OUT_DIR = Path(__file__).parent / "data"
OUT_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# 1. athletes.csv
# ---------------------------------------------------------------------------

N_ATHLETES = 42  # one more row gets added later (duplicate) -> 43 rows in the file

FIRST_NAMES_M = ["Liam", "Noah", "Lucas", "Milan", "Finn", "Arthur", "Louis", "Jules",
                 "Victor", "Senne", "Mathis", "Warre", "Robbe", "Seppe", "Wout", "Tuur",
                 "Stan", "Bram", "Jasper", "Cas", "Niels"]
FIRST_NAMES_F = ["Emma", "Olivia", "Mila", "Lena", "Nora", "Fien", "Marie", "Elise",
                  "Fleur", "Amber", "Vic", "Lotte", "Juul", "Noor", "Yana", "Julie",
                  "Hanne", "Britt", "Silke", "Roos", "Zoe"]
LAST_NAMES = ["Peeters", "Janssens", "Maes", "Jacobs", "Mertens", "Willems", "Claes",
              "Goossens", "Wouters", "De Smet", "Dubois", "Lambert", "Simon", "Michiels",
              "Hermans", "Vermeulen", "Vandamme", "Verhoeven", "Bogaert", "Coppens",
              "De Backer", "Lemmens"]

# Canonical positions, but we deliberately write them inconsistently to disk
POSITIONS_CANONICAL = ["Forward", "Midfielder", "Defender", "Goalkeeper"]
POSITION_VARIANTS = {
    "Forward": ["Forward", "forward ", "FWD", "forward"],
    "Midfielder": ["Midfielder", "midfielder", "MID", " Midfielder"],
    "Defender": ["Defender", "defender ", "DEF", "defender"],
    "Goalkeeper": ["Goalkeeper", "goalkeeper", "GK", "Goalkeeper "],
}

# Stratified position assignment (fixed counts, then shuffled) instead of
# independent random draws, so every position - including goalkeeper - ends
# up with enough athletes for meaningful group-by examples later on.
position_counts = {"Forward": 13, "Midfielder": 12, "Defender": 12, "Goalkeeper": 5}
assert sum(position_counts.values()) == N_ATHLETES
position_pool = [pos for pos, n in position_counts.items() for _ in range(n)]
RNG.shuffle(position_pool)

rows = []
for i in range(1, N_ATHLETES + 1):
    athlete_id = f"A{i:03d}"
    gender = RNG.choice(["M", "F"])
    first_name = RNG.choice(FIRST_NAMES_M if gender == "M" else FIRST_NAMES_F)
    last_name = RNG.choice(LAST_NAMES)
    name = f"{first_name} {last_name}"

    # age category U13/U15/U17 -> birth year relative to the 2026 season
    age = RNG.integers(12, 18)  # 12 through 17 years old
    birth_year = 2026 - age
    birth_month = RNG.integers(1, 13)
    birth_day = RNG.integers(1, 28)
    birthdate = f"{birth_year:04d}-{birth_month:02d}-{birth_day:02d}"

    position_canonical = position_pool[i - 1]
    position = RNG.choice(POSITION_VARIANTS[position_canonical])

    height_cm = round(RNG.normal(100 + age * 4.5, 6), 1)
    weight_kg = round(RNG.normal(15 + age * 3, 4), 1)

    rows.append({
        "athlete_id": athlete_id,
        "name": name,
        "birthdate": birthdate,
        "gender": gender,
        "position": position,
        "height_cm": height_cm,
        "weight_kg": weight_kg,
    })

athletes = pd.DataFrame(rows)

# Missing values: scatter some NaN into height_cm and gender
missing_idx = RNG.choice(athletes.index, size=4, replace=False)
athletes.loc[missing_idx[:2], "height_cm"] = np.nan
athletes.loc[missing_idx[2:], "gender"] = np.nan

# One duplicate athlete: same person, two rows (slightly different weight so
# it is not a byte-for-byte copy, just like a real double entry would look)
dup_source = athletes.iloc[10].copy()
dup_source["athlete_id"] = f"A{N_ATHLETES + 1:03d}"
dup_source["name"] = athletes.iloc[10]["name"]  # exact same name + birthdate
athletes = pd.concat([athletes, pd.DataFrame([dup_source])], ignore_index=True)

# Comma-decimal numbers (European locale export) in the weight_kg column -> stored as text
athletes["weight_kg"] = athletes["weight_kg"].apply(
    lambda v: "" if pd.isna(v) else str(v).replace(".", ",")
)

athletes.to_csv(OUT_DIR / "athletes.csv", index=False)

# ---------------------------------------------------------------------------
# 2. tests.csv
# ---------------------------------------------------------------------------

# We generate test data for every athlete row, including the duplicate ID,
# so the merge exercise in session 2 (inner vs. left join) has something to show.
test_rows = []
test_id = 1
test_moments = [1, 2, 3]
date_per_moment = {
    1: "2026-09-14",
    2: "2026-10-19",
    3: "2026-11-23",
}

for _, ath in athletes.iterrows():
    n_moments = RNG.choice([2, 3], p=[0.3, 0.7])
    chosen_moments = test_moments[:n_moments]
    # mild progression across the season
    base_sprint10 = RNG.normal(2.1, 0.15)
    base_sprint30 = RNG.normal(5.4, 0.3)
    base_cmj = RNG.normal(28, 5)
    base_yoyo = RNG.integers(14, 20)

    for m in chosen_moments:
        progress = (m - 1) * 0.02
        sprint10 = round(max(base_sprint10 - progress + RNG.normal(0, 0.05), 1.5), 2)
        sprint30 = round(max(base_sprint30 - progress * 2 + RNG.normal(0, 0.08), 4.0), 2)
        cmj = round(base_cmj + (m - 1) * RNG.normal(0.8, 0.3) + RNG.normal(0, 1.0), 1)
        yoyo = int(np.clip(base_yoyo + (m - 1) + RNG.integers(-1, 2), 12, 21))

        # Deliberate: sprint times sometimes stored in milliseconds instead of seconds
        if RNG.random() < 0.12:
            sprint10 = round(sprint10 * 1000, 0)
        if RNG.random() < 0.12:
            sprint30 = round(sprint30 * 1000, 0)

        test_rows.append({
            "test_id": test_id,
            "athlete_id": ath["athlete_id"],
            "test_moment": m,
            "date": date_per_moment[m],
            "sprint_10m_s": sprint10,
            "sprint_30m_s": sprint30,
            "cmj_height_cm": cmj,
            "yoyo_level": yoyo,
        })
        test_id += 1

tests = pd.DataFrame(test_rows)

# Scatter missing values across a few columns
for col in ["cmj_height_cm", "yoyo_level", "sprint_30m_s"]:
    idx = RNG.choice(tests.index, size=6, replace=False)
    tests.loc[idx, col] = np.nan

tests.to_csv(OUT_DIR / "tests.csv", index=False)

# ---------------------------------------------------------------------------
# 3. hr_session.csv
# ---------------------------------------------------------------------------

# Five athletes wear a heart-rate sensor + GPS during one training (2026-11-09)
session_athletes = athletes.iloc[[0, 1, 2, 3, 4]]["athlete_id"].tolist()
session_date = "2026-11-09"
duration_s = 40 * 60  # 40-minute training

hr_rows = []
for athlete_id in session_athletes:
    hr_rest = RNG.integers(60, 75)
    hr_max = RNG.integers(195, 205)
    t = np.arange(duration_s)

    # Shape: easy warm-up, two interval blocks, easy cool-down
    warmup = np.clip(t / (8 * 60), 0, 1)
    interval = 0.5 + 0.5 * np.sin(t / 90.0) ** 2
    cooldown = np.clip((duration_s - t) / (6 * 60), 0, 1)
    intensity = warmup * cooldown * (0.55 + 0.35 * interval)
    intensity = np.clip(intensity, 0.15, 1.0)

    heart_rate = hr_rest + (hr_max - hr_rest) * intensity + RNG.normal(0, 2, size=duration_s)
    heart_rate = np.clip(heart_rate, hr_rest - 5, hr_max + 3).round(0).astype(int)

    speed = 2.0 + 20.0 * np.clip(intensity - 0.4, 0, 1) + RNG.normal(0, 0.6, size=duration_s)
    speed = np.clip(speed, 0, 28).round(2)

    for sec, hr, sp in zip(t, heart_rate, speed):
        hr_rows.append({
            "athlete_id": athlete_id,
            "date": session_date,
            "time_s": int(sec),
            "heart_rate_bpm": int(hr),
            "speed_kmh": float(sp),
        })

hr_session = pd.DataFrame(hr_rows)

# A small number of missing heart-rate readings (sensor drop-out)
idx = RNG.choice(hr_session.index, size=25, replace=False)
hr_session.loc[idx, "heart_rate_bpm"] = np.nan

hr_session.to_csv(OUT_DIR / "hr_session.csv", index=False)

print("Generated:")
print(f"  {OUT_DIR / 'athletes.csv'}   -> {len(athletes)} rows")
print(f"  {OUT_DIR / 'tests.csv'}      -> {len(tests)} rows")
print(f"  {OUT_DIR / 'hr_session.csv'} -> {len(hr_session)} rows")
