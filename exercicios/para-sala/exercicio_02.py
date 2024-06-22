# Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não
pergunta = input("Qual é a capital do Brasil? a) Rio de Janeiro b) Brasília c) Buenos Aires d) Quito")

if pergunta == "a" or pergunta == "c" or pergunta == "d":
   print("resposta errada") 
else: 
   print("resposta correta")
