# Escreva um programa que, dado dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos. 

numero1 = float(input("Insira um primeiro número"))
numero2 = float(input("Insira um segundo número"))

if numero1 > numero2:
    print(f"O {numero1} é maior que o {numero2}")
else:
    print(f"O {numero2} é maior que o {numero1}")

diferenca_numeros = numero1 - numero2

print(f"A diferença entre o primeiro número e o segundo número é de {diferenca_numeros}")


