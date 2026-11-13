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
    # Introductie Python I - Functies, variabelen en Conditionals

    Welkom! In deze cursus ben je de nieuwe data-analist van een
    (fictieve) jeugdclub voor voetbal en atletiek. Later krijg je de
    volledige exportbestanden van de club - atletenprofielen, resultaten
    van fysieke testen en hartslagmetingen - en zet je die om in tabellen,
    statistieken en grafieken.

    Voor we daaraan kunnen beginnen, hebben we de bouwstenen van de taal
    zelf nodig. Vandaag schrijf je je eerste echte **programma's**: kleine
    stukjes code die iets **vragen**, er iets mee **doen** en een antwoord
    **tonen** - een sprinttijd omzetten naar km/u, een rommelig ingetypte
    naam opkuisen, een hartslag indelen in een zone.

    **Na dit labo kun je:** tekst tonen met `print` en vragen met `input`,
    waarden opslaan in variabelen, tekst opkuisen met stringmethodes,
    rekenen met gehele getallen en kommagetallen, je eigen functies
    schrijven, en je code beslissingen laten nemen met vergelijkingen,
    `and` / `or` / `not`, `if` / `elif` / `else` en `match`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Een paar dingen over marimo voor we beginnen

    Dit notebook is **reactief**: telkens je een cel aanpast, worden alle
    cellen die ervan afhangen automatisch opnieuw uitgevoerd, in de juiste
    volgorde - niet noodzakelijk van boven naar onder. Probeer de
    schuifregelaar hieronder.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    demo_slider = mo.ui.slider(1, 10, value=5, label="Verschuif mij")
    demo_slider
    return (demo_slider,)


@app.cell(hide_code=True)
def _(demo_slider, mo):
    mo.md(f"""
    {demo_slider.value} in het kwadraat is **{demo_slider.value ** 2}**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Merk op dat je niets met de hand opnieuw moest uitvoeren - de
    schuifregelaar verschuiven was genoeg.

    Nog vier dingen om te weten:

    - De **laatste expressie** van een cel wordt boven de cel getoond.
      Alles wat je met `print(...)` afdrukt, verschijnt in de
      console-uitvoer net eronder.
    - Een cel met `input()` **wacht op jou**: onder de cel verschijnt een
      invoervak. Typ je antwoord en druk op Enter. Zolang je niets
      ingevuld hebt, wacht de rest van het notebook. Wil je iets anders
      proberen? Voer de cel opnieuw uit met het ▶-knopje (of
      Ctrl/Cmd + Enter).
    - **Twee cellen kunnen niet dezelfde variabelenaam definiëren.** Krijg
      je een fout die zegt dat een variabele "is defined by another
      cell", kies dan een andere, meer beschrijvende naam.
    - Oefencellen bevatten een `...` als plaatshouder of een `# TODO`-
      commentaar. Vervang die door je eigen code. De cel er net onder
      controleert je antwoord automatisch en kleurt groen als het juist is.
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
    _CHECKS_FILE = "lab1_checks.py"
    _CHECKS_URL = f"https://raw.githubusercontent.com/PACE-Ghent/Data-Science-1-2026/main/checks/{_CHECKS_FILE}"
    if _sys.platform == "emscripten":
        from urllib.request import urlopen as _urlopen

        _checks_source = _urlopen(_CHECKS_URL).read().decode("utf-8")
    else:
        from urllib.request import urlretrieve as _urlretrieve

        _checks_path = (mo.notebook_dir() / ".." / "checks" / _CHECKS_FILE).resolve()
        if not _checks_path.is_file():
            _checks_path.parent.mkdir(exist_ok=True)
            _urlretrieve(_CHECKS_URL, _checks_path)
        _checks_source = _checks_path.read_text()
    checks = _types.ModuleType("checks")
    exec(_checks_source, checks.__dict__)
    return (checks,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Je eerste programma: `print` en `input`

    Een programma doet bijna altijd drie dingen: het krijgt **invoer**,
    het **verwerkt** die, en het toont **uitvoer** denk aan de toverhoed van de eerste les. Voor invoer en uitvoer
    heeft Python twee ingebouwde **functies**:

    - `print(...)` toont iets. Geef je meerdere waarden mee, gescheiden
      door komma's, dan zet `print` er een spatie tussen. Met `sep=` kies
      je zelf wat ertussen komt, met `end=` wat erachter komt (standaard
      een nieuwe regel).
    - `input(vraag)` toont de vraag, wacht tot de gebruiker iets typt en
      op Enter drukt, en **geeft terug** wat er getypt werd - altijd als
      **tekst**.

    Een **functie** kan je vergelijken met een wiskundige functie: je geeft er een of meerdere **argumenten** aan mee, en ze geeft een **resultaat** terug.

    Tekst heet in Python een **string** en zet je tussen aanhalingstekens:
    `"Yana"` of `'Yana'`. Zonder aanhalingstekens denkt Python dat `Yana`
    de naam van een variabele is.
    """)
    return


