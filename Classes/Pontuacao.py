class Pontuacao:
    def __init__(self, jogador, data):
        self.jogador = jogador
        self.data = data
        self.pontuacao_total = 0
        self.combo_atual = 0  # Contador para o combo atual
        self.maior_combo = 0  # Maior sequência de acertos consecutivos

    def calcular_pontuacao_nivel(self, tamanho_palavra, dificuldade, tentativas_necessarias, erros_restantes):
        """
        Calcula a pontuação do nível com o bônus por combo.
        """
        return (tamanho_palavra + dificuldade) * (tentativas_necessarias + erros_restantes) + self.maior_combo

    def registrar_acerto(self):
        """
        Incrementa o combo atual e atualiza o maior combo se necessário.
        """
        self.combo_atual += 1
        if self.combo_atual > self.maior_combo:
            self.maior_combo = self.combo_atual

    def registrar_erro(self):
        """
        Reseta o combo atual ao registrar um erro.
        """
        self.combo_atual = 0

    def atualizar_pontuacao_total(self, pontos):
        """
        Incrementa a pontuação total do jogador com os pontos do nível.
        """
        self.pontuacao_total += pontos

    def exibir_pontuacao(self):
        """
        Exibe as pontuações e o maior combo.
        """
        print(f"\n=== Pontuação ===")
        print(f"Última Pontuação: {self.pontuacao_total}")
        print(f"Pontuação Total Acumulada: {self.jogador.pontuacao_maxima}")
        print(f"Maior Combo no Nível: {self.maior_combo}")
        print("=================\n")

    def salvar_pontuacao(self, pontos_nivel):
        if pontos_nivel <= 0: 
            pontos_nivel = 0
        self.atualizar_pontuacao_total(pontos_nivel)

        jogador_atual = self.data.buscar_jogador(self.jogador.email)
        if jogador_atual:
            pontuacao_maxima = max(int(jogador_atual["PontuacaoMaxima"]), self.pontuacao_total)

            self.data.atualizar_jogador(
                email=self.jogador.email,
                pontuacao_maxima=pontuacao_maxima,
                ultima_pontuacao=self.pontuacao_total
            )

            self.jogador.pontuacao_maxima = pontuacao_maxima
            self.jogador.ultima_pontuacao = self.pontuacao_total

            # Atualiza o ranking
            self.atualizar_posicao_ranking()
            print("\nPontuação salva com sucesso!")

    def atualizar_posicao_ranking(self):
        jogadores = self.data.listar_jogadores()
        # Ordena jogadores pela pontuação máxima em ordem decrescente
        jogadores_ordenados = sorted(jogadores, key=lambda x: int(x["PontuacaoMaxima"]), reverse=True)

        for posicao, jogador in enumerate(jogadores_ordenados, start=1):
            # Atualiza a posição no CSV
            self.data.atualizar_jogador(
                email=jogador["Email"],
                posicao_ranking=posicao
            )

            # Atualiza a posição do jogador atual no objeto
            if jogador["Email"] == self.jogador.email:
                self.jogador.posicao_ranking = posicao

        print(f"Sua posição no ranking foi atualizada: {self.jogador.posicao_ranking}")
