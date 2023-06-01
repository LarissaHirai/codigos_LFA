import re

class Transicoes:
    def __init__(self, a, b, c):
        self.arg1 = a
        self.arg2 = b
        self.arg3 = c

class Automato:
    def __init__(self):
        self.alfabeto = ['a','b']
        self.estados = ['q0','q1','q2','q3','q4','q5','q6']
        self.transicoes = []
        self.estadoInicial = 'q0'
        self.estadoFinal = ['q4', 'q5', 'q6', 'q7']

    def inserirFuncaoTransicao(self, q, a, p):
        self.transicoes.append(Transicoes(q,a,q))

    def funcaoTransicao(self, q, a):
        for i in self.transicoes:
            if i.arg1==q and i.arg2==a:
                return i.arg3
        return -1

    def transicaoEstendida(self,q,w):
        if len(w) == 0:
            return q
        a=w[len(w)-1]
        x=w[:len(w)-1]
        return self.funcaoTransicao(self.transicaoEstendida(q,x),a)

a=Automato()
a.inserirFuncaoTransicao('q0','a','q1')
a.inserirFuncaoTransicao('q0','b','q0')
a.inserirFuncaoTransicao('q1','a','q2')
a.inserirFuncaoTransicao('q1','b','q3')
a.inserirFuncaoTransicao('q2','a','q4')
a.inserirFuncaoTransicao('q2','b','q5')
a.inserirFuncaoTransicao('q3','a','q6')
a.inserirFuncaoTransicao('q3','b','q7')
a.inserirFuncaoTransicao('q4','a','q4')
a.inserirFuncaoTransicao('q4','b','q5')
a.inserirFuncaoTransicao('q5','a','q6')
a.inserirFuncaoTransicao('q5','b','q7')
a.inserirFuncaoTransicao('q6','a','q2')
a.inserirFuncaoTransicao('q6','b','q3')
a.inserirFuncaoTransicao('q7','a','q1')
a.inserirFuncaoTransicao('q7','b','q0')


