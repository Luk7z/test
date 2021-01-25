""" *-----------------------------------------------------------------*
                  Este módulo é a entrada no sistema
     *----------------------------------------------------------------*
           Objetivo do Programa: Pesquisa de Hotel mais barato
"""
from datetime import date
from hotel2   import Taxa
#  Variáveis com valores fixos (Convenção: Todas as letras são maiúsculas)
REGULAR = "Regular".upper()
REWARD  = "Reward".upper()
"""
  *-------------------------------------------------------------------*
          Função para obter o dia da semana de uma determinada data
  *-------------------------------------------------------------------*
"""
def obtemDiaSemana(dataEntrada):
    DIAS = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]

    dataDDMMAA = dataEntrada.split('/')
    dia = int(dataDDMMAA[0])
    mes = int(dataDDMMAA[1])
    ano = int(dataDDMMAA[2])
    dataAlvo = date(year=ano, month=mes, day=dia)
    indice_da_semana = dataAlvo.weekday()           #Indice da semana
    dia_da_semana = DIAS[indice_da_semana]          #Dia da semana
    numero_do_dia_da_semana = dataAlvo.isoweekday() #Numero do dia da semana
    return numero_do_dia_da_semana

"""
   *-------------------------------------------------------------------*
                   Aqui inicia a lógica do programa
   *-------------------------------------------------------------------*
"""
listaDeDiasPesquisa =  []    #Lista com dias da semana solicitados pelo usuário (reserva)
#
tipoClienteMaiusculo = ""
entrada = input(" ")
entradaSplit = entrada.split(',')
entradaSeparada = [i.lstrip() for i in entradaSplit]
#
#  este looping de repetição garante a entrada correta do tipo de cliente
#
sentinela = False   #variável para controlar looping de repetição
#
while (sentinela == False):
    tipoClienteMaiusculo = entradaSeparada[0].upper()
    if (tipoClienteMaiusculo == REGULAR) or (tipoClienteMaiusculo == REWARD):
        sentinela = True
    else:
        entrada = input("Please enter a valid customer type and the required data: ")
        entradaSplit = entrada.split(',')
        entradaSeparada = [i.lstrip() for i in entradaSplit]
#
flag = False

#
# Este looping de repetição obtem lista com todas dias da semana requeridas
#
for item in entradaSeparada:
    if flag==True:
       indiceSemana = obtemDiaSemana(item)
       listaDeDiasPesquisa.append(indiceSemana)
    flag=True

#
tax = Taxa() #instanciar a classe Taxa
if  tipoClienteMaiusculo == REGULAR:
    tipo = 0
else:
    tipo = 1
print("The cheapest Hotel is: {}\n".format(tax.obtemTaxa(tipo,listaDeDiasPesquisa)))
print("*---------------------------------------------* ")
print("Thank you for using Miami Hotels network!")
print("*---------------------------------------------* \n")
