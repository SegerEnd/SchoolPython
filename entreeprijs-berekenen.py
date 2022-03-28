yesList = ["ja","yes","jawel","jazeker"] #Een lijst met mogelijke ja antwoorden op vragen
noList = ["nee","no","neen","nein","nope"] #Een lijst met mogelijke nee antwoorden op vragen
dagNameList = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag'] #Een lijst met namen van de week

prijs = 0 #Ik maak de variable prijs en zorg ervoor dat deze op 0 begint.

import datetime #Ik importeer datetime om de dag van de week te bepalen.

#Deze functie zorgt ervoor dat als je de naamvan de dag van de week invoert dat deze naar een getal word omgezet bijvoorbeeld dinsdag word 2.
def dagCalc():
        global dag #Dit doe ik zodat de variable dag ook buiten de functie beschikbaar is. 
        global dagNameList #Dit zorgt ervoor dat hij de global variable dagNameList heeft.
        
        #1.Systeem vraagt welke dag het is
        dag = input("Welke dag van de week is het? ").lower().capitalize() #2.Actor voert de dag van de week in #Het syteem vraagt welke dag van de week het is je kunt deze beantwoorden met 1 t/m 7 of maandag tot zondag en hij maakt ze eerst allemaal kleine letters en maakt daarna de eerste letter een hoofdletter.

        if dag.isdigit() == False: #Check als de ingevoerde waarde nit uit cijfers bestaat.
            if dag in dagNameList: #Kijk of de ingevoerde waarde overeenkomt met de dagNameList.
                if dag == 'Maandag': #Kijk de waarde dag overeenkomt met maandag.
                    dag = str(1) #Als deze overeenkomt mat Maandag dan maakt hij van de variable dag de string 1. Voor de volgende dagen geld hetzelfde.
                elif dag == 'Dinsdag':
                    dag = str(2)
                elif dag == 'Woensdag':
                    dag = str(3)
                elif dag == 'Donderdag':
                    dag = str(4)
                elif dag == 'Vrijdag':
                    dag = str(5)
                elif dag == 'Zaterdag':
                    dag = str(6)
                elif dag == 'Zondag':
                    dag = str(7)

            else: #Check als een waarde van dag niet overeenkomt met een woord uit dagNameList. ALs dit zo is geeft hij een foutmelding en begint hij de funcite dagCalc() opnieuw.
                print("\nEr is een een fout opgetreden! Er kon geen dag worden herkent aan uw opgegeven waarde!") #Ik gebruik \n dit op een nieuwe regel te printen.
                print("Probeer het opnieuw!\n")
                dagCalc() #Start de functie opnieuw

        elif dag.isnumeric(): #Check als de waarde van dag numeric is (uit alleen cijfers) bestaat.
            if int(dag) <= 0: #Als de waarde van dag 0 is of onder 0 dan geeft hij een foutmelding en roept hij de functie opnieuw aan.
                print("\nEr is een een fout opgetreden! Het getal kan niet kleiner zijn dan 1 (maandag)!")
                print("Probeer het opnieuw!\n")
                dagCalc() #roep de functie opnieuw aan
            elif int(dag) >= 8: #Als de waarde van dag 8 is of obven de 8 dan geeft hij een foutmelding en roept hij de functie opnieuw aan.
                print("\nEr is een een fout opgetreden! Het getal kan niet groter zijn dan 7 (zondag)!")
                print("Probeer het opnieuw!\n")
                dagCalc() #roep de functie opnieuw aan


print("Welkom bij het betaal/kassa systeem van het zwembad!\n") #Dit is de eerste regel die ik print zo weten ze dat ze het betaal/kassa systeem gebruiken

DagZelfInvoeren = str(input("Wilt u de dag zelf invoeren? Anders bepaalt het systeem de datum. ").lower()) #De computer vraagt of je zelf de dag in wilt voeren of dat deze door bepaalt word door je systeem tijd. Daarna maakt hij ze allemaal kleine letters.

if DagZelfInvoeren in yesList: #Chack als je de vraag beantwoord met Ja of elk ander woord uit de yesList. 
    dag = "undefined" #de variable dag bestaat in eerste instansie alwel maar word overschreven als je een dag invoert.

    dagCalc() #Ik roep de functie dagCalc aan om zo te beginnen met de functie en mensen de dag handmatig te laten kiezen.
    
    print("Jouw ingevoerde dag is: "+ str(dag) +" / "+ dagNameList[int(int(dag)-1)]) #Als de gebruiker een datum heeft gekozen print ik deze uit en zeg erbij welk getal de dag is en welke naam de dag is bijv: Maandag en het nummer van de dag bij maandag is deze 1.

