import random


def bubble_sort(arr):
    for i in range(len(arr) - 1, 2, -1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [i for i in range(10)]
random.shuffle(arr)
print(arr)
bubble_sort(arr)
print(arr)
