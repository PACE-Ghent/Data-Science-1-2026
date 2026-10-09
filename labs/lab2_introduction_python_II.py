import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Introduction to Python II - Functions, Strings, Collections and Loops

    Last week we worked with **one athlete at a time**. A real club has
    dozens of athletes, each with several test results - and we don't
    want to copy-paste the same three lines of code forty times.

    Today we build the tools to scale up: our **own functions** to reuse
    code, **string methods** to clean up messy text, **collections**
    (lists, tuples, dictionaries, sets) to store many values at once,
    and **loops** to process all of them. We end by reading the club's
    real `athletes.csv` file with plain Python.

    **By the end of this session you can:** write and call your own
    functions, clean text with string methods, explain where a variable
    is visible (scope), store data in lists, tuples, dictionaries and
    sets, and process them with `for` and `while` loops.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Quick marimo reminder: each variable can be defined by **only one
    cell**, and exercise cells contain a `...` placeholder or a `# TODO`
    comment for you to replace. The cell right below checks your answer.
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
    import sys

    # In the browser (marimo.app / WASM) there is no local data/ folder,
    # so read the CSV files straight from GitHub instead.
    if sys.platform == "emscripten":
        DATA_DIR = "https://raw.githubusercontent.com/PACE-Ghent/Data-Science-1-2026/main/data"
    else:
        DATA_DIR = str(mo.notebook_dir() / ".." / "data")
    return (DATA_DIR,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Warm-up: recap of last week (13:00-13:15)

    During a 30 m sprint test, timing gates also record the 10 m split.
    The part between 10 m and 30 m (a "flying 20 m") tells you something
    about an athlete's **maximal** speed, because the acceleration phase
    is mostly over.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 1 - flying 20 m
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Compute the time between 10 m and 30 m, rounded to 2 decimals, in
    `flying_20m_s`. Then compute the average speed over those 20 m in
    km/h, rounded to 1 decimal, in `flying_20m_kmh`.
    """)
    return


@app.cell
def _():
    warmup_sprint_10m_s = 1.92
    warmup_sprint_30m_s = 5.21
    # TODO: time between 10 m and 30 m, then speed in km/h
    flying_20m_s = ...
    flying_20m_kmh = ...
    return flying_20m_kmh, flying_20m_s


@app.cell
def _(check_exercise, flying_20m_kmh, flying_20m_s):
    def _check():
        assert flying_20m_s is not ... and flying_20m_kmh is not ..., "Replace both `...`."
        assert flying_20m_s == 3.29, f"Expected 3.29 s, got {flying_20m_s}."
        assert flying_20m_kmh == 21.9, (
            f"Expected 21.9 km/h, got {flying_20m_kmh}. (20 m / time gives m/s; multiply by 3.6 for km/h.)"
        )

    check_exercise(
        _check,
        "Now imagine doing this for 43 athletes, 3 test moments each... "
        "That's what functions and loops are for.",
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Writing your own functions (13:15-14:00)

    Last week you **called** functions such as `round()` and `max()`.
    Now you'll **define** your own:

    ```python
    def speed_kmh(distance_m, time_s):
        '''Average speed in km/h over a distance run in a given time.'''
        speed_ms = distance_m / time_s
        return speed_ms * 3.6
    ```

    - `def` starts the definition, followed by the function's **name**
      and its **parameters** between parentheses, and a colon.
    - The indented **body** runs every time the function is called.
    - `return` hands a value back to whoever called the function - and
      immediately ends the function.
    - The text in triple quotes right below the `def` line is the
      **docstring**: documentation for whoever uses the function
      (`help(speed_kmh)` shows it).

    Defining a function does nothing visible yet - it only runs when you
    **call** it: `speed_kmh(30, 5.34)`. The values you pass in are called
    **arguments**.
    """)
    return


@app.cell
def _():
    def speed_kmh(distance_m, time_s):
        """Average speed in km/h over a distance run in a given time."""
        speed_ms = distance_m / time_s
        return speed_ms * 3.6

    print(speed_kmh(30, 5.34))
    print(speed_kmh(20, 3.29))
    print(speed_kmh(time_s=5.34, distance_m=30))  # keyword arguments: order doesn't matter
    return (speed_kmh,)