@app.cell
def _():
    print("Yana", "De Backer")
    print("Yana", "De Backer", sep="")
    print("10 m", "1.92 s", "Yana", sep=" | ")
    print("Opwarmen...", end=" ")
    print("klaar!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    De cel hieronder gebruikt `input()`. Typ je naam in het vak dat onder
    de cel verschijnt en druk op Enter.

    Het antwoord van `input()` bewaren we in een **variabele**
    (`athlete_name`), zodat we het daarna kunnen gebruiken. De laatste
    regel is een **f-string**: zet een `f` voor het openingsaanhalingsteken,
    en je kunt variabelen tussen accolades `{...}` in de tekst zetten.
    """)
    return


@app.cell
def _():
    athlete_name = input("Hoe heet je? ")
    print("Hallo,", athlete_name)
    print(f"Welkom bij de club, {athlete_name}!")

    return


app._unparsable_cell(
    r"""
    print("Welkom bij de club! \n Welke ploeg traint er nu?")
    print(r"Welkom bij de club! \n Welke ploeg traint er nu?")
    -
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Variabelen

    Een **variabele** is een naam die naar een waarde verwijst. Je maakt
    er een aan met één `=`-teken: de naam staat links, de waarde rechts.

    ```python
    height_cm = 167.1
    ```

    Lees dit als "*`height_cm` verwijst nu naar de waarde 167.1*", niet
    als een wiskundige vergelijking.

    Regels en afspraken voor namen:

    - Namen mogen letters, cijfers en underscores bevatten, maar mogen
      **niet met een cijfer beginnen** (`30m_sprint` is ongeldig,
      `sprint_30m` is prima).
    - Namen zijn **hoofdlettergevoelig**: `Height` en `height` zijn twee
      verschillende variabelen.
    - In Python is `snake_case` de afspraak: woorden in kleine letters,
      gescheiden door underscores.
    - Kies **beschrijvende** namen en zet de eenheid erin als die er is:
      `sprint_30m_s` zegt je veel meer dan `s` of `x`.
    - Variabelenamen schrijven we in het **Engels**, net zoals de rest van
      de code. Zo lees je ze vlot samen met Python zelf (`if`, `print`,
      ...) en met de kolomnamen in de data van de club.
    """)
    return


@app.cell
def _():
    name = "Yana De Backer"
    birth_year = 2010
    height_cm = 167.1
    weight_kg = 65.5
    sprint_30m_s = 5.34
    is_injured = False

    print(name)
    print("Lengte:", height_cm, "cm")
    print(f"{name} weegt {weight_kg} kg.")
    return birth_year, height_cm, is_injured, name, sprint_30m_s


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 1 - welkom in de club
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    De club wil elk nieuw lid persoonlijk welkom heten. Vraag met
    `input()` de naam van het nieuwe lid en bewaar die in `new_member`.
    Maak daarna met een f-string de boodschap `welcome_message`, in
    precies deze vorm:

    `Welkom bij de club, Lotte Janssens!`

    Druk de boodschap af en voer de cel een paar keer uit met
    verschillende namen.
    """)
    return


@app.cell
def _():
    # TODO: vraag de naam met input() en maak de boodschap met een f-string
    new_member = ...
    welcome_message = ...
    print(welcome_message)
    return new_member, welcome_message


@app.cell(hide_code=True)
def _(checks, new_member, welcome_message):
    checks.welcome(new_member, welcome_message)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Werken met tekst: stringmethodes (13:35-14:05)

    Wat mensen intypen, is zelden netjes: spaties te veel, alles in
    hoofdletters, een komma in plaats van een punt. Gelukkig hebben
    strings in Python heel wat ingebouwde functies om tekst op te kuisen.
    Zo'n functie die bij een waarde hoort, heet een **methode**. Je roept
    ze op met een punt: `waarde.methode(argumenten)`.

    | Methode | Doet | Voorbeeld | Resultaat |
    |---|---|---|---|
    | `.strip()` | spaties aan beide uiteinden weghalen | `" forward ".strip()` | `"forward"` |
    | `.lower()` / `.upper()` | kleine / hoofdletters | `"FWD".lower()` | `"fwd"` |
    | `.title()` | elk woord met een hoofdletter | `"yana de backer".title()` | `"Yana De Backer"` |
    | `.capitalize()` | enkel de eerste letter een hoofdletter | `"goed gelopen".capitalize()` | `"Goed gelopen"` |
    | `.replace(oud, nieuw)` | tekst vervangen | `"65,5".replace(",", ".")` | `"65.5"` |
    | `.startswith(x)` | begint de tekst met `x`? | `"A001".startswith("A")` | `True` |

    Daarnaast geeft de ingebouwde functie `len(tekst)` het aantal tekens,
    en haal je met `tekst[0]` het eerste teken op (Python begint te tellen
    bij `0`; `tekst[-1]` is het laatste teken).

    **Belangrijk:** een methode verandert de oorspronkelijke string nooit,
    ze **geeft een nieuwe terug**. Wil je het resultaat bijhouden, ken het
    dan toe aan een variabele: `position = position.strip()`. Methodes kun
    je ook **aan elkaar rijgen**: `raw.strip().title()` kuist eerst de
    spaties op en zet daarna de hoofdletters goed.
    """)
    return


@app.cell
def _():
    raw_position = "  forward "
    raw_position.strip()
    print(repr(raw_position))  # onveranderd! repr() toont de aanhalingstekens, zodat je de spaties ziet

    cleaned_position = raw_position.strip().title()
    print(repr(cleaned_position))

    print("65,5".replace(",", "."))
    print(len("Yana"), "Yana"[0], "Yana"[-1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Opknippen en uitpakken

    `.split(sep)` knipt een tekst in stukken op elke plek waar `sep`
    staat, en geeft die stukken terug in een **lijst** (meer over lijsten
    in het volgende labo). Weet je hoeveel stukken er zijn, dan kun je ze
    in één keer **uitpakken** in evenveel variabelen:

    ```python
    day, month, year = "27/05/2010".split("/")
    ```

    Geef je een tweede argument mee, dan knipt `.split` maximaal zoveel
    keer: `"Yana De Backer".split(" ", 1)` knipt enkel bij de **eerste**
    spatie en geeft `["Yana", "De Backer"]`.
    """)
    return


