saque = int(input("Digite quanto quer sacar: "))

nota1 = 0
nota10 = 0
nota20 = 0
nota50 = 0
nota100 = 0

while saque > 0:
    while saque >= 100:
        nota100 = nota100 + 1
        saque = saque - 100
    while saque >= 50:
        nota50 = nota50 + 1
        saque = saque - 50
    while saque >= 20:
        nota20 = nota20 + 1
        saque = saque - 20
    while saque >= 10:
        nota10 = nota10 + 1
        saque = saque - 10
    while saque >= 1:
        nota1 = nota1 + 1
        saque = saque - 1
        
print(f"""Voce vai receber {nota100} notas de R$100, 
{nota50} notas de R$50,
{nota20} notas de R$20,
{nota10} notas de R$10,
{nota1} notas de R$1,""")