@app.cell
def _(mo):
    mo.md(r"""
    ### `return` is not the same as `print`

    A function that only **prints** shows something on screen, but gives
    nothing back: the result of calling it is `None`. You can't compute
    further with it.
    """)
    return


@app.cell
def _():
    def print_speed_kmh(distance_m, time_s):
        print(distance_m / time_s * 3.6)

    printed_result = print_speed_kmh(30, 5.34)
    print("What came back:", printed_result)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Default values

    A parameter can have a **default value**, used when the caller
    doesn't pass that argument. Parameters with a default go **after**
    the ones without.
    """)
    return


@app.cell
def _(speed_kmh):
    def sprint_speed_kmh(time_s, distance_m=30):
        """Speed in km/h for a sprint test; the default distance is 30 m."""
        return round(speed_kmh(distance_m, time_s), 1)

    print(sprint_speed_kmh(5.34))
    print(sprint_speed_kmh(1.92, distance_m=10))
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 2 - a BMI function
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Write a function `bmi(weight_kg, height_cm)` that **returns** the BMI
    rounded to 1 decimal. Remember: BMI = weight in kg / (height in
    **metres**)².
    """)
    return


@app.cell
def _():
    def bmi(weight_kg, height_cm):
        """Body Mass Index, rounded to 1 decimal."""
        # TODO: compute and return the BMI
        return ...

    return (bmi,)


@app.cell
def _(bmi, check_exercise):
    def _check():
        assert bmi(65.5, 167.1) is not ..., "Replace `return ...` with the BMI computation."
        assert bmi(65.5, 167.1) is not None, "Your function returns None - did you `print` instead of `return`?"
        assert bmi(65.5, 167.1) == 23.5, f"bmi(65.5, 167.1) should be 23.5, got {bmi(65.5, 167.1)}."
        assert bmi(66.2, 176.3) == 21.3, f"bmi(66.2, 176.3) should be 21.3, got {bmi(66.2, 176.3)}."

    check_exercise(_check, "One function, reusable for every athlete in the club.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 3 - heart rate zones as a function
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Turn last week's heart rate zone logic into a function
    `hr_zone(heart_rate, hr_max=200)` that returns the zone as an integer:

    | % of `hr_max` | Zone |
    |---|---|
    | below 60 | `1` |
    | 60 up to 70 | `2` |
    | 70 up to 80 | `3` |
    | 80 up to 90 | `4` |
    | 90 or higher | `5` |

    Tip: inside a function you can `return` straight from each branch of
    the `if` / `elif` / `else`.
    """)
    return


@app.cell
def _():
    def hr_zone(heart_rate, hr_max=200):
        """Heart rate zone (1-5) based on the percentage of hr_max."""
        # TODO: compute the percentage and return the zone
        return ...

    return (hr_zone,)


@app.cell
def _(check_exercise, hr_zone):
    def _check():
        assert hr_zone(150) is not ..., "Replace `return ...` with your zone logic."
        cases = [
            ((100,), 1), ((130,), 2), ((150,), 3), ((170,), 4), ((190,), 5),
            ((119,), 1), ((120,), 2), ((180,), 5),
            ((150, 180), 4), ((150, 250), 2),
        ]
        for args, expected in cases:
            call = f"hr_zone({', '.join(str(a) for a in args)})"
            assert hr_zone(*args) == expected, f"`{call}` should be {expected}, got {hr_zone(*args)!r}."

    check_exercise(_check, "Your function handles every zone, and the default `hr_max` works.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. String methods (14:00-14:40)

    In Python every value is an **object**, and many objects come with
    their own built-in functions, called **methods**. You call a method
    with a dot: `value.method(arguments)`. Strings have a lot of them -
    exactly what you need for messy club exports.

    | Method | Does | Example | Result |
    |---|---|---|---|
    | `.strip()` | remove spaces at both ends | `" forward ".strip()` | `"forward"` |
    | `.lower()` / `.upper()` | change case | `"FWD".lower()` | `"fwd"` |
    | `.title()` | capitalise every word | `"yana de backer".title()` | `"Yana De Backer"` |
    | `.replace(old, new)` | replace text | `"65,5".replace(",", ".")` | `"65.5"` |
    | `.split(sep)` | cut into a list of pieces | `"2010-05-27".split("-")` | `["2010", "05", "27"]` |
    | `.startswith(x)` | does it start with `x`? | `"A001".startswith("A")` | `True` |
    | `.count(x)` | how often does `x` occur? | `"Backer".count("e")` | `1` |

    Strings can also be **indexed** and **sliced** (counting starts at
    `0`): `"Yana"[0]` is `"Y"`, `"2010-05-27"[:4]` is `"2010"`. And
    `x in text` checks whether `x` occurs somewhere in `text`.

    **Important:** strings are **immutable**. A method never changes the
    original string, it **returns a new one**. If you want to keep the
    result, assign it: `position = position.strip()`.
    """)
    return


