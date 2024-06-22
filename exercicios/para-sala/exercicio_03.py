# Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de respostas (sim ou não), mostre uma mensagem de sua escolha na tela

def verificacao_gosta_nome(gosta_do_nome):
    if gosta_do_nome == "Sim" or gosta_do_nome == "sim":
       return "Sorte a sua!"
    else: gosta_do_nome == "Não" or gosta_do_nome == "não"
    return "Sinto muito!"


inserir_nome = input("Insira o seu nome:")
gosta_do_nome = input("Você gosta do seu nome?")

resultado = verificacao_gosta_nome(gosta_do_nome)

print(resultado)