@app.cell
def _():
    print("27/05/2010".split("/"))
    day, month, year = "27/05/2010".split("/")
    print(day, month, year)
    print("Yana De Backer".split(" "))
    print("Yana De Backer".split(" ", 1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 2 - een rommelig inschrijvingsformulier
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Op het online inschrijvingsformulier typen ouders de naam van hun kind
    op allerlei manieren: `"  yana de BACKER "`, `"STAN mertens"`, ...
    Vraag met `input()` een naam en bewaar die in `raw_name`. Maak daarna
    `clean_name`: zonder spaties vooraan en achteraan, en met elk woord
    met een hoofdletter (`"Yana De Backer"`).

    Test je code met een paar rommelig ingetypte namen.
    """)
    return


@app.cell
def _():
    # TODO: vraag een naam met input() en kuis ze op met stringmethodes
    raw_name = ...
    clean_name = ...
    print(repr(clean_name))
    return clean_name, raw_name


@app.cell(hide_code=True)
def _(checks, clean_name, raw_name):
    checks.clean_name(raw_name, clean_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 3 - een naam voor op het shirt
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Op de wedstrijdshirts van de club staat de **familienaam in
    hoofdletters**. Vraag met `input()` een volledige naam (voornaam,
    spatie, familienaam) en bewaar die in `full_name`. Knip de naam bij de
    **eerste** spatie op en pak de stukken uit in `first_name` en
    `last_name` - zo blijft een familienaam als `De Backer` heel. Maak
    daarna `shirt_name`: de familienaam in hoofdletters.

    Voor `Yana De Backer` is `shirt_name` dus `"DE BACKER"`.
    """)
    return


@app.cell
def _():
    # TODO: vraag de naam, knip ze op met split en maak de shirtnaam
    full_name = ...
    first_name = ...
    last_name = ...
    shirt_name = ...
    print(shirt_name)
    return first_name, full_name, last_name, shirt_name


@app.cell(hide_code=True)
def _(checks, first_name, full_name, last_name, shirt_name):
    checks.shirt_name(first_name, full_name, last_name, shirt_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Getallen: `int`, `float` en rekenen (14:05-15:00)

    Elke waarde in Python heeft een **type**. De vier die je voortdurend
    zult gebruiken:

    | Type | Voorbeeld | Voorbeeld uit de club |
    |---|---|---|
    | `int` (geheel getal) | `2010` | geboortejaar, aantal trainingen, rugnummer |
    | `float` (kommagetal) | `5.34` | sprinttijd, lengte, gewicht |
    | `str` (string = tekst) | `"Yana De Backer"` | naam, positie |
    | `bool` (booleaanse waarde) | `True` / `False` | is de atleet geblesseerd? |

    Daarnaast is er `None`, de manier waarop Python "*geen waarde*" zegt -
    bijvoorbeeld voor een test die nooit afgelegd werd.

    Je hoeft een type nooit te *declareren*: Python **kent het type
    automatisch toe** op basis van de waarde. `2010` wordt een `int`,
    `2010.0` een `float` en `"2010"` een `str`. De ingebouwde functie
    `type()` vertelt je welk type een waarde heeft. Let op: Python
    gebruikt een **punt** als decimaalteken, dus `176.3` en niet `176,3`.
    """)
    return


@app.cell
def _(birth_year, height_cm, is_injured, name):
    print(type(name))
    print(type(birth_year))
    print(type(height_cm))
    print(type(is_injured))
    print(type(None))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `input()` geeft altijd tekst

    Het type bepaalt wat je met een waarde kunt doen. `2010 + 1` is
    `2011`, maar `"2010" + "1"` plakt de twee teksten aan elkaar tot
    `"20101"`. En omdat `input()` **altijd een string** teruggeeft - ook als
    de gebruiker een getal typt - moet je die tekst eerst **omzetten**
    voor je ermee kunt rekenen:

    | Functie | Zet om naar | Voorbeeld |
    |---|---|---|
    | `int(...)` | geheel getal | `int("16")` -> `16`, `int(5.9)` -> `5` (kapt af, rondt niet af!) |
    | `float(...)` | kommagetal | `float("63.9")` -> `63.9` |
    | `str(...)` | tekst | `str(2010)` -> `"2010"` |

    Vaak doe je het vragen en omzetten in één regel:
    `age = int(input("Leeftijd? "))`.
    """)
    return


@app.cell
def _(birth_year, name):
    print("2010" + "1")
    print(birth_year + 1)
    print(int("16") + 1)
    print(int(5.9))
    print(float("63.9") * 2)
    print(f"{name} is geboren in {birth_year}.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rekenen

    | Operator | Betekenis | Voorbeeld | Resultaat |
    |---|---|---|---|
    | `+` | optellen | `5.34 + 0.1` | `5.44` |
    | `-` | aftrekken | `2026 - 2010` | `16` |
    | `*` | vermenigvuldigen | `5.6 * 3.6` | `20.16` |
    | `/` | delen (altijd een float) | `30 / 5` | `6.0` |
    | `//` | gehele deling (geheel deel) | `135 // 60` | `2` |
    | `%` | modulo (rest) | `135 % 60` | `15` |
    | `**` | macht | `1.67 ** 2` | `2.7889` |

    De gewone volgorde van bewerkingen geldt: eerst `**`, dan `*` `/` `//`
    `%`, dan `+` `-`. Gebruik **haakjes** zodra je twijfelt - ze kosten
    niets en maken duidelijk wat je bedoelt.

    `round(waarde, cijfers)` rondt een getal af. Wil je enkel bij het
    *tonen* afronden, dan kan dat in een f-string met een opmaakcode na
    een dubbelpunt: `f"{speed:.1f}"` toont 1 cijfer na de komma.
    """)
    return


@app.cell
def _(sprint_30m_s):
    speed_ms = 30 / sprint_30m_s
    print("Gemiddelde snelheid:", round(speed_ms, 2), "m/s")
    print(f"Gemiddelde snelheid: {speed_ms * 3.6:.1f} km/u")

    session_duration_s = 135
    print(session_duration_s // 60, "min", session_duration_s % 60, "s")

    print(2 + 3 * 4)
    print((2 + 3) * 4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Variabelen overschrijven

    Je kunt een variabele op elk moment een nieuwe waarde geven - de oude
    waarde wordt gewoon vergeten. De rechterkant wordt **eerst**
    uitgerekend, dus je kunt de oude waarde gebruiken om de nieuwe te
    berekenen. `+=`, `-=`, `*=` en `/=` zijn afkortingen voor precies dat:

    ```python
    sessions = 12
    sessions = sessions + 1   # 13
    sessions += 1             # 14, hetzelfde, maar korter
    ```

    Omdat types automatisch toegekend worden, kan overschrijven zelfs het
    type veranderen: `x = 5` gevolgd door `x = "vijf"` is perfect
    toegelaten (maar verwarrend - vermijd het).

    **Pas op met ingebouwde namen.** Schrijf je `max = 190` (voor een
    maximale hartslag) of `input = "5.3"`, dan overschrijf je ongemerkt de
    ingebouwde functie `max` of `input`, en een latere `max(5.3, 5.1)`
    crasht. Gebruik in de plaats `hr_max = 190`.

    **Een eigenaardigheid van marimo:** binnen één cel mag je een
    variabele zo vaak overschrijven als je wilt. Over cellen heen kan dat
    niet: elke variabele wordt door precies één cel gedefinieerd.
    """)
    return


@app.cell
def _():
    yoyo_level = 16.5
    print("Begin van het seizoen:", yoyo_level)
    yoyo_level = yoyo_level + 1.0
    print("Na de voorbereiding:", yoyo_level)
    yoyo_level += 0.5
    print("Midden in het seizoen:", yoyo_level)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 4 - hoe snel was die sprint?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Vraag met `input()` de tijd op de 30 m-sprint in seconden (bv.
    `5.34`), zet die om naar een `float` en bewaar ze in `sprint_time_s`.
    Bereken daarna de gemiddelde snelheid in km/u, afgerond op 1 decimaal,
    in `speed_kmh`. (Afstand gedeeld door tijd geeft m/s; maal 3.6 geeft
    km/u.)

    Druk het resultaat af in deze vorm: `30 m in 5.34 s = 20.2 km/u`.
    """)
    return


@app.cell
def _():
    # TODO: vraag de tijd, zet ze om naar float en bereken de snelheid
    sprint_time_s = ...
    speed_kmh = ...
    return speed_kmh, sprint_time_s


@app.cell(hide_code=True)
def _(checks, speed_kmh, sprint_time_s):
    checks.sprint_speed(speed_kmh, sprint_time_s)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 5 - werk de trainingsteller bij
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Stan heeft dit seizoen al 12 trainingen gevolgd. Vraag met `input()`
    hoeveel trainingen er deze week bij kwamen, bewaar dat als **geheel
    getal** in `sessions_this_week`, en tel het op bij `season_sessions`
    met `+=`.
    """)
    return


