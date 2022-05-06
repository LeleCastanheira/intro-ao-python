from datetime import datetime, date, time, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.

aniversario = input("Digite a data do seu próximo aniversário (dd/mm/aaaa): ")
data = datetime.strptime(aniversario, '%d/%m/%Y')
hoje = datetime.now()
calculo =  (data - hoje)
print(f"Faltam {calculo.days} dias para seu aniversário!")

pergunta_1 = str(input("Você gosta de aniversário? [sim/não] ")).strip().lower()[0]
pergunta_2 = str(input("Você pretente fazer uma festa de aniversário? [sim/não] ")).strip().lower()[0]

if (pergunta_1 == 's' and pergunta_2 == 's'):
  print("Você ganhará presentes porque gosta de aniversário e também fará uma festa")
else:
  print("Você não ganhará presentes")