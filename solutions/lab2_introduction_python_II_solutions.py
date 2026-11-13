import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Introductie Python II - Lussen, fouten en modules

    Vorige week schreef je programma's voor **één atleet tegelijk**: één
    sprinttijd omzetten, één naam opkuisen, één hartslag indelen. Een
    echte club heeft tientallen atleten, elk met meerdere testresultaten -
    en we willen niet veertig keer dezelfde regels code kopiëren en
    plakken.

    Vandaag leer je je code **herhalen** met lussen, **veel waarden
    tegelijk** bewaren in lijsten en dictionaries, **fouten opvangen** in
    plaats van te crashen, en code van anderen gebruiken via **modules**.
    We sluiten af door het echte bestand `athletes.csv` van de club in te
    lezen en samen te vatten met gewone Python.

    **Na dit labo kun je:** code herhalen met `while`- en `for`-lussen,
    data bewaren en verwerken in lijsten en dictionaries, een foutmelding
    lezen en de fout herstellen, fouten opvangen met `try` / `except`,
    blijven vragen tot de invoer geldig is, en modules zoals `math`,
    `random` en `statistics` importeren en gebruiken.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Kort marimo-geheugensteuntje:

    - Elke variabele kan door **slechts één cel** gedefinieerd worden.
    - Oefencellen bevatten een `...` als plaatshouder of een
      `# TODO`-commentaar die je moet vervangen. De cel er net onder
      controleert je antwoord.
    - Een cel met `input()` wacht tot je iets typt in het invoervak onder
      de cel en op Enter drukt. Voer de cel opnieuw uit (▶ of
      Ctrl/Cmd + Enter) om iets anders te proberen.
    """)
    return


@app.cell
def _(mo):
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

    return (check_exercise,)


@app.cell
def _(mo):
    import sys

    # De CSV-bestanden staan in de map data/ één niveau hoger, zoals in de
    # cursusmap. Bestanden die daar ontbreken (bv. omdat je enkel dit
    # notebook gedownload hebt), worden er één keer naartoe gedownload.
    # In de browser (marimo.app) worden ze rechtstreeks van GitHub gelezen.
    _DATA_URL = "https://raw.githubusercontent.com/PACE-Ghent/Data-Science-1-2026/main/data"
    _DATA_FILES = ["athletes.csv"]
    if sys.platform == "emscripten":
        DATA_DIR = _DATA_URL
    else:
        from urllib.request import urlretrieve as _download

        _data_dir = (mo.notebook_dir() / ".." / "data").resolve()
        _data_dir.mkdir(exist_ok=True)
        for _name in _DATA_FILES:
            if not (_data_dir / _name).exists():
                _download(f"{_DATA_URL}/{_name}", _data_dir / _name)
        DATA_DIR = str(_data_dir)
    return (DATA_DIR,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Opwarming: herhaling van vorige week (13:15-13:30)

    Tijdens een sprinttest over 30 m registreren de tijdspoortjes ook de
    tussentijd op 10 m. Het stuk tussen 10 m en 30 m (een "vliegende
    20 m") zegt iets over de **maximale** snelheid van een atleet, omdat
    de acceleratiefase dan grotendeels voorbij is.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 1 - vliegende 20 m
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Schrijf `flying_20m_kmh(split_10m_s, time_30m_s)` die de gemiddelde
    snelheid over de 20 m tussen de twee tijdspoortjes teruggeeft, in
    km/u en afgerond op 1 decimaal. Voor een tussentijd van 1.92 s en een
    eindtijd van 5.21 s is dat 21.9 km/u.

    Probeer je functie daarna uit in de cel eronder: vraag beide tijden
    met `input()` en druk de snelheid af.
    """)
    return


@app.cell
def _():
    def flying_20m_kmh(split_10m_s, time_30m_s):
        """Gemiddelde snelheid in km/u tussen 10 m en 30 m."""
        return round(20 / (time_30m_s - split_10m_s) * 3.6, 1)

    return (flying_20m_kmh,)


@app.cell
def _(check_exercise, flying_20m_kmh):
    def _check():
        result = flying_20m_kmh(1.92, 5.21)
        assert result is not ..., 'Vervang eerst elke `...` door je eigen code.'
        assert result is not None, 'Je functie geeft None terug - gebruikte je `print` in plaats van `return`?'
        for args in [(1.92, 5.21), (1.85, 4.98), (2.05, 5.71)]:
            result = flying_20m_kmh(*args)
            exact = 20 / (args[1] - args[0]) * 3.6
            assert abs(result - exact) <= 0.05 + 1e-9 and result == round(result, 1), (
                '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=f"flying_20m_kmh{args}", value=result)
                + " Controleer de formule, de eenheden en de afronding op 1 decimaal."
            )

    check_exercise(
        _check,
        "Stel je nu voor dat je dit moet doen voor 43 atleten, met elk 3 testmomenten... "
        "Daarvoor dienen lussen.",
    )
    return