@app.cell
def _():
    season_sessions = 12
    # TODO: vraag het aantal trainingen van deze week (een int) en gebruik +=
    sessions_this_week = ...
    print("Trainingen dit seizoen:", season_sessions)
    return season_sessions, sessions_this_week


@app.cell(hide_code=True)
def _(checks, season_sessions, sessions_this_week):
    checks.season_sessions(season_sessions, sessions_this_week)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 6 - duur van de Yo-Yo-test
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    De software van de Yo-Yo intermittent recovery test geeft de duur
    van de test in seconden (bv. `1385`). Vraag die duur met `input()` als
    geheel getal in `yoyo_duration_s`, en gebruik `//` en `%` om ze op te
    splitsen in hele minuten (`yoyo_minutes`) en resterende seconden
    (`yoyo_seconds`). Druk af: `1385 s = 23 min 5 s`.
    """)
    return


@app.cell
def _():
    # TODO: vraag de duur en gebruik // en %
    yoyo_duration_s = ...
    yoyo_minutes = ...
    yoyo_seconds = ...
    return yoyo_duration_s, yoyo_minutes, yoyo_seconds


@app.cell(hide_code=True)
def _(checks, yoyo_duration_s, yoyo_minutes, yoyo_seconds):
    checks.yoyo_time(yoyo_duration_s, yoyo_minutes, yoyo_seconds)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ☕ Pauze (15:00-15:10)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Eigen functies schrijven (15:10-15:55)

    Je hebt al heel wat functies **opgeroepen**: `print()`, `input()`,
    `int()`, `round()`, `len()`. Nu ga je er zelf **definiëren** - je eigen
    bouwblokken, die je zo vaak kunt hergebruiken als je wilt:

    ```python
    def average_speed_kmh(distance_m, time_s):
        '''Gemiddelde snelheid in km/u over een afstand gelopen in een gegeven tijd.'''
        speed_ms = distance_m / time_s
        return speed_ms * 3.6
    ```

    - `def` begint de definitie, gevolgd door de **naam** van de functie,
      haar **parameters** tussen haakjes, en een dubbelpunt.
    - De **body** springt in (4 spaties) en wordt uitgevoerd telkens de
      functie opgeroepen wordt. Inspringen is in Python geen versiering:
      het bepaalt welke regels bij de functie horen.
    - `return` geeft een waarde terug aan wie de functie opriep - en
      beëindigt de functie meteen.
    - De tekst tussen drie aanhalingstekens net onder de `def`-regel is de
      **docstring**: documentatie voor wie de functie gebruikt.

    Een functie definiëren doet nog niets zichtbaars - ze wordt pas
    uitgevoerd als je ze **oproept**: `average_speed_kmh(30, 5.34)`. De
    waarden die je meegeeft, heten **argumenten**.
    """)
    return


