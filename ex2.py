"""Faça um programa que leia um nome de usuário e a sua e não aceite a senha
igual ao nome do usuário,mostrando uma mensagem de erro
e voltando a pedir as informações."""
while True:
    nome = input('Digite o nome')
    senha = input('Digite a Senha')
    if senha == nome:
        print('Voçê Digitou a Senha igual ao Nome')
    else:
        print('Você acertou')
        break