@app.cell
def _(flying_20m_kmh):
    split_text = input("Tussentijd op 10 m (s): ")
    finish_text = input("Eindtijd op 30 m (s): ")
    print(flying_20m_kmh(float(split_text), float(finish_text)), "km/u")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Herhalen met `while` (13:30-14:00)

    Een `while`-lus herhaalt haar (ingesprongen) body **zolang een
    voorwaarde `True` is**:

    ```python
    while condition:
        # wordt herhaald zolang condition True is
    ```

    Python controleert de voorwaarde **voor elke ronde**. Is ze `False`,
    dan gaat het programma verder na de lus. Zorg er dus voor dat er in de
    lus iets verandert waardoor de voorwaarde ooit `False` wordt - anders
    stopt de lus nooit. (Zit je toch vast in een oneindige lus? Klik op
    het stopknopje van de cel.)

    `while` is handig als je op voorhand **niet weet hoeveel herhalingen**
    je nodig hebt: "*hoeveel weken tot...*", "*blijf vragen tot...*".
    """)
    return


@app.cell
def _():
    # Na hoeveel weken heeft de ploeg in totaal 100 km gelopen, aan 12.5 km per week?
    distance_so_far_km = 0
    weeks_counted = 0
    while distance_so_far_km < 100:
        distance_so_far_km += 12.5
        weeks_counted += 1
    print(weeks_counted, "weken,", distance_so_far_km, "km")

    countdown = 3
    while countdown > 0:
        print(countdown, "...")
        countdown -= 1
    print("Start!")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### `while True` en `break`: blijven vragen tot het klopt

    `break` stopt een lus **meteen**, waar je ook zit in de body. Samen
    met `while True` (een lus die in principe nooit stopt) geeft dat een
    patroon dat je heel vaak zult gebruiken om invoer te vragen:

    ```python
    while True:
        answer = input("Doe je mee aan de training? (ja/nee) ").strip().lower()
        if answer == "ja" or answer == "nee":
            break
        print("Antwoord met ja of nee.")
    ```

    De lus vraagt opnieuw en opnieuw, tot het antwoord geldig is - en pas
    dan gaat het programma verder.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 2 - hoeveel weken tot het doel?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Een atleet zit op een bepaald Yo-Yo-niveau, en gaat er met het nieuwe
    trainingsplan elke week een vast aantal niveaus op vooruit. Schrijf
    `weeks_to_target(start_level, target_level, gain_per_week)` die met
    een `while`-lus berekent na hoeveel **weken** het doelniveau bereikt
    (of overschreden) is.

    Voorbeeld: van 15.5 naar 18 aan 0.4 per week duurt 7 weken. Zit de
    atleet al op of boven het doel, dan is het antwoord 0.
    """)
    return


@app.cell
def _():
    def weeks_to_target(start_level, target_level, gain_per_week):
        """Aantal weken tot target_level bereikt is."""
        level = start_level
        weeks = 0
        while level < target_level:
            level += gain_per_week
            weeks += 1
        return weeks

    return (weeks_to_target,)


@app.cell
def _(check_exercise, weeks_to_target):
    def _check():
        result = weeks_to_target(15.5, 18, 0.4)
        assert result is not ..., 'Vervang eerst elke `...` door je eigen code.'
        assert result is not None, 'Je functie geeft None terug - gebruikte je `print` in plaats van `return`?'
        cases = [((15.5, 18, 0.4), 7), ((15, 18, 0.5), 6), ((10, 12, 0.3), 7), ((17, 17, 0.5), 0), ((18.5, 18, 0.5), 0)]
        for args, expected in cases:
            result = weeks_to_target(*args)
            assert result == expected, '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=f"weeks_to_target{args}", value=result)

    check_exercise(_check, "Je `while`-lus stopt precies op tijd - ook als het doel al bereikt is.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 3 - een geldig rugnummer
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Rugnummers bij de club gaan van **1 tot en met 99**.

    1. Schrijf `is_valid_jersey(text)` die `True` teruggeeft als `text`
       (eventueel met spaties rond) een geheel getal van 1 tot en met 99
       is, en anders `False`. Tip: de stringmethode `.isdigit()` geeft
       `True` als een tekst enkel uit cijfers bestaat (`"7".isdigit()` is
       `True`, `"abc".isdigit()` en `"-5".isdigit()` zijn `False`). Zet de
       tekst pas om naar een `int` als je zeker weet dat het kan.
    2. Schrijf in de cel daaronder een `while True`-lus die met `input()`
       een rugnummer blijft vragen tot `is_valid_jersey` `True` geeft, en
       bewaar het geldige nummer daarna als `int` in `jersey_number`.
    """)
    return


@app.cell
def _():
    def is_valid_jersey(text):
        """True als text een geheel getal van 1 tot en met 99 is."""
        text = text.strip()
        return text.isdigit() and 1 <= int(text) <= 99

    return (is_valid_jersey,)


@app.cell
def _(check_exercise, is_valid_jersey):
    def _check():
        result = is_valid_jersey("7")
        assert result is not ..., 'Vervang eerst elke `...` door je eigen code.'
        cases = {
            "7": True, " 10 ": True, "99": True, "1": True,
            "0": False, "100": False, "abc": False, "": False, "-5": False, "7.5": False,
        }
        for text, expected in cases.items():
            result = is_valid_jersey(text)
            assert result is expected, '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=f"is_valid_jersey({text!r})", value=result)

    check_exercise(_check, "Enkel gehele getallen van 1 tot en met 99 komen erdoor.")
    return


@app.cell
def _(is_valid_jersey):
    while True:
        jersey_text = input("Rugnummer (1-99): ")
        if is_valid_jersey(jersey_text):
            break
        print("Ongeldig rugnummer, probeer opnieuw.")
    jersey_number = int(jersey_text)
    print("Rugnummer:", jersey_number)
    return (jersey_number,)


@app.cell
def _(check_exercise, jersey_number):
    def _check():
        assert jersey_number is not ..., 'Vervang eerst elke `...` door je eigen code.'
        assert isinstance(jersey_number, int) and not isinstance(jersey_number, bool), (
            f"`jersey_number` is een {type(jersey_number).__name__}, geen geheel getal."
        )
        assert 1 <= jersey_number <= 99, '`{name}` heeft nog niet de verwachte waarde (je kreeg {value!r}). Lees de opgave opnieuw.'.format(name="jersey_number", value=jersey_number)

    check_exercise(_check, f"Rugnummer {jersey_number} genoteerd. Probeer ook eens een ongeldig nummer.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Lijsten en `for`-lussen (14:00-14:40)

    Een **lijst** bewaart veel waarden, in een vaste volgorde, onder één
    naam: `times = [5.41, 5.34, 5.29]`.

    - Index vanaf `0`: `times[0]` is het eerste element, `times[-1]` het
      laatste. De slice `times[1:3]` geeft de elementen 1 en 2.
    - `len()`, `min()`, `max()`, `sum()` en `sorted()` werken allemaal op
      lijsten.
    - `x in times` controleert of een waarde in de lijst zit.
    - `.append(x)` voegt een element achteraan toe. Een lege lijst maak je
      met `[]`.

    **marimo-tip:** pas een lijst (bv. met `.append`) enkel aan in **de
    cel die ze aanmaakt**. marimo merkt niet op wanneer een andere cel een
    lijst ter plaatse verandert, dus afhankelijke cellen zouden niet
    opnieuw uitgevoerd worden.
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

    season_sprints_s.append(5.22)  # dezelfde cel - geen probleem
    print(season_sprints_s)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### `for`: iets doen voor elk element

    Een `for`-lus voert haar body **één keer uit voor elk element** van een
    lijst, telkens met de lusvariabele die naar het volgende element
    verwijst:

    ```python
    for time_s in season_sprints_s:
        print(time_s)
    ```

    Drie patronen die je keer op keer zult gebruiken:

    - **Optellen of tellen**: begin met `total = 0` vóór de lus, en tel er
      binnen de lus bij op.
    - **Omzetten of filteren naar een nieuwe lijst**: begin met een lege
      lijst `[]` en gebruik `.append()` binnen de lus (eventueel binnen een
      `if`).
    - **Overslaan of stoppen**: `continue` springt naar het volgende
      element, `break` stopt de lus.

    Handige hulpmiddelen:

    - `range(n)` geeft de getallen `0, 1, ..., n - 1`; `range(1, 4)` geeft
      `1, 2, 3`.
    - `enumerate(items, start=1)` geeft paren `(nummer, item)`.

    **marimo-tip:** de lusvariabele is een gewone variabele van de cel.
    Laat ze beginnen met een underscore (`for _time in ...`), zodat je de
    naam in andere cellen opnieuw kunt gebruiken.
    """)
    return


