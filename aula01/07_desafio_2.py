# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora

# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.

# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.

cidade = str(input("Qual cidade você mora? ")).strip()
estado = str(input("E em qual estado você mora? ")).strip()
print("Você mora na cidade: " , cidade.upper())
print(f"Que fica no estado: {estado.upper()}")