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
    import numpy as np

    return (pd,)


@app.cell
def _(mo):
    mo.md(r"""
    # Data Processing I - From File to Tidy Table

    Welcome! For the next three sessions you are the new data analyst for a
    (fictional) youth football / athletics club. The head coach has handed
    you three export files from the club's systems:

    - **`athletes.csv`** - one row per athlete: ID, birthdate, gender,
      position, height and weight.
    - **`tests.csv`** - results from physical tests (10 m / 30 m sprint,
      countermovement jump height, Yo-Yo level) taken at several test
      moments during the season.
    - **`hr_session.csv`** - heart rate and speed per second for a few
      athletes during one training session, like an export from a Polar
      or Garmin device.

    The data is **real-world messy on purpose**: inconsistent position
    labels (`"Forward"`, `"forward "`, `"FWD"`), sprint times that are
    sometimes stored in milliseconds, missing values, a duplicated
    athlete, and a column that uses a comma as decimal separator. Today's
    goal is to turn this into a tidy, trustworthy table.

    **By the end of this session you can:** load a dataset, explore it,
    select and filter rows and columns, add new columns, and perform
    basic cleaning.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## A few things about marimo before we start

    This notebook is **reactive**: whenever you change a cell, every
    other cell that depends on it re-runs automatically, in the correct
    order - not necessarily top to bottom. Try the slider below.
    """)
    return


@app.cell
def _(mo):
    demo_slider = mo.ui.slider(1, 10, value=5, label="Move me")
    demo_slider
    return (demo_slider,)


@app.cell
def _(demo_slider, mo):
    mo.md(f"""
    {demo_slider.value} squared is **{demo_slider.value ** 2}**.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Notice that you didn't have to re-run anything by hand - moving the
    slider was enough.

    The second thing to know: **two cells cannot define the same global
    variable.** In a normal script you might write:

    ```python
    df = pd.read_csv(...)
    df = df.dropna()
    df = df.sort_values("age")
    ```

    In marimo, if you split these three lines into three different
    cells, you will get an error, because all three try to define `df`.
    The fix is good practice anyway: give each step a **descriptive
    name** (`tests_raw` -> `tests_no_missing` -> `tests_sorted`), or keep
    the whole chain inside a single cell. You will see this pattern
    throughout the notebook.

    Finally: exercise cells contain a `...` placeholder. Replace it with
    your own code. The cell right below it checks your answer
    automatically and turns green when it's correct.
    """)
    return


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
    ## Where does the data come from?

    For local development, this notebook reads the CSV files from the
    `data/` folder next to this project. When you deploy the notebook on
    **molab** (or share a WASM notebook link), there is no local
    filesystem to read from - point `DATA_DIR` at the raw URL of a
    GitHub repository instead, for example:

    ```python
    DATA_DIR = "https://raw.githubusercontent.com/<org>/<repo>/main/data"
    ```

    `pandas.read_csv` accepts both local paths and URLs, so nothing else
    in this notebook needs to change.
    """)
    return


@app.cell
def _(mo):
    # Local development default. For molab / WASM, replace with a raw GitHub URL.
    DATA_DIR = str(mo.notebook_dir() / ".." / "data")
    return (DATA_DIR,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Warm-up: why not just use Excel?

    `tests.csv` has a few hundred rows and eight columns - you *could*
    open it in Excel. But watch what happens once we need to combine
    three files, recompute a derived column for every row, or repeat the
    same cleaning step every week. Let's peek at the raw text of the file
    first.
    """)
    return


@app.cell
def _(DATA_DIR, mo):
    from pathlib import Path

    raw_lines_preview = Path(DATA_DIR, "tests.csv").read_text().splitlines()[:6]
    mo.vstack([mo.md("**First lines of `tests.csv`, as plain text:**"), mo.md("```\n" + "\n".join(raw_lines_preview) + "\n```")])
    return


@app.cell
def _(mo):
    mo.md("""
    Readable, but every value is just text, there is no notion of a column type, and there is no easy way to filter or aggregate. That is exactly what pandas gives us.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Loading and exploring a dataset (13:20-14:00)

    The core loading function is `pd.read_csv`. Once loaded, a handful
    of methods give you a fast first impression of any dataset:

    | Method | What it tells you |
    |---|---|
    | `.head()` | the first few rows |
    | `.shape` | (number of rows, number of columns) |
    | `.dtypes` | the data type pandas guessed per column |
    | `.info()` | dtypes + memory usage + non-null counts in one view |
    | `.describe()` | count, mean, std, min/max, quartiles for numeric columns |
    """)
    return


