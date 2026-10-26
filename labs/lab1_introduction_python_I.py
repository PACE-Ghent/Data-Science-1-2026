import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Introduction to Python I - Variables, Types and Decisions

    Welcome! In this course you are the new data analyst for a
    (fictional) youth football / athletics club. Later on you will get
    the club's full export files - athlete profiles, physical test
    results and heart rate recordings - and turn them into tables,
    statistics and charts.

    Before we can do any of that, we need the building blocks of the
    language itself. Today we work with **one athlete at a time**: their
    height, their sprint time, their jump height. Next week we'll handle
    whole lists of athletes.

    **By the end of this session you can:** store values in variables,
    recognise Python's basic data types, compute with numbers, compare
    values and combine conditions, let your code make decisions with
    `if` / `elif` / `else`, read an error message without panicking, and
    use built-in functions and the `math` module.
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(demo_slider, mo):
    mo.md(f"{demo_slider.value} squared is **{demo_slider.value ** 2}**.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice that you didn't have to re-run anything by hand - moving the
    slider was enough.

    Three more things to know:

    - The **last expression** of a cell is shown above the cell. Anything
      you `print(...)` appears in the console output right below it.
    - **Two cells cannot define the same variable name.** If you get an
      error saying a variable "is defined by another cell", pick a
      different, more descriptive name. We'll come back to this in the
      section on overwriting variables.
    - Exercise cells contain a `...` placeholder or a `# TODO` comment.
      Replace it with your own code. The cell right below it checks your
      answer automatically and turns green when it's correct.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    import sys as _sys
    import types as _types

    # The answer checks live in a separate file (checks/ in the course
    # repository), so that this notebook does not give the answers away.
    _CHECKS_FILE = "lab1_checks.py"
    if _sys.platform == "emscripten":
        from urllib.request import urlopen as _urlopen

        _checks_source = _urlopen(
            f"https://raw.githubusercontent.com/PACE-Ghent/Data-Science-1-2026/main/checks/{_CHECKS_FILE}"
        ).read().decode("utf-8")
    else:
        _checks_source = (mo.notebook_dir() / ".." / "checks" / _CHECKS_FILE).read_text()
    checks = _types.ModuleType("checks")
    exec(_checks_source, checks.__dict__)
    return (checks,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Variables (13:15-13:40)

    A **variable** is a name that refers to a value. You create one with
    a single `=` sign: the name goes on the left, the value on the right.

    ```python
    height_cm = 167.1
    ```

    Read this as "*`height_cm` now refers to the value 167.1*", not as a
    mathematical equation.

    Naming rules and conventions:

    - Names may contain letters, digits and underscores, but may **not
      start with a digit** (`30m_sprint` is invalid, `sprint_30m` is fine).
    - Names are **case sensitive**: `Height` and `height` are two
      different variables.
    - Python convention is `snake_case`: lowercase words separated by
      underscores.
    - Choose **descriptive** names and include the unit when there is
      one: `sprint_30m_s` tells you much more than `s` or `x`.
    """)
    return


@app.cell
def _():
    name = "Yana De Backer"
    birth_year = 2010
    height_cm = 167.1
    weight_kg = 65.5
    sprint_30m_s = 5.34
    is_injured = False

    print(name)
    print("Height:", height_cm, "cm")
    return birth_year, height_cm, is_injured, name, sprint_30m_s, weight_kg


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 1 - store a goalkeeper's profile
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Lotte Janssens is one of the club's goalkeepers. She was born in
    **2010**, is **176.3 cm** tall and weighs **66.2 kg**. Store these
    values in the variables `keeper_name`, `keeper_birth_year`,
    `keeper_height_cm` and `keeper_weight_kg`.
    """)
    return


@app.cell
def _():
    # TODO: replace every ... with the correct value
    keeper_name = ...
    keeper_birth_year = ...
    keeper_height_cm = ...
    keeper_weight_kg = ...
    return keeper_birth_year, keeper_height_cm, keeper_name, keeper_weight_kg


@app.cell(hide_code=True)
def _(checks, keeper_birth_year, keeper_height_cm, keeper_name, keeper_weight_kg):
    checks.keeper_profile(
        keeper_birth_year,
        keeper_height_cm,
        keeper_name,
        keeper_weight_kg,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Data types (13:40-14:10)

    Every value in Python has a **type**. The four you'll use constantly:

    | Type | Example | Club example |
    |---|---|---|
    | `int` (integer) | `2010` | birth year, number of sessions, Yo-Yo level |
    | `float` (decimal number) | `5.34` | sprint time, height, weight |
    | `str` (string = text) | `"Yana De Backer"` | name, position |
    | `bool` (boolean) | `True` / `False` | is the athlete injured? |

    There is also `None`, Python's way to say "*no value*" - for
    example a test that was never taken.

    You never have to *declare* a type: Python **assigns the type
    automatically** based on the value. `2010` becomes an `int`, `2010.0`
    a `float` and `"2010"` a `str`. The built-in function `type()`
    tells you which type a value has.
    """)
    return


@app.cell
def _(birth_year, height_cm, is_injured, name):
    print(type(name))
    print(type(birth_year))
    print(type(height_cm))
    print(type(is_injured))
    print(type(None))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The type decides what you can do with a value. `2010 + 1` is `2011`,
    but `"2010" + "1"` glues the two texts together into `"20101"`.
    Data read from a file or a form usually arrives as **text**, so
    converting between types is something you'll do all the time:

    | Function | Converts to | Example |
    |---|---|---|
    | `int(...)` | integer | `int("16")` -> `16`, `int(5.9)` -> `5` (cuts off, doesn't round!) |
    | `float(...)` | decimal number | `float("63.9")` -> `63.9` |
    | `str(...)` | text | `str(2010)` -> `"2010"` |
    | `bool(...)` | boolean | `bool(0)` -> `False`, `bool(3)` -> `True` |

    Finally, an **f-string** lets you put variables inside a piece of
    text: put an `f` before the opening quote, and the variable between
    curly braces.
    """)
    return


@app.cell
def _(birth_year, name):
    print("2010" + "1")
    print(birth_year + 1)
    print(int("16") + 1)
    print(int(5.9))
    print(f"{name} was born in {birth_year}.")
    return


@app.cell
def _(mo):
    type_quiz = mo.ui.radio(
        options=["int", "float", "str", "bool"],
        label="What is the type of `30 / 5`? (Think first, then check with `type(30 / 5)` in a new cell.)",
    )
    type_quiz
    return (type_quiz,)


@app.cell
def _(mo, type_quiz):
    mo.callout(
        mo.md("Correct - the `/` operator always returns a `float`, even when the result is a whole number (`6.0`)."),
        kind="success",
    ) if type_quiz.value == "float" else mo.md(
        "Pick an option above." if type_quiz.value is None else "Not quite - try `type(30 / 5)` in a new cell."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 2 - convert text to numbers
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A registration form delivered the weight and the jersey number of a
    new player as text. Convert `weight_text` to a `float` and store it
    in `weight_from_text`, and convert `jersey_text` to an `int` stored
    in `jersey_number`.
    """)
    return


@app.cell
def _():
    weight_text = "63.9"
    jersey_text = "7"

    # TODO: convert both texts to the right number type
    weight_from_text = ...
    jersey_number = ...
    return jersey_number, weight_from_text


@app.cell(hide_code=True)
def _(checks, jersey_number, weight_from_text):
    checks.type_conversion(jersey_number, weight_from_text)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Overwriting variables (14:10-14:25)

    A variable can be given a new value at any time - the old value is
    simply forgotten:

    ```python
    yoyo_level = 16.5
    yoyo_level = 18.0      # after a good pre-season
    ```

    The right-hand side is evaluated **first**, so you can use the old
    value to compute the new one. `+=`, `-=`, `*=` and `/=` are shorthands
    for exactly that:

    ```python
    sessions = 12
    sessions = sessions + 1   # 13
    sessions += 1             # 14, same thing, shorter
    ```

    Because types are assigned automatically, overwriting can even change
    the type: `x = 5` followed by `x = "five"` is perfectly legal (but
    confusing - avoid it).

    **Watch out for built-in names.** Python has built-in functions such
    as `max`, `min`, `sum`, `type` and `print`. Writing `max = 190` (for
    a maximum heart rate) silently overwrites the function `max`, and a
    later `max(5.3, 5.1)` crashes. Use `hr_max = 190` instead.

    **marimo twist:** inside a single cell you can overwrite a variable
    as often as you like. Across cells you can't: each variable is
    defined by exactly one cell. That keeps the notebook predictable -
    marimo always knows which cell a value comes from.
    """)
    return


@app.cell
def _():
    yoyo_level = 16.5
    print("Start of season:", yoyo_level)
    yoyo_level = yoyo_level + 1.0
    print("After pre-season:", yoyo_level)
    yoyo_level += 0.5
    print("Mid-season:", yoyo_level)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 3 - update a session counter
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Stan has attended 12 training sessions so far. This week he attends 3
    more. Update `season_sessions` in the cell below using `+=` (don't
    just type `15`!).
    """)
    return


@app.cell
def _():
    season_sessions = 12
    # TODO: add this week's 3 sessions to season_sessions using +=
    return (season_sessions,)


@app.cell(hide_code=True)
def _(checks, season_sessions):
    checks.season_sessions(season_sessions)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Arithmetic operators (14:25-15:00)

    | Operator | Meaning | Example | Result |
    |---|---|---|---|
    | `+` | addition | `5.34 + 0.1` | `5.44` |
    | `-` | subtraction | `2026 - 2010` | `16` |
    | `*` | multiplication | `5.6 * 3.6` | `20.16` |
    | `/` | division (always a float) | `30 / 5` | `6.0` |
    | `//` | floor division (whole part) | `135 // 60` | `2` |
    | `%` | modulo (remainder) | `135 % 60` | `15` |
    | `**` | power | `1.67 ** 2` | `2.7889` |

    The usual order of operations applies: `**` first, then `*` `/` `//`
    `%`, then `+` `-`. Use **parentheses** whenever in doubt - they cost
    nothing and make your intent clear. `round(value, digits)` rounds a
    result for display.
    """)
    return


