import numpy as np
import random

#Aqui estou usando Arrays pois sei o tamanho total de cada tema, para essa primeria parte o tamanho total é de 40 itens por tema

animais = np.array([
    "Cachorro", "Gato", "Leão", "Tigre", "Elefante", "Girafa", "Cavalo", "Macaco",
    "Zebra", "Panda", "Rinoceronte", "Hipopótamo", "Canguru", "Urso", "Lobo",
    "Raposa", "Coelho", "Ovelha", "Vaca", "Porco", "Cabra", "Javali", "Leopardo",
    "Águia", "Falcão", "Tartaruga", "Jacaré", "Crocodilo", "Tubarão", "Golfinho",
    "Baleia", "Pinguim", "Lince", "Camelo", "Dromedário", "Esquilo", "Cobra",
    "Coruja", "Papagaio", "Flamingo", "Gavião"
])

paises = np.array([
    "Brasil", "Argentina", "Estados Unidos", "Canadá", "México", "Alemanha", "França", 
    "Espanha", "Itália", "Portugal", "Japão", "China", "Índia", "Rússia", "Austrália", 
    "Nova Zelândia", "África do Sul", "Egito", "Nigéria", "Marrocos", "Arábia Saudita", 
    "Israel", "Turquia", "Grécia", "Reino Unido", "Irlanda", "Suécia", "Noruega", 
    "Dinamarca", "Finlândia", "Coreia do Sul", "Indonésia", "Filipinas", "Tailândia", 
    "Vietnã", "Colômbia", "Peru", "Chile", "Venezuela", "Cuba", "Uruguai"
])

comidas = np.array([
    "Feijoada", "Pão de queijo", "Brigadeiro", "Coxinha", "Acarajé", "Moqueca", "Farofa", 
    "Vatapá", "Baião de dois", "Churrasco", "Tapioca", "Quindim", "Arroz carreteiro", 
    "Caldo de cana", "Pastel", "Bolinho de chuva", "Cuscuz", "Rabada", "Empadão", 
    "Escondidinho", "Canjica", "Pamonha", "Arroz de leite", "Bolo de rolo", "Tacacá", 
    "Dobradinha", "Galinhada", "Polenta", "Caruru", "Mungunzá", "Sarapatel", 
    "Peixada", "Feijão tropeiro", "Bobó de camarão", "Vaca atolada", "Maniçoba", 
    "Curau", "Bolinho de bacalhau", "Bolo de milho", "Frango com quiabo", "Paçoca"
])

objetos = np.array([
    "Mesa", "Cadeira", "Lâmpada", "Telefone", "Computador", "Relógio", "Chave", 
    "Bicicleta", "Carro", "Caneta", "Lápis", "Caderno", "Livro", "Copo", "Garfo", 
    "Colher", "Faca", "Prato", "Janela", "Porta", "Televisão", "Fone de ouvido", 
    "Mochila", "Óculos", "Sapato", "Camisa", "Geladeira", "Fogão", "Micro-ondas", 
    "Sofá", "Cama", "Tapete", "Chuveiro", "Espelho", "Escova de dentes", "Pente", 
    "Bolsa", "Carteira", "Guarda-chuva", "Caneca", "Abajur"
])

def escolher_tema_palavra():
    # Dicionário com os arrays e seus nomes
    temas = {
        "Animais": animais,
        "Países": paises,
        "Comidas": comidas,
        "Objetos": objetos
    }
    
    # Escolher um tema aleatoriamente
    tema_escolhido = random.choice(list(temas.keys()))
    
    # Escolher uma palavra aleatória do array escolhido
    palavra_escolhida = random.choice(temas[tema_escolhido])
    
    # Retornar a string formatada com o separador "|"
    return f"{tema_escolhido} | {palavra_escolhida}"

