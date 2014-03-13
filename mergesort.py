from quicksort import quick_sort


def merge_sort(list1, list2):

    output = []
    p1 = p2 = 0

    while p1 < len(list1) and p2 < len(list2):

        item1, item2 = list1[p1], list2[p2]

        if item1 < item2:
            output.append(item1)
            p1 += 1
        elif item2 < item1:
            output.append(item2)
            p2 += 1
        else:
            output.append(item1)
            p1 += 1
            p2 += 1

    if p1 == len(list1):
        output += list2[-(len(list2)-p2):]
    elif p2 == len(list2):
        output += list1[-(len(list1)-p2):]

    return output


if __name__ == '__main__':

    # list1 = input('Enter first list of items: ').split(',')
    # list2 = input('Enter second list of items: ').split(',')

    list1 = ['apple','damson','pear','orange','banana','plumb','carrot']
    list2 = ['cat','zebra','frog','dog','mouse']

    list1 = quick_sort(list1, 0, len(list1)-1)
    list2 = quick_sort(list2, 0, len(list2)-1)

    print(merge_sort(list1, list2))