@app.cell
def _(sprint_30m_s):
    speed_ms = 30 / sprint_30m_s
    speed_kmh = speed_ms * 3.6
    print("Average speed:", round(speed_ms, 2), "m/s")
    print("Average speed:", round(speed_kmh, 1), "km/h")
    return


@app.cell
def _():
    session_duration_s = 135
    print(session_duration_s // 60, "min", session_duration_s % 60, "s")

    print(2 + 3 * 4)
    print((2 + 3) * 4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 4 - Yo-Yo test duration
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An athlete ran the Yo-Yo intermittent recovery test for 1385 seconds.
    Use `//` and `%` to split this into whole minutes (`yoyo_minutes`) and
    remaining seconds (`yoyo_seconds`).
    """)
    return


@app.cell
def _():
    yoyo_duration_s = 1385
    # TODO: use // and % on yoyo_duration_s
    yoyo_minutes = ...
    yoyo_seconds = ...
    return yoyo_minutes, yoyo_seconds


@app.cell(hide_code=True)
def _(checks, yoyo_minutes, yoyo_seconds):
    checks.yoyo_time(yoyo_minutes, yoyo_seconds)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 5 - Lotte's BMI
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Body Mass Index is weight in kg divided by the **square** of height in
    **metres**. Compute `keeper_bmi` from `keeper_weight_kg` and
    `keeper_height_cm` (Exercise 1). Mind the units and the parentheses!
    """)
    return


@app.cell
def _(keeper_height_cm, keeper_weight_kg):
    # TODO: BMI = weight_kg / (height in metres) ** 2
    keeper_bmi = ...
    return (keeper_bmi,)


@app.cell(hide_code=True)
def _(checks, keeper_bmi):
    checks.keeper_bmi(keeper_bmi)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ☕ Break (15:00-15:10)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Relational (comparison) operators (15:10-15:30)

    Comparison operators compare two values and always give a `bool`:

    | Operator | Meaning |
    |---|---|
    | `==` | equal to |
    | `!=` | not equal to |
    | `<` / `>` | smaller / greater than |
    | `<=` / `>=` | smaller / greater than or equal to |

    Don't mix up `=` (assign a value) and `==` (compare two values).

    Two pitfalls worth knowing now, because you'll meet both in the real
    club data later:

    - Text comparison is **exact**: `"Forward" == "forward "` is `False`
      (different capital letter, plus a trailing space).
    - Decimal numbers are stored approximately: `0.1 + 0.2 == 0.3` is
      `False`! Compare floats with a tolerance instead, e.g.
      `abs(a - b) < 1e-9`.
    """)
    return


@app.cell
def _(height_cm, sprint_30m_s):
    print(sprint_30m_s < 5.5)
    print(height_cm >= 170)
    print("Forward" == "forward ")
    print(0.1 + 0.2 == 0.3, 0.1 + 0.2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 6 - compare with the club norms
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The coach considers a 30 m sprint **under 5.0 s** "fast", and a
    countermovement jump (CMJ) of **at least 30 cm** "explosive". Using
    Yana's `sprint_30m_s` and the `cmj_height_cm` below, store the two
    comparisons in `is_fast` and `is_explosive`.
    """)
    return


