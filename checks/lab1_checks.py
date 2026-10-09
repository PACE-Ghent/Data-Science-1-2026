"""Answer checks for lab 1 (Introductie Python I).

Loaded by the lab and solutions notebooks. The checks live here, outside
the notebook, so that the notebook itself does not give the answers away.
"""

import marimo as mo

NOT_FILLED_IN = "Replace every `...` with your own code first."
WRONG_VALUE = "`{name}` does not have the expected value yet (got {value!r}). Re-read the exercise."


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


def keeper_profile(keeper_birth_year, keeper_height_cm, keeper_name, keeper_weight_kg):
    def _check():
        values = {
            "keeper_name": (keeper_name, "Lotte Janssens"),
            "keeper_birth_year": (keeper_birth_year, 2010),
            "keeper_height_cm": (keeper_height_cm, 176.3),
            "keeper_weight_kg": (keeper_weight_kg, 66.2),
        }
        for name, (value, expected) in values.items():
            assert value is not ..., NOT_FILLED_IN
            assert value == expected, WRONG_VALUE.format(name=name, value=value)

    return check_exercise(_check, "Lotte's profile is stored in four well-named variables.")


def type_conversion(jersey_number, weight_from_text):
    def _check():
        assert weight_from_text is not ... and jersey_number is not ..., NOT_FILLED_IN
        assert isinstance(weight_from_text, float), (
            f"`weight_from_text` has the wrong data type: it is a {type(weight_from_text).__name__}."
        )
        assert isinstance(jersey_number, int), (
            f"`jersey_number` has the wrong data type: it is a {type(jersey_number).__name__}."
        )
        assert weight_from_text == 63.9 and jersey_number == 7, "The values changed during conversion."

    return check_exercise(_check, "Both values are now real numbers you can compute with.")


def season_sessions(season_sessions):
    def _check():
        assert season_sessions == 15, WRONG_VALUE.format(name="season_sessions", value=season_sessions)

    return check_exercise(_check, "Stan is at 15 sessions.")


def yoyo_time(yoyo_minutes, yoyo_seconds):
    def _check():
        assert yoyo_minutes is not ... and yoyo_seconds is not ..., NOT_FILLED_IN
        assert yoyo_minutes == 23, WRONG_VALUE.format(name="yoyo_minutes", value=yoyo_minutes)
        assert yoyo_seconds == 5, WRONG_VALUE.format(name="yoyo_seconds", value=yoyo_seconds)

    return check_exercise(_check, "1385 s is 23 min 5 s.")


def keeper_bmi(keeper_bmi):
    def _check():
        assert keeper_bmi is not ..., NOT_FILLED_IN
        assert abs(keeper_bmi - 66.2 / 1.763**2) < 0.01, (
            f"{keeper_bmi} is not Lotte's BMI. Check the units and the order of the operations."
        )

    return check_exercise(_check, "Lotte's BMI is about 21.3.")


def comparisons(is_explosive, is_fast):
    def _check():
        assert isinstance(is_fast, bool) and isinstance(is_explosive, bool), (
            "Both variables should hold a comparison result (True or False)."
        )
        assert is_fast is False, "`is_fast` is not right yet. Check the comparison operator."
        assert is_explosive is True, (
            "`is_explosive` is not right yet. Read the wording of the threshold carefully."
        )

    return check_exercise(_check, "Yana is explosive, but not (yet) fast.")


def eligible_u16(eligible_u16):
    def _check():
        assert isinstance(eligible_u16, bool), "`eligible_u16` should be True or False."
        assert eligible_u16 is False, "`eligible_u16` is not right yet. Re-read the eligibility rule."

    return check_exercise(_check, "Yana is too old for U16 this season.")


def jump_category(cmj_slider, jump_category):
    def _check():
        jump = cmj_slider.value
        expected = "below average" if jump < 25 else "average" if jump < 32 else "above average"
        assert jump_category is not ..., NOT_FILLED_IN
        assert jump_category == expected, (
            f"{jump_category!r} is not the right category for {jump} cm. Check your thresholds."
        )

    return check_exercise(_check, f"{cmj_slider.value} cm is {jump_category!r}. Try the other branches too!")


