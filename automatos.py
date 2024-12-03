from copy import deepcopy
import random

class Automato():
    def __init__(self,nome: str, alfabeto: list[str], estados: list[str], programa: list[list], inicial: str, final:list[str]):

        self.nome = nome
        self.alfabeto = alfabeto
        self.estados = estados
        self.programa = programa
        self.inicial = inicial
        self.final = final
        self.fita=''
        self.finalizou = False
        
        self.estadoAtual = inicial
    
    def proximoEstado(self, caminho: str) -> str:
        '''
            Retorna o proximo estado a partir do estado atual, com base no caminho passado.
            Argumentos:
                caminho: Qual caminho (do alfabeto) será percorrido
            Retorno:
                Proximo estado depois de percorrer o caminho (Retorna None se for um caminho inválido)
        '''
        alfabetoIndice = self.alfabeto.index(caminho)
        estadoIndice = self.estados.index(self.estadoAtual)
        return self.programa[estadoIndice][alfabetoIndice]

    def percorrer(self, caminho: str):
        '''
            Define o estado atual para o próximo estado, com base no caminho definido.
            Argumentos:
                caminho: Qual caminho (do alfabeto) será percorrido
        '''
        self.estadoAtual = self.proximoEstado(caminho)
    
    def caminhoValido(self, caminho: str) -> bool:
        '''
            Verifica se o caminho para o estado atual é válido
            Argumentos:
                caminho: Caminho que será verificado
        '''
        return self.programa[self.estados.index(self.estadoAtual)][self.alfabeto.index(caminho)] != None
    
    def fitaValida(self, fita:str) -> tuple[bool,str]:
        '''
            Verifica se a fita possui elementos pertencentes no alfabeto
            Retorna:
                Bool: Se a fita é válida
                Str: Caractere inválido na fita
        '''
        for i in fita:
            if not self.caminhoValido(i):
                return (False,i)
        return (True,'')
    
    def sorteiaCaminho(self):
        '''
            Seleciona um caminho válido aleatório para percorrer
        '''
        while True:
            aux=random.choice(self.alfabeto)
            if self.caminhoValido(aux):
                self.percorrer(aux)
                self.fita += aux
                break
    
    def ehEstadoFinal(self) -> bool:
        return self.estadoAtual in self.final

# Caso 1

caso1A = Automato(
    nome='Caso 1A',
    alfabeto=['c','b','p'],
    estados=['A','c1c','c1b','c3c','c3b','r2','p1'],
    programa=[[None, 'c1c','p1'],
              [None, 'c3c', None],
              ['p1',None, None],
              [None, 'r2', None],
              ['c1b', None, None],
              ['c3b',None, None],
              [None, None, None]],
    inicial='A',
    final=['p1']
)

caso1B = Automato(
    nome='Caso 1B',
    alfabeto=['c','b','p'],
    estados=['B','c2c','c2b','c4c','c4b','r3','p2'],
    programa=[[None,'c2c','p2'],
              [None,'c4c',None],
              ['p2',None,None],
              [None, 'r3', None],
              ['c2b',None, None],
              ['c4b', None, None],
              [None, None, None]],
    inicial='B',
    final=['p2']
)

caso1C = Automato(
    nome='Caso 1C',
    alfabeto=['d'],
    estados=['C','c1e','c2e','p3'],
    programa=[['c1e'],
              ['c2e'],
              ['p3'],
              [None]],
    inicial='C',
    final=['p3']
)

caso1D = Automato(
    nome='Caso 1D',
    alfabeto=['e','p'],
    estados=['D','c4d','c3d','p4','p5'],
    programa=[['c4d',None],
              ['c3d','p4'],
              ['p5',None],
              [None,None],
              [None,None]],
    inicial='D',
    final=['p4','p5']
)

# Caso 2

caso2A = Automato(
    nome='Caso 2A',
    alfabeto=['c','b','e','p'],
    estados=['A','c1c','c1b','c3c','c3b','r2','p1','p5'],
    programa=[[None, 'c1c',None, 'p1'],
              [None,'c3c',None,None],
              ['p1',None,None,None],
              [None,'r2','p5',None],
              [None,None,None,None],
              [None,None,None,None],
              [None,None,None,None]],
    inicial='A',
    final=['p1','p5']
)

caso2B = Automato(
    nome='Caso 2B',
    alfabeto=['c','b','d','p'],
    estados=['B','c2c','c2b','c4c','c4b','r3','p2','p3'],
    programa=[[None,'c2c',None,'p2'],
              [None,'c4c','p3',None],
              ['p2',None,'p3',None],
              [None,'r3',None,None],
              ['c2b',None,None,None],
              ['c4b',None,None,None],
              [None,None,None,None],
              [None,None,None,None]],
    inicial='B',
    final=['p2','p3']
)

caso2C = Automato(
    nome='Caso 2C',
    alfabeto=['c','b','d'],
    estados=['C','c1e','c2e','c2b','c4c','c4b','r3','p2','p3'],
    programa=[
        [None,None,'c1e'],
        [None,None,'c2e'],
        ['p2','c4c','p3'],
        ['p2',None,'p3'],
        [None,'r3',None],
        ['c2b',None,None],
        ['c4b',None,None],
        [None,None,None],
        [None,None,None]],
    inicial='C',
    final=['p2','p3']
)

caso2D = Automato(
    nome='Caso 2D',
    alfabeto=['c','b','e'],
    estados=['D','c1b','c3b','c3d','c4d','r2','p1','p5'],
    programa=[
        [None,None,'c4d'],
        ['p1',None,None],
        ['c1b',None,'p5'],
        ['c1b','r2','p5'],
        [None,None,'c3d'],
        ['c3b',None,None],
        [None,None,None]
    ],
    inicial='D',
    final=['p1','p5']
)

# Caso 3
completo = Automato(
    nome='Caso 3',
    alfabeto= ["c","b", "e", "d", "p"],
    estados= ["A", "B", "C", "D", "c1c", "c1b", "c1e", "c2e", "c2b", "c2c", "c3c", "c3b", "c3d", "c4c", "c4b", "c4d", "r2", "r3", "p1", "p2", "p3", "p4", "p5"],
    programa= [
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
    inicial= 'A',
    final= ["p1", "p2", "p3", "p4", "p5"]
)