@app.cell
def _():
    loop_sprints_s = [5.41, 5.34, 5.29, 5.36]

    loop_total_s = 0
    for _time in loop_sprints_s:
        loop_total_s += _time
    print("Gemiddelde:", round(loop_total_s / len(loop_sprints_s), 2))

    quick_times = []
    for _time in loop_sprints_s:
        if _time < 5.35:
            quick_times.append(_time)
    print("Onder 5.35 s:", quick_times)

    for _number, _time in enumerate(loop_sprints_s, start=1):
        print(f"Test {_number}: {_time} s")

    for _lap in range(1, 4):
        print("Ronde", _lap)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 4 - overloop de testdag
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Schrijf twee functies die een lijst van 30 m-tijden verwerken met een
    `for`-lus:

    - `count_under(times, limit)` geeft terug hoeveel tijden **onder**
      `limit` liggen.
    - `to_kmh(times)` geeft een **nieuwe lijst** terug met elke tijd
      omgezet naar km/u (`30 / tijd * 3.6`), afgerond op 1 decimaal, in
      dezelfde volgorde.
    """)
    return


@app.cell
def _():
    def count_under(times, limit):
        """Aantal tijden in times dat kleiner is dan limit."""
        count = 0
        for time_s in times:
            if time_s < limit:
                count += 1
        return count

    def to_kmh(times):
        """Lijst van 30 m-tijden omgezet naar km/u, afgerond op 1 decimaal."""
        speeds = []
        for time_s in times:
            speeds.append(round(30 / time_s * 3.6, 1))
        return speeds

    return count_under, to_kmh


@app.cell
def _(check_exercise, count_under, to_kmh):
    def _check():
        times = [5.34, 5.62, 5.29, 5.71, 5.48, 5.93, 5.12, 5.55]
        result = count_under(times, 5.5)
        assert result is not ... and to_kmh(times) is not ..., 'Vervang eerst elke `...` door je eigen code.'
        for limit, expected in [(5.5, 4), (5.3, 2), (5.0, 0), (6.0, 8)]:
            result = count_under(times, limit)
            assert result == expected, '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=f"count_under(times, {limit})", value=result)
        assert count_under([], 5.5) == 0, '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call="count_under([], 5.5)", value=count_under([], 5.5))
        speeds = to_kmh(times)
        assert isinstance(speeds, list), f"`to_kmh` moet een lijst teruggeven, niet een {type(speeds).__name__}."
        assert speeds == [round(30 / t * 3.6, 1) for t in times], (
            f"`to_kmh(times)` gaf {speeds}. Controleer de omzetting, de afronding en de volgorde."
        )
        assert to_kmh([]) == [], '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call="to_kmh([])", value=to_kmh([]))

    check_exercise(_check, "Twee lussen: één die telt, één die een nieuwe lijst opbouwt.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 5 - de ploeglijst
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    De trainer typt voor elke wedstrijd de namen van de spelers in - snel,
    en dus rommelig.

    1. Schrijf `format_roster(names)` die een lijst van namen omzet naar
       een **genummerde, alfabetische** ploeglijst: een nieuwe lijst van
       strings zoals `"1. Bram Peeters"`. Kuis elke naam eerst op
       (`.strip().title()`) en sorteer daarna - anders staat `"BRAM"` vóór
       `"emma"` om de verkeerde reden. Tip: `sorted()` en `enumerate(...,
       start=1)`.
    2. Schrijf in de cel daaronder een programma dat begint met een lege
       lijst `roster_names`, met `input()` namen blijft vragen en ze
       toevoegt, en **stopt bij een lege invoer** (gewoon Enter). Druk
       daarna elke regel van `format_roster(roster_names)` af.
    """)
    return


@app.cell
def _():
    def format_roster(names):
        """Genummerde, alfabetische lijst van opgekuiste namen."""
        cleaned = []
        for name in names:
            cleaned.append(name.strip().title())
        lines = []
        for number, name in enumerate(sorted(cleaned), start=1):
            lines.append(f"{number}. {name}")
        return lines

    return (format_roster,)


