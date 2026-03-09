def interpolation_search(arr, x):

    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:

        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1


lista = list(range(2, 101, 2))
print(interpolation_search(lista, 2))
print(interpolation_search(lista, 50))
print(interpolation_search(lista, 100))