@app.cell
def _(DATA_DIR, pd):
    athletes_raw = pd.read_csv(f"{DATA_DIR}/athletes.csv")
    athletes_raw.head()
    return (athletes_raw,)


@app.cell
def _(athletes_raw):
    athletes_raw.shape
    return


@app.cell
def _(athletes_raw):
    athletes_raw.dtypes
    return


@app.cell
def _(athletes_raw):
    athletes_raw.describe(include="all")
    return


@app.cell
def _(mo):
    mo.md("""
    marimo can also render any dataframe as an interactive, sortable, searchable table with `mo.ui.table`. Try sorting by `height_cm` or searching for a name.
    """)
    return


@app.cell
def _(athletes_raw, mo):
    athletes_table = mo.ui.table(athletes_raw, page_size=10, label="athletes_raw")
    athletes_table
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 1 - load `tests.csv`
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Load `tests.csv` into a variable called `tests_raw`, and store its `.shape` in `tests_raw_shape`.
    """)
    return


@app.cell
def _(DATA_DIR, pd):
    # TODO: read data/tests.csv into `tests_raw` and store its shape
    tests_raw = pd.read_csv(f"{DATA_DIR}/tests.csv")
    tests_raw_shape = ...
    return tests_raw, tests_raw_shape


@app.cell
def _(check_exercise, tests_raw, tests_raw_shape):
    def _check():
        assert tests_raw_shape is not ..., "Replace `...` with `tests_raw.shape`."
        assert tests_raw_shape == tests_raw.shape, "That is not `tests_raw.shape`."
        assert tests_raw_shape[1] == 8, f"Expected 8 columns, got {tests_raw_shape[1]}."

    check_exercise(
        _check,
        f"`tests.csv` has {tests_raw.shape[0]} rows and {tests_raw.shape[1]} columns.",
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Selecting and filtering (14:00-14:50)

    A few core tools:

    - `df[["col_a", "col_b"]]` selects columns.
    - `df.loc[row_condition, column_list]` selects rows *and* columns at
      once.
    - A **boolean condition** such as `df["age"] < 16` produces a column
      of `True`/`False` values that you can pass straight into `.loc`.
    - `.sort_values("col")` sorts rows; add `ascending=False` to reverse.
    """)
    return


@app.cell
def _(athletes_raw):
    names_and_positions = athletes_raw[["name", "position"]]
    names_and_positions.head()
    return


@app.cell
def _(athletes_raw):
    only_forwards_raw = athletes_raw.loc[athletes_raw["position"] == "Forward"]
    only_forwards_raw.shape
    return


@app.cell
def _(mo):
    mo.md("""
    Only the rows spelled exactly `"Forward"` matched - `"forward "` and `"FWD"` did not. Keep that in mind; we'll fix it soon. For now, let's filter using something that isn't affected by spelling: the birthdate. Athletes born after 2010-09-01 are younger than 16 for the 2026 season.
    """)
    return


@app.cell
def _(athletes_raw, pd):
    younger_than_16 = pd.to_datetime(athletes_raw["birthdate"]) > "2010-09-01"
    athletes_raw.loc[younger_than_16, ["name", "birthdate", "position"]].head()
    return (younger_than_16,)


@app.cell
def _(mo):
    mo.md("""
    Sorting: which 30 m sprint times look the *slowest*? Sort descending and look at the top of the table.
    """)
    return


@app.cell
def _(tests_raw):
    tests_sorted_by_sprint = tests_raw.sort_values("sprint_30m_s", ascending=False)
    tests_sorted_by_sprint.head()
    return


@app.cell
def _(mo):
    mo.md("""
    The very top rows are in the thousands - over 1500 "seconds" for a 30 m sprint would mean the athlete stopped for a coffee halfway. Those are the values stored in milliseconds instead of seconds (5.97 s became 5970). Another thing to fix during cleaning.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 2 - forwards younger than 16
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Combine a position filter with the age filter above into `forwards_u16_raw`: rows from `athletes_raw` where `position` is exactly `"Forward"` **and** the athlete was born after 2010-09-01. (Yes, the exact-spelling condition will miss some forwards - that's expected for now.)
    """)
    return


