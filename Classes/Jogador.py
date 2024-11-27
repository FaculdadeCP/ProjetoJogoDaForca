class Jogador:
    def __init__(self, email, nome, pontuacao_maxima=0, ultima_pontuacao=0, posicao_ranking=0):
        self.email = email
        self.nome = nome
        self.pontuacao_maxima = pontuacao_maxima
        self.ultima_pontuacao = ultima_pontuacao
        self.posicao_ranking = posicao_ranking

    def atualizar_pontuacao(self, nova_pontuacao):
        self.ultima_pontuacao = nova_pontuacao
        if nova_pontuacao > self.pontuacao_maxima:
            self.pontuacao_maxima = nova_pontuacao

    def atualizar_posicao(self, nova_posicao):
        self.posicao_ranking = nova_posicao

    def __str__(self):
        return (f"Nome: {self.nome}, Email: {self.email}, "
                f"Pontuação Máxima: {self.pontuacao_maxima}, Última Pontuação: {self.ultima_pontuacao}, "
                f"Posição no Ranking: {self.posicao_ranking}")

    def to_dict(self):
        return {
            "Email": self.email,
            "Nome": self.nome,
            "PontuacaoMaxima": self.pontuacao_maxima,
            "UltimaPontuacao": self.ultima_pontuacao,
            "PosicaoRanking": self.posicao_ranking
        }

    @staticmethod
    def from_dict(dados):
        return Jogador(
            email=dados["Email"],
            nome=dados["Nome"],
            pontuacao_maxima=int(dados["PontuacaoMaxima"]),
            ultima_pontuacao=int(dados["UltimaPontuacao"]),
            posicao_ranking=int(dados["PosicaoRanking"])
        )