@app.cell
def _(check_exercise, format_roster):
    def _check():
        names = [" emma verhoeven", "BRAM PEETERS", "yana de backer "]
        result = format_roster(names)
        assert result is not ..., 'Vervang eerst elke `...` door je eigen code.'
        assert result is not None, 'Je functie geeft None terug - gebruikte je `print` in plaats van `return`?'
        assert isinstance(result, list), f"`format_roster` moet een lijst teruggeven, niet een {type(result).__name__}."
        expected = ["1. Bram Peeters", "2. Emma Verhoeven", "3. Yana De Backer"]
        assert result == expected, (
            '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=f"format_roster({names})", value=result)
            + " Kuis je de namen op vóór je sorteert?"
        )
        assert format_roster([]) == [], '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call="format_roster([])", value=format_roster([]))

    check_exercise(_check, "Een nette, genummerde ploeglijst.")
    return


@app.cell
def _(format_roster):
    roster_names = []
    while True:
        roster_entry = input("Naam (leeg = stoppen): ")
        if roster_entry == "":
            break
        roster_names.append(roster_entry)

    for _line in format_roster(roster_names):
        print(_line)
    return (roster_names,)


@app.cell
def _(check_exercise, roster_names):
    def _check():
        assert roster_names is not ..., 'Vervang eerst elke `...` door je eigen code.'
        assert isinstance(roster_names, list), "`roster_names` moet een lijst zijn."
        assert len(roster_names) > 0, "Je lijst is leeg - typ minstens één naam voor je stopt."
        assert all(isinstance(name, str) and name != "" for name in roster_names), (
            "`roster_names` mag enkel ingevulde namen bevatten - niet de lege invoer waarmee je stopt."
        )

    check_exercise(_check, "Je programma stopt netjes bij een lege invoer.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. Dictionaries (14:40-15:30, met pauze)

    Een **dictionary** koppelt **sleutels** (keys) aan **waarden**
    (values). In plaats van een waarde op te zoeken via haar positie, zoek
    je ze op via haar naam: `athlete["position"]`.

    - `d[key]` geeft de waarde, en geeft een `KeyError` als de sleutel
      ontbreekt. `d.get(key, default)` geeft in dat geval `default` terug.
    - `d[key] = value` voegt een sleutel toe of overschrijft hem.
    - `key in d` controleert of een sleutel bestaat.
    - `for key, value in d.items():` overloopt alle paren.

    Twee toepassingen die je vandaag nodig hebt:

    - Een **opzoektabel**, bv. om rommelige labels om te zetten naar nette.
    - **Tellen per categorie**: begin met een lege dict `{}` en doe
      `counts[key] = counts.get(key, 0) + 1` voor elk element.
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
    print(yana.get("yoyo_level", "niet getest"))
    yana["weight_kg"] = 65.5  # dezelfde cel - geen probleem
    for _key, _value in yana.items():
        print(f"{_key:>12}: {_value}")
    return


@app.cell
def _():
    raw_positions = [
        "defender ", "midfielder", "Defender", "MID", "goalkeeper", "Forward",
        "GK", "FWD", "forward", "Midfielder", "DEF", "forward ", "FWD", "midfielder",
    ]

    demo_counts = {}
    for _label in raw_positions:
        _key = _label.strip().lower()
        demo_counts[_key] = demo_counts.get(_key, 0) + 1
    print(demo_counts)
    return (raw_positions,)


@app.cell
def _(mo):
    mo.md(r"""
    ### Sets

    Een **set** houdt enkel **unieke** waarden bij, zonder volgorde. Een
    lijst omzetten naar een set is de snelste manier om te zien welke
    verschillende waarden erin zitten - hier: hoe rommelig de kolom
    `position` echt is.
    """)
    return


@app.cell
def _(raw_positions):
    print(len(raw_positions), "labels,", len(set(raw_positions)), "verschillende:")
    print(set(raw_positions))
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 6 - een opzoektabel voor posities
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    De kolom `position` in de export van de club is een rommeltje:
    `"Forward"`, `"forward "`, `"FWD"`, `"MID"`, `"GK"`, ... Vul
    `POSITION_MAP` aan met de ontbrekende labels voor verdedigers
    (`defender`, `def`) en doelmannen (`goalkeeper`, `gk`), en schrijf
    `clean_position(raw)`: maak `raw` uniform met `.strip().lower()` en
    zoek het op met `.get(...)`, waarbij je `"Unknown"` teruggeeft als het
    label niet in de tabel staat.

    De nette labels blijven in het Engels, zoals in de data van de club.
    """)
    return


@app.cell
def _():
    POSITION_MAP = {
        "forward": "Forward",
        "fwd": "Forward",
        "midfielder": "Midfielder",
        "mid": "Midfielder",
        "defender": "Defender",
        "def": "Defender",
        "goalkeeper": "Goalkeeper",
        "gk": "Goalkeeper",
    }

    def clean_position(raw):
        """Zet een rommelig positielabel om naar een net label met POSITION_MAP."""
        return POSITION_MAP.get(raw.strip().lower(), "Unknown")

    return (clean_position,)


@app.cell
def _(check_exercise, clean_position):
    def _check():
        assert clean_position("FWD") is not ..., 'Vervang eerst elke `...` door je eigen code.'
        cases = {
            "Forward": "Forward", "forward ": "Forward", "FWD": "Forward",
            "midfielder": "Midfielder", "MID": "Midfielder",
            "defender ": "Defender", "DEF": "Defender",
            "Goalkeeper": "Goalkeeper", "GK": "Goalkeeper", "coach": "Unknown",
        }
        for raw, expected in cases.items():
            result = clean_position(raw)
            assert result == expected, '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=f"clean_position({raw!r})", value=result)

    check_exercise(_check, "Elk rommelig label wordt een net label.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ☕ Pauze (15:00-15:10)
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 7 - tel de atleten per positie
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Schrijf `count_positions(labels)`: overloop een lijst van rommelige
    labels, kuis elk label op met je `clean_position`, en geef een
    dictionary terug die telt hoe vaak elke nette positie voorkomt, bv.
    `{"Defender": 3, "Midfielder": 4, ...}`. Test ze in de cel met
    `raw_positions` van hierboven.
    """)
    return