@app.cell
def _():
    # TODO: select rows where position == "Forward" AND younger_than_16 is True
    forwards_u16_raw = ...
    return (forwards_u16_raw,)


@app.cell
def _(athletes_raw, check_exercise, forwards_u16_raw, younger_than_16):
    def _check():
        assert forwards_u16_raw is not ..., "Replace `...` with a filtered dataframe."
        expected = athletes_raw.loc[
            (athletes_raw["position"] == "Forward") & younger_than_16
        ]
        assert len(forwards_u16_raw) == len(expected), (
            f"Expected {len(expected)} rows, got {len(forwards_u16_raw)}."
        )
        assert (forwards_u16_raw["position"] == "Forward").all(), (
            "All rows must have position == 'Forward'."
        )

    check_exercise(_check, "That combination of filters is correct.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 3 - find the suspicious (raw) 30 m sprints
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Select the rows from `tests_raw` where `sprint_30m_s` is (strictly) greater than 20 - no real 30 m sprint takes that long, so these must be the millisecond-bug rows. Store the result in `suspicious_30m_raw`, sorted from most to least extreme.
    """)
    return


@app.cell
def _():
    # TODO: filter tests_raw for sprint_30m_s > 20, then sort descending
    suspicious_30m_raw = ...
    return (suspicious_30m_raw,)


@app.cell
def _(check_exercise, suspicious_30m_raw, tests_raw):
    def _check():
        assert suspicious_30m_raw is not ..., "Replace `...` with your filtered, sorted dataframe."
        expected = tests_raw.loc[tests_raw["sprint_30m_s"] > 20].sort_values(
            "sprint_30m_s", ascending=False
        )
        assert len(suspicious_30m_raw) == len(expected), (
            f"Expected {len(expected)} rows, got {len(suspicious_30m_raw)}."
        )
        assert list(suspicious_30m_raw["sprint_30m_s"]) == list(expected["sprint_30m_s"]), (
            "The rows are not sorted from most to least extreme."
        )

    check_exercise(
        _check,
        "You just found every row with an implausible sprint time - "
        "all of them are the millisecond bug, not real speed.",
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. New columns (15:05-15:50)

    Adding a column is just an assignment: `df["new_col"] = ...`. A few
    examples we'll need for this club:

    - **Age** from `birthdate`.
    - **Speed** in m/s and km/h from a sprint time.
    - **BMI** from height and weight - but `weight_kg` is stored as text
      with a *comma* as decimal separator (`"57,5"`), a common artifact
      of European-locale exports. We need to convert it to a proper
      number first.
    """)
    return


@app.cell
def _(athletes_raw):
    athletes_raw["weight_kg"].head()
    return


@app.cell
def _(athletes_raw):
    weight_kg_numeric = athletes_raw["weight_kg"].str.replace(",", ".").astype(float)
    weight_kg_numeric.head()
    return (weight_kg_numeric,)


@app.cell
def _(athletes_raw, pd):
    REFERENCE_DATE = pd.Timestamp("2026-09-14")
    age_years = (REFERENCE_DATE - pd.to_datetime(athletes_raw["birthdate"])).dt.days // 365
    age_years.head()
    return (REFERENCE_DATE,)


@app.cell
def _(tests_raw):
    speed_ms_raw = 30 / tests_raw["sprint_30m_s"]
    speed_kmh_raw = speed_ms_raw * 3.6
    speed_kmh_raw.describe()
    return


@app.cell
def _(mo):
    mo.md("""
    A max speed over 1000 km/h confirms it: some sprint times are in milliseconds. We'll fix the units properly in the cleaning section, then this computation will make sense.
    """)
    return


@app.cell
def _(athletes_raw):
    position_counts_raw = athletes_raw["position"].value_counts()
    position_counts_raw
    return (position_counts_raw,)


@app.cell
def _(mo, position_counts_raw):
    mo.md(f"""
    `value_counts()` on the raw `position` column returns "
        f"**{len(position_counts_raw)}** distinct labels, even though the "
        f"club only has 4 real positions. That's our cleaning target.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 4 - BMI
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Body Mass Index is `weight_kg / (height_cm / 100) ** 2`. Using
    `weight_kg_numeric` (already converted to a number above) and
    `athletes_raw["height_cm"]`, create a new column `bmi` on
    `athletes_raw` and store the whole (mutated) dataframe in
    `athletes_with_bmi`.
    """)
    return


