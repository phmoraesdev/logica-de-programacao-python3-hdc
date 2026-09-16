# Exercicio 32: imprima os numeros de 20 ate 0, 
# mas interrompa o loop com break assim que chegar em 5
i = 20

while i >= 0:
    print(i)
    if i == 5:
        break
    i = i - 1

print("Pos loop")