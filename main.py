'''
Universidade Federal do Tocantins - Campus Palmas
Disciplina: Linguagens Formais e Autômatos
Professor: Alexandre Rossini
Alunas: Fernanda Plessim e Larissa Hirai
Curso: Ciência da Computação
'''

# Trabalho 3

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

def validar_formulario(nome, cpf, email, telefone):
    v_nome = validar_nome(nome)
    v_cpf = validar_cpf(cpf)
    v_email = validar_email(email)
    v_telefone = validar_telefone(telefone)
    if v_nome == True:
        print("Nome válido!")
    else:
        print("Nome inválido! O nome deve conter no máximo 50 símbolos alfabéticos e espaços.")
    if v_cpf == True:
        print("CPF válido!")
    else:
        print("CPF inválido! O CPF deve conter apenas algarismos numéricos (0-9) ou estar no formato padrão (000.000.000-00).")
    if v_email == True:
        print("E-mail válido!")
    else:
        print("E-mail inválido! O E-mail deve seguir o formato adequado.")
    if v_telefone == True:
        print("Telefone válido!")
    else:
        print("Telefone inválido! O telefone deve estar em um dos formatos permitidos.")


nome = input("Digite o nome: ")
cpf = input("Digite o CPF: ")
email = input("Digite o E-mail: ")
telefone = input("Digite o telefone: ")
validar_formulario(nome, cpf, email, telefone)
