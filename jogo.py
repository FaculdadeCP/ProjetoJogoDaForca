import tkinter as tk
import numpy as np
from Partida import remover_acentos, escolher_tema_palavra

class ForcaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        # Remover a opção de maximizar e centralizar a janela
        self.root.resizable(False, False)
        self.centralizar_janela(600, 450)

        self.tema = ""
        self.palavra = ""
        self.caracteres = []
        self.letras_corretas = np.array([])
        self.letras_tentadas = set()
        self.tentativas = 6

        # Widgets
        self.tema_label = tk.Label(self.root, text="Tema: ", font=("Arial", 14))
        self.tema_label.pack(pady=10)

        self.palavra_label = tk.Label(self.root, text="Palavra: ", font=("Arial", 16))
        self.palavra_label.pack(pady=10)

        self.tentativas_label = tk.Label(self.root, text="Tentativas restantes: 6", font=("Arial", 14))
        self.tentativas_label.pack(pady=10)

        self.letras_tentadas_label = tk.Label(self.root, text="Letras tentadas: ", font=("Arial", 14))
        self.letras_tentadas_label.pack(pady=10)

        # Inicializa o jogo
        self.iniciar_jogo()

        # Criação dos botões das letras (A-Z + Espaço e -)
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        self.criar_botoes_letras()

    def centralizar_janela(self, width, height):
        """Centraliza a janela na tela"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (width / 2))
        y_cordinate = int((screen_height / 2) - (height / 2))

        self.root.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

    def iniciar_jogo(self):
        """Inicia uma nova partida"""
        dadosPartida = escolher_tema_palavra()
        self.tema, self.palavra = dadosPartida.split(" | ")

        self.caracteres = list(self.palavra)
        self.letras_corretas = np.full(len(self.caracteres), '_')
        self.letras_tentadas = set()
        self.tentativas = 6

        self.atualizar_interface()

    def criar_botoes_letras(self):
        """Cria botões para cada letra do alfabeto, incluindo 'Espaço' e '-'"""
        alfabeto = "abcdefghijklmnopqrstuvwxyz"

        # Criar botões de letras A-Z com 7 colunas por linha
        for i, letra in enumerate(alfabeto):
            btn = tk.Button(self.buttons_frame, text=letra.upper(), width=4, height=2, command=lambda l=letra: self.tentar_letra(l))
            btn.grid(row=i//7, column=i % 7, padx=5, pady=5)

        # Botão "Espaço" ao lado do botão "Z", ocupando as duas últimas colunas
        btn_espaco = tk.Button(self.buttons_frame, text="Espaço", width=10, height=2, command=lambda: self.tentar_letra(' '))
        btn_espaco.grid(row=3, column=5, columnspan=2, padx=5, pady=5)  # Alinhado ao lado do "Z", centralizado

        # Criar botão para "-"
        btn_traco = tk.Button(self.buttons_frame, text="-", width=4, height=2, command=lambda: self.tentar_letra('-'))
        btn_traco.grid(row=3, column=7, padx=5, pady=5)  # Alinhado à direita do botão "Espaço"

    def tentar_letra(self, letra):
        """Função chamada ao clicar em uma letra"""
        letra_normalizada = remover_acentos(letra)
        
        if letra in self.letras_tentadas:
            return  # Letra já foi tentada

        self.letras_tentadas.add(letra)
        palavra_normalizada = [remover_acentos(char).lower() for char in self.caracteres]

        if letra_normalizada in palavra_normalizada:
            for idx, char in enumerate(palavra_normalizada):
                if char == letra_normalizada:
                    self.letras_corretas[idx] = self.caracteres[idx]
        else:
            self.tentativas -= 1

        self.atualizar_interface()

        if "_" not in self.letras_corretas:
            self.encerrar_jogo("Parabéns! Você acertou a palavra!")
        elif self.tentativas == 0:
            self.encerrar_jogo(f"Você perdeu! A palavra era: {self.palavra}")

    def atualizar_interface(self):
        """Atualiza a interface de acordo com o progresso do jogo"""
        self.tema_label.config(text=f"Tema: {self.tema}")
        self.palavra_label.config(text=f"Palavra: {' '.join(self.letras_corretas)}")
        self.tentativas_label.config(text=f"Tentativas restantes: {self.tentativas}")
        self.letras_tentadas_label.config(text=f"Letras tentadas: {', '.join(sorted(self.letras_tentadas))}")

    def encerrar_jogo(self, mensagem):
        """Exibe uma mensagem de final de jogo"""
        resultado = tk.messagebox.askquestion("Fim de jogo", f"{mensagem}\nQuer jogar novamente?")
        if resultado == 'yes':
            self.iniciar_jogo()
        else:
            self.root.quit()

# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    game = ForcaGame(root)
    root.mainloop()
