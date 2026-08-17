import marimo

__generated_with = "0.23.16"
app = marimo.App(
    width="wide",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Introduction to Python for Sport Scientists
    ### A 4-hour hands-on course

    - Store and manipulate athlete data using Python's core data types
    - Write loops and conditional logic to process training data
    - Write your **own functions** to reuse analysis code
    - Read a piece of Python code with confidence

    We'll use running/cycling examples throughout: heart rate, training load,
    distance, pace. Every code cell in this notebook is **live** — change a
    number, re-run, and everything downstream updates automatically. That's
    the point of a marimo notebook: it behaves like a reactive spreadsheet.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 1 — Why Python? (10 min)

    Sport science increasingly means **data**: GPS files, heart rate monitors,
    power meters, questionnaires, video. Excel breaks down fast once:

    - You have hundreds of files that all need the same processing
    - You need reproducible analysis (run it again next week, get the same result)
    - You want to combine biomechanics, physiology, and training-load data in one place

    Python is a general-purpose programming language that has become a
    standard tool in sport science and exercise physiology research because:

    - It's free and open source
    - It has mature libraries for data (Polars, NumPy, pandas), statistics
      (SciPy, statsmodels), and plotting (matplotlib)
    - Code is a written, shareable, re-runnable record of your analysis —
      unlike a series of manual clicks in Excel

    Today we focus on **core Python**, the building blocks every one of
    those libraries is built on top of.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 2 — Variables & Data Types (30 min)

    A **variable** is a name that points to a value stored in memory —
    think of it as a labeled box.

    Python has a few core built-in types you'll use constantly:

    | Type | Example | Sport science use |
    |---|---|---|
    | `int` | `25` | age in years, number of reps |
    | `float` | `72.5` | weight in kg, VO2max |
    | `str` | `"Anna"` | athlete name |
    | `bool` | `True` | is the athlete injured? |

    Python figures out the type automatically from the value you assign —
    this is called **dynamic typing**. We'll still *write* the type
    ourselves with a **type hint** (`age: int = 25`); it costs nothing at
    runtime but makes the code much easier to read and to check with tools.
    """)
    return


@app.cell
def _():
    name: str = "Anna"
    age: int = 24
    height_m: float = 1.72
    weight_kg: float = 63.5
    is_injured: bool = False
    return age, height_m, is_injured, name, weight_kg


@app.cell
def _(age: int, height_m: float, is_injured: bool, mo, name: str):
    mo.md(f"""
    `name` is of type `{type(name).__name__}`
    `age` is of type `{type(age).__name__}`
    `height_m` is of type `{type(height_m).__name__}`
    `is_injured` is of type `{type(is_injured).__name__}`

    Try changing the values in the cell above — this cell updates
    automatically the moment you re-run it, no need to manually re-execute
    anything downstream.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 3 — Strings & f-strings (20 min)

    You'll constantly need to build readable text from variables — for
    reports, print statements, or file names. An **f-string** (formatted
    string) lets you embed variables directly inside text using curly
    braces `{ }`, and even format numbers (e.g. `.1f` rounds to one
    decimal).
    """)
    return


@app.cell
def _(age: int, height_m: float, name: str, weight_kg: float):
    bmi_preview: float = weight_kg / (height_m**2)
    summary: str = f"{name} is {age} years old, {height_m} m tall, and weighs {weight_kg} kg."
    print(summary)
    print(f"Rough BMI: {bmi_preview:.1f}")
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 4 — Lists (30 min)

    A **list** stores an ordered sequence of values. Perfect for a series
    of heart rate samples, session distances, or lap times.

    Key facts:

    - Written with square brackets: `[10, 20, 30]`
    - **Indexed from 0** — the first element is `my_list[0]`
    - Mutable — you can change, add, or remove elements after creation
    """)
    return


@app.cell
def _():
    heart_rates: list[int] = [142, 150, 155, 149, 160, 158, 145]
    return (heart_rates,)


