# Você é a professora de Ciências e está lançando as notas das alunas.
# Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.
alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]


# Comece o programa perguntando o nome da aluna.


# Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
# Notas abaixo de 60 devem ser impressas com a cor vermelha, e notas a partir de 90 devem ser
# impressas com a cor verde.
# Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.

import colorama
colorama.init()

def colorir_notas():
  for i, turma in enumerate(alunas):
    if nome == turma:
      if notas[i] < 60:
        print(f"Nota: " + colorama.Fore.RED + str(notas[i]) + colorama.Style.RESET_ALL)
      elif notas[i] >= 90:
        print(f"Nota: " + colorama.Fore.GREEN + str(notas[i]) + colorama.Style.RESET_ALL)
      else:
        print(f"Nota: {notas[i]}")

  
nome = input("Digite seu nome: ").strip().capitalize()
if nome in alunas:
  print(f"Aluna: {nome}")
  print(colorir_notas())
else:
  print(colorama.Fore.RED + "Erro: Aluna não encontrada." + colorama.Style.RESET_ALL)