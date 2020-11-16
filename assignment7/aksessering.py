# a)
def split_string(a):
    for char in a:
        print(char)

# b)
def third_letter(string):
    if len(string) >= 3:
        letter = list(string)[2]
        return letter
    else:
        return "q"

# c)
def largest_index_string(string):
    return len(string) - 1