def hr_zone(heart_rate_slider, hr_max, hr_percent, hr_zone):
    def _check():
        assert hr_percent is not ..., NOT_FILLED_IN
        expected_percent = heart_rate_slider.value / hr_max * 100
        assert abs(hr_percent - expected_percent) < 1e-9, (
            f"`hr_percent` is not right yet (got {hr_percent})."
        )
        expected_zone = 1
        for limit in (60, 70, 80, 90):
            if expected_percent >= limit:
                expected_zone += 1
        assert hr_zone == expected_zone, (
            f"Zone {hr_zone!r} is not right for {expected_percent:.1f}% of HRmax. Check your thresholds."
        )

    return check_exercise(_check, f"{heart_rate_slider.value} bpm is zone {hr_zone}.")


def fix_name_error(greeting):
    def _check():
        assert greeting == "Welcome, Emma Verhoeven", f"Got {greeting!r}."

    return check_exercise(_check, "NameError fixed - it was a typo in the variable name.")


def fix_type_error(age_message):
    def _check():
        assert age_message == "Age: 16", f"Got {age_message!r}."

    return check_exercise(
        _check,
        "TypeError fixed - you can't add text and a number; convert with `str()` or use an f-string.",
    )


def fix_value_error(parsed_weight_kg):
    def _check():
        assert parsed_weight_kg == 61.1, f"Got {parsed_weight_kg!r}."

    return check_exercise(
        _check,
        "ValueError fixed. Next week you'll learn to do this automatically "
        "with the string method `.replace(\",\", \".\")`.",
    )


def fix_zero_division_error(average_session_min):
    def _check():
        assert average_session_min == 0, f"Got {average_session_min!r}."

    return check_exercise(_check, "ZeroDivisionError avoided with a simple `if`.")


def sprint_summary(best_sprint_s, sprint_spread_s):
    def _check():
        assert best_sprint_s is not ... and sprint_spread_s is not ..., NOT_FILLED_IN
        assert best_sprint_s == 5.29, WRONG_VALUE.format(name="best_sprint_s", value=best_sprint_s)
        assert sprint_spread_s == 0.12, (
            WRONG_VALUE.format(name="sprint_spread_s", value=sprint_spread_s) + " Mind the rounding."
        )

    return check_exercise(_check, "Best 5.29 s, with only 0.12 s between his best and worst run.")


def lane_8(cones_needed, lane_8_length_m, lane_8_radius_m):
    def _check():
        assert lane_8_radius_m is not ... and lane_8_length_m is not ..., NOT_FILLED_IN
        assert abs(lane_8_radius_m - 45.34) < 1e-6, (
            WRONG_VALUE.format(name="lane_8_radius_m", value=lane_8_radius_m)
        )
        assert abs(lane_8_length_m - 453.66) < 0.01, (
            WRONG_VALUE.format(name="lane_8_length_m", value=lane_8_length_m)
        )
        assert cones_needed == 91, (
            WRONG_VALUE.format(name="cones_needed", value=cones_needed) + " Mind the rounding direction."
        )

    return check_exercise(
        _check,
        "A lap in lane 8 is about 453.7 m - almost 54 m more than lane 1. "
        "That's why the start line is staggered!",
    )


def selection(
    candidate_birth_year,
    candidate_has_exemption,
    candidate_is_injured,
    candidate_name,
    candidate_sprint_30m_s,
    candidate_yoyo_level,
    selected,
    selection_message,
):
    def _check():
        expected = (
            (2026 - candidate_birth_year < 16 or candidate_has_exemption)
            and (candidate_sprint_30m_s < 5.5 or candidate_yoyo_level >= 17)
            and not candidate_is_injured
        )
        assert isinstance(selected, bool), "`selected` should be True or False."
        assert selected == expected, (
            f"`selected` is {selected}, but the coach's rules say otherwise for these inputs."
        )
        expected_message = f"{candidate_name} is {'' if expected else 'not '}selected."
        assert selection_message == expected_message, (
            f"The message {selection_message!r} does not have the requested wording."
        )

    return check_exercise(_check, "Your selection logic matches the coach's rules.")