@app.cell
def _(clean_position):
    def count_positions(labels):
        """Aantal keer dat elke nette positie voorkomt in labels."""
        counts = {}
        for label in labels:
            position = clean_position(label)
            counts[position] = counts.get(position, 0) + 1
        return counts

    return (count_positions,)


@app.cell
def _(check_exercise, count_positions):
    def _check():
        raw = [
            "defender ", "midfielder", "Defender", "MID", "goalkeeper", "Forward",
            "GK", "FWD", "forward", "Midfielder", "DEF", "forward ", "FWD", "midfielder",
        ]
        result = count_positions(raw)
        assert result is not ..., 'Vervang eerst elke `...` door je eigen code.'
        assert isinstance(result, dict), f"`count_positions` moet een dictionary teruggeven, niet een {type(result).__name__}."
        expected = {"Defender": 3, "Midfielder": 4, "Goalkeeper": 2, "Forward": 5}
        assert result == expected, (
            f"Voor de 14 voorbeeldlabels gaf je functie {result}. Zijn de sleutels de nette positienamen?"
        )
        assert count_positions(["coach", "GK"]) == {"Unknown": 1, "Goalkeeper": 1}, (
            '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call="count_positions(['coach', 'GK'])", value=count_positions(["coach", "GK"]))
        )
        assert count_positions([]) == {}, '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call="count_positions([])", value=count_positions([]))

    check_exercise(_check, "14 rommelige labels, 4 nette posities.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Lijsten van dictionaries

    Echte data is vaak een **lijst van dictionaries**: één dictionary per
    rij, met de kolomnamen als sleutels. Zo komt straks ook het
    atletenbestand van de club binnen. Een `for`-lus overloopt de rijen,
    en met `row["kolom"]` haal je er een waarde uit.

    Een waarde die ontbreekt, is vaak `None`. Test daarop met `is None`
    (en niet met `== None`), en sla zo'n rij over met `continue`.
    """)
    return


@app.cell
def _():
    test_results = [
        {"name": "Yana De Backer", "cmj_cm": 30.0},
        {"name": "Stan Mertens", "cmj_cm": None},
        {"name": "Emma Verhoeven", "cmj_cm": 33.5},
    ]
    for _row in test_results:
        if _row["cmj_cm"] is None:
            print(_row["name"], "werd niet getest")
            continue
        print(_row["name"], "sprong", _row["cmj_cm"], "cm")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 8 - wie was het snelst?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Schrijf `fastest(results)`: `results` is een lijst van dictionaries
    met de sleutels `"name"` en `"sprint_30m_s"`. Geef de **naam** terug
    van de atleet met de snelste (kleinste) tijd. Sommige atleten werden
    niet getest (`None`) - sla die over.

    Tip: houd tijdens de lus de beste tijd tot nu toe en de bijhorende naam
    bij. Begin met `best_time = None`, en vervang de beste tijd als die nog
    `None` is of als de huidige tijd kleiner is.
    """)
    return


@app.cell
def _():
    def fastest(results):
        """Naam van de atleet met de kleinste sprint_30m_s (None wordt overgeslagen)."""
        best_time = None
        best_name = None
        for row in results:
            time_s = row["sprint_30m_s"]
            if time_s is None:
                continue
            if best_time is None or time_s < best_time:
                best_time = time_s
                best_name = row["name"]
        return best_name

    return (fastest,)


