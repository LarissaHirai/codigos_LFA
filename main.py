'''
Universidade Federal do Tocantins - Campus Palmas
Disciplina: Linguagens Formais e Autômatos
Professor: Alexandre Rossini
Alunas: Fernanda Plessim e Larissa Hirai
Curso: Ciência da Computação
'''

# Trabalho 2

import re

def validar_nome(nome):
    padrao = r'^[a-zA-Z ]{1,50}$'  # Expressão regular para validar o nome
    return re.match(padrao, nome) is not None

# Exemplo de uso:
nome = input("Digite o nome: ")

if validar_nome(nome):
    print("Nome válido!")
else:
    print("Nome inválido! O nome deve conter no máximo 50 símbolos alfabéticos e espaços.")
