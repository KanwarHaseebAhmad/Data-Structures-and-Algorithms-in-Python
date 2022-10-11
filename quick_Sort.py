def quick_sort(list_a):
    length = len(list_a)

    if length <= 1:
        return list_a
    else:
        pivot = list_a.pop()


    items_greater = []
    items_lower = []

    for item in list_a:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([8,4,7,5,6,3,4,1,2,0]))
