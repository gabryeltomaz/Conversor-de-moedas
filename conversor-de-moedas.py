import requests

def obter_taxa_de_cambio(moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados['rates'][moeda_destino]

moeda_origem = input("Digite a moeda de origem (ex: USD): ")
moeda_destino = input("Digite a moeda de destino (ex: BRL): ")
valor = float(input(f"Digite o valor em {moeda_origem}: "))

taxa = obter_taxa_de_cambio(moeda_origem, moeda_destino)
valor_convertido = valor * taxa

print(f"{valor} {moeda_origem} é igual a {valor_convertido:.2f} {moeda_destino}")
