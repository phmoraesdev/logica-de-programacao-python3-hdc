idade = int(input("Qual a sau idade? "))

# if aninhado e quando temos um if dentro do outro
if idade >= 18:
    print("Voce pode entrar na balada")
    metodoDePagamento = input("Como voce vai pagar a entrada? ")
    if metodoDePagamento == "dinheiro":
        print("A fila do dinheiro e a numero 1")
    else:
        print("A fila de cartao e a numero 2")
else:
    print("Voce nao pode entrar na balada")
