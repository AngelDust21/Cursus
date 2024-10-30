from tabulate import tabulate

# Python Data Types: Differences and Similarities
data = [
    ["Kenmerk", "Tuple", "Lijst", "Set", "Dictionary", "String"],
    ["Orde", "Geordend", "Geordend", "Ongeordend", "Ongeordend (behoudt invoervolgorde)", "Geordend"],
    ["Wijzigbaarheid", "Niet wijzigbaar (immutable)", "Wijzigbaar (mutable)", "Wijzigbaar (mutable)", "Wijzigbaar (mutable)", "Niet wijzigbaar (immutable)"],
    ["Duplicaten", "Toegestaan", "Toegestaan", "Niet toegestaan", "Sleutels: niet toegestaan, Waarden: toegestaan", "Toegestaan"],
    ["Toegang", "Index-gebaseerd", "Index-gebaseerd", "Lidmaatschapstest (met `in`)", "Sleutel-gebaseerd", "Index-gebaseerd"],
    ["Gebruiksscenario", "Constante gegevens (coördinaten)", "Gegevens die vaak wijzigen", "Unieke items (bijv. tags)", "Gegevens op basis van sleutel-waarde (bijv. contactgegevens)", "Tekst manipulatie"],
    ["Syntax", "(item1, item2)", "[item1, item2]", "{item1, item2}", "{\"key1\": \"value1\"}", "\"tekst\" of 'tekst'"],
    ["Indexering", "Ja", "Ja", "Nee", "Ja (op basis van sleutels)", "Ja"],
    ["Bewerkingen", "Concatenatie, slicing", "Toevoegen, verwijderen, sorteren", "Toevoegen, verwijderen", "Toevoegen, opvragen, verwijderen", "Concatenatie, slicing"],
    ["Gebruik als Sleutel in Dictionary", "Ja", "Nee", "Ja", "Nee", "Ja (als het kort is)"],
    ["Kan zowel Key als Value zijn", "Ja", "Nee", "Nee", "Nee", "Ja"],
    ["Kan alleen als Key zijn", "Ja", "Nee", "Nee", "Nee", "Ja"],
    ["Kan alleen als Value zijn", "Nee", "Ja", "Ja", "Ja", "Nee"],
    ["Iterabiliteit", "Ja", "Ja", "Ja", "Ja (keys, values, items)", "Ja"],
    ["Type van Gegevens", "Gemengd", "Gemengd", "Uniek en immutable", "Sleutels: immutable, Waarden: gemengd", "Tekst (karakters)"],
    ["Gebruik van Geheugen", "Efficiënt (immutable)", "Meer geheugen (mutable)", "Gemiddeld", "Gemiddeld", "Efficiënt (immutable)"],
    ["Prestatie (Toegangstijd)", "O(1) (indexering)", "O(1) (indexering)", "O(1) (gemiddeld, lidmaatschap)", "O(1) (gemiddeld, sleutel)", "O(1) (indexering)"],
    ["Hernoemen/Index Manipulatie", "Nee", "Ja", "Nee", "Nee", "Nee"],
    ["Typeveiligheid", "Geen beperkingen, gemengd", "Geen beperkingen, gemengd", "Uniek en immutable", "Sleutels: immutable, Waarden: gemengd", "Enkel tekens"] ,
    ["Toepasselijkheid in Functioneel Programmeren", "Ja", "Beperkt (mutable)", "Beperkt (mutable)", "Beperkt (mutable)", "Ja"]
]

# Converteer de gegevens naar een tabel en print deze
tabel = tabulate(data, headers="firstrow", tablefmt="grid")
print(tabel)

