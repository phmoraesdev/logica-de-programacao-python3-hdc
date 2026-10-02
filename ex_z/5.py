# Você recebe um número inteiro N onde 1 <= N <= 10^6. Para cada regra
# abaixo, decida e imprima uma única linha:
# - Se N for divisível por 3 e por 5 ao mesmo tempo, imprima "FizzBuzz".
# - Se for divisível só por 3, imprima "Fizz".
# - Se for divisível só por 5, imprima "Buzz".
# - Caso contrário, imprima o próprio número N.

n = int(input())

if (n % 3 == 0) and (n % 5 == 0):
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)