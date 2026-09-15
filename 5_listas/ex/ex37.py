# crie uma lsita com 5 valores zerados
# faca um loop para percorrer a lista e preencha os valores zerados
# os valores devem ser inseridos pelo usuario
# imprima o resultao final com print

lista = [0, 0, 0, 0, 0]

print(lista)

i = 0

while i < 5:
    numero = int(input(f"Digite um numero {i}: "))
    lista[i] = numero
    i = i + 1

print(lista)

