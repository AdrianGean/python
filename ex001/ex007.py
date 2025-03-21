
minha_tupla = (1, 2, 3, 4, 5)

try:
   
    minha_tupla[1] = 10  
except TypeError as e:
 
    print("Erro:", e)

print("A tupla continua inalterada:", minha_tupla)