def evenoneven():
    getal = int(input("Voer een getal in: "))  
    if (getal % 2) == 0:  
       print("{0} is een even getal \n".format(getal))
    else:  
       print("{0} is een oneven getal \n".format(getal))

    print("Nog een keer proberen?")
    evenoneven()

evenoneven()

x = len(evenoneven)

print(x)
