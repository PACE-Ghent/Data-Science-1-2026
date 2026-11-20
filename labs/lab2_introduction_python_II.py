import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
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

    **Na dit labo kun je:** code herhalen met `while`- en `for`-lussen,
    data bewaren en verwerken in lijsten en dictionaries, een foutmelding
    lezen en de fout herstellen, fouten opvangen met `try` / `except`,
    blijven vragen tot de invoer geldig is, en modules zoals `math`,
    `random` en `statistics` importeren en gebruiken.
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    import sys as _sys
    import types as _types

    # De antwoordcontroles staan in een apart bestand (checks/ in de
    # cursusrepository), zodat dit notebook de antwoorden niet verklapt.
    # Het controlebestand staat in de map checks/ één niveau hoger, zoals
    # in de cursusmap. Ontbreekt het daar (bv. omdat je enkel dit notebook
    # gedownload hebt), dan wordt het er één keer naartoe gedownload. In de
    # browser (marimo.app) wordt het rechtstreeks van GitHub gelezen.
    _CHECKS_FILE = "lab2_checks.py"
    _CHECKS_URL = f"https://raw.githubusercontent.com/PACE-Ghent/Data-Science-1-2026/main/checks/{_CHECKS_FILE}"
    if _sys.platform == "emscripten":
        from urllib.request import urlopen as _urlopen

        _checks_source = _urlopen(_CHECKS_URL).read().decode("utf-8")
    else:
        from urllib.request import urlretrieve

        _checks_path = (mo.notebook_dir() / ".." / "checks" / _CHECKS_FILE).resolve()
        if not _checks_path.is_file():
            _checks_path.parent.mkdir(exist_ok=True)
            urlretrieve(_CHECKS_URL, _checks_path)
        _checks_source = _checks_path.read_text()
    checks = _types.ModuleType("checks")
    exec(_checks_source, checks.__dict__)
    return (checks,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Herhalen met `while`

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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 2 - hoeveel weken tot het doel?
    """)
    return


@app.cell(hide_code=True)
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


@app.function
def weeks_to_target(start_level, target_level, gain_per_week):
    """Aantal weken tot target_level bereikt is."""
    # TODO: houd het niveau en het aantal weken bij in een while-lus
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.weeks_to_target(weeks_to_target)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 3 - een geldig rugnummer
    """)
    return


@app.cell(hide_code=True)
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


@app.function
def is_valid_jersey(text):
    """True als text een geheel getal van 1 tot en met 99 is."""
    # TODO: kuis text op, controleer of het enkel cijfers zijn, en dan de grenzen
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.is_valid_jersey(is_valid_jersey)
    return


@app.cell
def _():
    # TODO: blijf vragen met input() tot is_valid_jersey(...) True is,
    # en bewaar het nummer daarna als int in jersey_number
    jersey_number = ...
    print("Rugnummer:", jersey_number)
    return (jersey_number,)


