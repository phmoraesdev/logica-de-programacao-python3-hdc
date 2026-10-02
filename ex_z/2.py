# Você recebe dois números inteiros A e B, cada um em uma linha, onde
# -1000 <= A, B <= 1000. Troque os valores de A e B SEM usar uma terceira
# variável auxiliar, e imprima os dois valores trocados, um por linha,
# na ordem (novo A, novo B).

a = int(input(""))
b = int(input(""))

a = a + b
b = a - b
a = a - b

print(a)
print(b)