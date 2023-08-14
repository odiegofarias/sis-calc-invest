import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

options = Options()
options.add_argument('--headless=new')

navegador = webdriver.Chrome(options=options)

def acessa_caminho(xpath):
    caminho = navegador.find_element(by=By.XPATH, value=f'{xpath}')

    return caminho

def converte_p_float(taxa):
    try:
        taxa = taxa[7:11].replace(',', '.')
        taxa = float(taxa)

        return taxa
    except:
        return 'Não foi possível converter a taxa'

def acessa_tesouro():
    link = 'https://www.tesourodireto.com.br/titulos/precos-e-taxas.htm'
    navegador.get(url=link)
    sleep(2)

    fecha_cookies = acessa_caminho('//*[@id="onetrust-close-btn-container"]/button')
    fecha_cookies.click()
    sleep(1)

    taxa_str = acessa_caminho('//*[@id="td-ipca"]/div[2]/div[3]/div[1]/span').text
    print(converte_p_float(taxa_str))

def preco_atual_ativo(entrada):
    resposta = requests.get(f'https://statusinvest.com.br/fundos-imobiliarios/{entrada}', headers=headers)

    soup = BeautifulSoup(resposta.text, 'html.parser')

    preco_ativo = soup.find('div', {'title': 'Valor atual do ativo'})
    preco = preco_ativo.contents[5].text.replace(',', '.')
    print(float(preco))


if __name__ == '__main__':
    acessa_tesouro()
    preco_atual_ativo('RBRL11')
