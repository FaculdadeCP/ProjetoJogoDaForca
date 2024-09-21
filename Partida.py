import numpy as np
import unicodedata  # Para normalizar e remover acentos
from Palavras import escolher_tema_palavra

tema = ""
palavra = ""
letra = ""
caracteres = list()  # Lista de caracteres da palavra
letras_corretas = np.array([])  # Array para armazenar as letras corretas já descobertas
letras_tentadas = set()  # Conjunto para armazenar as letras já tentadas
tentativas = 6  # Número de tentativas (fixo em 6)

def remover_acentos(texto):
    """Função para normalizar e remover acentos de um texto."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def Comecar():
    global palavra, tema, caracteres, letras_corretas, letras_tentadas, tentativas

    dadosPartida = escolher_tema_palavra()
    tema, palavra = dadosPartida.split(" | ")

    caracteres = list(palavra) 
    letras_corretas = np.full(len(caracteres), '_')  # Inicializa o array de tamanho fixo com '_'
    letras_tentadas = set()
    tentativas = 6

    print(f"O jogo começou! O seu tema é: {tema}")
    print(f"A palavra tem {len(palavra)} letras!")
    print("Boa sorte!")

    # Loop do jogo
    while tentativas > 0 and "_" in letras_corretas:
        print(f"Tema: {tema}")
        print(f"Letras tentadas: {', '.join(letras_tentadas)}")  # Mostra as letras já tentadas
        print("")

        # Exibe a palavra com os caracteres corretos descobertos
        print(f"\nPalavra: {' '.join(letras_corretas)}")
        print("")
        print(f"Você tem {tentativas} tentativas restantes.")

        insere_letra()

    if "_" not in letras_corretas:

        print(f"Parabéns! Você acertou a palavra: {palavra}")
        input("Pressione qualquer tecla para voltar ao menu...")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")
        input("Pressione qualquer tecla para voltar ao menu...")

def insere_letra():
    while True:  # Loop para garantir que a entrada seja válida
        letra = input("Digite uma letra: ").lower()  # Converte para minúscula para padronizar
        
        # Verifica se a entrada tem exatamente 1 caractere e é uma letra
        if len(letra) == 1 and letra.isalpha():
            validar_letra(letra)
            break
        else:
            print("Entrada inválida! Digite apenas uma única letra.")


def validar_letra(letra):
    global tentativas

    # Normaliza a letra inserida para remover acentos
    letra_normalizada = remover_acentos(letra)

    if letra in letras_tentadas or letra_normalizada in letras_tentadas:
        # Se a letra já foi tentada, informa ao jogador e não diminui tentativas
        print(f"Você já tentou a letra '{letra}'. Tente outra.")
        insere_letra()
    else:
        # Adiciona a letra ao conjunto de letras tentadas (mantém acento original para exibição)
        letras_tentadas.add(letra)
        
        # Normaliza a palavra para a comparação
        palavra_normalizada = [remover_acentos(char).lower() for char in caracteres]

        if letra_normalizada in palavra_normalizada:  # Verifica se a letra está na palavra, ignorando acentos
            # Atualiza o array de letras corretas
            for idx, char in enumerate(palavra_normalizada):
                if char == letra_normalizada:
                    letras_corretas[idx] = caracteres[idx]  # Substitui o "_" pela letra correta no array original
            print(f"A letra '{letra}' está presente na palavra!")
        else:
            # Se a letra não estiver presente, diminui o número de tentativas
            tentativas -= 1
            print(f"A letra '{letra}' NÃO está presente na palavra.")
