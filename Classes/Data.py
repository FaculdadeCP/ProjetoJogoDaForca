import csv
import os

class Data:
    def __init__(self, arquivo="dados.csv"):
        self.arquivo = arquivo
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Email", "Nome", "Senha", "PontuacaoMaxima", "UltimaPontuacao", "PosicaoRanking"])

    def adicionar_jogador(self, email, nome, senha, pontuacao_maxima=0, ultima_pontuacao=0, posicao_ranking=0):
        with open(self.arquivo, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, nome, senha, pontuacao_maxima, ultima_pontuacao, posicao_ranking])

    def listar_jogadores(self):
        jogadores = []
        with open(self.arquivo, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                jogadores.append(row)
        return jogadores

    def atualizar_jogador(self, email, pontuacao_maxima=None, ultima_pontuacao=None, posicao_ranking=None):
        jogadores = self.listar_jogadores()
        with open(self.arquivo, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Email", "Nome", "Senha", "PontuacaoMaxima", "UltimaPontuacao", "PosicaoRanking"])
            writer.writeheader()
            for jogador in jogadores:
                if jogador["Email"] == email:
                    if pontuacao_maxima is not None:
                        jogador["PontuacaoMaxima"] = pontuacao_maxima
                    if ultima_pontuacao is not None:
                        jogador["UltimaPontuacao"] = ultima_pontuacao
                    if posicao_ranking is not None:
                        jogador["PosicaoRanking"] = posicao_ranking
                writer.writerow(jogador)

    def buscar_jogador(self, email):
        jogadores = self.listar_jogadores()
        for jogador in jogadores:
            if jogador["Email"] == email:
                return jogador
        return None
    

