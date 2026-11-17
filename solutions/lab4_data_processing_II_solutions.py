import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import pandas as pd

    return (pd,)


@app.cell
def _(mo):
    mo.md(r"""
    # Data Processing II - Combine, Summarize, Reshape

    Same club, same three files, one week later. Today we go beyond a
    single tidy table: combining information that lives in different
    files, summarizing groups of rows into statistics, reshaping tables
    between "wide" and "long" layouts, and working with a per-second
    time series.

    **By the end of this session you can:** aggregate data with
    `groupby`, combine tables with `merge`, reshape with `melt` and
    `pivot`, and compute basic time-series features (rolling average,
    resampling).
    """)
    return


@app.cell
def _(mo):
    # Local development default. For molab / WASM, replace with a raw GitHub URL,
    # e.g. "https://raw.githubusercontent.com/<org>/<repo>/main/data".
    DATA_DIR = str(mo.notebook_dir() / ".." / "data")
    return (DATA_DIR,)


@app.cell
def _(mo):
    def check_exercise(check_fn, success_message):
        """Run `check_fn`; show a green callout on success, else an explanation."""
        try:
            check_fn()
        except AssertionError as e:
            message = str(e) or "The result is not correct yet."
            return mo.callout(mo.md(f"**Not yet correct.** {message}"), kind="warn")
        except Exception as e:
            return mo.callout(
                mo.md(f"**Error while checking your answer:** {type(e).__name__}: {e}"),
                kind="danger",
            )
        return mo.callout(mo.md(f"**Correct!** {success_message}"), kind="success")

    return (check_exercise,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Recap - repair a broken cleaning cell (13:00-13:15)

    The cell below is a tiny, self-contained cleaning pipeline with two
    bugs. Fix them directly in the cell (a typo in a column name, and a
    missing text-to-number conversion) until `mini_clean` has 5 rows, a
    `position` column with only `"FORWARD"` / `"MIDFIELDER"` values, and
    a numeric `weight_kg` column.
    """)
    return


@app.cell
def _(pd):
    mini_messy = pd.DataFrame(
        {
            "position": [" Forward", "forward", "FORWARD ", "Midfielder", "midfielder "],
            "weight_kg": ["57,5", "60,3", "56,8", "61,6", "49,0"],
        }
    )

    mini_clean = mini_messy.copy()
    mini_clean["position"] = mini_clean["position"].str.strip().str.upper()
    mini_clean["weight_kg"] = mini_clean["weight_kg"].str.replace(",", ".").astype(float)
    mini_clean
    return (mini_clean,)


@app.cell
def _(check_exercise, mini_clean):
    def _check():
        assert len(mini_clean) == 5
        assert set(mini_clean["position"]) == {"FORWARD", "MIDFIELDER"}
        assert mini_clean["weight_kg"].dtype.kind == "f"

    check_exercise(_check, "The mini cleaning pipeline runs correctly now.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Loading last week's cleaned data

    We repeat (in a slightly more compact form) the cleaning from Data
    Processing I: normalize `position`, convert `weight_kg` to a number,
    and derive `age`. On purpose, we do **not** remove the duplicate
    athlete yet - that will matter in the merge section below.
    """)
    return


@app.cell
def _(pd):
    def clean_positions(position_column):
        position_map = {
            "forward": "Forward", "fwd": "Forward",
            "midfielder": "Midfielder", "mid": "Midfielder",
            "defender": "Defender", "def": "Defender",
            "goalkeeper": "Goalkeeper", "gk": "Goalkeeper",
        }
        return position_column.str.strip().str.lower().map(position_map)

    def fix_sprint_units(seconds_column):
        return seconds_column.where(seconds_column < 20, seconds_column / 1000)

    REFERENCE_DATE = pd.Timestamp("2026-09-14")
    return REFERENCE_DATE, clean_positions, fix_sprint_units


