notas = [5, 9, 7, 4, 8]
print(notas)

i = 0
soma_notas = 0

while i < 5:
    soma_notas = soma_notas + notas[i]
    i = i + 1
media = soma_notas / 5
print(f"A meida do aluno foi de {media} ")