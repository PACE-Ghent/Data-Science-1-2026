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
    import plotly.express as px

    return pd, px


@app.cell
def _(mo):
    mo.md(r"""
    # Data Visualization I - Tell the Story with Plotly

    Two sessions ago you turned messy exports into a tidy table. Last
    session you combined and reshaped that table. Today you turn it into
    pictures a coach can actually use: the right chart for the right
    question, built with `plotly.express`, and made interactive with
    marimo's UI elements.

    **By the end of this session you can:** choose a chart type for a
    given question, build the standard plotly express charts, add extra
    dimensions with color/facet/size, and wire up simple interactivity.
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
    ## Setup: reload the cleaned data

    Same cleaning pipeline as the previous two sessions, compressed into
    one cell. `combined` is one row per (athlete, test moment); `hr_zoned`
    is the per-second training session with a heart-rate zone already
    attached.
    """)
    return


@app.cell
def _(DATA_DIR, pd):
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

    athletes = pd.read_csv(f"{DATA_DIR}/athletes.csv").assign(
        position=lambda d: clean_positions(d["position"]),
        weight_kg=lambda d: d["weight_kg"].str.replace(",", ".").astype(float),
        age=lambda d: (REFERENCE_DATE - pd.to_datetime(d["birthdate"])).dt.days // 365,
    ).drop_duplicates(subset=["name", "birthdate"], keep="first")

    tests = pd.read_csv(f"{DATA_DIR}/tests.csv").assign(
        sprint_10m_s=lambda d: fix_sprint_units(d["sprint_10m_s"]),
        sprint_30m_s=lambda d: fix_sprint_units(d["sprint_30m_s"]),
    )

    combined = athletes.merge(tests, on="athlete_id", how="inner")

    hr_session = pd.read_csv(f"{DATA_DIR}/hr_session.csv")
    hr_session["timestamp"] = pd.to_datetime(hr_session["date"]) + pd.to_timedelta(
        hr_session["time_s"], unit="s"
    )
    hr_with_age = hr_session.merge(athletes[["athlete_id", "age", "name"]], on="athlete_id", how="left")
    hr_with_age["hr_max"] = 220 - hr_with_age["age"]
    hr_with_age["pct_hr_max"] = 100 * hr_with_age["heart_rate_bpm"] / hr_with_age["hr_max"]
    hr_zoned = hr_with_age.assign(
        hr_zone=lambda d: pd.cut(
            d["pct_hr_max"], bins=[0, 60, 70, 80, 90, 1000],
            labels=["Zone 1", "Zone 2", "Zone 3", "Zone 4", "Zone 5"],
        )
    )
    combined.shape, hr_zoned.shape
    return athletes, combined, hr_zoned


@app.cell
def _(mo):
    mo.md(r"""
    ## Chart colors

    We fix one color per position up front and reuse it in every chart
    below, instead of letting each chart pick its own colors. That way,
    "Forward" is always the same color across the whole dashboard -
    readers only have to learn the legend once.
    """)
    return


