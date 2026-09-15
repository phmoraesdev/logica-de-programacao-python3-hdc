# strings dinamicas: formas de encaixar valores de variaveis dentro de um texto
# existem 3 formas, da mais antiga pra mais atual

name = "Pedro"
# antigo: %s (string) dentro do texto, valor vem depois com %
print("Ola, meu nome e %s" % name)
# %s = String
# %d = Decimal integer
# %f = Float

# no meio: {} dentro do texto, valor vem com .format()
print("Ola, meu nome e {}".format(name))

# atual: f-string, a variavel vai direto dentro de {}
print(f"Ola, meu nome e {name}")

# --- f-string com float: casas decimais ---
pi = 3.141592653589793

# ":.2f" depois da variavel = 2 casas decimais (float)
print(f"O valor de pi e {pi:.2f}")

# a mesma coisa no formato antigo
print("O valor de pi e %.2f" % pi)
