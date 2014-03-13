def quick_sort(items, first, last):

    if last > first:
        p = first
        kp = last

        while not p == kp:

            if ((p > kp and items[p] > items[kp])
                or (kp > p and items[kp] > items[p])):

                item = items[p]

                items[p] = items[kp]
                items[kp] = item

            if p > kp:
                p -= 1
            elif kp > p:
                p += 1

        items = quick_sort(items, first, p-1)
        items = quick_sort(items, p+1, last)

    return items[::-1]


if __name__ == '__main__':

    # items = input('Enter list of items: ').split(',')
    items = ['dog','frog','sheep','pig','leopard','lion','cheetah','steve']
    print(quick_sort(items, 0, len(items)-1))