@app.cell
def _():
    POSITION_COLORS = {
        "Forward": "#2a78d6",
        "Midfielder": "#eb6834",
        "Defender": "#1baf7a",
        "Goalkeeper": "#eda100",
    }
    ZONE_COLORS = {
        "Zone 1": "#cde2fb",
        "Zone 2": "#86b6ef",
        "Zone 3": "#3987e5",
        "Zone 4": "#1c5cab",
        "Zone 5": "#0d366b",
    }
    return POSITION_COLORS, ZONE_COLORS


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Principles: the right chart for the right question (13:00-13:30)

    | Question type | Example | Good chart |
    |---|---|---|
    | Distribution | How are sprint times spread out? | histogram, box |
    | Comparison | Which position jumps highest, on average? | bar, box |
    | Relationship | Does a faster sprint mean a higher jump? | scatter |
    | Evolution over time | Is this athlete's heart rate climbing? | line |

    A chart type is a claim about which of these questions matters most -
    picking the wrong one, or drawing it carelessly, can mislead just as
    easily as it can inform.
    """)
    return


@app.cell
def _(POSITION_COLORS, combined, px):
    good_chart = px.bar(
        combined.groupby("position", as_index=False)["sprint_30m_s"].mean(),
        x="position",
        y="sprint_30m_s",
        color="position",
        color_discrete_map=POSITION_COLORS,
        title="Average 30 m sprint time by position",
        labels={"sprint_30m_s": "Average sprint time (s)", "position": "Position"},
    )
    good_chart.update_yaxes(rangemode="tozero")
    good_chart
    return


@app.cell
def _(mo):
    mo.md("""
    The bars start at zero, so their *heights* honestly represent the differences between positions.
    """)
    return


@app.cell
def _(POSITION_COLORS, combined, px):
    sprint_means_by_position = combined.groupby("position", as_index=False)["sprint_30m_s"].mean()
    misleading_chart = px.bar(
        sprint_means_by_position,
        x="position",
        y="sprint_30m_s",
        color="position",
        color_discrete_map=POSITION_COLORS,
        title="MISLEADING (on purpose) - average 30 m sprint time by position",
        labels={"sprint_30m_s": "Average sprint time (s)", "position": "Position"},
    )
    misleading_chart.update_yaxes(
        range=[sprint_means_by_position["sprint_30m_s"].min() - 0.05, sprint_means_by_position["sprint_30m_s"].max() + 0.05]
    )
    misleading_chart
    return


@app.cell
def _(mo):
    mo.md("""
    The y-axis no longer starts at zero: the same small real differences now look enormous. This is one of the most common ways sports graphics mislead - a truncated or non-zero baseline.
    """)
    return


@app.cell
def _(mo):
    chart_critique = mo.ui.multiselect(
        options=[
            "The y-axis does not start at 0",
            "The colors are randomly assigned",
            "The chart type (bar) is wrong for this question",
            "The title does not match the data",
        ],
        label="What, specifically, makes the second chart misleading? (select all that apply)",
    )
    chart_critique
    return (chart_critique,)


@app.cell
def _(chart_critique, mo):
    mo.callout(mo.md("Correct."), kind="success") if chart_critique.value == [
        "The y-axis does not start at 0"
    ] else mo.md("Select the option(s) you think apply.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Basic plotly express charts (13:30-14:30)

    Every `plotly.express` function follows the same shape:
    `px.<chart_type>(dataframe, x=..., y=..., color=..., title=...,
    labels={...}, hover_data=[...])`. Long-format data (one row per
    observation, as we built in Data Processing II) is exactly what
    these functions expect - no reshaping needed at chart time.
    """)
    return


@app.cell
def _(athletes, px):
    height_histogram = px.histogram(
        athletes,
        x="height_cm",
        nbins=15,
        title="Distribution of athlete height",
        labels={"height_cm": "Height (cm)"},
    )
    height_histogram
    return


@app.cell
def _(POSITION_COLORS, combined, px):
    sprint_box = px.box(
        combined,
        x="position",
        y="sprint_30m_s",
        color="position",
        color_discrete_map=POSITION_COLORS,
        title="30 m sprint time by position",
        labels={"sprint_30m_s": "Sprint time (s)", "position": "Position"},
        hover_data=["name"],
    )
    sprint_box
    return


@app.cell
def _(POSITION_COLORS, combined, px):
    sprint_vs_jump = px.scatter(
        combined,
        x="sprint_30m_s",
        y="cmj_height_cm",
        color="position",
        color_discrete_map=POSITION_COLORS,
        title="Sprint time vs. jump height",
        labels={"sprint_30m_s": "30 m sprint time (s)", "cmj_height_cm": "Jump height (cm)"},
        hover_data=["name", "test_moment"],
    )
    sprint_vs_jump
    return


@app.cell
def _(mo):
    mo.md("""
    A line chart needs something to walk along the x-axis - here, `test_moment`. Because `combined` is already long (one row per athlete per test moment), we can plot every athlete's progress directly, no pivoting required.
    """)
    return


@app.cell
def _(combined, px):
    progress_line = px.line(
        combined.sort_values("test_moment"),
        x="test_moment",
        y="sprint_30m_s",
        color="athlete_id",
        title="30 m sprint time across the season, per athlete",
        labels={"sprint_30m_s": "Sprint time (s)", "test_moment": "Test moment"},
    )
    progress_line.update_layout(showlegend=False)
    progress_line
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 1 - a histogram of your own
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Build `weight_histogram`: a `px.histogram` of `athletes["weight_kg"]`, with a `title` and an `x` label set through `labels=`.
    """)
    return


@app.cell
def _():
    # TODO: px.histogram of weight_kg, with a title and an x-axis label
    weight_histogram = ...
    return (weight_histogram,)


@app.cell
def _(check_exercise, weight_histogram):
    def _check():
        assert weight_histogram is not ..., "Replace `...` with a px.histogram figure."
        assert weight_histogram.data[0].type == "histogram", "The chart should be a histogram."
        assert weight_histogram.layout.title.text, "Add a `title=` to the chart."
        assert weight_histogram.layout.xaxis.title.text, "Add an x-axis label via `labels=`."

    check_exercise(_check, "A properly labeled histogram.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. More dimensions: color, facet, size (14:30-15:15)

    `color` encodes a category as hue, `facet_col` splits one chart into
    a row of small charts, and `size` encodes a number as marker size -
    combine them and a single scatter plot can show four or five
    variables at once.
    """)
    return