@app.cell
def _():
    raw_position = "  forward "
    raw_position.strip()
    print(repr(raw_position))  # unchanged!

    cleaned_position = raw_position.strip().title()  # methods can be chained
    print(repr(cleaned_position))

    print("65,5".replace(",", "."))
    print("Yana De Backer".split(" "))
    print("2010-05-27"[:4])
    print("De" in "Yana De Backer")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Formatting numbers in f-strings

    Inside the curly braces of an f-string you can add a **format spec**
    after a colon: `{value:.2f}` shows 2 decimals, `{value:>8}` right-aligns
    in 8 characters. Great for tidy reports.
    """)
    return


@app.cell
def _(speed_kmh):
    report_speed = speed_kmh(30, 5.34)
    print(f"Speed: {report_speed}")
    print(f"Speed: {report_speed:.1f} km/h")
    print(f"|{'Yana':>8}|{5.34:>6.2f}|")
    print(f"|{'Stan':>8}|{5.62:>6.2f}|")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 4 - parse a weight
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The club's export stores weights as text with a **comma** as decimal
    separator (`"65,5"`) - and sometimes with stray spaces. Write
    `parse_weight(text)` that returns the weight as a `float`.
    """)
    return


@app.cell
def _():
    def parse_weight(text):
        """Convert a weight like ' 65,5' to the float 65.5."""
        # TODO: clean the text, then convert it to a float
        return ...

    return (parse_weight,)


@app.cell
def _(check_exercise, parse_weight):
    def _check():
        assert parse_weight("65,5") is not ..., "Replace `return ...`."
        for text, expected in [("65,5", 65.5), (" 59,6", 59.6), ("70", 70.0), ("61.1 ", 61.1)]:
            result = parse_weight(text)
            assert isinstance(result, float), f"parse_weight({text!r}) should return a float, got {type(result).__name__}."
            assert result == expected, f"parse_weight({text!r}) should be {expected}, got {result!r}."

    check_exercise(_check, "Commas, dots and stray spaces are all handled.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 5 - clean a position label
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The `position` column of the club's export is a mess: `"Forward"`,
    `"forward "`, `"FWD"`, `"MID"`, `"GK"`, `"defender "`, ... Write
    `clean_position(raw)` that returns one of the four clean labels
    `"Forward"`, `"Midfielder"`, `"Defender"` or `"Goalkeeper"`, and
    `"Unknown"` for anything else.

    The abbreviations are `fwd`, `mid`, `def` and `gk`. Tip: first
    normalise the text with `.strip().lower()`, then use `if` / `elif`
    with `or`.
    """)
    return


@app.cell
def _():
    def clean_position(raw):
        """Map a messy position label to one of four clean labels."""
        # TODO: normalise raw, then return the clean label
        return ...

    return (clean_position,)


@app.cell
def _(check_exercise, clean_position):
    def _check():
        assert clean_position("Forward") is not ..., "Replace `return ...`."
        cases = {
            "Forward": "Forward", "forward ": "Forward", "FWD": "Forward",
            "midfielder": "Midfielder", "MID": "Midfielder",
            "defender ": "Defender", "DEF": "Defender",
            "goalkeeper": "Goalkeeper", "GK": "Goalkeeper",
            "coach": "Unknown",
        }
        for raw, expected in cases.items():
            assert clean_position(raw) == expected, (
                f"clean_position({raw!r}) should be {expected!r}, got {clean_position(raw)!r}."
            )

    check_exercise(_check, "Every messy label maps to a clean one.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 6 - birth year from a date
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Birthdates are stored as text in the format `"YYYY-MM-DD"`. Write
    `birth_year_from_date(date_text)` that returns the year as an `int`.
    There are two ways: `.split("-")` gives a list whose first element
    (`[0]`) is the year, or slice the first four characters.
    """)
    return