@app.cell(hide_code=True)
def _(checks, jersey_number):
    checks.jersey_input(jersey_number)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Lijsten en `for`-lussen

    ### `list`

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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `tuple`

    Een **tuple** bewaart ook meerdere waarden, in een vaste volgorde, onder
    één naam. Het verschil met een lijst: een tuple kan je na het aanmaken
    **niet meer veranderen**. Je schrijft een tuple met ronde haakjes:
    `splits = (5.41, 5.34, 5.29)`.

    - Index vanaf `0`, net als bij lijsten: `splits[0]` is het eerste
      element, `splits[-1]` het laatste. De slice `splits[1:3]` geeft een
      **nieuwe tuple** met de elementen 1 en 2.
    - `len()`, `min()`, `max()`, `sum()` en `sorted()` werken ook op tuples.
      Let op: `sorted()` geeft altijd een **lijst** terug.
    - `x in splits` controleert of een waarde in de tuple zit.
    - Er is geen `.append()`: je kunt niets toevoegen, verwijderen of
      vervangen. Een element erbij geeft een nieuwe tuple:
      `splits + (5.25,)`.
    - Een lege tuple maak je met `()`. Een tuple met één element schrijf je
      met een komma: `(5.41,)`. De komma maakt er een tuple van, niet de
      haakjes: `(5.41)` is gewoon een getal.
    - Je kunt een tuple **uitpakken** in aparte variabelen:
      `naam, tijd = ("Wout", 5.41)`.
    - Gebruik een tuple voor een vast groepje waarden dat bij elkaar hoort,
      bv. `(lat, lon)` of `(naam, tijd)`. Moet de verzameling nog groeien of
      veranderen, gebruik dan een lijst.

    **marimo-tip:** een tuple kan niet ter plaatse veranderen, dus het
    probleem van lijsten heb je hier niet. Elke "wijziging" maakt een nieuwe
    tuple, en die nieuwe waarde ziet marimo wel. Geef de nieuwe tuple wel
    een **nieuwe naam**, bv. `alle_splits = splits + (5.25,)`. marimo laat
    niet toe dat twee cellen dezelfde variabele definiëren, dus
    `splits = splits + (5.25,)` in een andere cel geeft een fout.
    """)
    return


@app.cell
def _():
    uitslag = [("Yana", 5.41), ("Lotte", 5.34), ("Jana", 5.29), ("Lina", 5.36)]
    for _naam, _tijd in uitslag:
        print(f"{_naam}: {_tijd} s")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Waarom een tuple en geen lijst?** Een tuple zegt: "deze waarden horen
    vast bij elkaar en veranderen niet". Neem een uitslag waarin elke renner
    een paar `(naam, tijd)` is:

    ```python
    uitslag = [("Wout", 5.41), ("Remco", 5.34), ("Tadej", 5.29)]
    ```

    De buitenste structuur is een **lijst**, want er kunnen nog renners
    bijkomen (`uitslag.append(("Jonas", 5.38))`). Elk paar is een **tuple**,
    want een naam hoort altijd bij zijn eigen tijd. Met een tuple kan je die
    koppeling niet per ongeluk breken:

    ```python
    renner = uitslag[0]
    renner[1] = 5.00   # TypeError: 'tuple' object does not support item assignment
    ```

    Was `renner` een lijst geweest, dan had Python de tijd zonder
    foutmelding overschreven, en zat er een verkeerde tijd in je uitslag.
    Met een tuple krijg je meteen een fout, en zie je de vergissing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 4 - overloop de testdag
    """)
    return


@app.cell(hide_code=True)
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
        # TODO: tel met een for-lus
        return ...

    def to_kmh(times):
        """Lijst van 30 m-tijden omgezet naar km/u, afgerond op 1 decimaal."""
        # TODO: bouw een nieuwe lijst op met .append()
        return ...

    return count_under, to_kmh


@app.cell(hide_code=True)
def _(checks, count_under, to_kmh):
    checks.test_day(count_under, to_kmh)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 5 - de ploeglijst
    """)
    return


@app.cell(hide_code=True)
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


@app.function
def format_roster(names):
    """Genummerde, alfabetische lijst van opgekuiste namen."""
    # TODO: kuis op, sorteer en nummer
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.format_roster(format_roster)
    return


@app.cell
def _():
    # TODO: vraag namen tot de invoer leeg is, en druk de ploeglijst af
    roster_names = ...
    return (roster_names,)


@app.cell(hide_code=True)
def _(checks, roster_names):
    checks.roster_input(roster_names)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Dictionaries

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
    for _key, _value in yana.items():
        print(f"{_key}: {_value}")
    return (yana,)


@app.cell
def _(yana):
    print(yana["name"])
    return


@app.cell
def _(yana):
    print(yana.get("yoyo_level", "niet getest"))
    return


@app.cell
def _(yana):
    yana["weight_kg"] = 65.5  # dezelfde cel - geen probleem
    return


@app.cell
def _(yana):
    print(yana.keys())
    return


@app.cell
def _(yana):
    print(yana.values())
    return


@app.cell
def _(yana):
    print(yana.items())
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 6 - een opzoektabel voor posities
    """)
    return