@app.cell
def _(sprint_30m_s):
    cmj_height_cm = 30.0
    # TODO: two comparisons, each giving True or False
    is_fast = ...
    is_explosive = ...
    return is_explosive, is_fast


@app.cell(hide_code=True)
def _(checks, is_explosive, is_fast):
    checks.comparisons(is_explosive, is_fast)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Logical operators (15:30-15:50)

    Logical operators combine booleans:

    | Expression | True when... |
    |---|---|
    | `a and b` | both `a` and `b` are `True` |
    | `a or b` | at least one of them is `True` |
    | `not a` | `a` is `False` |

    Python also allows **chained comparisons**, which read like maths:
    `140 <= heart_rate <= 160` means "*heart rate between 140 and 160*".

    When you combine `and`, `or` and `not` in one expression, `not` is
    evaluated first, then `and`, then `or`. Once again: parentheses make
    it readable.
    """)
    return


@app.cell
def _(height_cm, is_injured, sprint_30m_s):
    heart_rate = 152
    print(sprint_30m_s < 5.5 and height_cm > 160)
    print(sprint_30m_s < 5.0 or height_cm > 160)
    print(not is_injured)
    print(140 <= heart_rate <= 160)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 7 - U16 eligibility
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An athlete may play in the U16 competition of the 2026 season if they
    turn **younger than 16** in 2026 (i.e. `2026 - birth_year < 16`)
    **and** they are **not injured**. Use Yana's `birth_year` and
    `is_injured` to store the result in `eligible_u16`.
    """)
    return


