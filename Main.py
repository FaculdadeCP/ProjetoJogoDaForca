from Classes.Data import Data
from Classes.Jogador import Jogador
from Classes.Menu import Menu


if __name__ == "__main__":
    data = Data()  # Inicializa o gerenciador do CSV
    menu = Menu(data)  # Inicializa o menu com o gerenciador de dados

    print("=== Bem-vindo ao Jogo da Forca ===")
    jogador = None
    while jogador is None:  # Continua pedindo email até login ou cadastro bem-sucedido
      jogador = menu.obter_jogador()
    
    # Exibe o menu principal após login/cadastro
    menu.exibir_menu_principal(jogador)
    

