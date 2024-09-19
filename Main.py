import os
import platform
from Partida import *


def limpar_tela():
    # Detecta o sistema operacional e executa o comando apropriado
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def exibir_menu():
    print("=== MENU ===")
    print("1 - Jogar")
    print("2 - Como jogar?")
    print("3 - Sair")

def jogar():
    limpar_tela()
    Comecar()
  

def como_jogar():
    limpar_tela()
    print("=== Como jogar? ===")
    print("Uma palavra é escolhida aleatóriamente dentro do banco de palavras do jogo")
    print("a cada rodada você irá informar uma letra do alfabeto no terminal")
    print("caso a letra informada seja correta! será possivel visualizar onde na palavra essa letra se encaixa")
    print("Para cada letra informada incorreta uma parte do seu personagem é mandado para forca")
    print("Seu objetivo é acertar a palavra antes de ficar sem partes do personagem")
    print("")
    input("Pressione qualquer tecla para voltar ao menu...")

def main():
    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("Digite o número da opção: ")
        
        if opcao == "1":
            jogar()
        elif opcao == "2":
            como_jogar()
        elif opcao == "3":
            print("Saindo do jogo. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione qualquer tecla para tentar novamente...")

if __name__ == "__main__":
    main()
