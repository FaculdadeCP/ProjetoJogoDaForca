import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from Partida import remover_acentos, escolher_tema_palavra
import os

class ForcaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        # Remover a opção de maximizar e centralizar a janela
        self.root.resizable(False, False)
        self.centralizar_janela(800, 400)  # Aumenta o tamanho da janela para caber a imagem

        self.tema = ""
        self.palavra = ""
        self.caracteres = []
        self.letras_corretas = np.array([])
        self.letras_tentadas = set()
        self.tentativas = 6
        self.botoes = {}  # Dicionário para armazenar os botões das letras

        # Caminho das imagens
        current_dir = os.path.dirname(__file__)
        self.img_paths = [os.path.join(current_dir, f"Resource/forca_{i}.png") for i in range(7)]  # Imagens da forca 0-6
        self.img_forca = None

        # Frame para organizar layout
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Frame esquerdo para a imagem da forca e labels de tentativas e letras tentadas
        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)

        # Label para as tentativas restantes (acima da imagem)
        self.tentativas_label = tk.Label(self.left_frame, text="Tentativas restantes: 6", font=("Arial", 14))
        self.tentativas_label.pack()

        # Label para exibir a imagem da forca
        self.forca_label = tk.Label(self.left_frame)
        self.forca_label.pack()

        # Label para letras tentadas (abaixo da imagem)
        self.letras_tentadas_label = tk.Label(self.left_frame, text="Letras tentadas: ", font=("Arial", 14))
        self.letras_tentadas_label.pack()

        # Frame direito para o jogo
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10)

        # Widgets
        self.tema_label = tk.Label(self.right_frame, text="Tema: ", font=("Arial", 14))
        self.tema_label.pack(pady=10)

        self.palavra_label = tk.Label(self.right_frame, text="Palavra: ", font=("Arial", 16))
        self.palavra_label.pack(pady=10)

        # Inicializa o jogo
        self.iniciar_jogo()

        # Criação dos botões das letras (A-Z + Espaço e -)
        self.buttons_frame = tk.Frame(self.right_frame)
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
        self.resetar_botoes()

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
        btn = tk.Button(self.buttons_frame, text=letra.upper(), font=("Arial", 10, "bold"), width=largura, height=2,
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
        
        # Formatar as letras tentadas para quebrar linha a cada 8 letras
        letras_tentadas_lista = sorted(self.letras_tentadas)
        linhas_letras_tentadas = [', '.join(letras_tentadas_lista[i:i+8]) for i in range(0, len(letras_tentadas_lista), 8)]
        letras_tentadas_formatadas = '\n'.join(linhas_letras_tentadas)
        
        self.letras_tentadas_label.config(text=f"Letras tentadas:\n{letras_tentadas_formatadas}")

        # Redimensiona e atualiza a imagem da forca de acordo com as tentativas restantes
        img = Image.open(self.img_paths[6 - self.tentativas])
        img = img.resize((250, 250), Image.Resampling.LANCZOS)  # Redimensiona a imagem para 250x250
        self.img_forca = ImageTk.PhotoImage(img)
        self.forca_label.config(image=self.img_forca)

    def encerrar_jogo(self, mensagem):
        """Exibe uma mensagem de final de jogo"""
        resultado = tk.messagebox.askquestion("Fim de jogo", f"{mensagem}\nQuer jogar novamente?")
        if resultado == 'yes':
            self.iniciar_jogo()  # Reseta o jogo
        else:
            from Menu import mostrar_menu  # Import atrasado para evitar ciclo de importação
            self.root.destroy()  # Fecha a janela do jogo antes de voltar ao menu
            mostrar_menu()  # Volta para o menu principal
