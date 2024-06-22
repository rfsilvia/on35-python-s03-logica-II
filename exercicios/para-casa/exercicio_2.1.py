# Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado. 

pergunta_operacoes_matematicas = input ("Escolha uma das seguintes operações matemáticas: a) adição b)subtração c) multiplicação d) divisão").lower()

if pergunta_operacoes_matematicas == "a":
    numero1 = float (input("Digite um número"))
    numero2 = float (input("Digite um segundo número"))
    print(f"O resultado da adição desses dois números é {numero1 + numero2} ")
elif pergunta_operacoes_matematicas == "b":
    numero1 = float (input("Digite um número"))
    numero2 = float (input("Digite um segundo número"))
    print(f"O resultado da subtração desses dois números é {numero1 - numero2} ")
elif pergunta_operacoes_matematicas == "c":
    numero1 = float (input("Digite um número"))
    numero2 = float (input("Digite um segundo número"))
    print(f"O resultado da multiplicação desses dois números é {numero1 * numero2} ")
else:
    pergunta_operacoes_matematicas == "d"
    numero1 = float (input("Digite um número"))
    numero2 = float (input("Digite um segundo número"))
    print(f"O resultado da divisão desses dois números é {numero1 / numero2} ")