@app.cell
def _():
    def birth_year_from_date(date_text):
        """Return the year of a 'YYYY-MM-DD' date as an int."""
        # TODO: extract the year and convert it to an int
        return ...

    return (birth_year_from_date,)


@app.cell
def _(birth_year_from_date, check_exercise):
    def _check():
        assert birth_year_from_date("2010-05-27") is not ..., "Replace `return ...`."
        assert birth_year_from_date("2010-05-27") == 2010, (
            f"Expected 2010, got {birth_year_from_date('2010-05-27')!r}. Did you convert to int?"
        )
        assert birth_year_from_date("2014-02-07") == 2014, "Wrong result for '2014-02-07'."

    check_exercise(_check, "Years extracted and converted.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. Scope: where is a variable visible? (14:40-15:00)

    Variables created **inside** a function (including its parameters)
    are **local**: they only exist while the function runs, and are
    invisible outside it. Variables created outside any function are
    **global**: a function can *read* them.

    Assigning to a name inside a function creates a **new local
    variable**, even if a global with the same name exists. The global
    stays untouched.

    Before running anything, predict what the code below prints:

    ```python
    threshold = 5.5

    def is_fast(time_s):
        threshold = 5.0
        return time_s < threshold

    print(is_fast(5.3), threshold)
    ```
    """)
    return


@app.cell
def _(mo):
    scope_quiz = mo.ui.radio(
        options=["True 5.5", "False 5.5", "True 5.0", "False 5.0"],
        label="What does the code above print?",
    )
    scope_quiz
    return (scope_quiz,)


@app.cell
def _(mo, scope_quiz):
    mo.callout(
        mo.md(
            "Correct - inside the function `threshold` is a *local* 5.0, so 5.3 is not fast. "
            "The global `threshold` is still 5.5."
        ),
        kind="success",
    ) if scope_quiz.value == "False 5.5" else mo.md(
        "Pick an option above." if scope_quiz.value is None else "Not quite - run the cell below and look again."
    )
    return


@app.cell
def _():
    sprint_threshold_s = 5.5

    def is_fast_sprint(time_s):
        sprint_threshold_s = 5.0  # a new, local variable
        local_note = "I only exist inside the function"
        return time_s < sprint_threshold_s

    print(is_fast_sprint(5.3), sprint_threshold_s)
    # print(local_note)  # uncomment this line: NameError, local_note is local
    return


@app.cell
def _(mo):
    mo.md(r"""
    Good practice: a function should get everything it needs through its
    **parameters**, and hand its result back with `return`. Functions
    that silently depend on global variables are hard to reuse and test.

    **marimo twist:** a variable whose name starts with an underscore
    (`_total`) is **local to its cell** - other cells can't see it, and
    you can reuse the name in another cell. That's handy for throw-away
    helper variables, like loop counters.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 7 - remove a hidden global
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The function `age_in_season` below depends on the global
    `SEASON_YEAR`. Rewrite it so the season year becomes a **parameter**
    `season_year` with a **default value** of `2026`. After your change,
    `age_in_season(2010)` should still be `16`, and
    `age_in_season(2010, season_year=2030)` should be `20`.
    """)
    return


@app.cell
def _():
    SEASON_YEAR = 2026

    # TODO: make season_year a parameter with default 2026
    def age_in_season(birth_year):
        return SEASON_YEAR - birth_year

    return (age_in_season,)


@app.cell
def _(age_in_season, check_exercise):
    def _check():
        assert age_in_season(2010) == 16, f"age_in_season(2010) should be 16, got {age_in_season(2010)!r}."
        try:
            age_2030 = age_in_season(2010, season_year=2030)
        except TypeError:
            raise AssertionError("`age_in_season` has no `season_year` parameter yet.")
        assert age_2030 == 20, f"age_in_season(2010, season_year=2030) should be 20, got {age_2030!r}."

    check_exercise(_check, "The function no longer depends on a hidden global.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ☕ Break (15:00-15:10)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Collections (15:10-16:00)

    A **collection** stores many values under a single name. Python has
    four built-in ones:

    | Type | Written as | Ordered? | Changeable? | Duplicates? | Club example |
    |---|---|---|---|---|---|
    | `list` | `[5.34, 5.29, 5.41]` | yes | yes | yes | sprint times over a season |
    | `tuple` | `(167.1, 65.5)` | yes | no | yes | (height, weight) pair |
    | `dict` | `{"name": "Yana", "position": "Defender"}` | yes | yes | keys unique | one athlete's profile |
    | `set` | `{"Forward", "Defender"}` | no | yes | no | the distinct positions |

    ### Lists

    - Index from `0`: `times[0]` is the first element, `times[-1]` the
      last one. Slicing `times[1:3]` gives elements 1 and 2.
    - `len()`, `min()`, `max()`, `sum()` and `sorted()` all work on lists.
    - `x in times` checks whether a value is present.
    - Lists are **mutable**: `.append(x)` adds an element *to the same
      list*.

    **marimo tip:** only modify a list (e.g. with `.append`) in the
    **same cell** that creates it. marimo doesn't notice when another
    cell changes a list in place, so dependent cells wouldn't re-run.
    """)
    return