@app.cell
def _(check_exercise, fastest):
    def _check():
        results = [
            {"name": "Yana De Backer", "sprint_30m_s": 5.34},
            {"name": "Stan Mertens", "sprint_30m_s": None},
            {"name": "Emma Verhoeven", "sprint_30m_s": 5.29},
            {"name": "Bram Peeters", "sprint_30m_s": 5.41},
        ]
        result = fastest(results)
        assert result is not ..., 'Vervang eerst elke `...` door je eigen code.'
        assert result is not None, 'Je functie geeft None terug - gebruikte je `print` in plaats van `return`?'
        assert result == "Emma Verhoeven", (
            f"Je functie gaf {result!r}. Geef de **naam** terug, en sla atleten zonder tijd (None) over."
        )
        assert fastest(results[:2]) == "Yana De Backer", (
            '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call="fastest(results[:2])", value=fastest(results[:2]))
        )
        assert fastest(results[1:2] + results[3:]) == "Bram Peeters", (
            "Je functie werkt niet als de eerste atleet geen tijd heeft."
        )

    check_exercise(_check, "Emma was vandaag de snelste.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Fouten en exceptions (15:30-16:25)

    Een foutmelding betekent niet dat je iets vreselijks gedaan hebt - het
    is Python dat je vrij precies vertelt wat er misliep. Professionele
    programmeurs zien er elke dag tientallen. De truc is ze **van onder
    naar boven te lezen**:

    ```
    Traceback (most recent call last):
      File "...", line 3, in <module>
        greeting = "Welkom, " + eror_name
                                ^^^^^^^^^
    NameError: name 'eror_name' is not defined. Did you mean: 'error_name'?
    ```

    1. **Laatste regel**: het *type* fout (`NameError`) en een boodschap.
       Vaak stelt die zelfs een oplossing voor ("*Did you mean...*").
    2. **Regels erboven**: *waar* het gebeurde - het regelnummer en de
       foute regel, met `^^^` onder de boosdoener.

    De foutmeldingen die je het vaakst zult tegenkomen:

    | Fout | Typische oorzaak |
    |---|---|
    | `SyntaxError` | Python kan de code niet eens lezen: een ontbrekende `:`, aanhalingsteken of haakje |
    | `IndentationError` | het inspringen klopt niet met de `if` / `for` / `def` waar het bij hoort |
    | `NameError` | een variabelenaam die niet bestaat (tikfout, of nog niet gedefinieerd) |
    | `TypeError` | een bewerking op het verkeerde type, bv. `"Leeftijd: " + 16` |
    | `ValueError` | juist type, onmogelijke waarde, bv. `float("61,1")` |
    | `ZeroDivisionError` | delen door nul |
    | `KeyError` | een sleutel die niet in de dictionary zit |
    | `IndexError` | een index voorbij het einde van de lijst |

    **De vier cellen hieronder zijn met opzet stuk.** Lees de foutmelding,
    en herstel elke cel zodat de controle eronder groen kleurt.
    """)
    return


@app.cell
def _():
    error_name = "Emma Verhoeven"
    greeting = "Welkom, " + error_name
    print(greeting)
    return (greeting,)


@app.cell
def _(check_exercise, greeting):
    def _check():
        assert greeting == "Welkom, Emma Verhoeven", f"Je kreeg {greeting!r}."

    check_exercise(_check, "NameError opgelost - het was een tikfout in de variabelenaam.")
    return


@app.cell
def _():
    athlete_age = 16
    age_message = "Leeftijd: " + str(athlete_age)
    print(age_message)
    return (age_message,)


@app.cell
def _(age_message, check_exercise):
    def _check():
        assert age_message == "Leeftijd: 16", f"Je kreeg {age_message!r}."

    check_exercise(
        _check,
        "TypeError opgelost - je kunt geen tekst en getal optellen; zet om met `str()` of gebruik een f-string.",
    )
    return


@app.cell
def _():
    yana_profile = {"name": "Yana De Backer", "position": "Defender", "height_cm": 167.1}
    yana_height_cm = yana_profile["height_cm"]
    print(yana_height_cm)
    return (yana_height_cm,)


@app.cell
def _(check_exercise, yana_height_cm):
    def _check():
        assert yana_height_cm == 167.1, f"Je kreeg {yana_height_cm!r}."

    check_exercise(_check, "KeyError opgelost - de sleutel moet exact overeenkomen, letter per letter.")
    return


@app.cell
def _():
    # Emma liep drie sprints; we willen de laatste.
    emma_sprints_s = [5.62, 5.55, 5.48]
    last_sprint_s = emma_sprints_s[-1]
    print(last_sprint_s)
    return (last_sprint_s,)


@app.cell
def _(check_exercise, last_sprint_s):
    def _check():
        assert last_sprint_s == 5.48, f"Je kreeg {last_sprint_s!r}."

    check_exercise(
        _check,
        "IndexError opgelost - een lijst van 3 elementen heeft de indexen 0, 1 en 2. "
        "Met `[-1]` krijg je altijd het laatste element, hoe lang de lijst ook is.",
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Fouten opvangen met `try` / `except`

    Sommige fouten kun je niet vermijden door je code beter te schrijven:
    je weet op voorhand niet wat een gebruiker gaat typen, of wat er in
    een exportbestand staat. Dan kun je de fout **opvangen**:

    ```python
    try:
        weight_kg = float(text)
    except ValueError:
        print("Dat is geen geldig getal.")
    else:
        print("Gelukt:", weight_kg)
    ```

    - Python probeert de code in `try`. Loopt daar iets mis met een
      `ValueError`, dan springt het meteen naar `except ValueError:` in
      plaats van te crashen.
    - Het (optionele) `else`-blok wordt enkel uitgevoerd als er **geen**
      fout was.
    - Vang altijd een **specifiek** type fout op. Een kale `except:` vangt
      ook fouten op die je niet verwachtte (zoals een tikfout in je eigen
      code), en verstopt zo echte bugs.

    Zelf een fout opgooien kan ook, met `raise ValueError("uitleg")` - zo
    laat je wie je functie verkeerd gebruikt duidelijk weten wat er mis is.
    """)
    return


@app.cell
def _():
    for _text in ["65.5", "65,5", "zesenvijftig"]:
        try:
            print(repr(_text), "->", float(_text))
        except ValueError:
            print(repr(_text), "-> geen geldig getal")

    total_training_min = 0
    n_sessions_attended = 0
    try:
        average_session_min = total_training_min / n_sessions_attended
    except ZeroDivisionError:
        average_session_min = 0
    print("Gemiddelde training:", average_session_min, "min")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 9 - lees een gewicht in
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    De export van de club bewaart gewichten als tekst, met een **komma**
    als decimaalteken (`"65,5"`), soms met verdwaalde spaties, en soms met
    onzin (`"onbekend"`, of helemaal leeg). Schrijf `parse_weight(text)`
    die het gewicht als `float` teruggeeft, en `None` als de tekst geen
    geldig getal is. Gebruik `try` / `except` - je programma mag niet
    crashen.
    """)
    return


@app.cell
def _():
    def parse_weight(text):
        """Zet een gewicht zoals ' 65,5' om naar 65.5, of None als dat niet kan."""
        try:
            return float(text.strip().replace(",", "."))
        except ValueError:
            return None

    return (parse_weight,)


@app.cell
def _(check_exercise, parse_weight):
    def _check():
        assert parse_weight("65,5") is not ..., 'Vervang eerst elke `...` door je eigen code.'
        cases = [("65,5", 65.5), (" 59,6", 59.6), ("70", 70.0), ("61.1 ", 61.1), ("onbekend", None), ("", None)]
        for text, expected in cases:
            result = parse_weight(text)
            call = f"parse_weight({text!r})"
            if expected is None:
                assert result is None, '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=call, value=result) + " Verwacht: None."
            else:
                assert isinstance(result, float), f"`{call}` geeft het verkeerde datatype terug: een {type(result).__name__}."
                assert result == expected, '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=call, value=result)

    check_exercise(_check, "Komma's, spaties en onzin worden allemaal opgevangen - zonder crash.")
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 10 - blijf vragen tot het lukt
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Combineer `while True`, `try` / `except` en `input()`: vraag een
    sprinttijd in seconden, en blijf vragen tot de gebruiker een geldig
    getal typt dat **groter dan 0** is. Bewaar het resultaat als `float`
    in `valid_sprint_s`.

    Test daarna met onzin (`abc`), een komma (`5,3`) en een negatief getal
    (`-2`), en kijk of je programma telkens netjes opnieuw vraagt.
    """)
    return


