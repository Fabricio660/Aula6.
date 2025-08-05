"""Faça um programa que leia e valide as segintes informações:
Nome:maior que 3 caracteres;
Idade: entre 0 a 150;
Salário:maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c' , 'v' , 'd' ;"""
#entrada do nome
nome = input('Digite o Nome')
 
#validação do nome
while len(nome)<3:
    nome = input("Digite o Nome")
#entrada idade

idade = int(input('Digite a idade entre [0 - 150]'))
#validação da idade
while idade<0 or idade>150:
    idade = int(input('Digite a idade [0 - 150]'))
#entrada do salario
    salario = float(input("Digite o salario"))
    #Validaçao salario
    while salario>0:





    