@app.cell
def _():
    season_sprints_s = [5.41, 5.34, 5.29, 5.36]
    print(season_sprints_s[0], season_sprints_s[-1])
    print(season_sprints_s[1:3])
    print(len(season_sprints_s), min(season_sprints_s), sum(season_sprints_s))
    print(sorted(season_sprints_s))
    print(5.29 in season_sprints_s)

    season_sprints_s.append(5.22)  # same cell - fine
    print(season_sprints_s)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Tuples

    A tuple is like a list that can't be changed after creation. You'll
    mostly meet them through **unpacking**: assigning the elements to
    several variables in one go. A function that returns several values
    separated by commas actually returns a tuple.
    """)
    return


@app.cell
def _():
    body = (167.1, 65.5)
    body_height_cm, body_weight_kg = body  # unpacking

    def min_and_max(values):
        return min(values), max(values)

    fastest_s, slowest_s = min_and_max([5.41, 5.34, 5.29])
    print(body_height_cm, body_weight_kg, fastest_s, slowest_s)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Dictionaries

    A dictionary maps **keys** to **values**. Instead of looking values up
    by position, you look them up by name: `athlete["position"]`.

    - `d[key]` gives the value, and raises a `KeyError` if the key is
      missing. `d.get(key, default)` returns `default` instead.
    - `d[key] = value` adds or overwrites a key.
    - `key in d` checks whether a key exists.
    - `d.keys()`, `d.values()` and `d.items()` give the keys, the values,
      and `(key, value)` pairs.

    A dictionary is also the perfect **lookup table** - for example to
    translate messy labels into clean ones.
    """)
    return


@app.cell
def _():
    yana = {
        "athlete_id": "A001",
        "name": "Yana De Backer",
        "position": "Defender",
        "height_cm": 167.1,
    }
    print(yana["name"])
    print(yana.get("yoyo_level", "not tested"))
    yana["weight_kg"] = 65.5  # same cell - fine
    print(yana.keys())
    print(yana)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Sets

    A set keeps only **unique** values, without order. Turning a list into
    a set is the quickest way to see which distinct values it contains.
    """)
    return


@app.cell
def _():
    raw_positions = [
        "defender ", "midfielder", "Defender", "MID", "goalkeeper", "Forward",
        "GK", "FWD", "forward", "Midfielder", "DEF", "forward ", "FWD", "midfielder",
    ]
    print(len(raw_positions), "labels,", len(set(raw_positions)), "distinct:")
    print(set(raw_positions))
    return (raw_positions,)


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 8 - a season of sprints
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Using the list `emma_sprints_s` below, compute:

    - `emma_n_tests`: the number of tests,
    - `emma_best_s`: her fastest time,
    - `emma_average_s`: her average time, rounded to 2 decimals,
    - `emma_last_two`: a list with her last two times (use slicing).
    """)
    return


