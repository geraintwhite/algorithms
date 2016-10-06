import random


def bubble_sort(arr):
    comparisons = swaps = 0
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print('comparisons {}, swaps {}'.format(comparisons, swaps))

arr = [i for i in range(100)]
random.shuffle(arr)
print(arr)
bubble_sort(arr)
print(arr)
