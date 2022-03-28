import datetime

datum = datetime.datetime.now()
jaar = datum.year

def leeftijdscheck():
    geboortejaar = input("Voer uw geboortejaar in: \n")

    leeftijd = int(jaar) - int(geboortejaar)

    if (leeftijd < 18):
        print("Je leeftijd is jonger dan 18. Klopt het dat je leeftijd",leeftijd,"is? \n")
    if (leeftijd >= 18):
        print("Je leeftijd ouder dan 18. Klopt het dat je leeftijd",leeftijd,"is? \n")

    print("Als deze fout is voer uw geboortejaar opnieuw in: \n")
    leeftijdscheck()

leeftijdscheck()
