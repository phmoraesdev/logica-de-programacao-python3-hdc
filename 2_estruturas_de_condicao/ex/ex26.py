# Exercicio 26: peça a categoria de um produto 
# (1, 2 ou 3) e imprima o tipo correspondente usando elif
cat = int(input("Digite a categoria do produto: "))

if cat == 1:
    print("O produto e uma bolsa")
elif cat == 2:
    print("O produto e um tenis")
elif cat == 3:
    print("O produto e uma mochila")
else:
    print("A categoria nao foi encontrada")