@app.cell
def _(DATA_DIR, REFERENCE_DATE, clean_positions, pd):
    athletes = pd.read_csv(f"{DATA_DIR}/athletes.csv").assign(
        position=lambda d: clean_positions(d["position"]),
        weight_kg=lambda d: d["weight_kg"].str.replace(",", ".").astype(float),
        age=lambda d: (REFERENCE_DATE - pd.to_datetime(d["birthdate"])).dt.days // 365,
    )
    athletes.head()
    return (athletes,)


@app.cell
def _(DATA_DIR, fix_sprint_units, pd):
    tests = pd.read_csv(f"{DATA_DIR}/tests.csv").assign(
        sprint_10m_s=lambda d: fix_sprint_units(d["sprint_10m_s"]),
        sprint_30m_s=lambda d: fix_sprint_units(d["sprint_30m_s"]),
    )
    tests.head()
    return (tests,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. groupby + agg (13:15-14:10)

    `groupby("column")` splits a dataframe into groups; call an
    aggregation afterwards (`.mean()`, `.size()`, `.agg(...)`) to
    summarize each group into one row.
    """)
    return


@app.cell
def _(athletes):
    mean_age_per_position = athletes.groupby("position")["age"].mean().round(1)
    mean_age_per_position
    return


@app.cell
def _(mo):
    mo.md("""
    `pd.cut` turns a numeric column into categories based on bin edges - perfect for age categories such as U13 / U15 / U17.
    """)
    return


@app.cell
def _(athletes, pd):
    athletes_with_age_group = athletes.assign(
        age_group=lambda d: pd.cut(
            d["age"], bins=[10, 12, 14, 16, 18], labels=["U13", "U15", "U17", "U19"]
        )
    )
    athletes_with_age_group[["name", "age", "age_group"]].head()
    return (athletes_with_age_group,)


@app.cell
def _(athletes_with_age_group):
    athletes_with_age_group.groupby(["position", "age_group"], observed=True).agg(
        n_athletes=("athlete_id", "size"),
        mean_height_cm=("height_cm", "mean"),
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 1 - group by gender and age group
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Using `athletes_with_age_group`, group by `gender` and `age_group`, then use `.agg(...)` to compute the mean `height_cm` and mean `weight_kg` per group. Store the result in `gender_age_summary` (use `observed=True` in `groupby` to skip empty combinations).
    """)
    return


@app.cell
def _(athletes_with_age_group):
    gender_age_summary = athletes_with_age_group.groupby(
        ["gender", "age_group"], observed=True
    ).agg(mean_height_cm=("height_cm", "mean"), mean_weight_kg=("weight_kg", "mean"))
    return (gender_age_summary,)