@app.cell
def _(athletes_raw):
    # TODO: compute BMI and assign it as a new column
    athletes_with_bmi = athletes_raw.copy()
    athletes_with_bmi["bmi"] = ...
    return (athletes_with_bmi,)


@app.cell
def _(athletes_with_bmi, check_exercise, weight_kg_numeric):
    def _check():
        assert athletes_with_bmi["bmi"].iloc[0] is not Ellipsis, "Replace `...` with the BMI formula."
        assert not athletes_with_bmi["bmi"].isna().all(), "The bmi column should not be all-missing."
        expected_first = weight_kg_numeric.iloc[0] / (athletes_with_bmi["height_cm"].iloc[0] / 100) ** 2
        assert abs(athletes_with_bmi["bmi"].iloc[0] - expected_first) < 1e-6, (
            "The formula does not match weight_kg / (height_cm / 100) ** 2."
        )

    check_exercise(_check, "Your BMI column is computed correctly.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 5 - age in years
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Create a column `age` on `athletes_raw` using the same approach as `age_years` above, and store the result in `athletes_with_age`.
    """)
    return


@app.cell
def _(athletes_raw):
    # TODO: add an "age" column computed from birthdate
    athletes_with_age = athletes_raw.copy()
    athletes_with_age["age"] = ...
    return (athletes_with_age,)


@app.cell
def _(REFERENCE_DATE, athletes_with_age, check_exercise, pd):
    def _check():
        assert athletes_with_age["age"].iloc[0] is not Ellipsis, "Replace `...` with an age computation."
        expected = (REFERENCE_DATE - pd.to_datetime(athletes_with_age["birthdate"])).dt.days // 365
        assert (athletes_with_age["age"].dropna() == expected.dropna()).all(), (
            "The ages don't match REFERENCE_DATE - birthdate, in whole years."
        )
        assert athletes_with_age["age"].dropna().between(10, 19).all(), (
            "Some ages fall outside a plausible youth-club range (10-19)."
        )

    check_exercise(_check, "Ages look correct and plausible.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Cleaning (15:50-17:00)

    Time to fix everything the previous sections uncovered. A quick
    overview of missing values first:
    """)
    return


@app.cell
def _(athletes_raw):
    athletes_raw.isna().sum()
    return


@app.cell
def _(tests_raw):
    tests_raw.isna().sum()
    return


@app.cell
def _(mo):
    mo.md(r"""
    **`dropna()` vs `fillna()`** - neither is automatically "correct":

    - `dropna()` throws away the whole row (or column). Reasonable when
      very few rows are affected and you have no good way to guess the
      missing value, e.g. a missing `gender`.
    - `fillna()` keeps the row and substitutes a value - a constant, the
      column mean/median, or a value carried over from a neighbouring
      row (`.ffill()` / `.bfill()`). Reasonable when the column matters
      for downstream analysis and a reasonable estimate exists, e.g.
      filling one missing `cmj_height_cm` with that athlete's own
      average over other test moments.

    There is no universal rule - you have to justify the choice for
    *each* column.
    """)
    return


@app.cell
def _(mo):
    cleaning_quiz = mo.ui.radio(
        options=[
            "Always drop rows with any missing value - it's the safest option.",
            "Always fill missing values with 0 so calculations don't break.",
            "Decide per column: drop if few rows are affected and no good "
            "estimate exists, otherwise fill with a justified value.",
        ],
        label="Two athletes are missing a height_cm value. What's the best default approach?",
    )
    cleaning_quiz
    return (cleaning_quiz,)


@app.cell
def _(cleaning_quiz, mo):
    mo.callout(
        mo.md("Correct - there is no one-size-fits-all rule, decide per column."),
        kind="success",
    ) if cleaning_quiz.value and cleaning_quiz.value.startswith("Decide per column") else mo.md(
        "Pick an option above."
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Cleaning text: `position`

    The pattern `.str.strip().str.lower()` removes stray whitespace and
    normalizes case, which collapses most of the duplicate labels at
    once. Remaining abbreviations (`"fwd"`, `"mid"`, ...) need an
    explicit mapping.
    """)
    return


@app.cell
def _(athletes_raw):
    position_normalized = athletes_raw["position"].str.strip().str.lower()
    position_normalized.value_counts()
    return (position_normalized,)


@app.cell
def _(position_normalized):
    POSITION_MAP = {
        "forward": "Forward",
        "fwd": "Forward",
        "midfielder": "Midfielder",
        "mid": "Midfielder",
        "defender": "Defender",
        "def": "Defender",
        "goalkeeper": "Goalkeeper",
        "gk": "Goalkeeper",
    }
    position_clean = position_normalized.map(POSITION_MAP)
    position_clean.value_counts()
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 6 - clean positions on a fresh copy
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Build `athletes_step1`: a copy of `athletes_raw` where the `position` column has been replaced by `position_clean` (defined above).
    """)
    return


