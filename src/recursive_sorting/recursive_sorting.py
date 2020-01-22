# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    merged_arr = []
    lft = 0
    rt = 0

    while lft < len(arrA) and rt < len(arrB):
        # if the right index value greater than the left index value
        # push left side to the merged array
        # increment the left index
        # else
        # push the right index value
        # increment the right index
        if arrA[lft] < arrB[rt]:
            merged_arr.append(arrA[lft])
            lft += 1
        else:
            merged_arr.append(arrB[rt])
            rt += 1
    while lft < len(arrA):
        # push left index value to merged arr
        # increment the index value
        merged_arr.append(arrA[lft])
        lft += 1
    while rt < len(arrB):
          # push right index value to the merged arr
          # increment the index
        merged_arr.append(arrB[rt])
        rt += 1
    return merged_arr

# [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # is the array len 1
    if len(arr) <= 1:
        return arr

    # take an arb mid point
    index_split = len(arr) // 2
    # create a left and right side
    left_side = merge_sort(arr[:index_split])
    right_side = merge_sort(arr[index_split:])
    return(merge(left_side, right_side))


print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