@app.cell
def _(birth_year, is_injured):
    # TODO: combine an age condition and an injury condition
    eligible_u16 = ...
    return (eligible_u16,)


@app.cell(hide_code=True)
def _(checks, eligible_u16):
    checks.eligible_u16(eligible_u16)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7. Control flow: `if` / `elif` / `else` (15:50-16:30)

    With conditions in hand, your code can make **decisions**:

    ```python
    if condition:
        # runs only when condition is True
    elif other_condition:
        # runs when condition was False and other_condition is True
    else:
        # runs when none of the above were True
    ```

    - The line with `if` / `elif` / `else` ends with a **colon** `:`.
    - The code that belongs to it is **indented** (4 spaces). Indentation
      is not decoration in Python - it defines which lines belong
      together.
    - Python checks the conditions **top to bottom** and runs only the
      **first** block whose condition is `True`. The order of your
      `elif`s therefore matters.

    Move the slider below and watch the message change.
    """)
    return


@app.cell
def _(mo):
    sprint_slider = mo.ui.slider(4.5, 6.5, step=0.05, value=5.34, label="30 m sprint (s)")
    sprint_slider
    return (sprint_slider,)


@app.cell
def _(sprint_slider):
    if sprint_slider.value < 5.0:
        sprint_feedback = "Excellent sprint!"
    elif sprint_slider.value < 5.5:
        sprint_feedback = "Good sprint."
    else:
        sprint_feedback = "Room for improvement."

    print(sprint_slider.value, "s ->", sprint_feedback)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 8 - classify a jump
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Classify the CMJ height from the slider below into `jump_category`:

    - below 25 cm -> `"below average"`
    - from 25 cm up to (not including) 32 cm -> `"average"`
    - 32 cm or more -> `"above average"`

    Move the slider around to test **every** branch - the check re-runs
    each time.
    """)
    return


