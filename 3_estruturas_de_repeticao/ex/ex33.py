# Exercicio 33: peça numeros ao usuario repetidamente 
# e saia do loop com break quando ele digitar 0
i = 0

while i < 1:
    numero = int(input("Entre com um numero: "))
    print(numero)
    if numero == 0:
        print("Saindo do loop")
        break

