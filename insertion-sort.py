import random


def insertion_sort(arr):
    for pos, element in enumerate(arr):
        while pos > 0 and arr[pos-1] > element:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = element


arr = [i for i in range(10)]
random.shuffle(arr)
print(arr)
insertion_sort(arr)
print(arr)