@app.cell
def _():
    def average_speed_kmh(distance_m, time_s):
        """Gemiddelde snelheid in km/u over een afstand gelopen in een gegeven tijd."""
        speed_ms = distance_m / time_s
        return speed_ms * 3.6

    print(average_speed_kmh(30, 5.34))
    print(average_speed_kmh(20, 3.29))
    print(average_speed_kmh(time_s=5.34, distance_m=30))  # argumenten met naam: de volgorde maakt niet uit
    return (average_speed_kmh,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `return` is niet hetzelfde als `print`

    Een functie die enkel **afdrukt**, toont iets op het scherm, maar geeft
    niets terug: het resultaat van de oproep is `None`. Daar kun je niet
    verder mee rekenen.
    """)
    return


@app.cell
def _():
    def print_speed_kmh(distance_m, time_s):
        print(distance_m / time_s * 3.6)

    printed_result = print_speed_kmh(30, 5.34)
    print("Wat er terugkwam:", printed_result)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Standaardwaarden

    Een parameter kan een **standaardwaarde** hebben, die gebruikt wordt
    als wie de functie oproept dat argument niet meegeeft. Parameters met
    een standaardwaarde komen **na** die zonder.
    """)
    return


@app.cell
def _(average_speed_kmh):
    def sprint_speed_kmh(time_s, distance_m=30):
        """Snelheid in km/u voor een sprinttest; de standaardafstand is 30 m."""
        return round(average_speed_kmh(distance_m, time_s), 1)

    print(sprint_speed_kmh(5.34))
    print(sprint_speed_kmh(1.92, distance_m=10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rekenen en vragen gescheiden houden

    Een goede gewoonte: laat de functie het **rekenwerk** doen, en vraag de
    invoer en toon het resultaat **buiten** de functie:

    ```python
    time_s = float(input("Tijd op de 30 m (s): "))
    print(sprint_speed_kmh(time_s))
    ```

    Zo kun je de functie testen zonder telkens iets te moeten typen - en
    dat is precies wat de controles onder de volgende oefeningen doen: ze
    roepen je functie op met een reeks vaste voorbeelden. In de cel
    "probeer je functie uit" mag je ze daarna zelf gebruiken met
    `input()`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 7 - een functie voor de BMI
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    De Body Mass Index is het gewicht in kg gedeeld door het **kwadraat**
    van de lengte in **meter**. Schrijf een functie `bmi(weight_kg,
    height_cm)` die de BMI afgerond op 1 decimaal **teruggeeft**. Let op de
    eenheden en de haakjes!
    """)
    return


@app.function
def bmi(weight_kg, height_cm):
    """Body Mass Index, afgerond op 1 decimaal."""
    # TODO: bereken de BMI en geef ze terug
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.bmi(bmi)
    return


@app.cell
def _():
    # Probeer je functie uit (wordt niet gecontroleerd): vraag met input()
    # een gewicht in kg en een lengte in cm, zet ze om naar float, en druk
    # het resultaat van bmi(...) af.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 8 - toon een tijd zoals een stopwatch
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Een stopwatch toont 1385 seconden als `23:05`: minuten, een dubbelpunt,
    en de seconden **altijd met twee cijfers**. Schrijf een functie
    `format_time(total_s)` die zo'n string teruggeeft.

    Tip: in een f-string toont de opmaakcode `:02d` een geheel getal met
    minstens 2 cijfers, aangevuld met nullen: `f"{5:02d}"` geeft `"05"`.
    """)
    return


@app.function
def format_time(total_s):
    """Toon een aantal seconden als 'm:ss', bv. 1385 -> '23:05'."""
    # TODO: bereken minuten en seconden, en geef de opgemaakte tekst terug
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.format_time(format_time)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Scope: waar is een variabele zichtbaar?

    Variabelen die je **binnen** een functie aanmaakt (ook haar
    parameters), zijn **lokaal**: ze bestaan enkel zolang de functie
    loopt, en zijn daarbuiten onzichtbaar. Variabelen die je buiten elke
    functie aanmaakt, zijn **globaal**: een functie kan ze *lezen*.

    Een waarde toekennen aan een naam binnen een functie maakt een
    **nieuwe lokale variabele**, ook als er al een globale variabele met
    dezelfde naam bestaat. De globale blijft onaangeroerd.

    **Voorspel eerst** wat de cel hieronder afdrukt, en voer ze dan pas
    uit. Haal daarna het `#` voor de laatste regel weg: welke fout krijg
    je, en waarom?
    """)
    return


@app.cell
def _():
    sprint_threshold_s = 5.5

    def is_fast_sprint(time_s):
        sprint_threshold_s = 5.0  # een nieuwe, lokale variabele
        local_note = "Ik besta enkel binnen de functie"
        return time_s < sprint_threshold_s

    print(is_fast_sprint(5.3), sprint_threshold_s)
    # print(local_note)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Goede gewoonte: een functie krijgt alles wat ze nodig heeft via haar
    **parameters**, en geeft haar resultaat terug met `return`. Functies
    die stilletjes afhangen van globale variabelen zijn moeilijk te
    hergebruiken en te testen.

    **Een eigenaardigheid van marimo:** een variabele waarvan de naam
    begint met een underscore (`_total`), is **lokaal in haar cel** -
    andere cellen zien ze niet, en je kunt de naam in een andere cel
    opnieuw gebruiken.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 9 - verwijder een verborgen globale variabele
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    De functie `age_in_season` hieronder hangt af van de globale variabele
    `SEASON_YEAR`. Herschrijf ze zodat het seizoensjaar een **parameter**
    `season_year` wordt met **standaardwaarde** `2026`. Na je aanpassing
    moet `age_in_season(2010)` nog altijd `16` zijn, en
    `age_in_season(2010, season_year=2030)` moet `20` zijn.
    """)
    return


