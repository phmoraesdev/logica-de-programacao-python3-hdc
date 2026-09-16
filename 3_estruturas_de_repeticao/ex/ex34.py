# Exercicio 34: peça um numero e verifique se ele e primo, 
# contando quantos divisores ele possui
num = int(input("Digite um numero: "))

divisoes = 0
contador = num

while contador > 0:
    if num % contador == 0:
        divisoes = divisoes + 1    
    contador = contador - 1

if divisoes == 2:
    print(f"O numero: {num} e primo")
else:
    print(f"O numero: {num} nao e primo")