@app.cell
def _(athletes_raw):
    # TODO: copy athletes_raw and overwrite the position column with position_clean
    athletes_step1 = athletes_raw.copy()
    athletes_step1["position"] = ...
    return (athletes_step1,)


@app.cell
def _(athletes_step1, check_exercise):
    def _check():
        assert athletes_step1["position"].iloc[0] is not Ellipsis, "Assign `position_clean` to the column."
        assert set(athletes_step1["position"].unique()) == {
            "Forward", "Midfielder", "Defender", "Goalkeeper",
        }, "There should be exactly 4 clean position labels left."

    check_exercise(_check, "Exactly the 4 real positions remain.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Cleaning numbers: milliseconds vs seconds

    Rule of thumb for this dataset: no human runs 10 m or 30 m in under
    1 second flat, so any sprint value above, say, 20 is almost
    certainly stored in milliseconds and needs to be divided by 1000.
    """)
    return


@app.cell
def _(tests_raw):
    def fix_sprint_units(seconds_column):
        return seconds_column.where(seconds_column < 20, seconds_column / 1000)

    sprint_10m_fixed = fix_sprint_units(tests_raw["sprint_10m_s"])
    sprint_10m_fixed.describe()
    return (fix_sprint_units,)


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 7 - fix `sprint_30m_s`
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Use `fix_sprint_units` on `tests_raw["sprint_30m_s"]` and store it in `sprint_30m_fixed`.
    """)
    return


@app.cell
def _():
    # TODO: apply fix_sprint_units to the sprint_30m_s column
    sprint_30m_fixed = ...
    return (sprint_30m_fixed,)


@app.cell
def _(check_exercise, sprint_30m_fixed):
    def _check():
        assert sprint_30m_fixed is not ..., "Replace `...` with fix_sprint_units(tests_raw['sprint_30m_s'])."
        assert sprint_30m_fixed.max() < 20, f"Max value {sprint_30m_fixed.max()} still looks like milliseconds."
        assert sprint_30m_fixed.min() > 3, "Minimum sprint time looks unrealistically low."

    check_exercise(_check, "All 30 m sprint times are now in a realistic range (seconds).")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Duplicates

    `duplicated(subset=...)` flags rows that share the given columns
    with an earlier row.
    """)
    return


@app.cell
def _(athletes_step1):
    duplicate_flags = athletes_step1.duplicated(subset=["name", "birthdate"], keep="first")
    athletes_step1.loc[athletes_step1.duplicated(subset=["name", "birthdate"], keep=False)]
    return


@app.cell
def _(mo):
    mo.md("""
    Same name, same birthdate, two different `athlete_id`s - a data entry mistake. `drop_duplicates(subset=..., keep="first")` removes the extra row.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 8 - remove the duplicate athlete
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Build `athletes_deduped` from `athletes_step1` by dropping duplicate `(name, birthdate)` combinations, keeping the first occurrence.
    """)
    return


@app.cell
def _():
    # TODO: drop duplicate (name, birthdate) rows, keep the first
    athletes_deduped = ...
    return (athletes_deduped,)


@app.cell
def _(athletes_deduped, athletes_step1, check_exercise):
    def _check():
        assert athletes_deduped is not ..., "Replace `...` with a drop_duplicates call."
        assert len(athletes_deduped) == len(athletes_step1) - 1, (
            f"Expected exactly one row removed, went from {len(athletes_step1)} to {len(athletes_deduped)}."
        )
        assert not athletes_deduped.duplicated(subset=["name", "birthdate"]).any(), (
            "There is still a duplicate name+birthdate combination."
        )

    check_exercise(_check, "The duplicate athlete is gone.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Putting it all together

    Below is one finished, clean version of `athletes.csv`, combining
    every step above: cleaned positions, numeric weight, BMI, age,
    deduplication, a friendlier column order (`rename` + column
    selection), and explicit dtypes (`astype`) so every column has the
    type it should have.
    """)
    return


