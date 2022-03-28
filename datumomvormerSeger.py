#Ik vraag de gebruiker om zijn datum in te vullen.
datum = input("Voor een datum in met deze volgorde: Maand, Dag, Jaar:")

#Ik split de woorden in een array
split = datum.split()

#Ik print de datum naar Jaar, Dag, Maand waarbij [0] de maand is [1]: De dag en [0] de maand.
print("Uw datum is omgezet naar Jaar, Dag, Maand:",split[2], split[1], split[0])