"""Antwoordcontroles voor labo 1 (Introductie Python I).

Wordt geladen door de labo- en oplossingsnotebooks. De controles staan hier,
buiten het notebook, zodat het notebook zelf de antwoorden niet verklapt.
"""

import marimo as mo

NOT_FILLED_IN = "Vervang eerst elke `...` door je eigen code."
WRONG_VALUE = "`{name}` heeft nog niet de verwachte waarde (je kreeg {value!r}). Lees de opgave opnieuw."
WRONG_RESULT = "`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r})."
RETURNS_NONE = "Je functie geeft None terug - gebruikte je `print` in plaats van `return`?"


def check_exercise(check_fn, success_message):
    """Voer `check_fn` uit; toon een groen kader bij succes, anders een uitleg."""
    try:
        check_fn()
    except AssertionError as e:
        message = str(e) or "Het resultaat is nog niet juist."
        return mo.callout(mo.md(f"**Nog niet juist.** {message}"), kind="warn")
    except Exception as e:
        return mo.callout(
            mo.md(f"**Fout bij het controleren van je antwoord:** {type(e).__name__}: {e}"),
            kind="danger",
        )
    return mo.callout(mo.md(f"**Juist!** {success_message}"), kind="success")


def welcome(new_member, welcome_message):
    def _check():
        assert new_member is not ... and welcome_message is not ..., NOT_FILLED_IN
        assert isinstance(new_member, str), "`new_member` moet de tekst bevatten die `input()` teruggeeft."
        assert welcome_message == f"Welkom bij de club, {new_member}!", (
            f"De boodschap {welcome_message!r} heeft niet precies de gevraagde vorm. "
            "Let op de komma, de spaties en het uitroepteken."
        )

    return check_exercise(_check, "Je eerste programma vraagt iets en antwoordt.")


def clean_name(raw_name, clean_name):
    def _check():
        assert raw_name is not ... and clean_name is not ..., NOT_FILLED_IN
        assert isinstance(raw_name, str), "`raw_name` moet de tekst bevatten die `input()` teruggeeft."
        assert clean_name == raw_name.strip().title(), (
            f"{clean_name!r} is nog niet helemaal opgekuist. "
            "Denk aan de spaties aan de uiteinden en aan de hoofdletters."
        )

    return check_exercise(
        _check,
        f"{raw_name!r} werd {clean_name!r}. Probeer ook een naam met extra spaties en rare hoofdletters.",
    )


def shirt_name(first_name, full_name, last_name, shirt_name):
    def _check():
        values = [full_name, first_name, last_name, shirt_name]
        assert all(value is not ... for value in values), NOT_FILLED_IN
        assert isinstance(full_name, str) and " " in full_name, (
            "Typ bij `input()` een naam met minstens één spatie, zoals `Yana De Backer`."
        )
        expected_first, expected_last = full_name.split(" ", 1)
        assert first_name == expected_first, WRONG_VALUE.format(name="first_name", value=first_name)
        assert last_name == expected_last, (
            WRONG_VALUE.format(name="last_name", value=last_name)
            + " Knip je enkel bij de eerste spatie?"
        )
        assert shirt_name == expected_last.upper(), WRONG_VALUE.format(name="shirt_name", value=shirt_name)

    return check_exercise(_check, f"Op het shirt komt {shirt_name!r}.")


def sprint_speed(speed_kmh, sprint_time_s):
    def _check():
        assert sprint_time_s is not ... and speed_kmh is not ..., NOT_FILLED_IN
        assert isinstance(sprint_time_s, float), (
            f"`sprint_time_s` is een {type(sprint_time_s).__name__}. "
            "`input()` geeft altijd tekst terug - zet die om naar het juiste getaltype."
        )
        exact = 30 / sprint_time_s * 3.6
        assert abs(speed_kmh - exact) <= 0.05 + 1e-9, (
            WRONG_VALUE.format(name="speed_kmh", value=speed_kmh) + " Controleer de formule en de eenheden."
        )
        assert speed_kmh == round(speed_kmh, 1), "Rond `speed_kmh` af op 1 decimaal."

    return check_exercise(_check, f"{sprint_time_s} s op de 30 m is {speed_kmh} km/u.")


def season_sessions(season_sessions, sessions_this_week):
    def _check():
        assert sessions_this_week is not ..., NOT_FILLED_IN
        assert isinstance(sessions_this_week, int), (
            f"`sessions_this_week` is een {type(sessions_this_week).__name__}, geen geheel getal."
        )
        assert season_sessions == 12 + sessions_this_week, (
            WRONG_VALUE.format(name="season_sessions", value=season_sessions)
        )

    return check_exercise(_check, f"De teller staat nu op {season_sessions} trainingen.")


def yoyo_time(yoyo_duration_s, yoyo_minutes, yoyo_seconds):
    def _check():
        values = [yoyo_duration_s, yoyo_minutes, yoyo_seconds]
        assert all(value is not ... for value in values), NOT_FILLED_IN
        assert isinstance(yoyo_duration_s, int), (
            f"`yoyo_duration_s` is een {type(yoyo_duration_s).__name__}, geen geheel getal."
        )
        assert yoyo_minutes == yoyo_duration_s // 60, WRONG_VALUE.format(name="yoyo_minutes", value=yoyo_minutes)
        assert yoyo_seconds == yoyo_duration_s % 60, WRONG_VALUE.format(name="yoyo_seconds", value=yoyo_seconds)

    return check_exercise(_check, f"{yoyo_duration_s} s is {yoyo_minutes} min {yoyo_seconds} s.")


