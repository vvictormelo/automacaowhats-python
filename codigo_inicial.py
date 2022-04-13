import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USD']['bid']
    cotacao_euro = requisicao_dic['EUR']['bid']
    cotacao_btc = requisicao_dic['BTC']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto

janela = Tk()
janela.title("Cotação atual das Moedas")
janela.geometry("300x100")

texto_orientacao = Label(janela, text='Clique no botão para ver as cotações das moedas')
texto_orientacao.grid(column=0, row=0, padx=10, pady=15) # localização

botao = Button(janela, text="Buscar cotações Dólar/Euro/BTC", command=pegar_cotacoes) # função sem os parentese
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