@app.cell
def _(mo):
    cmj_slider = mo.ui.slider(15, 45, step=0.5, value=27.5, label="CMJ height (cm)")
    cmj_slider
    return (cmj_slider,)


@app.cell
def _(cmj_slider):
    # TODO: write an if / elif / else that sets jump_category
    # based on cmj_slider.value
    jump_category = ...
    return (jump_category,)


@app.cell(hide_code=True)
def _(checks, cmj_slider, jump_category):
    checks.jump_category(cmj_slider, jump_category)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 9 - heart rate zones
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A common way to express training intensity is the heart rate as a
    percentage of the athlete's maximal heart rate:
    `hr_percent = heart_rate / hr_max * 100`. Then:

    | `hr_percent` | Zone |
    |---|---|
    | below 60 | `1` |
    | 60 up to 70 | `2` |
    | 70 up to 80 | `3` |
    | 80 up to 90 | `4` |
    | 90 or higher | `5` |

    Compute `hr_percent` from the slider and `hr_max`, then set `hr_zone`
    to the right **integer**.
    """)
    return


@app.cell
def _(mo):
    heart_rate_slider = mo.ui.slider(80, 205, value=165, label="Heart rate (bpm)")
    heart_rate_slider
    return (heart_rate_slider,)


@app.cell
def _(heart_rate_slider):
    hr_max = 205
    # TODO: compute hr_percent, then set hr_zone with if / elif / else
    hr_percent = ...
    hr_zone = ...
    return hr_max, hr_percent, hr_zone


@app.cell(hide_code=True)
def _(checks, heart_rate_slider, hr_max, hr_percent, hr_zone):
    checks.hr_zone(heart_rate_slider, hr_max, hr_percent, hr_zone)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8. Learning to read errors (16:30-16:55)

    Errors are not a sign that you did something terrible - they are
    Python telling you, quite precisely, what went wrong. Professional
    programmers see dozens every day. The trick is to **read them from
    the bottom up**:

    ```
    Traceback (most recent call last):
      File "...", line 3, in <module>
        greeting = "Welcome, " + eror_name
                                 ^^^^^^^^^
    NameError: name 'eror_name' is not defined. Did you mean: 'error_name'?
    ```

    1. **Last line**: the error *type* (`NameError`) and a message.
       Often it even suggests a fix ("*Did you mean...*").
    2. **Lines above**: *where* it happened - the line number and the
       offending line, with `^^^` pointing at the culprit.

    The errors you'll meet most often:

    | Error | Typical cause |
    |---|---|
    | `SyntaxError` | Python can't even read the code: a missing `:`, quote or bracket |
    | `IndentationError` | indentation doesn't match the `if` / `else` it belongs to |
    | `NameError` | a variable name that doesn't exist (typo, or not defined yet) |
    | `TypeError` | an operation on the wrong type, e.g. `"Age: " + 16` |
    | `ValueError` | right type, impossible value, e.g. `float("61,1")` |
    | `ZeroDivisionError` | dividing by zero |

    **The four cells below are broken on purpose.** Run them, read the
    error, and fix each cell so that its check turns green.
    """)
    return


