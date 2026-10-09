"""Answer checks for lab 2 (Introductie Python II).

Loaded by the lab and solutions notebooks. The checks live here, outside
the notebook, so that the notebook itself does not give the answers away.
"""

import marimo as mo

NOT_FILLED_IN = "Replace every `...` with your own code first."
WRONG_VALUE = "`{name}` does not have the expected value yet (got {value!r}). Re-read the exercise."
WRONG_RESULT = "`{call}` does not return the expected result (got {value!r})."


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


def flying_20m(flying_20m_kmh, flying_20m_s):
    def _check():
        assert flying_20m_s is not ... and flying_20m_kmh is not ..., NOT_FILLED_IN
        assert flying_20m_s == 3.29, WRONG_VALUE.format(name="flying_20m_s", value=flying_20m_s)
        assert flying_20m_kmh == 21.9, (
            WRONG_VALUE.format(name="flying_20m_kmh", value=flying_20m_kmh) + " Mind the units."
        )

    return check_exercise(
        _check,
        "Now imagine doing this for 43 athletes, 3 test moments each... "
        "That's what functions and loops are for.",
    )


def bmi(bmi):
    def _check():
        assert bmi(65.5, 167.1) is not ..., NOT_FILLED_IN
        assert bmi(65.5, 167.1) is not None, "Your function returns None - did you `print` instead of `return`?"
        for args, expected in [((65.5, 167.1), 23.5), ((66.2, 176.3), 21.3)]:
            assert bmi(*args) == expected, (
                WRONG_RESULT.format(call=f"bmi{args}", value=bmi(*args)) + " Check the formula and the rounding."
            )

    return check_exercise(_check, "One function, reusable for every athlete in the club.")


def hr_zone(hr_zone):
    def _check():
        assert hr_zone(150) is not ..., NOT_FILLED_IN
        cases = [
            ((100,), 1), ((130,), 2), ((150,), 3), ((170,), 4), ((190,), 5),
            ((119,), 1), ((120,), 2), ((180,), 5),
            ((150, 180), 4), ((150, 250), 2),
        ]
        for args, expected in cases:
            call = f"hr_zone({', '.join(str(a) for a in args)})"
            assert hr_zone(*args) == expected, WRONG_RESULT.format(call=call, value=hr_zone(*args))

    return check_exercise(_check, "Your function handles every zone, and the default `hr_max` works.")


def parse_weight(parse_weight):
    def _check():
        assert parse_weight("65,5") is not ..., NOT_FILLED_IN
        for text, expected in [("65,5", 65.5), (" 59,6", 59.6), ("70", 70.0), ("61.1 ", 61.1)]:
            result = parse_weight(text)
            call = f"parse_weight({text!r})"
            assert isinstance(result, float), (
                f"`{call}` returns the wrong data type: a {type(result).__name__}."
            )
            assert result == expected, WRONG_RESULT.format(call=call, value=result)

    return check_exercise(_check, "Commas, dots and stray spaces are all handled.")


def clean_position(clean_position):
    def _check():
        assert clean_position("Forward") is not ..., NOT_FILLED_IN
        cases = {
            "Forward": "Forward", "forward ": "Forward", "FWD": "Forward",
            "midfielder": "Midfielder", "MID": "Midfielder",
            "defender ": "Defender", "DEF": "Defender",
            "goalkeeper": "Goalkeeper", "GK": "Goalkeeper",
            "coach": "Unknown",
        }
        for raw, expected in cases.items():
            assert clean_position(raw) == expected, (
                WRONG_RESULT.format(call=f"clean_position({raw!r})", value=clean_position(raw))
            )

    return check_exercise(_check, "Every messy label maps to a clean one.")


def birth_year_from_date(birth_year_from_date):
    def _check():
        assert birth_year_from_date("2010-05-27") is not ..., NOT_FILLED_IN
        for date, expected in [("2010-05-27", 2010), ("2014-02-07", 2014)]:
            result = birth_year_from_date(date)
            assert result == expected, (
                WRONG_RESULT.format(call=f"birth_year_from_date({date!r})", value=result)
                + " Check the data type too."
            )

    return check_exercise(_check, "Years extracted and converted.")


