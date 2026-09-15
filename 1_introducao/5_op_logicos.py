# operadores LOGICOS combinam valores booleanos e retornam um booleano
# NOT, AND e OR sao os tres operadores logicos

# --- NOT: inverte o valor ---
# True -> False
# False -> True
verdadeiro = True
falso = False

print(not verdadeiro)  # False
print(not falso)  # True

# --- AND: se tiver 1 False, ja da False ---
# so da True se os DOIS lados forem True
a = 5
b = 10
c = 2
d = 8

print(a > b and c > d)  # False and False -> False
print(a > b and c < d)  # False and True  -> False
print(c < d and b < c)  # True  and False -> False
print(a < b and b > c)  # True  and True  -> True


# --- OR: se tiver 1 True, ja da True ---
# so da False se os DOIS lados forem False
print(a > b or c < d)  # False or True  -> True
print(c < d or b < c)  # True  or False -> True
print(a < b or b > c)  # True  or True  -> True
print(a > b or c > d)  # False or False -> False
