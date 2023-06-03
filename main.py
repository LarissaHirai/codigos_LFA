'''
Universidade Federal do Tocantins - Campus Palmas
Disciplina: Linguagens Formais e Autômatos
Professor: Alexandre Rossini
Alunas: Fernanda Plessim e Larissa Hirai
Curso: Ciência da Computação
'''

# Trabalho 2

import re

class Transicoes:
    def __init__(self, q, w, p):
        self.arg1 = q
        self.arg2 = w
        self.arg3 = p

class Automato:
    def __init__(self):
        self.alfabeto = ['a', 'b']
        self.estados = []
        self.transicoes = []
        self.estadoInicial = 'q0'
        self.estadoFinal = []

    def inserirFuncaoTransicao(self, q, a, p):
        self.transicoes.append(Transicoes(q, a, p))

    def inserirEstadoFinal(self, q):
        self.estadoFinal.append(q)

    def inserirEstados(self, q):
        self.estados.append(q)

    def funcaoTransicao(self, q, a):
        for transicao in self.transicoes:
            if transicao.arg1 == q and transicao.arg2 == a:
                return transicao.arg3
        return -1

    def transicaoEstendida(self, q, w):
        if len(w) == 0:
            return q
        a = w[-1]
        x = w[:-1]
        return self.funcaoTransicao(self.transicaoEstendida(q, x), a)

    def verificarPalavra(self, palavra):
        estado_atual = self.estadoInicial
        vetor = list(palavra)
        for i in vetor:
            estado_atual = self.transicaoEstendida(estado_atual, i)
        if estado_atual in self.estadoFinal:
            return "A palavra pertence à linguagem reconhecida pelo autômato."
        else:
            return "A palavra não pertence à linguagem reconhecida pelo autômato."

automato = Automato()

automato.inserirFuncaoTransicao('q0', 'a', 'q1')
automato.inserirFuncaoTransicao('q0', 'b', 'q0')
automato.inserirFuncaoTransicao('q1', 'a', 'q2')
automato.inserirFuncaoTransicao('q1', 'b', 'q3')
automato.inserirFuncaoTransicao('q2', 'a', 'q4')
automato.inserirFuncaoTransicao('q2', 'b', 'q5')
automato.inserirFuncaoTransicao('q3', 'a', 'q6')
automato.inserirFuncaoTransicao('q3', 'b', 'q7')
automato.inserirFuncaoTransicao('q4', 'a', 'q4')
automato.inserirFuncaoTransicao('q4', 'b', 'q5')
automato.inserirFuncaoTransicao('q5', 'a', 'q6')
automato.inserirFuncaoTransicao('q5', 'b', 'q7')
automato.inserirFuncaoTransicao('q6', 'a', 'q2')
automato.inserirFuncaoTransicao('q6', 'b', 'q3')
automato.inserirFuncaoTransicao('q7', 'a', 'q1')
automato.inserirFuncaoTransicao('q7', 'b', 'q0')

automato.inserirEstadoFinal('q4')
automato.inserirEstadoFinal('q5')
automato.inserirEstadoFinal('q6')
automato.inserirEstadoFinal('q7')

automato.inserirEstados('q0')
automato.inserirEstados('q1')
automato.inserirEstados('q2')
automato.inserirEstados('q3')
automato.inserirEstados('q4')
automato.inserirEstados('q5')
automato.inserirEstados('q6')
automato.inserirEstados('q7')

palavra = input("Digite uma palavra: ")
resultado = automato.verificarPalavra(palavra)
print(resultado)
