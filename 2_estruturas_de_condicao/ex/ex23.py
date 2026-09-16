# Exercicio 23: peça um salario e diga se 
# e necessario pagar imposto de renda (acima de 1800)
salario = float(input("Entre com o valor do salario: "))

if salario > 1800:
    print("Valor acima de 1800, e necessario pagar imposto de renda")
else:
    print("Valor abaixo ou igual a 1800, nao e necessario pagar imposto de renda")
