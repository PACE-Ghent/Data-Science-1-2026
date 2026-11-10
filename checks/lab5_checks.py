"""Answer checks for lab 5 (Datavisualisatie I).

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


def weight_histogram(weight_histogram):
    def _check():
        assert weight_histogram is not ..., NOT_FILLED_IN
        assert weight_histogram.data[0].type == "histogram", "That is not the chart type asked for."
        assert weight_histogram.layout.title.text, "The chart has no title yet."
        assert weight_histogram.layout.xaxis.title.text, "The x-axis has no label yet."

    return check_exercise(_check, "A properly labeled histogram.")


def yoyo_by_age(yoyo_by_age):
    def _check():
        assert yoyo_by_age is not ..., NOT_FILLED_IN
        assert yoyo_by_age.data[0].type == "box", "That is not the chart type asked for."
        facet_annotations = [a.text for a in yoyo_by_age.layout.annotations]
        assert any("F" in t or "M" in t for t in facet_annotations), (
            "The chart is not split into one panel per gender yet."
        )

    return check_exercise(_check, "Faceting by gender works.")


def speed_line(speed_line):
    def _check():
        assert speed_line is not ..., NOT_FILLED_IN
        assert "lines" in speed_line.data[0].mode, "That is not the chart type asked for."
        assert speed_line.layout.title.text, "The chart has no title yet."

    return check_exercise(_check, "A proper speed-over-time line chart.")


def dashboard(dashboard_charts, dashboard_selector):
    def _check():
        assert dashboard_selector is not ... and dashboard_charts is not ..., NOT_FILLED_IN
        assert hasattr(dashboard_selector, "value"), "`dashboard_selector` should be a marimo UI element."
        assert len(dashboard_charts) == 3, (
            f"`dashboard_charts` holds {len(dashboard_charts)} charts, which is not the number asked for."
        )
        for fig in dashboard_charts:
            assert hasattr(fig, "data"), "Every item in `dashboard_charts` should be a plotly figure."

    return check_exercise(_check, "That's a coach-ready mini-dashboard.")
