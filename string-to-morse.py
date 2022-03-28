#Ik maak een functie genaamd main
def main():
    words = input("\nVul een woord in om deze naar morse te vertalen: ")
    words = words.upper() #.Upper() zorgt ervoor dat alle letters in de string in hoofdletters komen te staan.
    table = char_to_dots()

    i = 0

    try:
        while (i < len(words)):
            if (words[i] != " "):
                print(table[words[i]], end = " ")
            else:
                print("/", end = " ")
            i += 1 #Dit is nodig omdat anders hij het de hele tijd herhaalt.
    except:
        print("\nInvalid characters found - refer to morse code alphabet")

    #ik start de functie opnieuw zodat je hem niet op de run moet klikken.
    main()

def char_to_dots():
    char_to_dots = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',

  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',

  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',

  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',

  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',

  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',

  '6': '-....', '7': '--...', '8': '---..', '9': '----.',

  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',

  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',

  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'}

    return char_to_dots


main()
