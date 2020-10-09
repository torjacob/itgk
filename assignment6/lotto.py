from random import randint

numbers = []
for i in range(33):
    numbers.append(i+1)

myGuess = [2, 3, 5, 6, 8, 9, 31, 11, 7, 9]

def drawNumbers(numList, n = 7):
    resultList = []

    for i in range(n):
        n_random = randint(0, len(numList)-1)
        resultList.append(numList.pop(n_random))

    return resultList

def compList(a, b):
    lotto = set(a).intersection(b[0:6])
    tillegg = set(a).intersection(b[7:])
    return lotto, tillegg

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

def main(lottoNumbers, price):
    # Sammenlikner gjetta med tall som blir dratt i lotto
    returnedList = compList(drawNumbers(numbers), lottoNumbers)
    print(returnedList)
    # Finner hvor mange som var like for lottonummer og bonusnummer
    lottoHit = len(returnedList[0])
    bonusHit = len(returnedList[1])
    # Sjekker hvor mye spilleren har vunnet
    win = winnings(lottoHit, bonusHit)
    # Returnerer sum av Hva spiller har vunnet vs hva det kostet å spille
    return win - price

resultat = 0
for i in range(10000):
    resultat += main(myGuess, 5)

print(resultat)
