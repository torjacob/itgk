liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]

# DEL 1
def bubble_sort(array):
    while True:
        if array != array.sort():
            for i in range(len(array) - 1):
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
        return array

print(bubble_sort(liste))

# DEL 2
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
           if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
    return array

print(selection_sort(liste))

# DEL 3
# bubble er tregere enn selection, men ogsaa mer stabil
