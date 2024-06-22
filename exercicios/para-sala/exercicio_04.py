# Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja "sim", pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso do usuário responder "não", pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha. 

tem_irmaos = (input("Você tem irmãos? (responda sim ou não)"))


if tem_irmaos == "Sim" or tem_irmaos == "sim":
        quantidade_irmaos = int(input("Então você não é filho único. Quantos irmãos você tem?"))
        print(f"Você tem {quantidade_irmaos} irmãos")

else:
    gostaria_ter_irmaos = (input("Você gostaria de ter irmão? (responda sim ou não)"))  
    if gostaria_ter_irmaos == "Sim" or gostaria_ter_irmaos == "sim":
        print(f"As vezes nossos amigos são nossos verdadeiros irmãos")
    else: print(f"Que bom que você é uma pessoa bem resolvida!")
 