"""Answer checks for lab 3 (Dataverwerking I).

Loaded by the lab and solutions notebooks. The checks live here, outside
the notebook, so that the notebook itself does not give the answers away.
"""

import marimo as mo
import pandas as pd

NOT_FILLED_IN = "Replace every `...` with your own code first."


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


def tests_raw_shape(tests_raw, tests_raw_shape):
    def _check():
        assert tests_raw_shape is not ..., NOT_FILLED_IN
        assert tests_raw_shape == tests_raw.shape, (
            "That is not the number of rows and columns of `tests_raw`."
        )

    return check_exercise(
        _check,
        f"`tests.csv` has {tests_raw.shape[0]} rows and {tests_raw.shape[1]} columns.",
    )


def forwards_u16(athletes_raw, forwards_u16_raw, younger_than_16):
    def _check():
        assert forwards_u16_raw is not ..., NOT_FILLED_IN
        assert isinstance(forwards_u16_raw, pd.DataFrame), "`forwards_u16_raw` should be a dataframe."
        expected = athletes_raw.loc[
            (athletes_raw["position"] == "Forward") & younger_than_16
        ]
        assert (forwards_u16_raw["position"] == "Forward").all(), (
            "Some rows do not satisfy the position condition."
        )
        assert len(forwards_u16_raw) == len(expected), (
            f"Your filter keeps {len(forwards_u16_raw)} rows, which is not the expected number. "
            "Are both conditions applied?"
        )

    return check_exercise(_check, "That combination of filters is correct.")


def suspicious_30m(suspicious_30m_raw, tests_raw):
    def _check():
        assert suspicious_30m_raw is not ..., NOT_FILLED_IN
        assert isinstance(suspicious_30m_raw, pd.DataFrame), "`suspicious_30m_raw` should be a dataframe."
        expected = tests_raw.loc[tests_raw["sprint_30m_s"] > 20].sort_values(
            "sprint_30m_s", ascending=False
        )
        assert len(suspicious_30m_raw) == len(expected), (
            f"Your filter keeps {len(suspicious_30m_raw)} rows, which is not the expected number."
        )
        assert list(suspicious_30m_raw["sprint_30m_s"]) == list(expected["sprint_30m_s"]), (
            "The right rows, but not in the requested order."
        )

    return check_exercise(
        _check,
        "You just found every row with an implausible sprint time - "
        "all of them are the millisecond bug, not real speed.",
    )


def bmi_column(athletes_with_bmi, weight_kg_numeric):
    def _check():
        assert athletes_with_bmi["bmi"].iloc[0] is not Ellipsis, NOT_FILLED_IN
        assert not athletes_with_bmi["bmi"].isna().all(), "The `bmi` column should not be all-missing."
        expected_first = weight_kg_numeric.iloc[0] / (athletes_with_bmi["height_cm"].iloc[0] / 100) ** 2
        assert abs(athletes_with_bmi["bmi"].iloc[0] - expected_first) < 1e-6, (
            "The `bmi` values are not right yet. Check the units in your formula."
        )

    return check_exercise(_check, "Your BMI column is computed correctly.")


def age_column(REFERENCE_DATE, athletes_with_age):
    def _check():
        assert athletes_with_age["age"].iloc[0] is not Ellipsis, NOT_FILLED_IN
        expected = (REFERENCE_DATE - pd.to_datetime(athletes_with_age["birthdate"])).dt.days // 365
        assert athletes_with_age["age"].dropna().between(10, 19).all(), (
            "Some ages fall outside a plausible youth-club range (10-19)."
        )
        assert (athletes_with_age["age"].dropna() == expected.dropna()).all(), (
            "The ages are not right yet. They should be whole years on the reference date."
        )

    return check_exercise(_check, "Ages look correct and plausible.")


def clean_positions(athletes_step1):
    def _check():
        assert athletes_step1["position"].iloc[0] is not Ellipsis, NOT_FILLED_IN
        assert set(athletes_step1["position"].unique()) == {
            "Forward", "Midfielder", "Defender", "Goalkeeper",
        }, "The `position` column still contains labels that are not one of the clean positions."

    return check_exercise(_check, "Exactly the 4 real positions remain.")


def sprint_units(sprint_30m_fixed):
    def _check():
        assert sprint_30m_fixed is not ..., NOT_FILLED_IN
        assert sprint_30m_fixed.max() < 20, (
            f"The maximum value {sprint_30m_fixed.max()} still looks like milliseconds."
        )
        assert sprint_30m_fixed.min() > 3, "The minimum sprint time looks unrealistically low."

    return check_exercise(_check, "All 30 m sprint times are now in a realistic range (seconds).")


def deduplicate(athletes_deduped, athletes_step1):
    def _check():
        assert athletes_deduped is not ..., NOT_FILLED_IN
        assert not athletes_deduped.duplicated(subset=["name", "birthdate"]).any(), (
            "There is still a duplicated athlete in the result."
        )
        assert len(athletes_deduped) == len(athletes_step1) - 1, (
            f"The number of removed rows is not right: went from {len(athletes_step1)} "
            f"to {len(athletes_deduped)} rows."
        )

    return check_exercise(_check, "The duplicate athlete is gone.")


def fastest_per_position(athletes_clean, fastest_per_position, tests_clean):
    def _check():
        assert fastest_per_position is not ..., NOT_FILLED_IN
        assert "position" in fastest_per_position.columns and "sprint_30m_s" in fastest_per_position.columns, (
            "The result needs both a `position` and a `sprint_30m_s` column."
        )
        counts = fastest_per_position.groupby("position").size()
        assert (counts <= 5).all(), "Some positions have too many rows."
        best_sprint = tests_clean.groupby("athlete_id")["sprint_30m_s"].min().reset_index()
        expected = (
            athletes_clean.merge(best_sprint, on="athlete_id")
            .sort_values("sprint_30m_s")
            .groupby("position")
            .head(5)
        )
        assert set(fastest_per_position["athlete_id"]) == set(expected["athlete_id"]), (
            "These are not the athletes the coach is looking for. Re-read the steps of the exercise."
        )

    return check_exercise(_check, "That's the coach's shortlist - nicely done.")