@app.cell
def _():
    emma_sprints_s = [5.62, 5.55, 5.48, 5.51, 5.39]
    # TODO: use len, min, sum, round and slicing
    emma_n_tests = ...
    emma_best_s = ...
    emma_average_s = ...
    emma_last_two = ...
    return emma_average_s, emma_best_s, emma_last_two, emma_n_tests


@app.cell
def _(check_exercise, emma_average_s, emma_best_s, emma_last_two, emma_n_tests):
    def _check():
        for label, value in [("emma_n_tests", emma_n_tests), ("emma_best_s", emma_best_s),
                             ("emma_average_s", emma_average_s), ("emma_last_two", emma_last_two)]:
            assert value is not ..., f"Replace `...` for `{label}`."
        assert emma_n_tests == 5, f"Expected 5 tests, got {emma_n_tests}."
        assert emma_best_s == 5.39, f"Expected 5.39, got {emma_best_s}."
        assert emma_average_s == 5.51, f"Expected an average of 5.51, got {emma_average_s}."
        assert emma_last_two == [5.51, 5.39], f"Expected [5.51, 5.39], got {emma_last_two}."

    check_exercise(_check, "Emma is getting faster - her last test was her best.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 9 - a lookup table for positions
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The long `if` / `elif` chain in `clean_position` works, but a
    dictionary is shorter and easier to extend. Complete `POSITION_MAP`
    with the missing defender and goalkeeper labels, and write
    `clean_position_v2(raw)`: normalise `raw` with `.strip().lower()` and
    look it up with `.get(...)`, returning `"Unknown"` when the label is
    not in the map.
    """)
    return


@app.cell
def _():
    POSITION_MAP = {
        "forward": "Forward",
        "fwd": "Forward",
        "midfielder": "Midfielder",
        "mid": "Midfielder",
        # TODO: add the four missing entries
    }

    def clean_position_v2(raw):
        """Map a messy position label to a clean one using POSITION_MAP."""
        # TODO: normalise raw and look it up in POSITION_MAP
        return ...

    return (clean_position_v2,)


@app.cell
def _(check_exercise, clean_position_v2):
    def _check():
        assert clean_position_v2("FWD") is not ..., "Replace `return ...` in clean_position_v2."
        cases = {
            "forward ": "Forward", "MID": "Midfielder", "defender ": "Defender",
            "DEF": "Defender", "Goalkeeper": "Goalkeeper", "GK": "Goalkeeper", "coach": "Unknown",
        }
        for raw, expected in cases.items():
            assert clean_position_v2(raw) == expected, (
                f"clean_position_v2({raw!r}) should be {expected!r}, got {clean_position_v2(raw)!r}."
            )

    check_exercise(_check, "Same result as Exercise 5, in far fewer lines.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 6. Loops (16:00-16:50)

    A `for` loop runs its (indented) body **once for every element** of a
    collection, each time with the loop variable referring to the next
    element:

    ```python
    for time_s in season_sprints_s:
        print(time_s)
    ```

    A few patterns you'll use over and over:

    - **Accumulate**: start with `total = 0` before the loop, add to it
      inside the loop.
    - **Filter / transform into a new list**: start with an empty list
      `[]` and `.append()` inside the loop.
    - **Count per category**: start with an empty dict `{}` and do
      `counts[key] = counts.get(key, 0) + 1`.

    Handy helpers:

    - `range(n)` gives the numbers `0, 1, ..., n - 1`.
    - `enumerate(items)` gives `(index, item)` pairs.
    - `zip(a, b)` walks through two lists side by side.
    - `for key, value in d.items():` loops over a dictionary.
    - `break` stops the loop early; `continue` skips to the next element.

    A `while` loop repeats **as long as a condition is `True`** - useful
    when you don't know in advance how many repetitions you need. Make
    sure the condition eventually becomes `False`, or the loop never
    stops!

    **marimo tip:** the loop variable is an ordinary variable of the
    cell. Start it with an underscore (`for _time in ...`) so you can
    reuse the name in other cells.
    """)
    return


