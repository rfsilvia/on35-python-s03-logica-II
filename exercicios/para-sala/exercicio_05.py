#Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida

pergunta = input ("Escolha uma das seguintes bebidas: a) caipirinha b) mocktail c) gin & tônica")

if pergunta == "a" or pergunta == "A":
    print(f"Você escolheu caipirinha")

elif pergunta == "b" or pergunta == "B":
    print(f"Você escolheu mocktail")

else:
    print(f"Você escolheu gin & tônica")

    