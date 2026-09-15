num = float(input("Entre com um numero: "))

if num > 10:
    if num < 20:
        print(f"O numero multiplicado por 2 da {num * 2:.0f}")
    else:
        print(f"O numero multiplicado por 5 da {num * 5:.0f}")
else:
    print("O numero tem que ser mair que 10")