@app.cell
def _():
    loop_sprints_s = [5.41, 5.34, 5.29, 5.36]

    loop_total_s = 0
    for _time in loop_sprints_s:
        loop_total_s += _time
    print("Average:", round(loop_total_s / len(loop_sprints_s), 2))

    for _index, _time in enumerate(loop_sprints_s):
        print(f"Test {_index + 1}: {_time} s")

    for _name, _time in zip(["Yana", "Stan", "Emma"], [5.34, 5.62, 5.39]):
        print(_name, "ran", _time)
    return


@app.cell
def _(raw_positions):
    demo_counts = {}
    for _label in raw_positions:
        _key = _label.strip().lower()
        demo_counts[_key] = demo_counts.get(_key, 0) + 1

    for _key, _count in demo_counts.items():
        print(f"{_key:>12}: {_count}")
    return


@app.cell
def _():
    # while: how many weeks until the squad has run 100 km in total, at 12.5 km per week?
    distance_so_far_km = 0
    weeks_counted = 0
    while distance_so_far_km < 100:
        distance_so_far_km += 12.5
        weeks_counted += 1
    print(weeks_counted, "weeks,", distance_so_far_km, "km")
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Bonus - list comprehensions.** The "transform into a new list"
    pattern is so common that Python has a one-line shortcut for it:
    `[expression for item in items if condition]`. You'll see it often in
    other people's code.
    """)
    return


@app.cell
def _():
    comprehension_times_s = [5.41, 5.34, 5.29, 5.36]
    rounded_speeds = [round(30 / _t * 3.6, 1) for _t in comprehension_times_s]
    quick_times = [_t for _t in comprehension_times_s if _t < 5.35]
    print(rounded_speeds, quick_times)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 10 - loop over the test day
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    `test_day_s` holds the 30 m times of everyone tested today. With a
    `for` loop, compute:

    - `n_under_5_5`: how many times are **under 5.5 s**,
    - `test_day_kmh`: a new list with every time converted to km/h
      (`30 / time * 3.6`), rounded to 1 decimal, in the same order.
    """)
    return


@app.cell
def _():
    test_day_s = [5.34, 5.62, 5.29, 5.71, 5.48, 5.93, 5.12, 5.55]
    # TODO: start n_under_5_5 at 0 and test_day_kmh as an empty list,
    # then loop over test_day_s
    n_under_5_5 = ...
    test_day_kmh = ...
    return n_under_5_5, test_day_kmh, test_day_s


@app.cell
def _(check_exercise, n_under_5_5, test_day_kmh, test_day_s):
    def _check():
        assert n_under_5_5 is not ... and test_day_kmh is not ..., "Replace both `...`."
        assert n_under_5_5 == 4, f"Expected 4 times under 5.5 s, got {n_under_5_5}."
        expected = [round(30 / t * 3.6, 1) for t in test_day_s]
        assert isinstance(test_day_kmh, list), "`test_day_kmh` should be a list."
        assert test_day_kmh == expected, f"Expected {expected}, got {test_day_kmh}."

    check_exercise(_check, "Half of today's group ran under 5.5 s.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 11 - count athletes per position
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Loop over `raw_positions` (defined in the section on sets), clean each
    label with your `clean_position_v2`, and count how often each clean
    position occurs in a dictionary `position_counts`, e.g.
    `{"Defender": 3, "Midfielder": 4, ...}`.
    """)
    return


@app.cell
def _(clean_position_v2, raw_positions):
    # TODO: start with an empty dict and count the clean labels
    position_counts = ...
    return (position_counts,)


@app.cell
def _(check_exercise, position_counts):
    def _check():
        assert position_counts is not ..., "Replace `...` with a counting loop."
        expected = {"Defender": 3, "Midfielder": 4, "Goalkeeper": 2, "Forward": 5}
        assert position_counts == expected, f"Expected {expected}, got {position_counts}."

    check_exercise(_check, "14 messy labels, 4 clean positions.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 12 - how many weeks to reach the target?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    An athlete is at Yo-Yo level **15.5** and the target is level **18**.
    With the new training plan they improve by **0.4 levels per week**.
    Use a `while` loop to compute after how many weeks the target is
    reached (`weeks_to_target`), and the level at that moment
    (`level_reached`, rounded to 1 decimal).
    """)
    return


@app.cell
def _():
    start_level = 15.5
    target_level = 18
    weekly_gain = 0.4
    # TODO: while the level is below the target, add a week
    weeks_to_target = ...
    level_reached = ...
    return level_reached, weeks_to_target


