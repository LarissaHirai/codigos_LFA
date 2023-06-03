import re

class Transicoes:
    def __init__(self, q, w, p):
        self.arg1 = q
        self.arg2 = w
        self.arg3 = p

class Automato:
    def __init__(self):
        self.alfabeto = ['a', 'b']
        self.estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']
        self.transicoes = []
        self.estadoInicial = 'q0'
        self.estadoFinal = ['q4', 'q5', 'q6', 'q7']

    def inserirFuncaoTransicao(self, q, a, p):
        self.transicoes.append(Transicoes(q, a, p))

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

# Define the transition functions
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


palavra = input("Digite uma palavra: ")
resultado = automato.verificarPalavra(palavra)
print(resultado)
