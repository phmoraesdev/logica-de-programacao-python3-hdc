# o Interrompe o loop imediatamente, 
# mesmo que a condição ainda seja verdadeira
numero = 0

while numero < 10:
    print(numero)
    if numero == 5:
        break
    numero = numero + 1

print("Apos o numero!")