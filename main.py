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

def validar_cpf(cpf):
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$'  # Expressão regular para validar o CPF
    return re.match(padrao, cpf) is not None

def validar_email(email):
    padrao = r'^[\w._]{2,}@[\w._]{2,}\.[a-z]{3}$'  # Expressão regular para validar o e-mail
    return re.match(padrao, email) is not None

def validar_telefone(telefone):
    padrao = r'^\d{11}$|^\(\d{2}\)\d{5}-\d{4}$'  # Expressão regular para validar o telefone
    return re.match(padrao, telefone) is not None


op = 15
while op != 0:
    op = int(input("\nO que deseja verificar?\n1-Nome\n2-CPF\n3-E-mail\n4-Telefone\n0-Sair\n"))
    if op == 1:
        nome = input("Digite o nome: ")

        if validar_nome(nome):
            print("Nome válido!")
        else:
            print("Nome inválido! O nome deve conter no máximo 50 símbolos alfabéticos e espaços.")
    elif op == 2:
        cpf = input("Digite o CPF: ")

        if validar_cpf(cpf):
            print("CPF válido!")
        else:
            print("CPF inválido! O CPF deve conter apenas algarismos numéricos (0-9) ou estar no formato padrão (000.000.000-00).")
    elif op == 3:
        email = input("Digite o E-mail: ")

        if validar_email(email):
            print("E-mail válido!")
        else:
            print("E-mail inválido! O E-mail deve seguir o formato adequado.")
    elif op == 4:
        telefone = input("Digite o telefone: ")

        if validar_telefone(telefone):
            print("Telefone válido!")
        else:
            print("Telefone inválido! O telefone deve estar em um dos formatos permitidos.")

print("Saindo...")
