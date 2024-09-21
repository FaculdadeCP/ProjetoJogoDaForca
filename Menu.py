import tkinter as tk
import os
from tkinter import messagebox
from Partida import *
from jogo import ForcaGame 

def mostrar_menu():
    global root  # Tornar a variável root global
    # Inicialização da janela principal do Tkinter
    root = tk.Tk()
    root.title("Jogo da Forca - Menu Principal")

    # Remover o botão de maximizar
    root.resizable(False, False)

    # Definir o tamanho da janela
    window_width = 500
    window_height = 800

    # Centralizar a janela na tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    # Caminho para a imagem de fundo e imagens dos botões
    current_dir = os.path.dirname(__file__)
    background_path = os.path.join(current_dir, "Resource", "background.png")  # Substitua pelo nome da sua imagem de fundo
    image_path_sair = os.path.join(current_dir, "Resource", "btn_sair2.png")
    image_path_jogar = os.path.join(current_dir, "Resource", "btn_jogar2.png")
    image_path_como_jogar = os.path.join(current_dir, "Resource", "btn_ComoJogar2.png")

    # Carregar as imagens
    img_background = tk.PhotoImage(file=background_path)
    img_sair = tk.PhotoImage(file=image_path_sair)
    img_jogar = tk.PhotoImage(file=image_path_jogar)
    img_como_jogar = tk.PhotoImage(file=image_path_como_jogar)

    # Adicionar a imagem de fundo com um Label
    background_label = tk.Label(root, image=img_background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Widgets (botões) do menu principal com imagens
    menu_label = tk.Label(root,bg="#c0dce3")
    menu_label.pack(pady=100)

    btn_jogar = tk.Button(root, image=img_jogar, command=iniciar_jogo, borderwidth=0, highlightthickness=0,background="#c7e0e6")
    btn_jogar.pack(pady=5)

    btn_como_jogar = tk.Button(root, image=img_como_jogar, command=como_jogar, borderwidth=0, highlightthickness=0,background="#c7e0e6")
    btn_como_jogar.pack(pady=20)

    btn_sair = tk.Button(root, image=img_sair, command=sair, borderwidth=0, highlightthickness=0,background="#c7e0e6")
    btn_sair.pack(pady=5)

    # Inicia o loop da interface gráfica
    root.mainloop()

def iniciar_jogo():
    global root  # Tornar a variável root global
    root.destroy()  # Fecha a janela atual do menu
    # Cria uma nova janela para o jogo da Forca
    jogo_root = tk.Tk()
    ForcaGame(jogo_root)  # Inicia o jogo dentro da nova janela
    jogo_root.mainloop()

def como_jogar():
    info_text = (
       "\n"
        "• A palavra oculta está relacionada com o tema\n \n"
        "• O tamanho da palavra oculta (quantidade de letras) está representado pelos traços.\n\n"
        "• Clique em uma das letras. Se a letra existir na palavra, a letra será exibida, caso contrário, seu bonequinho ficará cada vez mais preso.\n\n"
        "• A cada erro uma parte do corpo do bonequinho é desenhada: cabeça, tronco, braço direito, braço esquerdo, perna direita e perna esquerda\n\n"
        "• O objetivo é descobrir a palavra oculta antes que o bonequinho fique completamente desenhado."
    )
    messagebox.showinfo("Jogo da Forca - Como Jogar?", info_text)

def sair():
    global root  # Tornar a variável root global
    root.destroy()
