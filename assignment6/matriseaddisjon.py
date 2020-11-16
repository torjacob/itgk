from random import randint

def main():
    A = random_matrise(4,3)
    print_matrise(A, 'A')
    B = random_matrise(3,4)
    print_matrise(B, 'B')
    C = random_matrise(3,4)
    print_matrise(C, 'C')
    D = adder_matrise(A,B)
    E = adder_matrise(B,C)
    print_matrise(E, 'B+C' )

# DEL 1
def random_matrise(x, y):
    a = []
    for i in range(x):
        b = []
        for j in range(y):
            b.append(randint(0, 9))
        a.append(b)
    return a

# DEL 2
def print_matrise(matrise, navn):
    print(navn, "=[")
    for i in range(len(matrise)):
        print(matrise[i])
    print("]")

# DEL 3
def adder_matrise(a, b):
    # c[x][y] = a[x][y] + b[x][y]
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        result = a # skal overskrives, brukes bare så jeg har dimensjonene
        for i in range(len(a)):
            for j in range(len(a[0])):
                result[i][j] = a[i][j] + b[i][j]
        return result
    else:
        print("Matrisene er ikke av samme dimensjon")

main()