@app.cell
def _(heart_rates: list[int], mo):
    first_reading: int = heart_rates[0]
    last_reading: int = heart_rates[-1]
    first_three: list[int] = heart_rates[0:3]
    n_readings: int = len(heart_rates)

    mo.md(
        f"""
        - First reading: `{first_reading}` (index `0`)
        - Last reading: `{last_reading}` (index `-1` — Python counts from the end too)
        - First three readings, via slicing `[0:3]`: `{first_three}`
        - Number of readings: `{n_readings}`, via `len()`
        """
    )
    return


@app.cell
def _(heart_rates: list[int], mo):
    heart_rates_extended: list[int] = heart_rates.copy()
    heart_rates_extended.append(152)  # add a new reading at the end
    max_hr_sample: int = max(heart_rates_extended)
    min_hr_sample: int = min(heart_rates_extended)

    mo.md(
        f"""
        `heart_rates_extended = heart_rates.copy()` then `.append(152)`:

        `{heart_rates_extended}`

        Max: `{max_hr_sample}` — Min: `{min_hr_sample}` (using the built-in
        `max()` and `min()` functions)
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 5 — Dictionaries (25 min)

    A **dictionary** stores `key: value` pairs. Instead of looking things
    up by position (like a list), you look values up by name — ideal for
    representing one athlete's profile.
    """)
    return


@app.cell
def _():
    athlete: dict[str, object] = {
        "name": "Anna",
        "age": 24,
        "sport": "cycling",
        "resting_hr": 48,
        "vo2max": 58.4,
    }
    return (athlete,)


@app.cell
def _(athlete: dict[str, object], mo):
    athlete_sport: str = athlete["sport"]
    athlete["ftp_watts"] = 265  # add a new key

    mo.md(
        f"""
        - Access a value: `athlete["sport"]` → `{athlete_sport}`
        - Add a new key: `athlete["ftp_watts"] = 265`

        Dictionary now looks like:

        `{athlete}`
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 6 — Conditionals: `if` / `elif` / `else` (30 min)

    Conditionals let your code make decisions:

    ```python
    if condition:
        ...
    elif other_condition:
        ...
    else:
        ...
    ```

    Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
    Logical operators: `and`, `or`, `not`
    """)
    return


@app.cell
def _(mo):
    hr_rest: int = 48
    hr_max: int = 190
    hr_current: int = 165

    hr_reserve_pct: float = (hr_current - hr_rest) / (hr_max - hr_rest) * 100

    if hr_reserve_pct < 60:
        hr_zone: str = "Zone 1-2 (easy)"
    elif hr_reserve_pct < 80:
        hr_zone = "Zone 3 (moderate)"
    else:
        hr_zone = "Zone 4-5 (hard)"

    mo.md(
        rf"""
        Using the **Karvonen formula** for heart rate reserve:

        $$\%HRR = \frac{{HR_{{current}} - HR_{{rest}}}}{{HR_{{max}} - HR_{{rest}}}} \times 100$$

        With current HR `{hr_current}`, resting HR `{hr_rest}`, max HR `{hr_max}`:
        `%HRR = {hr_reserve_pct:.1f}%` → **{hr_zone}**
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 7 — Loops: `for` and `while` (35 min)

    A `for` loop repeats an action **once for each item** in a sequence
    (like a list). A `while` loop repeats **as long as a condition stays
    true**, which is useful when you don't know the number of iterations
    in advance.
    """)
    return


@app.cell
def _(heart_rates: list[int], mo):
    total_hr: int = 0
    for reading in heart_rates:
        total_hr += reading
    avg_hr: float = total_hr / len(heart_rates)

    mo.md(
        f"Sum: `{total_hr}`, Average HR: `{avg_hr:.1f}` bpm — computed with a `for` loop over `heart_rates`."
    )
    return