@app.cell
def _(athletes_with_age_group, check_exercise, gender_age_summary):
    def _check():
        assert gender_age_summary is not ..., "Replace `...` with your grouped, aggregated dataframe."
        expected = athletes_with_age_group.groupby(
            ["gender", "age_group"], observed=True
        ).agg(
            mean_height_cm=("height_cm", "mean"), mean_weight_kg=("weight_kg", "mean")
        )
        assert set(gender_age_summary.columns) >= {"mean_height_cm", "mean_weight_kg"}, (
            "Expected columns named `mean_height_cm` and `mean_weight_kg`."
        )
        assert len(gender_age_summary) == len(expected), (
            f"Expected {len(expected)} groups, got {len(gender_age_summary)}."
        )

    check_exercise(_check, "Your group summary has the right shape and columns.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. merge (14:10-14:55)

    `pd.merge(left, right, on="key", how=...)` combines two tables on a
    shared key. `how="inner"` keeps only keys present in **both**
    tables; `how="left"` keeps every row of the left table, filling
    missing matches with `NaN`.
    """)
    return


@app.cell
def _(athletes, tests):
    merged_inner = athletes.merge(tests, on="athlete_id", how="inner")
    merged_left = athletes.merge(tests, on="athlete_id", how="left")
    (len(athletes), len(tests), len(merged_inner), len(merged_left))
    return (merged_inner,)


@app.cell
def _(mo):
    mo.md("""
    Both joins have the same length here because every athlete has at least one test result - with real-world data that is rarely guaranteed, which is exactly why the two behave differently in general. Now look for the duplicate athlete.
    """)
    return


@app.cell
def _(merged_inner):
    merged_inner.loc[
        merged_inner.duplicated(subset=["name", "birthdate"], keep=False)
    ][["athlete_id", "name", "birthdate", "test_moment", "sprint_30m_s"]]
    return


@app.cell
def _(mo):
    mo.md("""
    Same person, two different `athlete_id`s - the join itself works perfectly (it doesn't know these are the same person), but any summary statistic computed after the merge will silently count this athlete twice unless we deduplicate **by identity** (name + birthdate), not by ID.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    The fix is to deduplicate **before** merging, not after: drop duplicate `(name, birthdate)` rows from `athletes` first, so every remaining athlete keeps all of their own test moments once merged. Deduplicating *after* merging would incorrectly throw away an athlete's other test moments too, since those rows also share the same name + birthdate.
    """)
    return


@app.cell
def _(athletes, tests):
    combined = athletes.drop_duplicates(subset=["name", "birthdate"], keep="first").merge(
        tests, on="athlete_id", how="inner"
    )
    combined.shape
    return (combined,)


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 2 - what did deduplication cost us?

    `drop_duplicates(keep="first")` silently discards every row belonging
    to the *other* copy of the duplicate athlete. Before that data
    disappears from view, it's worth knowing how much of it there was.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Compute `rows_lost_to_dedup`: the number of rows in `merged_inner` (the un-deduplicated merge) whose `athlete_id` does **not** appear in `combined`.
    """)
    return


@app.cell
def _(combined, merged_inner):
    dropped_ids = set(merged_inner["athlete_id"]) - set(combined["athlete_id"])
    rows_lost_to_dedup = merged_inner["athlete_id"].isin(dropped_ids).sum()
    return (rows_lost_to_dedup,)


@app.cell
def _(check_exercise, combined, merged_inner, rows_lost_to_dedup):
    def _check():
        assert rows_lost_to_dedup is not ..., "Replace `...` with your row count."
        dropped_ids = set(merged_inner["athlete_id"]) - set(combined["athlete_id"])
        expected = merged_inner["athlete_id"].isin(dropped_ids).sum()
        assert rows_lost_to_dedup == expected, (
            f"Expected {expected} rows lost, got {rows_lost_to_dedup}."
        )

    check_exercise(
        _check,
        "That's how many test records would have silently vanished from "
        "view if you had not deliberately checked.",
    )

    check_exercise(_check, "`combined` is merged and free of duplicate athletes.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Wide ↔ long: `melt` and `pivot` (15:10-15:50)

    `tests` is already in **long** format: one row per
    `(athlete_id, test_moment)` combination. `pivot` turns it **wide**:
    one row per athlete, one column per test moment.
    """)
    return


@app.cell
def _(combined):
    sprint_wide = combined.pivot_table(
        index="athlete_id", columns="test_moment", values="sprint_30m_s"
    )
    sprint_wide.head()
    return (sprint_wide,)


@app.cell
def _(mo):
    mo.md("""
    In wide format, computing progress between two test moments is a single subtraction. A negative number means the athlete got *faster* (a lower time).
    """)
    return


@app.cell
def _(sprint_wide):
    sprint_progress_1_to_2 = (sprint_wide[2] - sprint_wide[1]).rename("sprint_30m_progress")
    sprint_progress_1_to_2.describe()
    return


@app.cell
def _(mo):
    mo.md("""
    `melt` is the inverse of `pivot`: it turns wide columns back into long `(id, variable, value)` rows - the format plotly express prefers, as we'll see next session.
    """)
    return


@app.cell
def _(sprint_wide):
    sprint_long_again = sprint_wide.reset_index().melt(
        id_vars="athlete_id", var_name="test_moment", value_name="sprint_30m_s"
    )
    sprint_long_again.head()
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 3 - progress in jump height
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Pivot `combined` to `cmj_wide` (index `athlete_id`, columns `test_moment`, values `cmj_height_cm`), then compute `cmj_progress_1_to_2` as the *difference* between test moment 2 and test moment 1 (moment 2 minus moment 1, so a **positive** number means the athlete jumped higher).
    """)
    return


@app.cell
def _(combined):
    cmj_wide = combined.pivot_table(index="athlete_id", columns="test_moment", values="cmj_height_cm")
    cmj_progress_1_to_2 = cmj_wide[2] - cmj_wide[1]
    return cmj_progress_1_to_2, cmj_wide


@app.cell
def _(check_exercise, cmj_progress_1_to_2, cmj_wide, combined):
    def _check():
        assert cmj_wide is not ..., "Replace `...` with a pivot_table call."
        expected_wide = combined.pivot_table(
            index="athlete_id", columns="test_moment", values="cmj_height_cm"
        )
        assert set(cmj_wide.columns) >= {1, 2}, "cmj_wide needs at least columns 1 and 2."
        assert cmj_progress_1_to_2 is not ..., "Replace `...` with cmj_wide[2] - cmj_wide[1]."
        expected_progress = expected_wide[2] - expected_wide[1]
        assert (cmj_progress_1_to_2.dropna().round(3) == expected_progress.dropna().round(3)).all(), (
            "cmj_progress_1_to_2 should equal test moment 2 minus test moment 1."
        )

    check_exercise(_check, "Your wide table and progress column are both correct.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 6. Time series with `hr_session.csv` (15:50-16:50)

    One training, five athletes, one heart-rate + speed reading per
    second.
    """)
    return


@app.cell
def _(DATA_DIR, pd):
    hr_session = pd.read_csv(f"{DATA_DIR}/hr_session.csv")
    hr_session["timestamp"] = pd.to_datetime(hr_session["date"]) + pd.to_timedelta(
        hr_session["time_s"], unit="s"
    )
    hr_session.head()
    return (hr_session,)


@app.cell
def _(mo):
    mo.md("""
    Heart-rate *zones* are usually expressed as a percentage of maximum heart rate. We estimate `hr_max` per athlete with the common rule-of-thumb `220 - age`, then use `pd.cut` to bucket `% hr_max` into 5 zones.
    """)
    return


@app.cell
def _(athletes, hr_session):
    hr_with_age = hr_session.merge(
        athletes[["athlete_id", "age"]], on="athlete_id", how="left"
    )
    hr_with_age["hr_max"] = 220 - hr_with_age["age"]
    hr_with_age["pct_hr_max"] = 100 * hr_with_age["heart_rate_bpm"] / hr_with_age["hr_max"]
    hr_with_age.head()
    return (hr_with_age,)


@app.cell
def _(hr_with_age, pd):
    hr_zoned = hr_with_age.assign(
        hr_zone=lambda d: pd.cut(
            d["pct_hr_max"],
            bins=[0, 60, 70, 80, 90, 1000],
            labels=["Zone 1", "Zone 2", "Zone 3", "Zone 4", "Zone 5"],
        )
    )
    hr_zoned["hr_zone"].value_counts()
    return (hr_zoned,)


@app.cell
def _(mo):
    mo.md("""
    Time per zone, per athlete, in minutes (each row is 1 second, so dividing a row count by 60 gives minutes):
    """)
    return


@app.cell
def _(hr_zoned):
    time_per_zone_minutes = (
        hr_zoned.groupby(["athlete_id", "hr_zone"], observed=True).size() / 60
    ).rename("minutes").reset_index()
    time_per_zone_minutes.head(10)
    return


@app.cell
def _(mo):
    mo.md("""
    A **rolling average** smooths out second-to-second noise; `resample` regroups a time-indexed series into fixed intervals (here, 1-minute bins) - both need the data sorted by time first.
    """)
    return


@app.cell
def _(hr_zoned):
    one_athlete = hr_zoned.loc[hr_zoned["athlete_id"] == hr_zoned["athlete_id"].iloc[0]].sort_values(
        "timestamp"
    )
    one_athlete_rolling = one_athlete.set_index("timestamp")["heart_rate_bpm"].rolling(
        "30s"
    ).mean()
    one_athlete_rolling.head()
    return (one_athlete,)


@app.cell
def _(one_athlete):
    one_athlete_per_minute = (
        one_athlete.set_index("timestamp")[["heart_rate_bpm", "speed_kmh"]]
        .resample("1min")
        .mean()
    )
    one_athlete_per_minute.head()
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 4 - time in zone 4-5 per athlete
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Using `hr_zoned`, compute `zone_4_5_minutes`: a Series indexed by `athlete_id` with the total minutes each athlete spent in `"Zone 4"` or `"Zone 5"` combined.
    """)
    return


@app.cell
def _(hr_zoned):
    zone_4_5_minutes = (
        hr_zoned.loc[hr_zoned["hr_zone"].isin(["Zone 4", "Zone 5"])].groupby("athlete_id").size() / 60
    )
    return (zone_4_5_minutes,)


@app.cell
def _(check_exercise, hr_zoned, zone_4_5_minutes):
    def _check():
        assert zone_4_5_minutes is not ..., "Replace `...` with your grouped computation."
        expected = (
            hr_zoned.loc[hr_zoned["hr_zone"].isin(["Zone 4", "Zone 5"])]
            .groupby("athlete_id")
            .size()
            / 60
        )
        assert set(zone_4_5_minutes.index) == set(expected.index), (
            "The set of athletes does not match."
        )
        aligned = zone_4_5_minutes.reindex(expected.index)
        assert (aligned.round(2) == expected.round(2)).all(), (
            "The minute counts don't match a Zone 4/5 filter + count / 60."
        )

    check_exercise(_check, "Time in zone 4-5 is computed correctly for every athlete.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 7. Mini-case, in pairs: training report (16:50-17:30)

    Build one summary row per athlete from `hr_zoned`: total minutes in
    zone 4-5, maximum speed reached, and total distance covered. Speed
    is recorded once per second, so distance for one row is
    `speed_kmh / 3600` kilometres; summing that over the session gives
    total distance.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Build `training_report`: one row per `athlete_id`, with columns `zone_4_5_minutes`, `max_speed_kmh` and `distance_km`. A `.agg` with a dictionary of named aggregations is one clean way to do this in a single `groupby` call - but any correct approach is fine.
    """)
    return


@app.cell
def _(hr_zoned):
    in_zone_4_5 = hr_zoned["hr_zone"].isin(["Zone 4", "Zone 5"])
    training_report = hr_zoned.assign(distance_km=hr_zoned["speed_kmh"] / 3600).groupby("athlete_id").agg(
        max_speed_kmh=("speed_kmh", "max"),
        distance_km=("distance_km", "sum"),
    )
    training_report["zone_4_5_minutes"] = in_zone_4_5.groupby(hr_zoned["athlete_id"]).sum() / 60
    return (training_report,)


@app.cell
def _(check_exercise, hr_zoned, training_report):
    def _check():
        assert training_report is not ..., "Replace `...` with your one-row-per-athlete summary."
        for col in ["zone_4_5_minutes", "max_speed_kmh", "distance_km"]:
            assert col in training_report.columns, f"Missing column `{col}`."
        assert set(training_report.index) == set(hr_zoned["athlete_id"].unique()) or set(
            training_report.get("athlete_id", [])
        ) == set(hr_zoned["athlete_id"].unique()), (
            "The report should have exactly one row per athlete in hr_zoned."
        )
        assert (training_report["distance_km"] > 0).all(), "Distance should be positive for every athlete."
        assert (training_report["max_speed_kmh"] <= 30).all(), "Max speed looks unrealistically high."

    check_exercise(_check, "Nice - that's a coach-ready training report.")
    return


@app.cell
def _(mo):
    mo.md("""
    See you next week for Datavisualisatie I, where `combined` and `hr_zoned` become the basis for a set of plotly charts and a small interactive dashboard.
    """)
    return


if __name__ == "__main__":
    app.run()
