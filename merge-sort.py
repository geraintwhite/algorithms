import random


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    out = []
    p1 = p2 = 0
    while len(out) < len(left) + len(right):
        if left[p1] < right[p2]:
            out.append(left[p1])
            p1 += 1
        else:
            out.append(right[p2])
            p2 += 1
        if p1 == len(left) or p2 == len(right):
            out.extend(left[p1:] or right[p2:])
            break
    return out


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = int(len(arr) / 2)

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


arr = [i for i in range(100)]
random.shuffle(arr)
print(arr)
arr = merge_sort(arr)
print(arr)