@app.cell
def _(mo):
    weekly_distances: list[float] = [45.0, 50.0, 38.0, 60.0, 42.0]
    target_km: float = 150.0
    cumulative_km: float = 0.0
    weeks_needed: int = 0

    while cumulative_km < target_km and weeks_needed < len(weekly_distances):
        cumulative_km += weekly_distances[weeks_needed]
        weeks_needed += 1

    mo.md(
        f"""
        Simulating training weeks until a target of `{target_km}` km is reached:

        After `{weeks_needed}` week(s), cumulative distance is `{cumulative_km:.1f}` km.

        Notice the `while` loop needs **two** stopping conditions here
        (distance reached, *or* we run out of weeks) — always make sure a
        `while` loop can actually stop, or it will run forever.
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ---
    ## ☕ Break (15 min)

    Stretch, grab a coffee. When we're back: **functions** — the single
    most useful concept for turning one-off code into reusable analysis
    tools.
    ---
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 8 — Functions (45 min)

    A function packages up a block of code so you can reuse it with
    different inputs, instead of copy-pasting.

    ```python
    def function_name(parameter: type) -> return_type:
        "\""Docstring: what the function does."\""
        ...
        return result
    ```

    - **Parameters** are the inputs the function needs
    - The **return type hint** (`-> float`) documents what comes back
    - The **docstring** (triple-quoted string right under `def`) is the
      function's built-in documentation
    """)
    return


@app.function
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI given weight in kilograms and height in meters."""
    return weight_kg / (height_m**2)


@app.cell
def _(height_m: float, mo, weight_kg: float):
    bmi_result: float = calculate_bmi(weight_kg, height_m)
    mo.md(f"`calculate_bmi({weight_kg}, {height_m})` → `{bmi_result:.1f}`")
    return (bmi_result,)


@app.function
def classify_bmi(bmi: float, verbose: bool = True) -> str:
    """Classify a BMI value into a WHO category.

    If `verbose` is True (the default), also print the result.
    """
    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "normal"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "obese"

    if verbose:
        print(f"BMI {bmi:.1f} -> {category}")
    return category


@app.cell
def _(bmi_result: float, mo):
    category: str = classify_bmi(bmi_result, verbose=False)

    mo.md(
        f"""
        `classify_bmi({bmi_result:.1f})` → **{category}**

        Two things worth noticing:

        - `verbose: bool = True` is a **default parameter** — if you don't
          pass a value for it, Python uses `True`. We overrode it above with
          `verbose=False`.
        - The docstring documents the function without you having to read its
          body — hover the function name in most editors to see it.
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 9 — Mini project: training log analyzer (40 min)

    Let's combine everything: variables, a list of dictionaries, a loop,
    and two functions, to summarize a week of training sessions.
    """)
    return


@app.cell
def _():
    training_sessions: list[dict[str, float]] = [
        {"day": "Mon", "distance_km": 8.0, "duration_min": 40.0},
        {"day": "Wed", "distance_km": 12.0, "duration_min": 58.0},
        {"day": "Fri", "distance_km": 5.0, "duration_min": 22.0},
        {"day": "Sun", "distance_km": 15.0, "duration_min": 78.0},
    ]
    return (training_sessions,)


@app.cell
def _():
    def total_distance(sessions: list[dict[str, float]]) -> float:
        """Sum the distance_km field across a list of session dicts."""
        total: float = 0.0
        for session in sessions:
            total += session["distance_km"]
        return total

    def pace_min_per_km(distance_km: float, duration_min: float) -> float:
        """Return pace in minutes per kilometer."""
        return duration_min / distance_km

    return pace_min_per_km, total_distance


@app.cell
def _(
    mo,
    pace_min_per_km,
    total_distance,
    training_sessions: list[dict[str, float]],
):
    weekly_total_km: float = total_distance(training_sessions)

    lines: list[str] = []
    for session in training_sessions:
        pace: float = pace_min_per_km(session["distance_km"], session["duration_min"])
        lines.append(
            f"- {session['day']}: {session['distance_km']} km in "
            f"{session['duration_min']} min → pace {pace:.2f} min/km"
        )

    mo.md(
        "**Weekly summary**\n\n"
        + "\n".join(lines)
        + f"\n\n**Total distance this week: {weekly_total_km:.1f} km**"
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 10 — Exercises & quiz (25 min)

    ### Try it live

    Move the sliders below — `calculate_bmi` and `classify_bmi` from
    earlier in the notebook re-run automatically on new input.
    """)
    return


