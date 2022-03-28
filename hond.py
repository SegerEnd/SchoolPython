class hond:
    def __init__(hond, name, age, blaf, ras):
        hond.name = name
        hond.age = age
        hond.blafg = blaf
        hond.ras = ras
    def blaf(hond):
        print(str(hond.blafg))
    def __str__(hond):
        return "Naam is:"+" "+hond.name+", zijn ras is: "+hond.ras+", zijn leeftijd is: "+str(hond.age)+" jaar"

list = []
list.append(hond("Sparkle", 2,"miauw","birmaan"))
list.append(hond("Fluffy", 4,"Blaf","Chihuahua"))
list.append(hond("Bezem", 7,"Woef Woef","Shiba"))

for hondobj in list:
    hondobj.blaf()
    print(hondobj)