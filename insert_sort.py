def insert_sort(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2


lista = [1,2,3,4,5,6,7]
print(lista)

insert_sort(lista)
print(lista)