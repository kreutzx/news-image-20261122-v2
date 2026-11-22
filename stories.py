# Story database for "The World in One Day" — Sunday 22 November 2026.
# Every item was reported on 22 Nov 2026 (UTC or a local zone where it was
# already / still 22 Nov). Each story carries its outlet and a certainty tag:
# CONFIRMED (multiple outlets / official), REPORTED (single-source reporting),
# DEVELOPING (still unfolding), CLAIM (one side's claim, unverified),
# FORECAST (scheduled / expected). The renderer counts stories, regions,
# drawn items and certainty tags from this data and prints them on the page.

DATE_LINE = "Sunday 22 November 2026"
PAPER = "THE WORLD IN ONE DAY"

HEROES = [
    {
        "kicker": "CLIMATE · ANTALYA, TÜRKIYE",
        "headline": "COP31 Talks Run Past Deadline Into Sunday, Final Package on the Table",
        "deck": ("Talks ran through Saturday night after Friday's deadline passed. President Kurum "
                 "tabled a package he says all can accept; objections closed at 03:00 GMT, plenary "
                 "at 06:00. Fossil fuels and adaptation finance are the hardest lines."),
        "source": "Reuters",
        "cert": "DEVELOPING",
        "region": "Europe",
        "art": "cop31",
    },
    {
        "kicker": "WAR · UKRAINE",
        "headline": "Russia's Mass Barrage: 400+ Drones and 110 Missiles Across Ukraine",
        "deck": ("Among the year's largest strikes: deaths in Kyiv, damage across seven regions. In "
                 "Kryvyi Rih, the president's home city, a 'triple-tap' — missiles, then drones on the "
                 "rescuers — killed a boy of seven and a paramedic, wounding about 60."),
        "source": "CNN · Al Jazeera · Ukr. Air Force",
        "cert": "CONFIRMED",
        "region": "Europe",
        "art": "ukraine",
    },
]

# Sections: (name, colour key, [stories]) — story = headline, source, cert, region, icon
SECTIONS = [
    ("WORLD", "world", [
        ("Bahrain: Iranian attack hits industrial facility; air defences intercept others", "Reuters", "CONFIRMED", "Middle East", "shield"),
        ("IRGC claims two US radar systems destroyed in Bahrain", "IRGC via Tasnim", "CLAIM", "Middle East", "radar"),
        ("Saudi Arabia intercepts three Houthi missiles", "Reuters · SPA", "REPORTED", "Middle East", "missile"),
        ("Tanker catches fire after striking a mine in the Strait of Hormuz", "UKMTO · Iran media", "REPORTED", "Middle East", "tanker"),
        ("Tehran claims a missile hit a US F-16 over Hormuz — not verified", "Iran state media", "CLAIM", "Middle East", "jet"),
        ("Russian cargo ship set ablaze by drones in Gulf of Finland; crew evacuated", "Al Jazeera", "CONFIRMED", "Europe", "ship"),
        ("Peru M6.8 quake: 152 homes uninhabitable as Lima residents flee", "USGS · local govt", "CONFIRMED", "Americas", "quake"),
        ("Mexico captures cartel leader 'El Chapo Isidro' in latest arrest", "Reuters", "CONFIRMED", "Americas", "badge"),
        ("Zelensky: timing of next peace talks rests on a US agenda for all sides", "Reuters", "REPORTED", "Europe", "dove"),
        ("Secret Hegseth memo curbs the US–Canada defence relationship", "Washington Post", "REPORTED", "Americas", "memo"),
    ]),
    ("MONEY & TECH", "money", [
        ("Wall Street rout: Nasdaq -5.28% in an AI-led sell-off (Fri close)", "Reuters", "CONFIRMED", "Americas", "chart"),
        ("EU and Indonesia officially sign 'ambitious' CEPA trade deal", "European Commission", "CONFIRMED", "Asia", "handshake"),
        ("Costa proposes a €1.78 trillion EU budget for 2028–2034", "Council draft", "REPORTED", "Europe", "coin"),
        ("Oil climbs on Hormuz risk: Brent ~$92.6, WTI ~$83.7 (Fri)", "Reuters", "CONFIRMED", "Middle East", "oil"),
        ("Gold slides 4.1% to $3,533 as margin calls bite; Bitcoin at $58.3k", "Market reports", "CONFIRMED", "Americas", "gold"),
    ]),
    ("SCIENCE & PLANET", "science", [
        ("Norway's Supreme Court rules climate-disputed oil licences invalid", "NTB", "CONFIRMED", "Europe", "leaf"),
        ("US military releases previously classified UFO footage", "US DoD reports", "REPORTED", "Americas", "ufo"),
        ("States aim for first rules on 'killer robots' by 2028", "UN talks reports", "REPORTED", "Europe", "robot"),
        ("Kenya discharges its last Ebola patient; DR Congo toll passes 5,300", "Health officials", "REPORTED", "Africa", "cross"),
    ]),
    ("SOCIETY & CULTURE", "society", [
        ("Manipur: 11 dead, 180+ hospitalised after drinking illicit alcohol", "Indian press", "CONFIRMED", "Asia", "bottle"),
        ("Nigeria: 24 bodies recovered after a boat capsizes, NEMA says", "NEMA", "CONFIRMED", "Africa", "boat"),
        ("Los Angeles jury convicts man of arson in Palisades wildfire retrial", "AP", "CONFIRMED", "Americas", "flame"),
        ("First time: Japan's SDF to use Indian ranges for live-fire training", "Asia Daily", "CONFIRMED", "Asia", "target"),
        ("Tens of thousands flock to Japan's mascot festival, 200 characters", "Japanese media", "CONFIRMED", "Asia", "mascot"),
    ]),
]