@app.cell
def _(mo):
    weight_input = mo.ui.number(start=30.0, stop=200.0, value=70.0, label="Weight (kg)")
    height_input = mo.ui.number(start=1.0, stop=2.5, value=1.75, step=0.01, label="Height (m)")
    mo.hstack([weight_input, height_input])
    return height_input, weight_input


@app.cell
def _(height_input, mo, weight_input):
    live_bmi: float = calculate_bmi(weight_input.value, height_input.value)
    live_category: str = classify_bmi(live_bmi, verbose=False)

    mo.md(
        f"BMI for {weight_input.value} kg / {height_input.value} m → "
        f"**{live_bmi:.1f}** ({live_category})"
    )
    return


@app.cell
def _(mo):
    quiz_answer = mo.ui.radio(
        options=["'a'", "'b'", "'c'", "IndexError"],
        label="What does `['a', 'b', 'c'][1]` return?",
    )
    quiz_answer
    return (quiz_answer,)


@app.cell
def _(mo, quiz_answer):
    if quiz_answer.value is None:
        feedback: str = "Pick an answer above to check yourself."
    elif quiz_answer.value == "'b'":
        feedback = "✅ Correct — indexing starts at 0, so index 1 is the second element."
    else:
        feedback = "❌ Not quite — remember indexing starts at 0, not 1."

    mo.md(feedback)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Your turn: write a function

    Write a function `time_in_zone(hr_list, lower, upper)` that takes a
    list of heart rate readings and returns how many of them fall between
    `lower` and `upper` (inclusive). A stub with a `TODO` is below — fill
    it in, then check your work against the solution underneath.
    """)
    return


@app.cell
def _(heart_rates: list[int]):
    def time_in_zone(hr_list: list[int], lower: int, upper: int) -> int:
        count: int = 0
        # TODO: loop through hr_list and increment count when
        # lower <= reading <= upper
        return count

    your_result: int = time_in_zone(heart_rates, 140, 155)
    return


@app.cell
def _(heart_rates: list[int], mo):
    def time_in_zone_solution(hr_list: list[int], lower: int, upper: int) -> int:
        """Count how many readings fall within [lower, upper], inclusive."""
        count: int = 0
        for reading in hr_list:
            if lower <= reading <= upper:
                count += 1
        return count

    solved_result: int = time_in_zone_solution(heart_rates, 140, 155)

    mo.accordion(
        {
            "Show solution": mo.md(
                f"""
                ```python
                def time_in_zone(hr_list: list[int], lower: int, upper: int) -> int:
                    count = 0
                    for reading in hr_list:
                        if lower <= reading <= upper:
                            count += 1
                    return count
                ```

                On our sample data: `time_in_zone(heart_rates, 140, 155)` → `{solved_result}`
                """
            )
        }
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## Part 11 — Wrap-up & next steps (10 min)

    Today you covered:

    - Variables and the four core types (`int`, `float`, `str`, `bool`)
    - `list` and `dict` — the two workhorse data structures
    - `if` / `elif` / `else` for decisions
    - `for` and `while` loops for repetition
    - Writing your own **functions**, with parameters, default values,
      return values, and docstrings

    That's genuinely enough to start automating real analysis tasks.

    **Where to go next:**

    - **Polars** (or pandas) for tabular data — think spreadsheets, but
      scriptable and fast
    - **NumPy** for numerical arrays and vectorized math
    - **matplotlib** for plots
    - Practice by rewriting something you currently do in Excel as a small
      Python script — that's usually the fastest way the concepts stick

    Keep this notebook — it's designed so every cell re-runs live; come
    back and experiment with the numbers whenever you want a refresher.
    """)
    return


if __name__ == "__main__":
    app.run()
