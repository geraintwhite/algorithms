import random


def quick_sort(arr, start=None, end=None):
    start = 0 if start is None else start
    end = len(arr) - 1 if end is None else end

    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i+1]
    arr[i+1] = arr[end]
    arr[end] = temp

    return i+1


arr = [i for i in range(100)]
random.shuffle(arr)
print(arr)
quick_sort(arr)
print(arr)
