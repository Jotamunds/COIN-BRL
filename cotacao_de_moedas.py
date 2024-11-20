import requests

class Moeda:
    def __init__(self):
        self.escolherMoeda()

    def escolherMoeda(self):
        moedaEscolhida = input("Digite o código da moeda desejada: ").upper()
        self.exibirMoeda(moedaEscolhida)

    def exibirMoeda(self, moeda):
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL")
        dicionario = requisicao.json()
        cotacao = dicionario[f"{moeda}BRL"]["bid"]

        print(f"{moeda}-BRL\nCotação: R${cotacao}")

if __name__ == "__main__":
    funcionando = True
    while funcionando:
        escolha = int(input("1 - Ver cotação\n2 - Sair\nEscolha: "))
        if escolha == 1:
            Moeda()
        elif escolha == 2:
            print("Fim do programa")
            funcionando = False
        else:
            print("ERRO - Valor inválido")
            funcionando = False