@app.cell
def _():
    SEASON_YEAR = 2026

    # TODO: maak van season_year een parameter met standaardwaarde 2026
    def age_in_season(birth_year):
        return SEASON_YEAR - birth_year

    return (age_in_season,)


@app.cell(hide_code=True)
def _(age_in_season, checks):
    checks.age_in_season(age_in_season)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Vergelijken en combineren (15:55-16:20)

    Vergelijkingsoperatoren vergelijken twee waarden en geven altijd een
    `bool` (`True` of `False`):

    | Operator | Betekenis |
    |---|---|
    | `==` | gelijk aan |
    | `!=` | niet gelijk aan |
    | `<` / `>` | kleiner / groter dan |
    | `<=` / `>=` | kleiner / groter dan of gelijk aan |

    Verwar `=` (een waarde toekennen) niet met `==` (twee waarden
    vergelijken).

    Twee valkuilen die je nu al best kent, want je komt ze allebei tegen in
    de echte data van de club:

    - Tekst vergelijken is **exact**: `"Forward" == "forward "` is `False`
      (een andere hoofdletter, plus een spatie achteraan). Kuis tekst dus
      eerst op met `.strip()` en `.lower()`.
    - Kommagetallen worden bij benadering opgeslagen: `0.1 + 0.2 == 0.3`
      is `False`! Vergelijk floats daarom met een tolerantie, bv.
      `abs(a - b) < 1e-9`.

    **Logische operatoren** combineren booleaanse waarden:

    | Expressie | Waar (`True`) als... |
    |---|---|
    | `a and b` | zowel `a` als `b` `True` zijn |
    | `a or b` | minstens één van beide `True` is |
    | `not a` | `a` `False` is |

    Python laat ook **geketende vergelijkingen** toe, die lezen zoals in
    de wiskunde: `140 <= heart_rate <= 160` betekent "*hartslag tussen 140
    en 160*". Combineer je `and`, `or` en `not` in één expressie, dan wordt
    eerst `not` uitgerekend, dan `and` en dan `or`. Haakjes maken het
    leesbaar.
    """)
    return


@app.cell
def _(height_cm, is_injured, sprint_30m_s):
    print(sprint_30m_s < 5.5)
    print("Forward" == "forward ")
    print("Forward".lower() == "forward ".strip().lower())
    print(0.1 + 0.2 == 0.3, 0.1 + 0.2)

    heart_rate = 152
    print(sprint_30m_s < 5.5 and height_cm > 160)
    print(sprint_30m_s < 5.0 or height_cm > 160)
    print(not is_injured)
    print(140 <= heart_rate <= 160)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 10 - mag deze atleet bij de U16 spelen?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Een atleet mag in de U16-competitie spelen als die in het seizoensjaar
    **jonger dan 16** wordt (dus `season_year - birth_year < 16`) **en**
    **niet geblesseerd** is. Schrijf `is_eligible_u16(birth_year,
    is_injured, season_year=2026)` die `True` of `False` teruggeeft.

    Je hebt hier geen `if` nodig: een vergelijking *is* al `True` of
    `False`, dus je kunt het resultaat van de hele expressie meteen
    teruggeven.
    """)
    return