@app.cell(hide_code=True)
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
        # TODO: voeg de vier ontbrekende items toe
    }

    def clean_position(raw):
        """Zet een rommelig positielabel om naar een net label met POSITION_MAP."""
        # TODO: maak raw uniform en zoek het op in POSITION_MAP
        return ...

    return (clean_position,)


@app.cell(hide_code=True)
def _(checks, clean_position):
    checks.clean_position(clean_position)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 7 - tel de atleten per positie
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Schrijf `count_positions(labels)`: overloop een lijst van rommelige
    labels, kuis elk label op met je `clean_position`, en geef een
    dictionary terug die telt hoe vaak elke nette positie voorkomt, bv.
    `{"Defender": 3, "Midfielder": 4, ...}`. Test ze in de cel met
    `raw_positions` van hierboven.
    """)
    return


@app.function
def count_positions(labels):
    """Aantal keer dat elke nette positie voorkomt in labels."""
    # TODO: begin met een lege dict en tel de nette labels
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.count_positions(count_positions)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 8 - wie was het snelst?
    """)
    return


@app.cell(hide_code=True)
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


@app.function
def fastest(results):
    """Naam van de atleet met de kleinste sprint_30m_s (None wordt overgeslagen)."""
    # TODO: overloop results en houd de beste tijd en naam bij
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.fastest(fastest)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Fouten

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
def _(eror_name):
    error_name = "Emma Verhoeven"
    greeting = "Welkom, " + eror_name
    print(greeting)
    return (greeting,)


@app.cell(hide_code=True)
def _(checks, greeting):
    checks.fix_name_error(greeting)
    return


@app.cell
def _():
    athlete_age = 16
    age_message = "Leeftijd: " + athlete_age
    print(age_message)
    return (age_message,)


@app.cell(hide_code=True)
def _(age_message, checks):
    checks.fix_type_error(age_message)
    return


@app.cell
def _():
    yana_profile = {"name": "Yana De Backer", "position": "Defender", "height_cm": 167.1}
    yana_height_cm = yana_profile["heigth_cm"]
    print(yana_height_cm)
    return (yana_height_cm,)


@app.cell(hide_code=True)
def _(checks, yana_height_cm):
    checks.fix_key_error(yana_height_cm)
    return


@app.cell
def _():
    # Emma liep drie sprints; we willen de laatste.
    emma_sprints_s = [5.62, 5.55, 5.48]
    last_sprint_s = emma_sprints_s[3]
    print(last_sprint_s)
    return (last_sprint_s,)


@app.cell(hide_code=True)
def _(checks, last_sprint_s):
    checks.fix_index_error(last_sprint_s)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Modules: code van anderen gebruiken

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
    from math import sqrt
    import random
    import statistics as stat

    return math, random, sqrt, stat


@app.cell
def _(math, sqrt):
    print(math.pi)
    print(sqrt(16))
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
def _(stat):
    demo_times_s = [5.34, 5.62, 5.29, 5.71, 5.48]
    print("Gemiddelde:", stat.mean(demo_times_s))
    print("Mediaan:", stat.median(demo_times_s))
    print("Standaardafwijking:", stat.stdev(demo_times_s))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 11 - hoe lang is baan 8?
    """)
    return


@app.cell(hide_code=True)
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
def _():
    def lane_length(lane):
        """Lengte in meter van een ronde in de gegeven baan."""
        # TODO: bereken de straal en daarna de lengte van de ronde
        return ...

    def cones_needed(lane, spacing_m=5):
        """Aantal kegels voor een ronde in de gegeven baan."""
        # TODO: gebruik lane_length en math.ceil
        return ...

    return cones_needed, lane_length


@app.cell(hide_code=True)
def _(checks, cones_needed, lane_length):
    checks.lane(cones_needed, lane_length)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 12 - statistieken van een testdag
    """)
    return


@app.cell(hide_code=True)
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


@app.function
def sprint_stats(times):
    """(gemiddelde, mediaan, standaardafwijking) van times, afgerond op 2 decimalen."""
    # TODO: gebruik statistics.mean, statistics.median en statistics.stdev
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.sprint_stats(sprint_stats)
    return


if __name__ == "__main__":
    app.run()