@app.cell
def _(REFERENCE_DATE, athletes_raw, pd):
    athletes_clean = (
        athletes_raw.assign(
            position=athletes_raw["position"].str.strip().str.lower().map(
                {
                    "forward": "Forward", "fwd": "Forward",
                    "midfielder": "Midfielder", "mid": "Midfielder",
                    "defender": "Defender", "def": "Defender",
                    "goalkeeper": "Goalkeeper", "gk": "Goalkeeper",
                }
            ),
            weight_kg=lambda d: d["weight_kg"].str.replace(",", ".").astype(float),
            age=lambda d: (REFERENCE_DATE - pd.to_datetime(d["birthdate"])).dt.days // 365,
        )
        .assign(bmi=lambda d: d["weight_kg"] / (d["height_cm"] / 100) ** 2)
        .drop_duplicates(subset=["name", "birthdate"], keep="first")
        .rename(columns={"gender": "sex"})
        .astype({"age": "Int64"})
        .reset_index(drop=True)
    )
    athletes_clean.head()
    return (athletes_clean,)


@app.cell
def _(athletes_clean):
    athletes_clean.dtypes
    return


@app.cell
def _(fix_sprint_units, tests_raw):
    tests_clean = tests_raw.assign(
        sprint_10m_s=fix_sprint_units(tests_raw["sprint_10m_s"]),
        sprint_30m_s=fix_sprint_units(tests_raw["sprint_30m_s"]),
    )
    tests_clean.describe()
    return (tests_clean,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 6. Challenge (17:00-17:30) - fastest 5 per position

    The coach wants a cleaned overview: **the 5 fastest athletes per
    position**, based on their best (lowest) 30 m sprint time across all
    test moments.

    This needs three ingredients you now have: `athletes_clean` (for
    position), `tests_clean` (for a trustworthy sprint time), and a way
    to combine and rank them. A short preview of a tool from next
    session: `groupby("position").head(5)` keeps the first 5 rows *per
    group* of an already-sorted dataframe - exactly what we need here.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Build `fastest_per_position`: merge `athletes_clean` and `tests_clean` on `athlete_id`, keep each athlete's *best* (minimum) `sprint_30m_s` per `athlete_id`, sort ascending by `sprint_30m_s`, then keep the top 5 rows per `position`.
    """)
    return


@app.cell
def _():
    # TODO: merge, reduce to each athlete's best sprint_30m_s, sort, then
    # take the top 5 per position.
    #
    # Hints:
    #   best_sprint = tests_clean.groupby("athlete_id")["sprint_30m_s"].min().reset_index()
    #   merged = athletes_clean.merge(best_sprint, on="athlete_id")
    #   fastest_per_position = merged.sort_values("sprint_30m_s").groupby("position").head(5)
    fastest_per_position = ...
    return (fastest_per_position,)


@app.cell
def _(athletes_clean, check_exercise, fastest_per_position, tests_clean):
    def _check():
        assert fastest_per_position is not ..., "Replace `...` with your merged, ranked dataframe."
        assert "position" in fastest_per_position.columns and "sprint_30m_s" in fastest_per_position.columns, (
            "The result needs both a `position` and a `sprint_30m_s` column."
        )
        counts = fastest_per_position.groupby("position").size()
        assert (counts <= 5).all(), "Some positions have more than 5 rows."
        best_sprint = tests_clean.groupby("athlete_id")["sprint_30m_s"].min().reset_index()
        expected = (
            athletes_clean.merge(best_sprint, on="athlete_id")
            .sort_values("sprint_30m_s")
            .groupby("position")
            .head(5)
        )
        assert set(fastest_per_position["athlete_id"]) == set(expected["athlete_id"]), (
            "The set of selected athletes does not match the expected top 5 per position."
        )

    check_exercise(_check, "That's the coach's shortlist - nicely done.")
    return


@app.cell
def _(mo):
    mo.md("""
    ## Exit ticket
    """)
    return


@app.cell
def _(mo):
    exit_ticket = mo.ui.text_area(
        label="What is the one pandas trick from today you're most likely to reuse, "
        "and what is still unclear?",
        rows=4,
        full_width=True,
    )
    exit_ticket
    return (exit_ticket,)


@app.cell
def _(exit_ticket, mo):
    mo.md("Thanks - see you next week for Data Processing II.") if exit_ticket.value else mo.md(
        "Write a few words above before you leave."
    )
    return


if __name__ == "__main__":
    app.run()
