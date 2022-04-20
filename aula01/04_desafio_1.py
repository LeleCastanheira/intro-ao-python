# 1. Peça ao seu usuário para inserir 3 dados: nome, idade e cidade.

# 2. Imprima no console uma única mensagem desejando boas vindas ao usuário.

nome = input("Digite seu nome: ")
idade = input("Agora digite sua idade: ")
cidade = input("E por último digite sua cidade: ")
print("Seja bem vindo(a), {}, você tem {} anos e veio da cidade {}".format(nome, idade, cidade))