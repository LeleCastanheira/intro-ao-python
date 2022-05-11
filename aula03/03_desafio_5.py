# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).


# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.

lista = list(range(1,61)) 

print("======= ↔ =====")
print(" Índice ↔ Item ")
print("======= ↔ =====")

for indice, item in enumerate(lista):
    if indice % 2 == 0:
        print(f'   {indice:2}   ↔  {item:2} ')