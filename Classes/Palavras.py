import requests

def obter_palavra(complexidade):
    """Função para obter uma palavra, categoria e complexidade da API."""
    # URL da API (substitua pela URL real da sua API)
    url = f"https://faccamp.pythonanywhere.com/hangman-api/getdata/{complexidade}"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 
        return resposta.json()
    except requests.RequestException as e:
        print(f"Erro ao obter a palavra da API: {e}")
        return None

def contar_letras(palavra):
    return len([char for char in palavra if char.isalpha()])

