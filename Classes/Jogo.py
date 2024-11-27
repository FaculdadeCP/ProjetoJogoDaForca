import random, os
from Classes.Palavras import obter_palavra, contar_letras
from Classes.Pontuacao import Pontuacao


class Jogo:
    def __init__(self, jogador, data):
        self.jogador = jogador
        self.data = data
        self.nivel = 1
        self.erros_permitidos = 6
        self.erros = 0
        self.acertos = 0
        self.palavra_atual = None
        self.palavra_revelada = None
        self.letras_tentadas = set() 
        self.pontos_rodada = 0
        self.palavras_usadas = [10]
        
    def limpar_console(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            
    def calcular_complexidade(self):
        if self.nivel in [5, 10, 15, 20] or self.nivel % 5 == 0:
            return 3
        elif self.nivel <= 4:
            return 1
        elif self.nivel in [6, 7, 8, 9]:
            return 2
        elif self.nivel in [11, 12, 13, 14]:
            return random.choice([1, 2])
        elif self.nivel >= 16:
            return random.choice([1, 2, 3])
        return 1

    def obter_palavra_para_jogo(self):
        """
        Busca uma nova palavra da API, verificando se ela já foi usada.
        """
        complexidade = self.calcular_complexidade()

        while True:
            # Obtém uma palavra da API
            self.palavra_atual = obter_palavra(complexidade)

            if not self.palavra_atual:
                print("Erro ao obter a palavra. Tente novamente.")
                continue  # Tenta buscar novamente

            palavra = self.palavra_atual["palavra"]

            # Verifica se a palavra já foi usada
            if palavra not in self.palavras_usadas:
                self.palavras_usadas.append(palavra)  # Adiciona a palavra ao array
                # Garante que o array não tenha mais de 10 elementos
                if len(self.palavras_usadas) > 10:
                    self.palavras_usadas.pop(0)  # Remove a palavra mais antiga
                self.palavra_revelada = ["_" if letra.isalpha() else letra for letra in palavra]
                break  # Sai do loop se a palavra for válida

        print(f"Palavras já usadas neste ciclo de 10 níveis: {self.palavras_usadas}")

    def exibir_palavra_revelada(self):
        """
        Exibe a palavra atual com letras já informadas e tentativas restantes.
        """
        self.limpar_console()  # Limpa o console antes de exibir a palavra
        palavra = self.palavra_atual["palavra"]
        letras_informadas = ", ".join(sorted(self.letras_tentadas))
        tentativas_restantes = self.erros_permitidos - self.erros

        if self.erros < 3:
            print(f"\033[1mNível:\033[0m {self.nivel} | \033[1mPontos:\033[0m {self.pontos_rodada}")
            print(f"\033[1mLetras já informadas:\033[0m: {letras_informadas} (\033[1mTentativas Restantes:\033[0m {tentativas_restantes})")
            print(f"\033[1mPalavra:\033[0m {' '.join(self.palavra_revelada)} (\033[1m{contar_letras(palavra)} Letras\033[0m)")
        else:
            print(f"\033[1mNível:\033[0m {self.nivel} | \033[1mPontos:\033[0m {self.pontos_rodada}")
            print(f"\033[1mCategoria:\033[0m {self.palavra_atual['categoria']}")
            print(f"\033[1mLetras já informadas:\033[0m: {letras_informadas} (\033[1mTentativas Restantes:\033[0m {tentativas_restantes})")
            print(f"\033[1mPalavra:\033[0m {' '.join(self.palavra_revelada)} (\033[1m{contar_letras(palavra)} Letras\033[0m)")

    def tentar_letra(self, letra):
        if letra in self.letras_tentadas:
            print(f"A letra '{letra}' já foi informada, por gentileza, informe outra.")
            return

        self.letras_tentadas.add(letra)

        if letra in self.palavra_atual["palavra"]:
            for i, l in enumerate(self.palavra_atual["palavra"]):
                if l == letra:
                    self.palavra_revelada[i] = letra
            self.acertos += 1
            self.pontuacao.registrar_acerto()  
            print("Acertou!")
        else:
            self.erros += 1
            self.pontuacao.registrar_erro() 
            print("Errou!")


    def verificar_vitoria(self):
        return "_" not in self.palavra_revelada

    def jogar(self):
        self.pontuacao = Pontuacao(self.jogador, self.data)

        while self.erros < self.erros_permitidos:
            self.obter_palavra_para_jogo()
            tentativas_necessarias = len(set(self.palavra_atual["palavra"]))
            erros_restantes = self.erros_permitidos - self.erros

            while not self.verificar_vitoria():
                self.exibir_palavra_revelada()
                letra = input("Digite uma letra: ").upper()
                if len(letra) != 1 or not letra.isalpha():
                    print("Entrada inválida. Digite apenas uma letra.")
                    continue
                self.tentar_letra(letra)
                if self.erros >= self.erros_permitidos:
                    # Exibe a palavra correta antes de encerrar
                    palavra_correta = self.palavra_atual["palavra"]
                    print(f"\nVocê perdeu! \nA palavra era: {palavra_correta} \nVoltando ao menu principal...")
                    self.pontuacao.salvar_pontuacao(0)
                    return  # Volta ao menu principal

            # Calcula a pontuação do nível
            tamanho_palavra = len(self.palavra_atual["palavra"])
            dificuldade = self.calcular_complexidade()
            pontos_nivel = self.pontuacao.calcular_pontuacao_nivel(tamanho_palavra, dificuldade, tentativas_necessarias, erros_restantes)

            print(f"\nVocê completou a palavra! Pontos obtidos: {pontos_nivel}")
            self.pontuacao.salvar_pontuacao(pontos_nivel)

            self.nivel += 1
            self.erros = 0
            self.acertos = 0
            self.pontos_rodada += pontos_nivel
            self.letras_tentadas.clear()
            self.pontuacao.combo_atual = 0  # Reseta o combo ao final do nível

        print("\nFim de jogo. Obrigado por jogar!")
        return
