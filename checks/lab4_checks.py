"""Answer checks for lab 4 (Dataverwerking II).

Loaded by the lab and solutions notebooks. The checks live here, outside
the notebook, so that the notebook itself does not give the answers away.
"""

import marimo as mo

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


def mini_clean(mini_clean):
    def _check():
        assert len(mini_clean) == 5, "`mini_clean` does not have the expected number of rows."
        assert set(mini_clean["position"]) == {"FORWARD", "MIDFIELDER"}, (
            "The `position` column does not hold the expected labels."
        )
        assert mini_clean["weight_kg"].dtype.kind == "f", "The `weight_kg` column is not numeric yet."

    return check_exercise(_check, "The mini cleaning pipeline runs correctly now.")


def gender_age_summary(athletes_with_age_group, gender_age_summary):
    def _check():
        assert gender_age_summary is not ..., NOT_FILLED_IN
        expected = athletes_with_age_group.groupby(
            ["gender", "age_group"], observed=True
        ).agg(
            mean_height_cm=("height_cm", "mean"), mean_weight_kg=("weight_kg", "mean")
        )
        assert set(gender_age_summary.columns) >= {"mean_height_cm", "mean_weight_kg"}, (
            "The summary does not have the column names asked for in the exercise."
        )
        assert len(gender_age_summary) == len(expected), (
            f"Your summary has {len(gender_age_summary)} groups, which is not the expected number. "
            "Check what you group by."
        )

    return check_exercise(_check, "Your group summary has the right shape and columns.")


def rows_lost_to_dedup(combined, merged_inner, rows_lost_to_dedup):
    def _check():
        assert rows_lost_to_dedup is not ..., NOT_FILLED_IN
        dropped_ids = set(merged_inner["athlete_id"]) - set(combined["athlete_id"])
        expected = merged_inner["athlete_id"].isin(dropped_ids).sum()
        assert rows_lost_to_dedup == expected, (
            f"{rows_lost_to_dedup} is not the number of rows that were lost."
        )

    return check_exercise(
        _check,
        "That's how many test records would have silently vanished from "
        "view if you had not deliberately checked.",
    )


def cmj_progress(cmj_progress_1_to_2, cmj_wide, combined):
    def _check():
        assert cmj_wide is not ... and cmj_progress_1_to_2 is not ..., NOT_FILLED_IN
        expected_wide = combined.pivot_table(
            index="athlete_id", columns="test_moment", values="cmj_height_cm"
        )
        assert set(cmj_wide.columns) >= {1, 2}, (
            "`cmj_wide` should have one column per test moment."
        )
        expected_progress = expected_wide[2] - expected_wide[1]
        assert (cmj_progress_1_to_2.dropna().round(3) == expected_progress.dropna().round(3)).all(), (
            "`cmj_progress_1_to_2` is not right yet. Check which test moments you compare, and in which order."
        )

    return check_exercise(_check, "Your wide table and progress column are both correct.")


def zone_4_5_minutes(hr_zoned, zone_4_5_minutes):
    def _check():
        assert zone_4_5_minutes is not ..., NOT_FILLED_IN
        expected = (
            hr_zoned.loc[hr_zoned["hr_zone"].isin(["Zone 4", "Zone 5"])]
            .groupby("athlete_id")
            .size()
            / 60
        )
        assert set(zone_4_5_minutes.index) == set(expected.index), (
            "The result should have one value per athlete, with `athlete_id` as the index."
        )
        aligned = zone_4_5_minutes.reindex(expected.index)
        assert (aligned.round(2) == expected.round(2)).all(), (
            "The minutes are not right yet. Check which zones you keep, and the unit of the result."
        )

    return check_exercise(_check, "Time in zone 4-5 is computed correctly for every athlete.")


def training_report(hr_zoned, training_report):
    def _check():
        assert training_report is not ..., NOT_FILLED_IN
        for col in ["zone_4_5_minutes", "max_speed_kmh", "distance_km"]:
            assert col in training_report.columns, f"Missing column `{col}`."
        assert set(training_report.index) == set(hr_zoned["athlete_id"].unique()) or set(
            training_report.get("athlete_id", [])
        ) == set(hr_zoned["athlete_id"].unique()), (
            "The report should have exactly one row per athlete in `hr_zoned`."
        )
        assert (training_report["distance_km"] > 0).all(), "Distance should be positive for every athlete."
        assert (training_report["max_speed_kmh"] <= 30).all(), "Max speed looks unrealistically high."

    return check_exercise(_check, "Nice - that's a coach-ready training report.")
