# Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não 
def verificacao_idade(idade) :
    if idade >= 18:
        return "Pessoa maior de idade"
    elif idade == 17:
        return "Logo será uma pessoa maior de idade"
    else:
        return "Pessoa menor de idade"
    
idade_inserida = int(input("insira a sua idade"))
resultado = verificacao_idade(idade_inserida)

print(resultado)