@app.function
def is_eligible_u16(birth_year, is_injured, season_year=2026):
    """True als de atleet in season_year bij de U16 mag spelen."""
    # TODO: combineer een voorwaarde op leeftijd en een voorwaarde op blessure
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.is_eligible_u16(is_eligible_u16)
    return


@app.cell
def _():
    # Probeer je functie uit (wordt niet gecontroleerd): vraag met input()
    # een geboortejaar (int) en druk is_eligible_u16(...) af voor een
    # atleet die niet geblesseerd is.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Beslissingen: `if`, `elif`, `else` en `match` (16:20-17:10)

    Met voorwaarden kan je code **beslissingen** nemen:

    ```python
    if condition:
        # wordt enkel uitgevoerd als condition True is
    elif other_condition:
        # wordt uitgevoerd als condition False was en other_condition True is
    else:
        # wordt uitgevoerd als geen van de vorige True was
    ```

    - De regel met `if` / `elif` / `else` eindigt op een **dubbelpunt** `:`.
    - De code die erbij hoort, **springt in** (4 spaties).
    - Python controleert de voorwaarden **van boven naar onder** en voert
      enkel het **eerste** blok uit waarvan de voorwaarde `True` is. De
      volgorde van je `elif`s doet er dus toe.

    Binnen een functie kun je vanuit elke tak meteen `return`en - de rest
    van de functie wordt dan niet meer uitgevoerd.
    """)
    return


@app.cell
def _():
    def sprint_feedback(time_s):
        """Feedback van de trainer op een 30 m-sprint."""
        if time_s < 5.0:
            return "Uitstekende sprint!"
        elif time_s < 5.5:
            return "Goede sprint."
        else:
            return "Er is ruimte voor verbetering."

    print(4.95, "s ->", sprint_feedback(4.95))
    print(5.34, "s ->", sprint_feedback(5.34))
    print(5.80, "s ->", sprint_feedback(5.80))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 11 - deel een sprong in
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Schrijf `jump_category(cmj_cm)` die een countermovement jump (CMJ)
    indeelt:

    - onder 25 cm -> `"onder gemiddeld"`
    - vanaf 25 cm tot (niet inbegrepen) 32 cm -> `"gemiddeld"`
    - 32 cm of meer -> `"boven gemiddeld"`
    """)
    return


@app.function
def jump_category(cmj_cm):
    """Categorie van een CMJ-hoogte in cm."""
    # TODO: geef de juiste categorie terug met if / elif / else
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.jump_category(jump_category)
    return