def bmi(bmi):
    def _check():
        result = bmi(66.2, 176.3)
        assert result is not ..., NOT_FILLED_IN
        assert result is not None, RETURNS_NONE
        for args, expected in [((66.2, 176.3), 21.3), ((65.5, 167.1), 23.5), ((80, 180), 24.7)]:
            assert bmi(*args) == expected, (
                WRONG_RESULT.format(call=f"bmi{args}", value=bmi(*args)) + " Controleer de formule en de afronding."
            )

    return check_exercise(_check, "Eén functie, herbruikbaar voor elke atleet van de club.")


def format_time(format_time):
    def _check():
        result = format_time(1385)
        assert result is not ..., NOT_FILLED_IN
        assert result is not None, RETURNS_NONE
        for total_s, expected in [(1385, "23:05"), (65, "1:05"), (600, "10:00"), (59, "0:59"), (0, "0:00")]:
            result = format_time(total_s)
            assert result == expected, WRONG_RESULT.format(call=f"format_time({total_s})", value=result)

    return check_exercise(_check, "Zo toont ook een stopwatch de tijd.")


def age_in_season(age_in_season):
    def _check():
        assert age_in_season(2010) == 16, (
            WRONG_RESULT.format(call="age_in_season(2010)", value=age_in_season(2010))
        )
        try:
            age_2030 = age_in_season(2010, season_year=2030)
        except TypeError:
            raise AssertionError("`age_in_season` heeft nog geen parameter `season_year`.")
        assert age_2030 == 20, (
            WRONG_RESULT.format(call="age_in_season(2010, season_year=2030)", value=age_2030)
        )

    return check_exercise(_check, "De functie hangt niet langer af van een verborgen globale variabele.")


def is_eligible_u16(is_eligible_u16):
    def _check():
        result = is_eligible_u16(2011, False)
        assert result is not ..., NOT_FILLED_IN
        assert isinstance(result, bool), f"Je functie moet True of False teruggeven, niet {result!r}."
        cases = [
            ((2011, False), True),
            ((2010, False), False),
            ((2011, True), False),
            ((2012, False), True),
            ((2012, False, 2028), False),
        ]
        for args, expected in cases:
            call = f"is_eligible_u16({', '.join(repr(a) for a in args)})"
            assert is_eligible_u16(*args) == expected, WRONG_RESULT.format(call=call, value=is_eligible_u16(*args))

    return check_exercise(_check, "Leeftijd en blessure, gecombineerd met `and` en `not`.")


def jump_category(jump_category):
    def _check():
        result = jump_category(28)
        assert result is not ..., NOT_FILLED_IN
        assert result is not None, RETURNS_NONE
        cases = [
            (20, "onder gemiddeld"), (24.9, "onder gemiddeld"), (25, "gemiddeld"),
            (31.9, "gemiddeld"), (32, "boven gemiddeld"), (40, "boven gemiddeld"),
        ]
        for jump, expected in cases:
            result = jump_category(jump)
            assert result == expected, (
                WRONG_RESULT.format(call=f"jump_category({jump})", value=result) + " Controleer je grenzen."
            )

    return check_exercise(_check, "Elke tak van je `if` / `elif` / `else` doet wat hij moet doen.")


def hr_zone(hr_zone):
    def _check():
        result = hr_zone(150)
        assert result is not ..., NOT_FILLED_IN
        assert result is not None, RETURNS_NONE
        cases = [
            ((100,), 1), ((130,), 2), ((150,), 3), ((165,), 4), ((190,), 5),
            ((119, 200), 1), ((120, 200), 2), ((140, 200), 3),
            ((160, 200), 4), ((179, 200), 4), ((180, 200), 5),
        ]
        for args, expected in cases:
            call = f"hr_zone({', '.join(str(a) for a in args)})"
            assert hr_zone(*args) == expected, WRONG_RESULT.format(call=call, value=hr_zone(*args))

    return check_exercise(_check, "Je functie kan met elke zone om, en de standaardwaarde van `hr_max` werkt.")


def team_line(team_line):
    def _check():
        result = team_line("GK")
        assert result is not ..., NOT_FILLED_IN
        assert result is not None, RETURNS_NONE
        cases = {
            "GK": "verdediging", " def ": "verdediging", "mid": "middenveld",
            "MID": "middenveld", "FWD": "aanval", "fwd ": "aanval", "coach": "onbekend",
        }
        for code, expected in cases.items():
            result = team_line(code)
            assert result == expected, WRONG_RESULT.format(call=f"team_line({code!r})", value=result)

    return check_exercise(_check, "Eén `match`, vijf mogelijke uitkomsten.")


def training(to_hours, training_group):
    def _check():
        result = to_hours("17:45")
        assert result is not ..., NOT_FILLED_IN
        for text, expected in [("17:45", 17.75), ("9:30", 9.5), ("16:00", 16.0), ("20:15", 20.25)]:
            result = to_hours(text)
            assert result == expected, WRONG_RESULT.format(call=f"to_hours({text!r})", value=result)
        assert training_group("18:00") is not ..., NOT_FILLED_IN
        cases = {
            "16:00": "U12", "17:29": "U12", "17:30": "U14", "18:59": "U14", "19:00": "U16",
            "20:29": "U16", "20:30": "geen training", "15:59": "geen training", "8:00": "geen training",
        }
        for text, expected in cases.items():
            result = training_group(text)
            assert result == expected, (
                WRONG_RESULT.format(call=f"training_group({text!r})", value=result) + " Controleer je grenzen."
            )

    return check_exercise(
        _check,
        "Tekst opknippen, omzetten naar getallen, een functie die een andere functie gebruikt, "
        "en beslissingen - alles van vandaag in één programma.",
    )
