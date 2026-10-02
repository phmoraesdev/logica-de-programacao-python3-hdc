# Exercicio 37: crie uma lista com 5 valores zerados e, 
# usando um loop, preencha cada posicao com um valor
# digitado pelo usuario; ao final, imprima a lista resultante
lista = [0, 0, 0, 0, 0]

print(lista)

i = 0

while i < 5:
    numero = int(input(f"Digite um numero {i}: "))
    lista[i] = numero
    i = i + 1

print(lista)

