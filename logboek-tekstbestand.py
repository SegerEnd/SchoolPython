import os
import datetime

noList = ["nee","no","neen","nee sorry","nein"] #Een lijst met mogelijke nee antwoorden op vragen


stop = False

while stop == False :
    bestand = open("C:/Users/Gebruiker/Desktop/logboek.txt", "a")
    invoer = input("Schrijf een tekst die je in het logboek wilt zetten: ")
    bestand.write(str(datetime.datetime.now().ctime()) +" // ")
    bestand.write(str(invoer))
    bestand.write("\n")

    bestand.close()

    bestand = open("C:/Users/Gebruiker/Desktop/logboek.txt", "r")
    print(bestand.read())

    bestand.close()
    
    stoppen = input("Wilt u nog een regel in het logboek toevoegen? ").lower().replace(",", "")
    if stoppen in noList:
        stop == True
        break