elif DagZelfInvoeren in noList: #Check als de gebruiker met nee antwoord of een ander woord uit de noList 
    dag = str(datetime.datetime.today().weekday() + 1) #Dan maakt hij van de variable dag de dag van jouw systeem en doe ik plus 1 omdat python telt vanaf 0 maar bij mij begint maandag op 1.

    print("De bepaalde dag door het systeem is: "+ str(dag) +" / "+ dagNameList[int(int(dag)-1)]) #Daarna print ik de dag van het systeem net als bij de vorige zeg ik welk nummer de dag heeft dus maandag is nummer 1 en de naam van de dag is: Maandag.

else:
    print("\nEr is een een fout opgetreden! Graag deze vraag met Ja of Nee beantwoorden!")
    print("Voer het nu handmatig in!\n")
    dagCalc() #Als de gebruiker niet met ja of nee antwoord of een woord uit de yesList/noList dan print hij een foutmelding en roept hij de functie handmatig invullen aan.

    print("Jouw ingevoerde dag is: "+ str(dag) +" / "+ dagNameList[int(int(dag)-1)]) #Als je daarna de dag juist hebt ingevuld print hijdat ook weer net als de vorige 2 met de naam en het nummer van de dag.

#Ik maak de functie prijzen in deze functie word het prijs van de kaartjes voor het zwembad berekent.
def prijzen():
    global yesList #Ik zorg ervoor dat de variable yesList/noList/dag en prijs in de functie beschikbaar zijn.
    global noList
    global dag
    doordeweeks = ['1','2','3','4','5'] #Dit zijn alle cijfers die op werkdagen zijn zodat ik een werkdag tarief kan berekenen emt de variable dag want maandag '1', dinsdag = '2' etc.
    weekend = ['6','7'] #Dit is hetzelfde als de variable doordeweeks alleen hier geef ik aan dat '6' en '7' bij het weekende horen.
    global prijs
    
    localPrijs = 0 #Ik zet de variable localPrijs op 0. Deze variable is alleen in deze functie en dit zorgt ervoor dat ik de prijs voor deze persoon kan weergeven daarna doe ik prijs = localPrijs + prijs om de localPrijs weer op de 'totaalprijs' te zetten.

    abon = "undefined"  #de variable abon bestaat in eerste instansie alwel maar word overschreven als je een ja of nee antwoord op de vraag of je een abonnement hebt.
    
    #3.Systeem vraagt of de bezoeker een abonnement heeft (ja/nee)
    abon = input("\nHeeft u een abonnement? ").lower() #4.Actor voert in of de bezoeker een abonnement heeft 

    #Deze while loop is om te kijken of de gebruiker niet een ander woord invoert die niet in de yesList of noList staat.
    while abon not in yesList or noList: 
        if abon in yesList: #als de waarde van abon in de yesList staat dan stopt hij deze while loop.
            break
        elif abon in noList: #als de waarde van abon in de noList staat dan stopt hij deze while loop.
            break
        else: #Als hij de volgende keer weer niet in de yesList of noList staat dan word de gebruiker opnieuw gevraagd om hij/zij een abonnement heeft.
                print("\nEr is een fout opgetreden! Graag de vraag met Ja of Nee beantwoorden!")
                print("Probeer het opnieuw!\n")
                abon = input("\nHeeft u een abonnement? ").lower() #4.Actor voert in of de bezoeker een abonnement heeft.

    #5.Systeem vraagt wat de leeftijd vande bezoeker is.
    age = int(input("Wat is uw leeftijd? ")) #6.Actor voert de leeftijd in.

    #Een while loop om te kijken of de gebruiker in gevulde getal groter is dan 100 of kleiner is dan 0
    while age < 0 or age > 100:
        #Als het ingevulde getal groter is dan 100 en kleiner dan 0 geeft hij een foutmelding en vraagt hij opnieuw naar de leeftijd.
        print("\nEr is een fout opgetreden! De leeftijd moet boven de 0 en onder de 100 zijn!")
        print("Probeer het opnieuw!\n")
        age = int(input("Wat is uw leeftijd? "))
        

    #Weekend tarief
    #Kinderen tussen 7 en 12 die een abonnement hebben betalen 2,50 euro
    #Kinderen tussen 7 en 12 zonder abonnement betalen 5 euro
    #Kinderen tussen 13 en 18 met abonnement betalen 5 euro
    #Kinderen vanaf 12 zonder abonnement betalen 7,50 euro
    #Volwassenen met abonnement betalen 5,00
    #Volwassenen zonder abonnement betalen 7,50

    #Werkdagen tarief
    #Iedereen met een abonnement betaalt 2,50 euro
    #Zonder abonnement: 5 euro

    if abon in yesList: #Check als je de vraag of je een abonnement hebt beantwoord met aan woord uit de yesList. 
        if dag in weekend: #Check als de variable dag een weekend is.
            #Als dit zo is print hij weekend tarief en berekent hij de prijs met abonnement en weekend tarief aan de hand van je ingevulde leeftijd.
            print("\nWeekend tarief")
            if age < 7:
                localPrijs = localPrijs + 250
            if age >= 7 and age <= 12:
                localPrijs = localPrijs + 250
            elif age >= 13 and age < 18:
                localPrijs = localPrijs + 500
            elif age >= 18:
                localPrijs = localPrijs + 500
        elif dag in doordeweeks: #Check als je ingevoerde dag op een werkdag is
            #Als dit zo is print hij werkdag tarief en berkent hij de prijs van een kaartje voor het zwembad met werkdag tarief en abonnements tarief.
            print("\nWerkdag tarief")
            localPrijs = localPrijs + 250

    if abon in noList: #Check als je de vraag of je een abonnement hebt beantwoord met aan woord uit de noList. 
        if dag in weekend: #Check als de variable dag een weekend is.
            #Als dit zo is print hij weekend tarief en berekent hij de prijs zonder abonnement en weekend tarief aan de hand van je ingevulde leeftijd.
            print("\nWeekend tarief")
            if age < 7:
                localPrijs = localPrijs + 500
            elif age >= 7 and age < 12:
                localPrijs = localPrijs + 500
            elif age >= 12:
                localPrijs = localPrijs + 750
            elif age >= 18:
                localPrijs = localPrijs + 750
        elif dag in doordeweeks: #Check als je ingevoerde dag op een werkdag is
            #Als dit zo is print hij weekend tarief en berekent hij de prijs zonder abonnement en weekend tarief aan de hand van je ingevulde leeftijd.
            print("\nWerkdag tarief")
            localPrijs = localPrijs + 500

    #7.Systeem berekent de prijzen en geeft deze terug aan de gebruiker
    print("--------------------------------------")
    print("De prijs voor deze persoon is: €"+str(int(localPrijs)/100)) #Ik doe de localPrijs gedeeld door 100 omdat je ik in python geen decimalen ik kon typen.
    prijs = localPrijs + prijs
    totaalprijs = int(prijs)/100 #Ik doe de Prijs gedeeld door 100 omdat je ik in python geen decimalen ik kon typen.
    print("Uw totale prijs is: €" +str(totaalprijs)) #daarna print ik de prijs.

    #8.Systeem vraagt of de actor nog een bezoeker wil toevoegen
    toevoegen = str(input("\nWilt u nog een persoon toevoegen? ").lower())
    #9.Actor voert nee in
    if toevoegen in noList:
        #10.Systeem geeftde totaalprijsterug aan de gebruiker
        print("Uw totale prijs is €" +str(totaalprijs))
    #Actor voert ja in dan roept hij de functie prijzen() opnieuw aan
    if toevoegen in yesList:
        prijzen()
    while toevoegen not in noList or yesList:
        if toevoegen in yesList: #als de waarde van abon in de yesList staat dan stopt hij deze while loop.
            prijzen()
            break
        elif toevoegen in noList: #als de waarde van abon in de noList staat dan stopt hij deze while loop.
            #10.Systeem geeftde totaalprijsterug aan de gebruiker
            print("Uw totale prijs is €" +str(totaalprijs))
            break
        else: #Als je de vraag niet met een woord uit de yesList of de noList hebt ingevuld dan vraagt hij of je opnieuw de vraag kan beantwoorden.
            print("\nEr is een fout opgetreden! Graag de vraag met Ja of Nee beantwoorden!")
            print("Probeer het opnieuw!\n")
            toevoegen = str(input("\nWilt u nog een persoon toevoegen? ").lower())
                

#roep de functie prijzen aan
prijzen()