# Voorbeeldresultaat
# +-----------------------------------------+----------------------------+-----------------------+--------------------+------------------------------------------+-----------------------+
# | Kenmerk                                 | Tuple                      | Lijst                 | Set                | Dictionary                               | String                |
# +-----------------------------------------+----------------------------+-----------------------+--------------------+------------------------------------------+-----------------------+
# | Orde                                    | Geordend                   | Geordend              | Ongeordend         | Ongeordend (behoudt invoervolgorde)      | Geordend              |
# | Wijzigbaarheid                          | Niet wijzigbaar (immutable)| Wijzigbaar (mutable)  | Wijzigbaar (mutable)| Wijzigbaar (mutable)                     | Niet wijzigbaar       |
# |                                         |                            |                       |                    |                                          | (immutable)           |
# | Duplicaten                              | Toegestaan                 | Toegestaan            | Niet toegestaan    | Sleutels: niet toegestaan, Waarden:      | Toegestaan            |
# |                                         |                            |                       |                    | toegestaan                                |                       |
# | Toegang                                 | Index-gebaseerd            | Index-gebaseerd       | Lidmaatschapstest  | Sleutel-gebaseerd                        | Index-gebaseerd       |
# |                                         |                            |                       | (met `in`)         |                                          |                       |
# | Gebruiksscenario                        | Constante gegevens         | Gegevens die vaak     | Unieke items       | Gegevens op basis van sleutel-waarde     | Tekst manipulatie     |
# |                                         | (coördinaten)             | wijzigen              | (bijv. tags)       | (bijv. contactgegevens)                  |                       |
# | Syntax                                  | (item1, item2)             | [item1, item2]        | {item1, item2}     | {"key1": "value1"}                      | "tekst" of 'tekst'   |
# | Indexering                              | Ja                         | Ja                    | Nee                | Ja (op basis van sleutels)               | Ja                    |
# | Bewerkingen                             | Concatenatie, slicing      | Toevoegen, verwijderen| Toevoegen,         | Toevoegen, opvragen, verwijderen         | Concatenatie, slicing |
# |                                         |                            | sorteren              | verwijderen        |                                          |                       |
# | Gebruik als Sleutel in                  | Ja                         | Nee                   | Ja                 | Nee                                      | Ja (als het kort is)  |
# | Dictionary                              |                            |                       |                    |                                          |                       |
# | Kan zowel Key als Value zijn            | Ja                         | Nee                   | Nee                | Nee                                      | Ja                    |
# | Kan alleen als Key zijn                 | Ja                         | Nee                   | Nee                | Nee                                      | Ja                    |
# | Kan alleen als Value zijn               | Nee                        | Ja                    | Ja                 | Ja                                       | Nee                   |
# | Iterabiliteit                           | Ja                         | Ja                    | Ja                 | Ja (keys, values, items)                 | Ja                    |
# | Type van Gegevens                       | Gemengd                    | Gemengd               | Uniek en immutable | Sleutels: immutable, Waarden: gemengd    | Tekst (karakters)     |
# | Gebruik van Geheugen                    | Efficiënt (immutable)      | Meer geheugen         | Gemiddeld          | Gemiddeld                                | Efficiënt (immutable) |
# |                                         |                            | (mutable)             |                    |                                          |                       |
# | Prestatie (Toegangstijd)                | O(1) (indexering)          | O(1) (indexering)     | O(1) (gemiddeld,   | O(1) (gemiddeld, sleutel)               | O(1) (indexering)     |
# |                                         |                            |                       | lidmaatschap)      |                                          |                       |
# | Hernoemen/Index Manipulatie             | Nee                        | Ja                    | Nee                | Nee                                      | Nee                   |
# | Typeveiligheid                          | Geen beperkingen, gemengd  | Geen beperkingen,     | Uniek en immutable | Sleutels: immutable, Waarden: gemengd    | Enkel tekens          |
# |                                         |                            | gemengd               |                    |                                          |                       |
# | Toepasselijkheid in Functioneel         | Ja                         | Beperkt (mutable)     | Beperkt (mutable)  | Beperkt (mutable)                        | Ja                    |
# | Programmeren                            |                            |                       |                    |                                          |                       |
# +-----------------------------------------+----------------------------+-----------------------+--------------------+------------------------------------------+-----------------------+