@app.cell
def _(POSITION_COLORS, combined, px):
    faceted_scatter = px.scatter(
        combined,
        x="sprint_30m_s",
        y="cmj_height_cm",
        color="position",
        color_discrete_map=POSITION_COLORS,
        facet_col="gender",
        size="weight_kg",
        title="Sprint vs. jump height, by position and gender",
        labels={"sprint_30m_s": "30 m sprint time (s)", "cmj_height_cm": "Jump height (cm)"},
        hover_data=["name"],
    )
    faceted_scatter
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 2 - add a facet
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Build `yoyo_by_age`: a `px.box` of `yoyo_level` (y) by `position` (x, colored using `POSITION_COLORS`), **faceted** by `gender` using `facet_col`.
    """)
    return


@app.cell
def _():
    # TODO: px.box of yoyo_level by position, colored by position, facet_col="gender"
    yoyo_by_age = ...
    return (yoyo_by_age,)


@app.cell
def _(check_exercise, yoyo_by_age):
    def _check():
        assert yoyo_by_age is not ..., "Replace `...` with a px.box figure."
        assert yoyo_by_age.data[0].type == "box", "The chart should be a box plot."
        facet_annotations = [a.text for a in yoyo_by_age.layout.annotations]
        assert any("F" in t or "M" in t for t in facet_annotations), (
            "No facet columns found - did you pass facet_col='gender'?"
        )

    check_exercise(_check, "Faceting by gender works.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. Heart-rate time series with zone bands (15:30-16:15)

    `add_hrect` draws a horizontal band behind the data - perfect for
    showing heart-rate zones without adding a second y-axis (which we
    deliberately never do: two different y-scales on one chart is one
    of the most common ways to mislead).
    """)
    return


@app.cell
def _(ZONE_COLORS, hr_zoned, px):
    one_athlete_id = hr_zoned["athlete_id"].iloc[0]
    one_athlete_hr = hr_zoned.loc[hr_zoned["athlete_id"] == one_athlete_id].sort_values("timestamp")

    hr_max = one_athlete_hr["hr_max"].iloc[0]
    hr_line = px.line(
        one_athlete_hr,
        x="timestamp",
        y="heart_rate_bpm",
        title=f"Heart rate during training - {one_athlete_hr['name'].iloc[0]}",
        labels={"heart_rate_bpm": "Heart rate (bpm)", "timestamp": "Time"},
    )
    zone_edges_pct = [0, 60, 70, 80, 90, 100]
    zone_names = ["Zone 1", "Zone 2", "Zone 3", "Zone 4", "Zone 5"]
    for _lo_pct, _hi_pct, _zone in zip(zone_edges_pct[:-1], zone_edges_pct[1:], zone_names):
        hr_line.add_hrect(
            y0=_lo_pct / 100 * hr_max,
            y1=_hi_pct / 100 * hr_max,
            fillcolor=ZONE_COLORS[_zone],
            opacity=0.35,
            line_width=0,
            annotation_text=_zone,
            annotation_position="right",
        )
    hr_line
    return


@app.cell
def _(hr_zoned, px):
    all_athletes_hr = px.line(
        hr_zoned.sort_values("timestamp"),
        x="timestamp",
        y="heart_rate_bpm",
        color="name",
        title="Heart rate during training - all 5 athletes",
        labels={"heart_rate_bpm": "Heart rate (bpm)", "timestamp": "Time"},
    )
    all_athletes_hr
    return


@app.cell
def _(mo):
    mo.md("""
    ### Exercise 3 - speed over time
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Build `speed_line`: a `px.line` of `speed_kmh` over `timestamp` for `one_athlete_hr` (defined above), with a title and axis labels.
    """)
    return


@app.cell
def _():
    # TODO: px.line of speed_kmh over timestamp for one_athlete_hr
    speed_line = ...
    return (speed_line,)


