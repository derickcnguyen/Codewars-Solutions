database = [
    ("english", "Welcome"),
    ("czech", "Vitejte"),
    ("danish", "Velkomst"),
    ("dutch", "Welkom"),
    ("estonian", "Tere tulemast"),
    ("finnish", "Tervetuloa"),
    ("flemish", "Welgekomen"),
    ("french", "Bienvenue"),
    ("german", "Willkommen"),
    ("irish", "Failte"),
    ("italian", "Benvenuto"),
    ("latvian", "Gaidits"),
    ("lithuanian", "Laukiamas"),
    ("polish", "Witamy"),
    ("spanish", "Bienvenido"),
    ("swedish", "Valkommen"),
    ("welsh", "Croeso")
]

def greet(language):
    if str(language).isdigit():
        return 'Welcome'
    language_lower = language.lower()
    for lang, greeting in database:
        if lang == language_lower:
            return greeting
    return "Welcome"
