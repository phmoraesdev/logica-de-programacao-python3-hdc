renda = float(input("Entre com a sua renda: "))
print(renda)

limite = 0

if renda < 2000:
    limite = 1000
elif renda < 4000:
    limite = 2000
elif renda < 10000:
    limite = 3000
elif renda > 10000:
    print("Voce precisa falar com o nosso gerente")
    limite = 3000

print(f"Parabens seu cartao foi aprovado e seu limite e de {limite}")