@app.cell
def _():
    error_name = "Emma Verhoeven"
    greeting = "Welcome, " + eror_name
    print(greeting)
    return (greeting,)


@app.cell(hide_code=True)
def _(checks, greeting):
    checks.fix_name_error(greeting)
    return


@app.cell
def _():
    athlete_age = 16
    age_message = "Age: " + athlete_age
    print(age_message)
    return (age_message,)


@app.cell(hide_code=True)
def _(age_message, checks):
    checks.fix_type_error(age_message)
    return


@app.cell
def _():
    # The form uses a comma as decimal separator, Python needs a dot.
    parsed_weight_kg = float("61,1")
    print(parsed_weight_kg)
    return (parsed_weight_kg,)


@app.cell(hide_code=True)
def _(checks, parsed_weight_kg):
    checks.fix_value_error(parsed_weight_kg)
    return


@app.cell
def _():
    # A new athlete has no sessions yet. Report 0 minutes on average
    # instead of crashing - use an if / else.
    total_training_min = 0
    n_sessions_attended = 0
    average_session_min = total_training_min / n_sessions_attended
    print(average_session_min)
    return (average_session_min,)


@app.cell(hide_code=True)
def _(average_session_min, checks):
    checks.fix_zero_division_error(average_session_min)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 9. Using functions and importing modules (16:55-17:20)

    You've already used a few **functions**: `print()`, `type()`,
    `int()`, `float()`, `round()`. A function is a named piece of code
    that you **call** with parentheses, passing it **arguments**, and
    that usually gives back (*returns*) a result. Some useful built-ins:

    | Function | Does | Example | Result |
    |---|---|---|---|
    | `len(x)` | length of a text (or list) | `len("Stan")` | `4` |
    | `round(x, n)` | round to `n` decimals | `round(5.3456, 2)` | `5.35` |
    | `abs(x)` | absolute value | `abs(-0.12)` | `0.12` |
    | `min(a, b, ...)` | smallest value | `min(5.34, 5.29)` | `5.29` |
    | `max(a, b, ...)` | largest value | `max(5.34, 5.29)` | `5.34` |

    Not sure what a function does? `help(round)` prints its
    documentation.

    Many more functions live in **modules** that you first need to
    **import**. The `math` module, for instance, has `math.pi`,
    `math.sqrt()`, `math.ceil()` (round up) and `math.floor()` (round
    down). Three ways to import:

    ```python
    import math                 # use as math.sqrt(16)
    from math import sqrt       # use as sqrt(16)
    import math as m            # use as m.sqrt(16) - handy for long names
    ```

    Imports go at the **top** of a notebook or script. Later in the
    course you'll import much bigger modules the same way:
    `import pandas as pd`.
    """)
    return


@app.cell
def _():
    import math

    return (math,)


@app.cell
def _(math, name):
    print(len(name))
    print(round(5.3456, 2))
    print(min(5.34, 5.29, 5.41), max(5.34, 5.29, 5.41))
    print(math.pi)
    print(math.sqrt(16))
    print(math.ceil(4.1), math.floor(4.9))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 10 - best sprint of the day
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Bram ran three 30 m sprints. Use built-in functions to store his best
    (fastest) time in `best_sprint_s`, and the difference between his
    slowest and fastest time, rounded to 2 decimals, in `sprint_spread_s`.
    """)
    return


@app.cell
def _():
    bram_sprint_1 = 5.41
    bram_sprint_2 = 5.29
    bram_sprint_3 = 5.36
    # TODO: use min(), max() and round()
    best_sprint_s = ...
    sprint_spread_s = ...
    return best_sprint_s, sprint_spread_s


