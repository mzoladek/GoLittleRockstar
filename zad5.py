def reverse_seq(n):
    lista = []
    for x in range(n, 0, -1):
        lista.append(x)
    return lista


wynik = reverse_seq(5)
print(wynik)