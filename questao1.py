#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
#informações.

def nome_senha():
    nome = input("Insira seu nome de usuário: ")
    senha = input("Insira sua senha: ")
    while senha == nome:
        senha = input("Senha não pode ser igual ao Nome!! Digite a senha novamente: ")

nome_senha()


