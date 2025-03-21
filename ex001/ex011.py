
numeros = []

quantidade = int(input("Quantos números deseja inserir? "))


for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)


numeros_pares = []
for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)

if numeros_pares:
    soma = 0
    for num in numeros_pares:
        soma += num
    media_pares = soma / len(numeros_pares)
    print(f"Média dos números pares: {media_pares:.2f}")
else:
    print("Não há números pares na lista.")