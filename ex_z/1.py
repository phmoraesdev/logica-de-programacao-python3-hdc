# Você recebe um número inteiro N onde 0 <= N <= 100, seguido por outra
# linha de entrada que contém uma palavra W com comprimento L onde
# 1 <= L <= 50. Sua tarefa é imprimir N linhas com a palavra W. As linhas
# da sua saída não devem ter espaços à esquerda ou à direita. Suas linhas
# de saída não devem ter espaços em branco no início ou no fim.

n = int(input())
w = (input()).strip()

for i in range(n):
    print(w)