"""Antwoordcontroles voor labo 2 (Introductie Python II).

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


def flying_20m(flying_20m_kmh):
    def _check():
        result = flying_20m_kmh(1.92, 5.21)
        assert result is not ..., NOT_FILLED_IN
        assert result is not None, RETURNS_NONE
        for args in [(1.92, 5.21), (1.85, 4.98), (2.05, 5.71)]:
            result = flying_20m_kmh(*args)
            exact = 20 / (args[1] - args[0]) * 3.6
            assert abs(result - exact) <= 0.05 + 1e-9 and result == round(result, 1), (
                WRONG_RESULT.format(call=f"flying_20m_kmh{args}", value=result)
                + " Controleer de formule, de eenheden en de afronding op 1 decimaal."
            )

    return check_exercise(
        _check,
        "Stel je nu voor dat je dit moet doen voor 43 atleten, met elk 3 testmomenten... "
        "Daarvoor dienen lussen.",
    )


def weeks_to_target(weeks_to_target):
    def _check():
        result = weeks_to_target(15.5, 18, 0.4)
        assert result is not ..., NOT_FILLED_IN
        assert result is not None, RETURNS_NONE
        cases = [((15.5, 18, 0.4), 7), ((15, 18, 0.5), 6), ((10, 12, 0.3), 7), ((17, 17, 0.5), 0), ((18.5, 18, 0.5), 0)]
        for args, expected in cases:
            result = weeks_to_target(*args)
            assert result == expected, WRONG_RESULT.format(call=f"weeks_to_target{args}", value=result)

    return check_exercise(_check, "Je `while`-lus stopt precies op tijd - ook als het doel al bereikt is.")


def is_valid_jersey(is_valid_jersey):
    def _check():
        result = is_valid_jersey("7")
        assert result is not ..., NOT_FILLED_IN
        cases = {
            "7": True, " 10 ": True, "99": True, "1": True,
            "0": False, "100": False, "abc": False, "": False, "-5": False, "7.5": False,
        }
        for text, expected in cases.items():
            result = is_valid_jersey(text)
            assert result is expected, WRONG_RESULT.format(call=f"is_valid_jersey({text!r})", value=result)

    return check_exercise(_check, "Enkel gehele getallen van 1 tot en met 99 komen erdoor.")


def jersey_input(jersey_number):
    def _check():
        assert jersey_number is not ..., NOT_FILLED_IN
        assert isinstance(jersey_number, int) and not isinstance(jersey_number, bool), (
            f"`jersey_number` is een {type(jersey_number).__name__}, geen geheel getal."
        )
        assert 1 <= jersey_number <= 99, WRONG_VALUE.format(name="jersey_number", value=jersey_number)

    return check_exercise(_check, f"Rugnummer {jersey_number} genoteerd. Probeer ook eens een ongeldig nummer.")


def test_day(count_under, to_kmh):
    def _check():
        times = [5.34, 5.62, 5.29, 5.71, 5.48, 5.93, 5.12, 5.55]
        result = count_under(times, 5.5)
        assert result is not ... and to_kmh(times) is not ..., NOT_FILLED_IN
        for limit, expected in [(5.5, 4), (5.3, 2), (5.0, 0), (6.0, 8)]:
            result = count_under(times, limit)
            assert result == expected, WRONG_RESULT.format(call=f"count_under(times, {limit})", value=result)
        assert count_under([], 5.5) == 0, WRONG_RESULT.format(call="count_under([], 5.5)", value=count_under([], 5.5))
        speeds = to_kmh(times)
        assert isinstance(speeds, list), f"`to_kmh` moet een lijst teruggeven, niet een {type(speeds).__name__}."
        assert speeds == [round(30 / t * 3.6, 1) for t in times], (
            f"`to_kmh(times)` gaf {speeds}. Controleer de omzetting, de afronding en de volgorde."
        )
        assert to_kmh([]) == [], WRONG_RESULT.format(call="to_kmh([])", value=to_kmh([]))

    return check_exercise(_check, "Twee lussen: één die telt, één die een nieuwe lijst opbouwt.")


def format_roster(format_roster):
    def _check():
        names = [" emma verhoeven", "BRAM PEETERS", "yana de backer "]
        result = format_roster(names)
        assert result is not ..., NOT_FILLED_IN
        assert result is not None, RETURNS_NONE
        assert isinstance(result, list), f"`format_roster` moet een lijst teruggeven, niet een {type(result).__name__}."
        expected = ["1. Bram Peeters", "2. Emma Verhoeven", "3. Yana De Backer"]
        assert result == expected, (
            WRONG_RESULT.format(call=f"format_roster({names})", value=result)
            + " Kuis je de namen op vóór je sorteert?"
        )
        assert format_roster([]) == [], WRONG_RESULT.format(call="format_roster([])", value=format_roster([]))

    return check_exercise(_check, "Een nette, genummerde ploeglijst.")


def roster_input(roster_names):
    def _check():
        assert roster_names is not ..., NOT_FILLED_IN
        assert isinstance(roster_names, list), "`roster_names` moet een lijst zijn."
        assert len(roster_names) > 0, "Je lijst is leeg - typ minstens één naam voor je stopt."
        assert all(isinstance(name, str) and name != "" for name in roster_names), (
            "`roster_names` mag enkel ingevulde namen bevatten - niet de lege invoer waarmee je stopt."
        )

    return check_exercise(_check, "Je programma stopt netjes bij een lege invoer.")


def clean_position(clean_position):
    def _check():
        assert clean_position("FWD") is not ..., NOT_FILLED_IN
        cases = {
            "Forward": "Forward", "forward ": "Forward", "FWD": "Forward",
            "midfielder": "Midfielder", "MID": "Midfielder",
            "defender ": "Defender", "DEF": "Defender",
            "Goalkeeper": "Goalkeeper", "GK": "Goalkeeper", "coach": "Unknown",
        }
        for raw, expected in cases.items():
            result = clean_position(raw)
            assert result == expected, WRONG_RESULT.format(call=f"clean_position({raw!r})", value=result)

    return check_exercise(_check, "Elk rommelig label wordt een net label.")


def count_positions(count_positions):
    def _check():
        raw = [
            "defender ", "midfielder", "Defender", "MID", "goalkeeper", "Forward",
            "GK", "FWD", "forward", "Midfielder", "DEF", "forward ", "FWD", "midfielder",
        ]
        result = count_positions(raw)
        assert result is not ..., NOT_FILLED_IN
        assert isinstance(result, dict), f"`count_positions` moet een dictionary teruggeven, niet een {type(result).__name__}."
        expected = {"Defender": 3, "Midfielder": 4, "Goalkeeper": 2, "Forward": 5}
        assert result == expected, (
            f"Voor de 14 voorbeeldlabels gaf je functie {result}. Zijn de sleutels de nette positienamen?"
        )
        assert count_positions(["coach", "GK"]) == {"Unknown": 1, "Goalkeeper": 1}, (
            WRONG_RESULT.format(call="count_positions(['coach', 'GK'])", value=count_positions(["coach", "GK"]))
        )
        assert count_positions([]) == {}, WRONG_RESULT.format(call="count_positions([])", value=count_positions([]))

    return check_exercise(_check, "14 rommelige labels, 4 nette posities.")


def fastest(fastest):
    def _check():
        results = [
            {"name": "Yana De Backer", "sprint_30m_s": 5.34},
            {"name": "Stan Mertens", "sprint_30m_s": None},
            {"name": "Emma Verhoeven", "sprint_30m_s": 5.29},
            {"name": "Bram Peeters", "sprint_30m_s": 5.41},
        ]
        result = fastest(results)
        assert result is not ..., NOT_FILLED_IN
        assert result is not None, RETURNS_NONE
        assert result == "Emma Verhoeven", (
            f"Je functie gaf {result!r}. Geef de **naam** terug, en sla atleten zonder tijd (None) over."
        )
        assert fastest(results[:2]) == "Yana De Backer", (
            WRONG_RESULT.format(call="fastest(results[:2])", value=fastest(results[:2]))
        )
        assert fastest(results[1:2] + results[3:]) == "Bram Peeters", (
            "Je functie werkt niet als de eerste atleet geen tijd heeft."
        )

    return check_exercise(_check, "Emma was vandaag de snelste.")


def fix_name_error(greeting):
    def _check():
        assert greeting == "Welkom, Emma Verhoeven", f"Je kreeg {greeting!r}."

    return check_exercise(_check, "NameError opgelost - het was een tikfout in de variabelenaam.")


def fix_type_error(age_message):
    def _check():
        assert age_message == "Leeftijd: 16", f"Je kreeg {age_message!r}."

    return check_exercise(
        _check,
        "TypeError opgelost - je kunt geen tekst en getal optellen; zet om met `str()` of gebruik een f-string.",
    )


def fix_key_error(yana_height_cm):
    def _check():
        assert yana_height_cm == 167.1, f"Je kreeg {yana_height_cm!r}."

    return check_exercise(_check, "KeyError opgelost - de sleutel moet exact overeenkomen, letter per letter.")


def fix_index_error(last_sprint_s):
    def _check():
        assert last_sprint_s == 5.48, f"Je kreeg {last_sprint_s!r}."

    return check_exercise(
        _check,
        "IndexError opgelost - een lijst van 3 elementen heeft de indexen 0, 1 en 2. "
        "Met `[-1]` krijg je altijd het laatste element, hoe lang de lijst ook is.",
    )


def parse_weight(parse_weight):
    def _check():
        assert parse_weight("65,5") is not ..., NOT_FILLED_IN
        cases = [("65,5", 65.5), (" 59,6", 59.6), ("70", 70.0), ("61.1 ", 61.1), ("onbekend", None), ("", None)]
        for text, expected in cases:
            result = parse_weight(text)
            call = f"parse_weight({text!r})"
            if expected is None:
                assert result is None, WRONG_RESULT.format(call=call, value=result) + " Verwacht: None."
            else:
                assert isinstance(result, float), f"`{call}` geeft het verkeerde datatype terug: een {type(result).__name__}."
                assert result == expected, WRONG_RESULT.format(call=call, value=result)

    return check_exercise(_check, "Komma's, spaties en onzin worden allemaal opgevangen - zonder crash.")


def sprint_input(valid_sprint_s):
    def _check():
        assert valid_sprint_s is not ..., NOT_FILLED_IN
        assert isinstance(valid_sprint_s, float), f"`valid_sprint_s` is een {type(valid_sprint_s).__name__}, geen float."
        assert valid_sprint_s > 0, f"{valid_sprint_s} is geen geldige tijd: een tijd moet groter zijn dan 0."

    return check_exercise(_check, f"{valid_sprint_s} s genoteerd. Probeer ook eens `abc`, `5,3` of `-2` te typen.")


def lane(cones_needed, lane_length):
    def _check():
        result = lane_length(8)
        assert result is not ... and cones_needed(8) is not ..., NOT_FILLED_IN
        for n, expected in [(1, 400.0), (4, 423.0), (8, 453.66)]:
            result = lane_length(n)
            assert abs(result - expected) < 0.01, WRONG_RESULT.format(call=f"lane_length({n})", value=result)
        for args, expected in [((8,), 91), ((4,), 85), ((8, 10), 46), ((2, 4), 102)]:
            result = cones_needed(*args)
            call = f"cones_needed({', '.join(str(a) for a in args)})"
            assert result == expected, (
                WRONG_RESULT.format(call=call, value=result) + " Let op de richting van de afronding."
            )

    return check_exercise(
        _check,
        "Een ronde in baan 8 is ongeveer 453.7 m - bijna 54 m meer dan in baan 1. "
        "Daarom is de startlijn verspringend!",
    )


def sprint_stats(sprint_stats):
    def _check():
        import statistics

        times = [5.34, 5.62, 5.29, 5.71, 5.48]
        result = sprint_stats(times)
        assert result is not ..., NOT_FILLED_IN
        assert result is not None, RETURNS_NONE
        assert isinstance(result, tuple) and len(result) == 3, (
            f"`sprint_stats` moet een tuple van 3 getallen teruggeven, je kreeg {result!r}."
        )
        expected = tuple(round(f(times), 2) for f in (statistics.mean, statistics.median, statistics.stdev))
        assert result == expected, WRONG_RESULT.format(call=f"sprint_stats({times})", value=result)

    return check_exercise(_check, "Gemiddelde, mediaan en standaardafwijking - zonder één formule zelf te schrijven.")


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
            f"`squad_counts` is nog niet juist (je kreeg {squad_counts}). "
            "Zijn de sleutels de nette positienamen?"
        )
        assert average_height_by_position == expected_heights, (
            f"`average_height_by_position` is nog niet juist (je kreeg {average_height_by_position}). "
            "Denk aan ontbrekende waarden en de afronding."
        )

    return check_exercise(
        _check,
        "Je hebt net een echte export opgekuist en samengevat met niets dan gewone Python. "
        "Volgende week doet pandas dit allemaal in een handvol regels.",
    )
