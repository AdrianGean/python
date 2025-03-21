
lista1 = [9,6,45,32]
lista2 = [8,9,6,58,32,68]


emcomum = []


for item in lista1:
    if item in lista2 and item not in emcomum:
       emcomum.append(item)


print("Elementos presentes em ambas as listas (sem repetição):", emcomum)