@app.cell
def _(check_exercise, level_reached, weeks_to_target):
    def _check():
        assert weeks_to_target is not ... and level_reached is not ..., "Replace both `...`."
        assert weeks_to_target == 7, f"Expected 7 weeks, got {weeks_to_target}."
        assert level_reached == 18.3, f"Expected level 18.3, got {level_reached}."

    check_exercise(_check, "Target reached after 7 weeks.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 7. Challenge (16:50-17:20) - the club's real athlete file

    Time to use everything together on the real export `athletes.csv`.
    Reading a CSV file is a job for the `csv` module from Python's
    standard library: `csv.DictReader` turns every line of the file into
    a **dictionary**, with the column names as keys. Note that every
    value arrives as **text**.

    The loading code is provided - look at the first two rows it prints.
    """)
    return


@app.cell
def _(DATA_DIR):
    import csv
    from pathlib import Path
    from urllib.request import urlopen

    # Path only understands local files; in the browser DATA_DIR is a URL.
    if DATA_DIR.startswith("http"):
        athletes_text = urlopen(f"{DATA_DIR}/athletes.csv").read().decode("utf-8")
    else:
        athletes_text = Path(DATA_DIR, "athletes.csv").read_text()
    athlete_lines = athletes_text.splitlines()
    athlete_rows = list(csv.DictReader(athlete_lines))

    print(len(athlete_rows), "athletes")
    print(athlete_rows[0])
    print(athlete_rows[1])
    return (athlete_rows,)


@app.cell
def _(mo):
    mo.md(r"""
    Build two dictionaries, keyed on the **clean** position (use
    `clean_position_v2`):

    - `squad_counts`: the number of athletes per position,
    - `average_height_by_position`: the average `height_cm` per position,
      rounded to 1 decimal.

    Watch out: a few athletes have an **empty** `height_cm` (an empty
    string). Skip those when computing the averages - but still count
    them in `squad_counts`.

    Hint: loop once over `athlete_rows` and keep three dicts up to date
    (counts, sum of heights, number of heights), then compute the
    averages in a second loop over the positions.
    """)
    return


@app.cell
def _(athlete_rows, clean_position_v2):
    # TODO: fill both dictionaries by looping over athlete_rows
    squad_counts = ...
    average_height_by_position = ...
    return average_height_by_position, squad_counts


@app.cell
def _(athlete_rows, average_height_by_position, check_exercise, squad_counts):
    def _check():
        assert squad_counts is not ..., "Replace `...` for `squad_counts`."
        assert average_height_by_position is not ..., "Replace `...` for `average_height_by_position`."
        position_map = {
            "forward": "Forward", "fwd": "Forward", "midfielder": "Midfielder", "mid": "Midfielder",
            "defender": "Defender", "def": "Defender", "goalkeeper": "Goalkeeper", "gk": "Goalkeeper",
        }
        expected_counts, heights = {}, {}
        for row in athlete_rows:
            position = position_map[row["position"].strip().lower()]
            expected_counts[position] = expected_counts.get(position, 0) + 1
            if row["height_cm"]:
                heights.setdefault(position, []).append(float(row["height_cm"]))
        expected_heights = {p: round(sum(h) / len(h), 1) for p, h in heights.items()}

        assert squad_counts == expected_counts, f"Expected {expected_counts}, got {squad_counts}."
        assert average_height_by_position == expected_heights, (
            f"Expected {expected_heights}, got {average_height_by_position}. "
            "Did you skip the empty heights and round to 1 decimal?"
        )

    check_exercise(
        _check,
        "You just cleaned and summarised a real export with nothing but core Python. "
        "Next week, pandas will do all of this in a handful of lines.",
    )
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
        label="Which of today's topics (functions, strings, scope, collections, loops) "
        "feels solid, and which one needs more practice?",
        rows=4,
        full_width=True,
    )
    exit_ticket
    return (exit_ticket,)


@app.cell
def _(exit_ticket, mo):
    mo.md("Thanks - see you next week for Data Processing I.") if exit_ticket.value else mo.md(
        "Write a few words above before you leave."
    )
    return


if __name__ == "__main__":
    app.run()