@app.cell
def _(check_exercise, speed_line):
    def _check():
        assert speed_line is not ..., "Replace `...` with a px.line figure."
        assert "lines" in speed_line.data[0].mode, "The chart should be a line chart."
        assert speed_line.layout.title.text, "Add a `title=` to the chart."

    check_exercise(_check, "A proper speed-over-time line chart.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Interactivity in marimo (16:15-16:45)

    A `mo.ui.dropdown` (or slider) is just a variable whose `.value`
    changes when the viewer interacts with it - use `.value` inside a
    chart-building cell and the chart becomes reactive automatically.
    """)
    return


@app.cell
def _(hr_zoned, mo):
    athlete_picker = mo.ui.dropdown(
        options=sorted(hr_zoned["name"].unique()), value=sorted(hr_zoned["name"].unique())[0],
        label="Athlete",
    )
    time_window = mo.ui.range_slider(
        start=0, stop=int(hr_zoned["time_s"].max()), step=60, value=(0, int(hr_zoned["time_s"].max())),
        label="Time window (s)", show_value=True,
    )
    mo.hstack([athlete_picker, time_window])
    return athlete_picker, time_window


@app.cell
def _(athlete_picker, hr_zoned, px, time_window):
    selected_hr = hr_zoned.loc[
        (hr_zoned["name"] == athlete_picker.value)
        & hr_zoned["time_s"].between(*time_window.value)
    ].sort_values("timestamp")

    reactive_hr_chart = px.line(
        selected_hr,
        x="timestamp",
        y="heart_rate_bpm",
        title=f"Heart rate - {athlete_picker.value}",
        labels={"heart_rate_bpm": "Heart rate (bpm)", "timestamp": "Time"},
    )
    reactive_hr_chart
    return


@app.cell
def _(mo):
    mo.md("""
    Move the dropdown or the slider - the chart above redraws on its own. **Optional**: `mo.ui.plotly` goes one step further and makes *selections on the chart itself* reactive - lasso a few points in the scatter below, then look at the table underneath it.
    """)
    return


@app.cell
def _(POSITION_COLORS, combined, mo, px):
    selectable_scatter = mo.ui.plotly(
        px.scatter(
            combined,
            x="sprint_30m_s",
            y="cmj_height_cm",
            color="position",
            color_discrete_map=POSITION_COLORS,
            title="Select points with the box or lasso tool",
            hover_data=["name"],
        )
    )
    selectable_scatter
    return (selectable_scatter,)


@app.cell
def _(pd, selectable_scatter):
    pd.DataFrame(selectable_scatter.value)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 6. Mini-dashboard assignment (16:45-17:30)

    Build a small "coach dashboard": **3 charts** plus **1 interactive
    selector** that at least one of the charts responds to. Reuse
    anything from this notebook - the goal is composition, not new
    chart types. This can double as your submission for this module and
    sets up the case presentations and the Project Lab next semester.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    `dashboard_selector` below is provided for you - remember that reading a UI element's `.value` has to happen in a **different** cell from the one that creates it, which is exactly why it's split out here.
    """)
    return


@app.cell
def _(combined, mo):
    dashboard_selector = mo.ui.dropdown(
        options=sorted(combined["position"].unique()), value="Forward", label="Position",
    )
    dashboard_selector
    return (dashboard_selector,)


@app.cell
def _(mo):
    mo.md("""
    Build `dashboard_charts`: a list of exactly 3 plotly figures, where at least one uses `dashboard_selector.value`.
    """)
    return


@app.cell
def _():
    # TODO: build a list of exactly 3 plotly figures as `dashboard_charts`,
    # where at least one chart depends on `dashboard_selector.value`.
    dashboard_charts = ...
    return (dashboard_charts,)


@app.cell
def _(check_exercise, dashboard_charts, dashboard_selector):
    def _check():
        assert hasattr(dashboard_selector, "value"), "dashboard_selector should be an mo.ui element."
        assert dashboard_charts is not ..., "Replace `...` with a list of 3 figures."
        assert len(dashboard_charts) == 3, f"Expected exactly 3 charts, got {len(dashboard_charts)}."
        for fig in dashboard_charts:
            assert hasattr(fig, "data"), "Every item in dashboard_charts should be a plotly figure."

    check_exercise(_check, "That's a coach-ready mini-dashboard.")
    return


@app.cell
def _(mo):
    mo.md("""
    Congratulations - you've gone from a messy CSV export to an interactive dashboard in three sessions. See you at the case presentations.
    """)
    return


if __name__ == "__main__":
    app.run()