@app.cell
def _():
    # Probeer je functie uit (wordt niet gecontroleerd): vraag met input()
    # een spronghoogte in cm en druk de categorie af.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 12 - hartslagzones
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Een veelgebruikte manier om de intensiteit van een training uit te
    drukken, is de hartslag als percentage van de maximale hartslag van de
    atleet: `heart_rate / hr_max * 100`. Schrijf `hr_zone(heart_rate,
    hr_max=205)` die de zone als **geheel getal** teruggeeft:

    | % van `hr_max` | Zone |
    |---|---|
    | onder 60 | `1` |
    | 60 tot 70 | `2` |
    | 70 tot 80 | `3` |
    | 80 tot 90 | `4` |
    | 90 of meer | `5` |
    """)
    return


@app.function
def hr_zone(heart_rate, hr_max=205):
    """Hartslagzone (1-5) op basis van het percentage van hr_max."""
    # TODO: bereken het percentage en geef de zone terug
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.hr_zone(hr_zone)
    return


@app.cell
def _():
    # Probeer je functie uit (wordt niet gecontroleerd): vraag met input()
    # een hartslag (int) en druk de zone af.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `match`: één waarde, veel mogelijke gevallen

    Vergelijk je één waarde met een hele reeks vaste mogelijkheden, dan is
    `match` vaak leesbaarder dan een lange `if` / `elif`-ketting:

    ```python
    match test_name:
        case "sprint_10m" | "sprint_30m":
            unit = "s"
        case "cmj":
            unit = "cm"
        case _:
            unit = "?"
    ```

    - Python overloopt de `case`s van boven naar onder en voert de eerste
      uit die overeenkomt.
    - `|` betekent "*of*": het geval past bij elk van de opgesomde waarden.
    - `case _:` vangt al de rest op, zoals een `else`.
    """)
    return


@app.cell
def _():
    def test_unit(test_name):
        """Eenheid waarin een fysieke test gemeten wordt."""
        match test_name:
            case "sprint_10m" | "sprint_30m":
                return "s"
            case "cmj":
                return "cm"
            case "yoyo":
                return "niveau"
            case _:
                return "?"

    for _test in ["sprint_30m", "cmj", "yoyo", "bankdrukken"]:
        print(_test, "->", test_unit(_test))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Oefening 13 - in welke linie speel je?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In de spelersdatabank staat de positie als afkorting, en niet altijd
    netjes ingetypt (`"GK"`, `" def "`, `"mid"`, ...). Schrijf
    `team_line(code)` die de afkorting eerst opkuist (spaties weg, alles
    in hoofdletters) en daarna met `match` de linie teruggeeft:

    | Afkorting | Linie |
    |---|---|
    | `GK` of `DEF` | `"verdediging"` |
    | `MID` | `"middenveld"` |
    | `FWD` | `"aanval"` |
    | iets anders | `"onbekend"` |
    """)
    return


@app.function
def team_line(code):
    """Linie (verdediging, middenveld, aanval) bij een positieafkorting."""
    # TODO: kuis code op en gebruik match
    return ...


@app.cell(hide_code=True)
def _(checks):
    checks.team_line(team_line)
    return


@app.cell
def _():
    # Probeer je functie uit (wordt niet gecontroleerd): vraag met input()
    # een afkorting en druk de linie af.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7. Uitdaging (17:10-17:30) - welke ploeg traint er nu?

    Een ouder komt aan op de club en wil weten welke ploeg er op dat
    moment op het veld staat. Het trainingsschema:

    | Van | Tot (niet inbegrepen) | Ploeg |
    |---|---|---|
    | 16:00 | 17:30 | `"U12"` |
    | 17:30 | 19:00 | `"U14"` |
    | 19:00 | 20:30 | `"U16"` |
    | ander uur | | `"geen training"` |

    1. Schrijf `to_hours(time_text)` die een tijd als `"17:45"` omzet naar
       een kommagetal in uren: `17.75`. (Knip op bij de `:`, zet beide
       stukken om naar getallen, en reken de minuten om naar een deel van
       een uur.)
    2. Schrijf `training_group(time_text)` die `to_hours` gebruikt en de
       ploeg teruggeeft volgens het schema.
    3. Maak in de laatste cel een klein programma: vraag met `input()` hoe
       laat het is, en druk af welke ploeg er traint.
    """)
    return


@app.cell
def _():
    def to_hours(time_text):
        """Zet een tijd 'uu:mm' om naar uren als kommagetal, bv. '17:45' -> 17.75."""
        # TODO: knip op bij ":" en reken om
        return ...

    def training_group(time_text):
        """Ploeg die op het gegeven uur traint."""
        # TODO: gebruik to_hours en if / elif / else
        return ...

    return to_hours, training_group


@app.cell(hide_code=True)
def _(checks, to_hours, training_group):
    checks.training(to_hours, training_group)
    return


if __name__ == "__main__":
    app.run()
