# Exercicio 25: peça um numero maior que 10; 
# se estiver entre 10 e 20 multiplique por 2, 
# senao multiplique por 5 (condicionais aninhadas)
num = float(input("Entre com um numero: "))

if num > 10:
    if num < 20:
        print(f"O numero multiplicado por 2 da {num * 2:.0f}")
    else:
        print(f"O numero multiplicado por 5 da {num * 5:.0f}")
else:
    print("O numero tem que ser mair que 10")