SPORT = [
    ("F1 Las Vegas: Verstappen on pole from Russell for the 04:00 UTC race", "Crash.net", "REPORTED", "Americas", "f1"),
    ("ATP Finals, Turin: Alcaraz to face Zverev in Sunday's title match", "BBC Sport", "CONFIRMED", "Europe", "tennis"),
    ("France beat Argentina to book a Nations final against the Springboks", "BBC Sport", "CONFIRMED", "Europe", "rugby"),
    ("Australia hold on for a narrow Nations Championship win over Wales", "BBC Sport", "CONFIRMED", "Oceania", "rugby"),
    ("Evanilson scores in a sixth straight game as Bournemouth beat Forest", "BBC Sport", "CONFIRMED", "Europe", "football"),
]

WIRE = [
    ("Zaporizhzhia struck by at least 12 glide bombs overnight", "Mapping reports", "REPORTED", "Europe"),
    ("Kharkiv drone strike injures 11 people, two of them children", "Regional govt", "CONFIRMED", "Europe"),
    ("Türkiye's state takes control of the last big independent news outlet", "Press reports", "REPORTED", "Europe"),
    ("Costa Concordia captain Schettino freed after serving his sentence", "Italian media", "CONFIRMED", "Europe"),
    ("Israel: Eisenkot pushes coalition talks as ex-PM refuses Netanyahu", "Israeli media", "REPORTED", "Middle East"),
]

# UTC timeline of the day, as reported (HH:MM UTC).
TIMELINE = [
    ("00:16", "Kharkiv drone hit, 11 hurt"),
    ("00:27", "Russian ship fired by drones"),
    ("01:05", "COP31 oil-gas row"),
    ("01:53", "Tehran F-16 claim"),
    ("02:15", "Peru: 152 homes lost"),
    ("02:47", "Glide bombs: Zaporizhzhia"),
    ("03:00", "COP31 objection deadline"),
    ("03:07", "Drones hit Dnipropetrovsk"),
    ("04:00", "Las Vegas GP lights out"),
    ("06:00", "COP31 plenary: deal vote"),
]

NUMBERS = [
    ("400+", "drones in barrage"),
    ("110", "missiles in strike"),
    ("6.8", "Peru quake magnitude"),
    ("$120bn", "adaptation finance"),
    ("-5.28%", "Nasdaq Friday close"),
    ("5,300+", "DR Congo Ebola toll"),
    ("24", "Nigeria capsize dead"),
    ("50", "Las Vegas GP laps"),
]


def all_stories():
    """Every counted story: heroes + section cards + sport + wire."""
    items = list(HEROES)
    for _name, _key, cards in SECTIONS:
        items.extend(cards)
    items.extend(SPORT)
    items.extend(WIRE)
    return items


def story_count():
    return len(all_stories())


def region_counts():
    counts = {}
    for s in all_stories():
        region = s["region"] if isinstance(s, dict) else s[3]
        counts[region] = counts.get(region, 0) + 1
    return counts


def cert_counts():
    counts = {}
    for s in all_stories():
        cert = s["cert"] if isinstance(s, dict) else s[2]
        counts[cert] = counts.get(cert, 0) + 1
    return counts