@app.cell
def _():
    while True:
        try:
            valid_sprint_s = float(input("Sprinttijd op 30 m (s): "))
        except ValueError:
            print("Dat is geen getal. Gebruik een punt als decimaalteken.")
        else:
            if valid_sprint_s > 0:
                break
            print("Een tijd moet groter zijn dan 0.")
    print("Genoteerd:", valid_sprint_s)
    return (valid_sprint_s,)


@app.cell
def _(check_exercise, valid_sprint_s):
    def _check():
        assert valid_sprint_s is not ..., 'Vervang eerst elke `...` door je eigen code.'
        assert isinstance(valid_sprint_s, float), f"`valid_sprint_s` is een {type(valid_sprint_s).__name__}, geen float."
        assert valid_sprint_s > 0, f"{valid_sprint_s} is geen geldige tijd: een tijd moet groter zijn dan 0."

    check_exercise(_check, f"{valid_sprint_s} s genoteerd. Probeer ook eens `abc`, `5,3` of `-2` te typen.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 6. Modules: code van anderen gebruiken (16:25-17:00)

    Python heeft veel meer functies dan `print`, `len` en `round`. Ze
    zitten verdeeld over **modules**, die je eerst moet **importeren**.
    De **standaardbibliotheek** komt mee met Python; andere modules (zoals
    pandas, volgende week) installeer je apart. Drie manieren om te
    importeren:

    ```python
    import math                 # gebruik als math.sqrt(16)
    from math import sqrt       # gebruik als sqrt(16)
    import statistics as stats  # gebruik als stats.mean(...) - handig voor lange namen
    ```

    Imports zet je **bovenaan** een notebook of script. Drie nuttige
    modules uit de standaardbibliotheek:

    | Module | Bevat bijvoorbeeld |
    |---|---|
    | `math` | `math.pi`, `math.sqrt()`, `math.ceil()` (naar boven afronden), `math.floor()` (naar beneden) |
    | `random` | `random.choice(lijst)`, `random.randint(a, b)`, `random.shuffle(lijst)` |
    | `statistics` | `statistics.mean()`, `statistics.median()`, `statistics.stdev()` |

    Weet je niet wat een functie doet? `help(math.ceil)` toont de
    documentatie.
    """)
    return


@app.cell
def _():
    import math
    import random
    import statistics

    return math, random, statistics


@app.cell
def _(math):
    print(math.pi)
    print(math.sqrt(16))
    print(math.ceil(4.1), math.floor(4.9))
    return


@app.cell
def _(random):
    squad = ["Yana", "Stan", "Emma", "Bram", "Lotte"]
    print("Neemt de penalty:", random.choice(squad))
    print("Dobbelsteen:", random.randint(1, 6))

    shuffled_squad = squad.copy()
    random.shuffle(shuffled_squad)
    print("Volgorde voor de opwarming:", shuffled_squad)
    return


@app.cell
def _(statistics):
    demo_times_s = [5.34, 5.62, 5.29, 5.71, 5.48]
    print("Gemiddelde:", statistics.mean(demo_times_s))
    print("Mediaan:", statistics.median(demo_times_s))
    print("Standaardafwijking:", statistics.stdev(demo_times_s))
    return


@app.cell
def _(mo):
    mo.md(r"""
    Voer de `random`-cel een paar keer opnieuw uit: je krijgt telkens iets
    anders. Wil je dat het toeval herhaalbaar is (handig om te testen),
    roep dan eerst `random.seed(42)` op.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 11 - hoe lang is baan 8?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Een standaard atletiekpiste van 400 m heeft twee rechte stukken van
    **84.39 m** en twee halve cirkels als bochten. Een ronde in baan 1
    wordt gemeten op een straal van **36.8 m**, en elke volgende baan ligt
    **1.22 m** verder naar buiten. Een ronde in baan `n` meet dus:

    $$2 \times 84.39 + 2 \pi r_n \qquad r_n = 36.8 + (n - 1) \times 1.22$$

    1. Schrijf `lane_length(lane)` die de lengte van een ronde in die baan
       teruggeeft. Gebruik `math.pi`.
    2. De trainer zet kegels langs de baan, om de `spacing_m` meter.
       Schrijf `cones_needed(lane, spacing_m=5)` die teruggeeft hoeveel
       kegels er nodig zijn voor een hele ronde. Gebruik `lane_length` en
       rond **naar boven** af met `math.ceil`.
    """)
    return


@app.cell
def _(math):
    def lane_length(lane):
        """Lengte in meter van een ronde in de gegeven baan."""
        radius_m = 36.8 + (lane - 1) * 1.22
        return 2 * 84.39 + 2 * math.pi * radius_m

    def cones_needed(lane, spacing_m=5):
        """Aantal kegels voor een ronde in de gegeven baan."""
        return math.ceil(lane_length(lane) / spacing_m)

    return cones_needed, lane_length


@app.cell
def _(check_exercise, cones_needed, lane_length):
    def _check():
        result = lane_length(8)
        assert result is not ... and cones_needed(8) is not ..., 'Vervang eerst elke `...` door je eigen code.'
        for n, expected in [(1, 400.0), (4, 423.0), (8, 453.66)]:
            result = lane_length(n)
            assert abs(result - expected) < 0.01, '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=f"lane_length({n})", value=result)
        for args, expected in [((8,), 91), ((4,), 85), ((8, 10), 46), ((2, 4), 102)]:
            result = cones_needed(*args)
            call = f"cones_needed({', '.join(str(a) for a in args)})"
            assert result == expected, (
                '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=call, value=result) + " Let op de richting van de afronding."
            )

    check_exercise(
        _check,
        "Een ronde in baan 8 is ongeveer 453.7 m - bijna 54 m meer dan in baan 1. "
        "Daarom is de startlijn verspringend!",
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ### Oefening 12 - statistieken van een testdag
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Schrijf `sprint_stats(times)` die drie getallen teruggeeft: het
    **gemiddelde**, de **mediaan** en de **standaardafwijking** van de
    tijden, elk afgerond op 2 decimalen. Gebruik de module `statistics`.

    Meerdere waarden teruggeven doe je door ze met komma's te scheiden:
    `return a, b, c`. Python maakt daar een **tuple** van - een soort lijst
    die je niet meer kunt veranderen - die je bij het oproepen weer kunt
    uitpakken: `mean_s, median_s, stdev_s = sprint_stats(times)`.
    """)
    return


