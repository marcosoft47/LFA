import random

quintupla ={
    'alfabeto': ["c","b", "e", "d", "p"],
    'estados': ["A", "B", "C", "D", "c1c", "c1b", "c1e", "c2e", "c2b", "c2c", "c3c", "c3b", "c3d", "c4c", "c4b", "c4d", "r2", "r3", "p1", "p2", "p3", "p4", "p5"],
    'programa': [
        [None, "c1c", None, None, "p1"],
        [None, "c2c", None, None, "p2"],
        [None, None, None, "c1e", None],
        [None, None,"c4d", None, None],
        [None, "c3c", None, "c2e", None],
        ["p1", None, None, "c2e", None],
        ["p1", "c3c", None, "c2e", None],
        ["p2", None, "c4c", "p3", None],
        ["p2", None, None, "p3", None],
        [None, 'c4c', "p3", None, None],
        [None, "r2", "p5", None, None],
        ["c1b", None, "p5", None, None],
        ["c1b", "r2", "p5", None, None],
        [None, "r3", "c3d", None, "p4"],
        ["c2b", None, "c3d", None, "p4"],
        ["c2b", "r3", "c3d", None, "p4"],
        ["c3b", None, None, None, None],
        ["c4b", None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]],
    'inicial': "A",
    'final': ["p1", "p2", "p3", "p4", "p5"]
}

semaforo = ["c2e", "c2b", "c2c", "c3c", "c3b", "c3d"]
semaforoEstado = False
pilha = 0
MAXIMOPILHA = 5

def fitaValida(fita:str, alfabeto:list) -> tuple[bool,str]:
    '''
        Verifica se a fita possui elementos pertencentes no alfabeto
        Retorna:
            Bool: Se a fita é válida
            Str: Caractere inválido na fita
    '''
    for i in fita:
        if not i in alfabeto:
            return (False,i)
    return (True,'')

def caminhar(estadoAtual:str, caminho:str, quintupla:dict) -> str:
    '''
        Percorre no autômato o caminho a partir do estado atual
        Retorna:
            Str: Novo estado atual após percorrer o caminho    
    '''

    alfabetoIndice = quintupla['alfabeto'].index(caminho)
    estadoIndice = quintupla['estados'].index(estadoAtual)
    return quintupla['programa'][estadoIndice][alfabetoIndice]
    
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
            pilha = 0
            semaforoEstado = not semaforoEstado


estadoAtual = random.choice('ABCD')

while not estadoAtual in quintupla["final"]:
    estadoAnterior = estadoAtual
    while True:
        estadoAtual=random.choice(quintupla["programa"][quintupla["estados"].index(estadoAnterior)])
        if estadoAtual != None:
            break
    # estadoAtual = caminhar(estadoAtual, caminho,quintupla)
    verificaSemaforo(estadoAtual, semaforo)
    print(estadoAtual)

print()
print()

if estadoAtual in quintupla['final']:
    print(f'Estado {estadoAtual} é um estado final')
    print('Fita válida!')
else:
    print(f'Estado {estadoAtual} não é um estado final')
    print('Fita inválida!')
