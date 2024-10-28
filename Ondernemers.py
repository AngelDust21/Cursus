import csv
from tabulate import tabulate

################################################################

def lees_facturen(bestand):
    """Lees facturen uit een CSV-bestand."""
    facturen = []
    with open(bestand, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            facturen.append(row)
    return facturen

################################################################

def toon_facturen(facturen):
    """Toon alle facturen in tabelvorm."""
    if facturen:
        print(tabulate(facturen, headers="keys", tablefmt="grid"))
    else:
        print("Geen facturen beschikbaar.")

################################################################

def voeg_factuur_toe(facturen):
    """Voeg een nieuwe factuur toe aan de lijst."""
    naam = input("Ondernemer naam: ")
    factuurnummer = input("Factuurnummer: ")
    bedrag = input("Bedrag: ")
    vervaldatum = input("Vervaldatum (YYYY-MM-DD): ")
    status = input("Status (Betaald/Onbetaald): ")
    betaalwijze = input("Betaalwijze (Contant/Bank): ")

    nieuwe_factuur = {
        "Ondernemer": naam,
        "Factuurnummer": factuurnummer,
        "Bedrag": bedrag,
        "Vervaldatum": vervaldatum,
        "Status": status,
        "Betaalwijze": betaalwijze
    }
    facturen.append(nieuwe_factuur)
    print(f"Factuur van {naam} toegevoegd.")

################################################################

def verwijder_factuur(facturen):
    """Verwijder een factuur van een specifieke ondernemer."""
    naam = input("Naam van de ondernemer om te verwijderen: ")
    factuur_gevonden = False
    for factuur in facturen:
        if factuur["Ondernemer"].lower() == naam.lower():
            facturen.remove(factuur)
            factuur_gevonden = True
            print(f"Factuur van {naam} verwijderd.")
            break
    if not factuur_gevonden:
        print(f"Geen factuur gevonden voor {naam}.")

################################################################

def schrijf_facturen(bestand, facturen):
    """Schrijf alle facturen terug naar het CSV-bestand."""
    veldnamen = ["Ondernemer", "Factuurnummer", "Bedrag", "Vervaldatum", "Status", "Betaalwijze"]
    with open(bestand, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=veldnamen)
        writer.writeheader()
        writer.writerows(facturen)

################################################################

# Start van het programma
bestand = 'facturen.csv'
facturen = lees_facturen(bestand)

# Toon huidige facturen
print("Huidige facturen:")
toon_facturen(facturen)

# Voeg nieuwe factuur toe
voeg_factuur_toe(facturen)
schrijf_facturen(bestand, facturen)
print("\nFacturen na toevoegen:")
toon_facturen(facturen)

# Verwijder een factuur
verwijder_factuur(facturen)
schrijf_facturen(bestand, facturen)
print("\nFacturen na verwijderen:")
toon_facturen(facturen)
