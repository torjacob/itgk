# a)
def concatinate(a, b):
    return a + " " + b

# b)
def cat_from_list(strings):
    cat = ""
    for string in strings:
        cat += string
    return cat

# c)
def print_first_letter(strings):
    for string in strings:
        print(string[0])

# d)
'''
Hva vil kodesnutten under skrive ut til skjerm?

    def func1(liste):
        streng = ""
        for s in liste:
            if len(s)>3:
                streng += s[3]
        return streng

    def func2(streng):
        streng += streng
        return streng

    print(func2(func1(["Klabert","Oslo","Tur","stubbe"])))
 '''
# Denne kodeblokken burde skrive "bobbob" til skjermen.
# func2 dobbler en streng
# func1 plukker fjerde bokstav av strenger i en liste og lager en streng
