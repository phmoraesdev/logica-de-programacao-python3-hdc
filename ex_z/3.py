# Você recebe um número real R (0 < R <= 10000) representando o raio de um
# círculo, em uma única linha. Usando uma constante para o valor de PI
# (use 3.14159), calcule a área do círculo e imprima o resultado com
# exatamente 2 casas decimais, sem texto adicional.

r = float(input())
pi = 3.14159

a = pi * (r ** 2)

print(f"{a:.2f}")