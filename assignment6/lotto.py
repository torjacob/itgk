from random import randint

# DEL 1
numbers = []
for i in range(33):
    numbers.append(i+1)

# DEL 2
myGuess = [2, 3, 5, 6, 8, 9, 31, 11, 7, 9]

# DEL 3
def drawNumbers(numList, n = 7):
    resultList = []

    for i in range(n):
        n_random = randint(0, len(numList)-1)
        resultList.append(numList.pop(n_random))

    return resultList

# DEL 3
def compList(a, b):
    lotto = set(a).intersection(b[0:6])
    tillegg = set(a).intersection(b[7:])
    return lotto, tillegg

# DEL 4
def winnings(alike, bonus = 0):
    d = {
        #  KEY    VALUE
        7      : 2749455,
        (6, 1) : 102110,
        6      : 3385,
        5      : 95,
        (4, 1) : 45
    }

    if bonus == 0:
        key = alike
    else:
        key = (alike, bonus)

    if key in d:
        return d[key]
    else:
        return 0

# DEL 4
def main(lottoNumbers, price):
    combinedReturn = compList(drawNumbers(numbers), lottoNumbers)
    lottoRetun = len(combinedReturn[0])
    bonusReturn = len(combinedReturn[1])
    win = winnings(lottoRetun, bonusReturn)
    return win - price

# DEL 5
totalWin = 0
for i in range(1000000):
    numbers = []
    for i in range(33):
        numbers.append(i+1)

    thisWin = main(myGuess, 5)
    if thisWin > 40:
        print("Storgevinst!: ", thisWin)
    totalWin += thisWin

print(totalWin)