@app.cell
def _(statistics):
    def sprint_stats(times):
        """(gemiddelde, mediaan, standaardafwijking) van times, afgerond op 2 decimalen."""
        mean_s = round(statistics.mean(times), 2)
        median_s = round(statistics.median(times), 2)
        stdev_s = round(statistics.stdev(times), 2)
        return mean_s, median_s, stdev_s

    return (sprint_stats,)


@app.cell
def _(check_exercise, sprint_stats):
    def _check():
        import statistics

        times = [5.34, 5.62, 5.29, 5.71, 5.48]
        result = sprint_stats(times)
        assert result is not ..., 'Vervang eerst elke `...` door je eigen code.'
        assert result is not None, 'Je functie geeft None terug - gebruikte je `print` in plaats van `return`?'
        assert isinstance(result, tuple) and len(result) == 3, (
            f"`sprint_stats` moet een tuple van 3 getallen teruggeven, je kreeg {result!r}."
        )
        expected = tuple(round(f(times), 2) for f in (statistics.mean, statistics.median, statistics.stdev))
        assert result == expected, '`{call}` geeft niet het verwachte resultaat terug (je kreeg {value!r}).'.format(call=f"sprint_stats({times})", value=result)

    check_exercise(_check, "Gemiddelde, mediaan en standaardafwijking - zonder één formule zelf te schrijven.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 7. Uitdaging (17:00-17:30) - het echte atletenbestand van de club

    Tijd om alles samen te gebruiken op de echte export `athletes.csv`.
    Een CSV-bestand inlezen is een taak voor de module `csv` uit de
    standaardbibliotheek: `csv.DictReader` maakt van elke regel van het
    bestand een **dictionary**, met de kolomnamen als sleutels - een lijst
    van dictionaries, zoals in oefening 8. Let op: elke waarde komt binnen
    als **tekst**.

    De code om in te lezen krijg je - bekijk de eerste twee rijen die ze
    afdrukt.
    """)
    return


@app.cell
def _(DATA_DIR):
    import csv
    from pathlib import Path
    from urllib.request import urlopen

    # Path begrijpt enkel lokale bestanden; in de browser is DATA_DIR een URL.
    if DATA_DIR.startswith("http"):
        athletes_text = urlopen(f"{DATA_DIR}/athletes.csv").read().decode("utf-8")
    else:
        athletes_text = Path(DATA_DIR, "athletes.csv").read_text()
    athlete_rows = list(csv.DictReader(athletes_text.splitlines()))

    print(len(athlete_rows), "atleten")
    print(athlete_rows[0])
    print(athlete_rows[1])
    return (athlete_rows,)


@app.cell
def _(mo):
    mo.md(r"""
    Bouw twee dictionaries, met de **nette** positie als sleutel (gebruik
    je `clean_position` uit oefening 6):

    - `squad_counts`: het aantal atleten per positie,
    - `average_height_by_position`: de gemiddelde `height_cm` per positie,
      afgerond op 1 decimaal.

    Opgelet: een paar atleten hebben een **lege** `height_cm` (een lege
    string). Sla die over bij het berekenen van de gemiddelden - maar tel
    ze wel mee in `squad_counts`.

    Hint: overloop `athlete_rows` één keer en houd drie dicts bij
    (aantallen, som van de lengtes, aantal lengtes), en bereken daarna de
    gemiddelden in een tweede lus over de posities.
    """)
    return


@app.cell
def _(athlete_rows, clean_position):
    squad_counts = {}
    height_sums = {}
    height_counts = {}
    for _row in athlete_rows:
        _position = clean_position(_row["position"])
        squad_counts[_position] = squad_counts.get(_position, 0) + 1
        if _row["height_cm"] != "":
            height_sums[_position] = height_sums.get(_position, 0) + float(_row["height_cm"])
            height_counts[_position] = height_counts.get(_position, 0) + 1

    average_height_by_position = {}
    for _position, _total in height_sums.items():
        average_height_by_position[_position] = round(_total / height_counts[_position], 1)
    print(squad_counts)
    print(average_height_by_position)
    return average_height_by_position, squad_counts


@app.cell
def _(athlete_rows, average_height_by_position, check_exercise, squad_counts):
    def _check():
        assert squad_counts is not ... and average_height_by_position is not ..., 'Vervang eerst elke `...` door je eigen code.'
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

    check_exercise(
        _check,
        "Je hebt net een echte export opgekuist en samengevat met niets dan gewone Python. "
        "Volgende week doet pandas dit allemaal in een handvol regels.",
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## Exit ticket

    Dit is voor jezelf: wat je hier typt, blijft in je eigen notebook en
    wordt naar niemand verstuurd. Schrijf het toch op - iets onder woorden
    brengen helpt - en neem de punten die nog niet duidelijk zijn mee naar
    het volgende labo, waar we ermee beginnen.
    """)
    return


@app.cell
def _(mo):
    exit_ticket = mo.ui.text_area(
        label="Welke onderwerpen van vandaag (lussen, lijsten, dictionaries, fouten, modules) "
        "zitten goed, en welk onderwerp vraagt nog oefening?",
        rows=4,
        full_width=True,
    )
    exit_ticket
    return (exit_ticket,)


@app.cell
def _(exit_ticket, mo):
    mo.md("Bedankt - tot volgende week voor Dataverwerking I.") if exit_ticket.value else mo.md(
        "Schrijf hierboven een paar woorden voor je vertrekt."
    )
    return


if __name__ == "__main__":
    app.run()
