
'''
    Testa se uma fita é válida ou não
    Sem suporte para AFN
    "Ah mas porque não recebe entrada de usuario?"
    mucho texto pra ficar testando, muda nas variáveis fazendo favor -b
'''
    
quintupla ={
    'alfabeto': ["a","b"],
    'estados': ["s0","s1"],
    # A ordem do programa deve seguir a ordem do alfabeto e do estado
    #   a   b   ...
    #s1
    #s2
    #...
    #
    'programa': [["s1",None],
                 ["s1","s1"]],
    'inicial': "s0",
    'final': ["s1"]
}

# fita = "abbababbbaaaabb"
fita = input("Informe a fita: ")



def fitaValida(fita:str, alfabeto:list) -> tuple[bool,str]:
    for i in fita:
        if not i in alfabeto:
            return (False,i)
    return (True,'')

def caminhar(estadoAtual:str, caminho:str, quintupla:dict) -> str:
    alfabetoIndice = quintupla['alfabeto'].index(caminho)
    estadoIndice = quintupla['estados'].index(estadoAtual)
    return quintupla['programa'][estadoIndice][alfabetoIndice]
    


# Nesse exemplo, a fita só será válida se a quantidade de a for múltipla de 3
ehValido = fitaValida(fita, quintupla['alfabeto'])
if ehValido[0]:
    print("Todos os elementos da fita estão no alfabeto!")
else:
    print(f'Fita inválida!\n{ehValido[1]} não está no alfabeto!')
    quit()


estadoAtual = quintupla['inicial']
print(f"Estados passados: {estadoAtual}",end=' ')
contador = 0

for i in fita:
    estadoAnterior = estadoAtual
    estadoAtual = caminhar(estadoAtual,i,quintupla)
    if estadoAtual == None:
        print(f"Fita inválida!\nNão é possível passar por {i} (posição {contador}) pelo estado {estadoAnterior}")
        quit()
    print(estadoAtual,end=' ')
    contador += 1

print()
print()

if estadoAtual in quintupla['final']:
    print(f'Estado {estadoAtual} é um estado final')
    print('Fita válida!')
else:
    print(f'Estado {estadoAtual} não é um estado final')
    print('Fita inválida!')
