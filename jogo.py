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
        self.botoes = {}  # Dicionário para armazenar os botões das letras

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
        """Inicia uma nova partida e reseta os botões"""
        # Resetar os botões ao iniciar um novo jogo
        self.resetar_botoes()

        # Recomeçar a lógica do jogo
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
            self.adicionar_botao(letra, i // 7, i % 7)

        # Botão "Espaço" ao lado do botão "Z", ocupando duas colunas
        self.adicionar_botao("Espaço", 3, 5, letra_real=' ', largura=12, col_span=2)

        # Criar botão para "-"
        self.adicionar_botao("-", 3, 7)

    def adicionar_botao(self, letra, row, col, letra_real=None, largura=4, col_span=1):
        """Função auxiliar para adicionar botões ao layout"""
        if letra_real is None:
            letra_real = letra.lower()
        btn = tk.Button(self.buttons_frame, text=letra.upper(),font=("Arial", 10, "bold"), width=largura, height=2,
                        command=lambda: self.tentar_letra(letra_real, btn))
        btn.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5)
        self.botoes[letra_real] = btn

    def resetar_botoes(self):
        """Reseta os botões para o estado inicial (habilitados e com a cor padrão)"""
        for letra, botao in self.botoes.items():
            botao.config(state=tk.NORMAL, bg="SystemButtonFace")  # Habilita o botão e restaura a cor padrão

    def tentar_letra(self, letra, botao):
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
            botao.config(bg="#bbf1ae")  # Se a letra estiver correta, o botão fica verde
        else:
            self.tentativas -= 1
            botao.config(bg="#f97773")  # Se a letra estiver incorreta, o botão fica vermelho

        botao.config(state=tk.DISABLED)  # Desabilita o botão após o clique
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
            resultado = tk.messagebox.askquestion("Fim de jogo", f"{mensagem}\nQuer jogar novamente?")
            if resultado == 'yes':
                self.iniciar_jogo()  # Reseta o jogo
            else:
                from Menu import mostrar_menu  # Import atrasado para evitar ciclo de importação
                self.root.destroy()  # Fecha a janela do jogo antes de voltar ao menu
                mostrar_menu()  # Volta para o menu principal


# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    game = ForcaGame(root)
    root.mainloop()
