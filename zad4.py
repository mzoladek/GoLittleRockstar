def minimum(arr):
    min = arr[0]
    for x in range(0, len(arr)):
        if arr[x] < min:
            min = arr[x]
    return min


def maximum(arr):
    max = arr[0]
    for x in range(0, len(arr)):
        if arr[x] > max:
            max = arr[x]
    return max


lista = [42, 54, 65, 87, 0, -5]
minimalna = minimum(lista)
print(minimalna)
maksymalna = maximum(lista)
print(maksymalna)