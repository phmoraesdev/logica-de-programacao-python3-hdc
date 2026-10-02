# Você recebe um número inteiro N onde -10^9 <= N <= 10^9, em uma única
# linha. Imprima "Positivo" se N > 0, "Negativo" se N < 0, ou "Zero" se
# N for igual a 0. Sem aspas, sem espaços extras.

n = int(input())

if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Zero")
