import csv
from tabulate import tabulate

################################################################

def lees_facturen_csv(bestand):
    afacturen = []
    try:
        with open(bestand, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                afacturen.append(row)
   

################################################################

def toon_ondernemers(ondernemers):
    if ondernemers:
        print(tabulate(ondernemers, headers="keys", tablefmt="fancy_grid"))
    else:
        print("Geen facturen beschikbaar om weer te geven.")

################################################################

def schrijf_facturen_naar_csv(bestand, facturen):
    veldnamen = ["Ondernemer", "Factuurnummer", "Bedrag", "Vervaldatum", "Status", "Betaalwijze"]
    with open(bestand, mode='w', newline='', encoding='utf-8') as zfile:
        writer = csv.DictWriter(zfile, fieldnames=veldnamen)
        writer.writeheader()
        writer.writerows(facturen)

################################################################

def voeg_facturen_toe(bfacturen):
    try:
        naam = input("Voer naam in: ")
        fac = int(input("Voer factuurnummer in: "))
        beb = float(input("Voer bedrag in: "))
        ver = input("Voer vervaldatum in (bijv. 2024-01-01): ")
        stat = input("Voer betaalstatus in (bijv. Onbetaald of Betaald): ")
        beta = input("Voer betaalwijze in (bijv. Contant of Bank): ")
        nieuw_factuur = {
            "Ondernemer": naam, "Factuurnummer": fac, "Bedrag": beb, "Vervaldatum": ver, "Status": stat, "Betaalwijze": beta
        }
        bfacturen.append(nieuw_factuur)
        print(f"Factuur {naam} is toegevoegd.")
        schrijf_facturen_naar_csv('facturen.csv', bfacturen)  # Directe update van de CSV
    except ValueError:
        print("Foutieve invoer. Zorg ervoor dat de ingevoerde gegevens juist zijn.")

################################################################

def verwijder_ondernemer(cfacturen):
    onder = input("Voer ondernemer in (of deel van de naam): ")
    for info_fac in cfacturen:
        if onder.lower() in info_fac["Ondernemer"].lower():
            cfacturen.remove(info_fac)
            print(f"Ondernemer {info_fac['Ondernemer']} is verwijderd.")
            schrijf_facturen_naar_csv('facturen.csv', cfacturen)  # Directe update van de CSV
            return
    print(f"Ondernemer {onder} niet gevonden.")

################################################################

def sorteer_op_fac_nummer(facturen):
    try:
        facturen.sort(
            key=lambda fac: int(fac["Factuurnummer"].strip()) if fac["Factuurnummer"].strip().isdigit() else float('inf'),
            reverse=True
        )
        print("\nFacturen gesorteerd op Factuurnummer (aflopend):")
        print(tabulate(facturen, headers="keys", tablefmt="fancy_grid"))
        schrijf_facturen_naar_csv('facturen.csv', facturen)  # Directe update van de CSV
    except ValueError as e:
        print(f"Er is een probleem bij het sorteren van factuurnummers: {e}")

################################################################

def bereken_bedrag_gemiddelde(facturen):
    try:
        totale_som = sum(float(factuur["Bedrag"]) for factuur in facturen if "Bedrag" in factuur and factuur["Bedrag"])
        aantal_facturen = len([factuur for factuur in facturen if "Bedrag" in factuur and factuur["Bedrag"]])
        fac_gemiddelde = totale_som / aantal_facturen if aantal_facturen else 0
        print(f"\nGemiddelde bedrag van alle facturen: {fac_gemiddelde:.2f}")
    except ValueError:
        print("Er is een probleem bij het berekenen van het gemiddelde bedrag.")

################################################################

# Voer de functies in de juiste volgorde uit

# Stap 1: Lees de facturen uit het CSV-bestand
facturen = lees_facturen_csv('facturen.csv')

# Stap 2: Toon de ingelezen facturen en het gemiddelde bedrag
print("\nOorspronkelijke facturen:")
toon_ondernemers(facturen)
bereken_bedrag_gemiddelde(facturen)

# Stap 3: Voeg een nieuwe factuur toe
voeg_facturen_toe(facturen)
print("\nFacturen na toevoegen van een nieuwe factuur:")
toon_ondernemers(facturen)

# Stap 4: Verwijder een ondernemer
verwijder_ondernemer(facturen)
print("\nFacturen na verwijderen van een ondernemer:")
toon_ondernemers(facturen)

# Stap 5: Sorteer de facturen op Factuurnummer en toon de gesorteerde lijst
sorteer_op_fac_nummer(facturen)
