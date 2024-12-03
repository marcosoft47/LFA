from copy import deepcopy
import random
from automatos import *

escolhasAutomatos = [caso1A, caso1B, caso1C, caso1D, caso2A,caso2B,caso2C,caso2D, completo]
semaforo = ["c2e", "c2b", "c2c", "c3c", "c3b", "c3d"]
semaforoEstado = False
pilha = 0
MAXIMOPILHA = 5

carros: list[Automato]
carros = []

nFim = 0
count = 0
fita = ''

def verificaSemaforo(estadoAtual:str, semaforo:list):
    '''
        Verifica se foi passado em um semáforo, se sim, empilha
    '''
    global pilha
    global semaforoEstado
    if estadoAtual in semaforo:
        pilha+=1
        print(f"empilhou: {pilha}")
        if pilha >= MAXIMOPILHA:
            print('Pilha cheia! Mudando o sinal do semáforo')
            pilha = 0
            semaforoEstado = not semaforoEstado

def informarCarros(auto:bool):
    count = 0
    print(f'Informe qual caso você quer usar no carro {count+1}:')
    print('1 - Caso 1A')
    print('2 - Caso 1B')
    print('3 - Caso 1C')
    print('4 - Caso 1D')
    print('5 - Caso 2A')
    print('6 - Caso 2B')
    print('7 - Caso 2C')
    print('8 - Caso 2C')
    print('9 - Caso Completo')
    print('0 - Fim escolhas')

    carros: list[Automato]
    carros = []
    while True:
        escolha = int(input(f'Escolha o caso para o carro {count+1}: '))
        if escolha == 0:
            break
        count += 1
        carros.append(deepcopy(escolhasAutomatos[escolha-1]))
        if escolha == len(escolhasAutomatos):
            escolha = input('Escolha qual será o estado inicial (A, B, C ou D): ')
            carros[-1].inicial = escolha.capitalize()
        if not auto:
            carros[-1].fita=input('Informe a fita do carro: ')
        carros[-1].nome = f'Carro {count}'
        print()
    return carros

print('Simulador automato com pilhas')
print('Deseja fazer um teste automático (e aleatório), ou manual?')
print('(1) Teste Manual\n(2) Teste automático')
escolha = int(input())

if escolha == 1:
    print('Teste Manual')
    
    carros = informarCarros(auto=False)
    print('Começando teste:')


    count = 0
    while True:
        print(f"Loop {count+1}")
        for i in carros:
            if i.finalizou:
                continue

            print(f'Carro atual: {i.nome} -> ', end='')

            if not i.fita[count] in i.alfabeto:
                print(f'Elemento {i.fita[count]} não pertence no alfabeto de {i.nome}')
                i.finalizou = True
                nFim += 1
                continue

            i.percorrer(i.fita[count])
            print(i.estadoAtual)

            if i.estadoAtual == None:
                print(f'Caminho inválido para o {i.nome}!')
                i.finalizou = True

            verificaSemaforo(i.estadoAtual, semaforo)
            if len(i.fita) <= count+1:
                print(f'Fim da fita do {i.nome}')
                i.finalizou = True
                nFim += 1
                continue
            if i.ehEstadoFinal():
                i.finalizou = True
                nFim += 1
                print('FIM')
        if nFim >= len(carros):
            break

        count += 1
        


elif escolha == 2:
    print('Teste automático')
    escolha = int(input('Definir automaticamente os casos?\n1 - Sim\n2 - Não\n'))

    if escolha == 1:
        qnt = int(input('Informe quantos carros você quer simular: '))
        for i in range(qnt):
            carros.append(deepcopy(random.choice(escolhasAutomatos)))
            print(f'Carro {i}: {carros[-1].nome}')
            carros[-1].nome = f'Carro {i}'
    elif escolha == 2:
        carros = informarCarros(auto=True)

    print()
    print()
    while True:
        count += 1
        print(f"Loop {count}")
        for i in carros:
            if i.ehEstadoFinal():
                continue
            print(f'Carro atual: {i.nome} -> ', end='')
            i.sorteiaCaminho()
            print(i.estadoAtual)
            verificaSemaforo(i.estadoAtual, semaforo)
            if i.ehEstadoFinal():
                nFim += 1
                print('FIM')
                break
        print(nFim)
        if nFim >= len(carros):
            break

    print('Fitas:')
    for i in carros:
        print(f'{i.nome}: {i.fita}')