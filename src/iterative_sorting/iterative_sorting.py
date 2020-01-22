# TO-DO: Complete the selection_sort() function below

# [3,65,7,33,0]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_value = min(arr[i:])
        smallest_value_index = arr.index(smallest_value)
        arr[smallest_value_index], arr[i] = arr[i], arr[smallest_value_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    x = True
    while x:
        x = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                x = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


print(selection_sort([3, 65, 7, 33, 0]))
print(bubble_sort([3, 65, 7, 33, 0]))