@app.cell(hide_code=True)
def _(best_sprint_s, checks, sprint_spread_s):
    checks.sprint_summary(best_sprint_s, sprint_spread_s)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Exercise 11 - how long is lane 8?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A standard 400 m track has two straights of **84.39 m** and two
    half-circle bends. A lap in lane 1 is measured at a radius of
    **36.8 m**, and every next lane lies **1.22 m** further out. So one
    lap in lane `n` measures:

    $$2 \times 84.39 + 2 \pi r_n \qquad r_n = 36.8 + (n - 1) \times 1.22$$

    1. Compute `lane_8_radius_m` and `lane_8_length_m` using `math.pi`.
    2. The coach puts a cone every 5 m along lane 8. How many cones are
       needed to cover the whole lap? Use `math.ceil` to round up, and
       store the result in `cones_needed`.
    """)
    return


@app.cell
def _(math):
    # TODO: radius, lap length and number of cones for lane 8
    lane_8_radius_m = ...
    lane_8_length_m = ...
    cones_needed = ...
    return cones_needed, lane_8_length_m, lane_8_radius_m


@app.cell(hide_code=True)
def _(checks, cones_needed, lane_8_length_m, lane_8_radius_m):
    checks.lane_8(cones_needed, lane_8_length_m, lane_8_radius_m)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 10. Challenge (17:20-17:30) - who makes the U16 selection?

    The coach's selection rules for the U16 tournament:

    1. The athlete must turn **younger than 16** in 2026, **or** have a
       `has_exemption` from the federation.
    2. **And** they must be quick **or** fit: a 30 m sprint **under
       5.5 s**, **or** a Yo-Yo level of **at least 17**.
    3. **And** they must **not** be injured.

    Using the variables in the cell below, set `selected` to `True` or
    `False`. Then build a `selection_message` with an `if` / `else` and
    an f-string, for example `"Stan Mertens is selected."` or
    `"Stan Mertens is not selected."`.

    Once your check is green, change the values of the input variables
    (e.g. make Stan injured) and verify that your code still gives the
    right answer.
    """)
    return


@app.cell
def _():
    candidate_name = "Stan Mertens"
    candidate_birth_year = 2012
    candidate_has_exemption = False
    candidate_sprint_30m_s = 5.62
    candidate_yoyo_level = 17.5
    candidate_is_injured = False
    return (
        candidate_birth_year,
        candidate_has_exemption,
        candidate_is_injured,
        candidate_name,
        candidate_sprint_30m_s,
        candidate_yoyo_level,
    )


@app.cell
def _(
    candidate_birth_year,
    candidate_has_exemption,
    candidate_is_injured,
    candidate_name,
    candidate_sprint_30m_s,
    candidate_yoyo_level,
):
    # TODO: combine the three rules into one boolean, then build the message
    selected = ...
    selection_message = ...
    print(selection_message)
    return selected, selection_message


@app.cell(hide_code=True)
def _(
    candidate_birth_year,
    candidate_has_exemption,
    candidate_is_injured,
    candidate_name,
    candidate_sprint_30m_s,
    candidate_yoyo_level,
    checks,
    selected,
    selection_message,
):
    checks.selection(
        candidate_birth_year,
        candidate_has_exemption,
        candidate_is_injured,
        candidate_name,
        candidate_sprint_30m_s,
        candidate_yoyo_level,
        selected,
        selection_message,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exit ticket
    """)
    return


@app.cell
def _(mo):
    exit_ticket = mo.ui.text_area(
        label="What is one thing from today that clicked, and what is still unclear?",
        rows=4,
        full_width=True,
    )
    exit_ticket
    return (exit_ticket,)


@app.cell
def _(exit_ticket, mo):
    mo.md("Thanks - see you next week for Introduction to Python II.") if exit_ticket.value else mo.md(
        "Write a few words above before you leave."
    )
    return


if __name__ == "__main__":
    app.run()
