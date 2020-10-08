# Imports
from sys import exit

# Globals
N_WOMEN = 0 
N_MEN = 0 
N_SUB = 0 
N_ITGK = 0 
AGE = -1
HOURS = []

class Question:
    def __init__(self, t, q, a, alt = "", e = ""):
        self.t = t
        self.q = q
        self.a = a
        self.alt = alt
        self.e = e

# Spørsmål, inkludert type på svar, og placeholder for svaret
QUESTIONS = [
    Question(str, "Hvilket kjønn er du? [m/f]: ", ""),
    Question(int, "Hvor gammer er du?: ", -1, "", "Du kan desverre ikke ta denne undersøkelsen."),
    Question(bool,"Tar du ett eller flere fag? [ja/nei]: ", False),
    Question(bool,"Tar du ITGK? [ja/nei]: ", False, "Tar virkelig *du* ITGK? [ja/nei]: "),
    Question(int, "Hvor mange timer bruker du daglig (i snitt) på lekser?: ", -1)
]

# Functions
def check_type(question):
    
    # Sender spørsmålet til riktig read funkskjon
    if question.t == str:
        read_str(question)
    elif question.t == bool:
        read_bool(question)
    elif question.t == int:
        read_int(question)
    
    
def read_str(q):
    global N_WOMEN, N_MEN
    
    q.a = str(input(q.q))
    
    if q.a.lower() == "mann" or q.a.lower() == "m":
        N_MEN += 1
    elif q.a.lower() == "kvinne" or q.a.lower() == "f":
        N_WOMEN +=1
    elif q.a.lower() == "hade":
        write_stats()
    else:
        print("Svar ikke innenfor parametrene")
        read_str(q)        

def read_bool(q):
    global N_ITGK, N_SUB
    
    q.a = str(input(q.q))
    
    if q.a.lower() == "ja" or q.a.lower() == "j":
        if len(q.alt) > 0:
            N_ITGK += 1
        else:
            N_SUB += 1
             
    elif q.a.lower() == "nei" or q.a.lower() == "n":
        if len(q.alt) > 0:
            return
        else:
            main()
    elif q.a.lower() == "hade":
        write_stats()
    else:
        print("Svar ikke innenfor parametrene")
        read_bool(q)
    

def read_int(q):
    global AGE, HOURS
    
    q.a = input(q.q)
    
    if q.a.lower() == "hade":
        write_stats()

    if int(AGE) == -1:
        AGE = q.a
        if int(AGE) > 25 or int(AGE) < 18:
            print(q.e)
            mai|n()
    else:
        HOURS.append(int(q.a))

def write_stats():
    global N_WOMEN, N_MEN, N_SUB, N_ITGK, HOURS
   
    average = sum(HOURS) / len(HOURS)

    print("Antall kvinner: ", N_WOMEN)
    print("Antall menn: ", N_MEN)
    print("Antall personer som tar fag: ", N_SUB)
    print("Antall personer som tar itgk: ", N_ITGK)
    print("Antall timer brukt i snitt på lekser: ", average)

    exit()

# Main Logic
def main():
    global AGE
    while True:
        print("")
        print("Velkommen til spørreundersøkelsen!")
        AGE = -1 # reverserer til -1 så alder ikke legges til HOURS array
        for i in range(len(QUESTIONS)):
            check_type(QUESTIONS[i])
            if str(QUESTIONS[i].a).lower() == "hade":
                write_stats()

# RUNIT
main()
