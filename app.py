# Módulo 1
from datetime import datetime
import random

print('--------------------Bem vindo a nossa empresa--------------------')
usuario = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
data_cadastro = datetime.now()
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
cartao = random.choice(cartoes)
data_aniversario = datetime.strptime(input('Informe data de aniversario dd/mm/aaaa: '), '%d/%m/%Y')

# Módulo 2
print(f'Olá {usuario}, seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}. Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}')
