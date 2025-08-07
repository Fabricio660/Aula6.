"""Faça um programa que leia e valide as segintes informações:
Nome:maior que 3 caracteres;
Idade: entre 0 a 150;
Salário:maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c' , 'v' , 'd' ;"""

nome = input('Digite seu nome:')

while len(nome)<3:
    nome = input('Digite seu nome:')
print(f'Você digitou um nome maior que 3 caracteres => {nome}')
idade = int(input('Digite sua idade entre [0 e 150]'))
while idade < 0 or idade > 150:
            print('Idade invalida, digite novamente sua idade entre [0 e 150]')
            
            #print(f'Sua idade é =>{idade}')

while True:
    try:
        salario = float(input("Digite seu salário: R$ "))
        if salario > 0:
            break
        else:
            print("Salário deve ser maior que zero.")
    except ValueError:
        print("Digite um número válido.")

while True:
    sexo = input("Digite seu sexo (f/m): ").strip().lower()
    if sexo in ['f', 'm']:
        break
    else:
        print("Sexo deve ser 'f' ou 'm'.")

while True:
    estado_civil = input("Digite seu estado civil (s - solteiro, c - casado, v - viúvo, d - divorciado): ").strip().lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil deve ser 's', 'c', 'v' ou 'd'.")


print("\n--- Dados válidos cadastrados ---")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
estados = {'s': 'Solteiro(a)', 'c': 'Casado(a)', 'v': 'Viúvo(a)', 'd': 'Divorciado(a)'}
print(f"Estado Civil: {estados[estado_civil]}")