def age_in_season(age_in_season):
    def _check():
        assert age_in_season(2010) == 16, (
            WRONG_RESULT.format(call="age_in_season(2010)", value=age_in_season(2010))
        )
        try:
            age_2030 = age_in_season(2010, season_year=2030)
        except TypeError:
            raise AssertionError("`age_in_season` has no `season_year` parameter yet.")
        assert age_2030 == 20, (
            WRONG_RESULT.format(call="age_in_season(2010, season_year=2030)", value=age_2030)
        )

    return check_exercise(_check, "The function no longer depends on a hidden global.")


def emma_tests(emma_average_s, emma_best_s, emma_last_two, emma_n_tests):
    def _check():
        values = {
            "emma_n_tests": (emma_n_tests, 5),
            "emma_best_s": (emma_best_s, 5.39),
            "emma_average_s": (emma_average_s, 5.51),
            "emma_last_two": (emma_last_two, [5.51, 5.39]),
        }
        for name, (value, _) in values.items():
            assert value is not ..., NOT_FILLED_IN
        for name, (value, expected) in values.items():
            assert value == expected, WRONG_VALUE.format(name=name, value=value)

    return check_exercise(_check, "Emma is getting faster - her last test was her best.")


def clean_position_v2(clean_position_v2):
    def _check():
        assert clean_position_v2("FWD") is not ..., NOT_FILLED_IN
        cases = {
            "forward ": "Forward", "MID": "Midfielder", "defender ": "Defender",
            "DEF": "Defender", "Goalkeeper": "Goalkeeper", "GK": "Goalkeeper", "coach": "Unknown",
        }
        for raw, expected in cases.items():
            assert clean_position_v2(raw) == expected, (
                WRONG_RESULT.format(call=f"clean_position_v2({raw!r})", value=clean_position_v2(raw))
            )

    return check_exercise(_check, "Same result as Exercise 5, in far fewer lines.")


def test_day(n_under_5_5, test_day_kmh, test_day_s):
    def _check():
        assert n_under_5_5 is not ... and test_day_kmh is not ..., NOT_FILLED_IN
        assert n_under_5_5 == 4, WRONG_VALUE.format(name="n_under_5_5", value=n_under_5_5)
        expected = [round(30 / t * 3.6, 1) for t in test_day_s]
        assert isinstance(test_day_kmh, list), "`test_day_kmh` should be a list."
        assert test_day_kmh == expected, (
            "`test_day_kmh` does not hold the expected speeds yet. Check the conversion and the rounding."
        )

    return check_exercise(_check, "Half of today's group ran under 5.5 s.")


def position_counts(position_counts):
    def _check():
        assert position_counts is not ..., NOT_FILLED_IN
        expected = {"Defender": 3, "Midfielder": 4, "Goalkeeper": 2, "Forward": 5}
        assert isinstance(position_counts, dict), "`position_counts` should be a dictionary."
        assert position_counts == expected, (
            f"The counts are not right yet (got {position_counts}). "
            "Are the keys the clean position names?"
        )

    return check_exercise(_check, "14 messy labels, 4 clean positions.")


def weeks_to_target(level_reached, weeks_to_target):
    def _check():
        assert weeks_to_target is not ... and level_reached is not ..., NOT_FILLED_IN
        assert weeks_to_target == 7, WRONG_VALUE.format(name="weeks_to_target", value=weeks_to_target)
        assert level_reached == 18.3, WRONG_VALUE.format(name="level_reached", value=level_reached)

    return check_exercise(_check, "Target reached after 7 weeks.")


def squad_summary(athlete_rows, average_height_by_position, squad_counts):
    def _check():
        assert squad_counts is not ... and average_height_by_position is not ..., NOT_FILLED_IN
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

        assert squad_counts == expected_counts, (
            f"`squad_counts` is not right yet (got {squad_counts}). "
            "Are the keys the clean position names?"
        )
        assert average_height_by_position == expected_heights, (
            f"`average_height_by_position` is not right yet (got {average_height_by_position}). "
            "Think about missing values and the rounding."
        )

    return check_exercise(
        _check,
        "You just cleaned and summarised a real export with nothing but core Python. "
        "Next week, pandas will do all of this in a handful of lines.",
    )
