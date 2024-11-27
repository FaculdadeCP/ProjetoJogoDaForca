from Classes.Jogador import Jogador
from Classes.Jogo import Jogo

class Menu:
    def __init__(self, data):
        self.data = data

    def atualizar_ranking(self):
        jogadores = self.data.listar_jogadores()
        jogadores_ordenados = sorted(jogadores, key=lambda x: int(x["PontuacaoMaxima"]), reverse=True)

        for posicao, jogador in enumerate(jogadores_ordenados, start=1):
            self.data.atualizar_jogador(
                email=jogador["Email"],
                posicao_ranking=posicao
            )

    def obter_jogador(self):
        while True:
            email = input("Informe seu email: ")
            jogador_data = self.data.buscar_jogador(email)
            
            if jogador_data:
                senha_arquivo = jogador_data["Senha"]
                senha = input("Informe sua senha: ")
                if senha == senha_arquivo:
                    # Atualiza o ranking antes de retornar o jogador
                    self.atualizar_ranking()
                    jogador = Jogador.from_dict(jogador_data)

                    print(f"\nBem vindo(a)! {jogador.nome}")
                    print(f"Sua pontuação do último jogo foi: {jogador.ultima_pontuacao}")
                    print(f"Sua pontuação máxima foi: {jogador.pontuacao_maxima}")
                    print(f"Sua posição no ranking é: {jogador.posicao_ranking}\n")
                    return jogador
                else:
                    print("Senha incorreta! Tente novamente.")
            else:
                print("Email não cadastrado. Vamos criar uma nova conta!")
                nome = input("Informe seu nome: ")
                senha = input("Crie uma senha: ")
                novo_jogador = Jogador(email=email, nome=nome)
                self.data.adicionar_jogador(email, nome, senha, novo_jogador.pontuacao_maxima, novo_jogador.ultima_pontuacao, novo_jogador.posicao_ranking)
                print("Conta criada com sucesso! Faça login novamente.")
                return None

    def exibir_top_5(self):
        self.atualizar_ranking()  # Garante que o ranking está atualizado
        jogadores = self.data.listar_jogadores()
        top_5 = sorted(jogadores, key=lambda x: int(x["PontuacaoMaxima"]), reverse=True)[:5]
        print("\n=== Top 5 do Ranking ===")
        for i, jogador in enumerate(top_5, start=1):
            print(f"{i}. {jogador['Nome']} - Pontuação Máxima: {jogador['PontuacaoMaxima']}")
        print("========================\n")


    def exibir_menu_principal(self, jogador):
        while True:
            print("O que você deseja fazer?")
            print("1- Jogar")
            print("2- Ver top 5 do ranking")
            print("3- Sair")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                # Passa o jogador e o data para o jogo
                jogo = Jogo(jogador, self.data)
                jogo.jogar() 
            elif opcao == "2":
                self.exibir_top_5()
            elif opcao == "3":
                print("\nSaindo... Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.")

