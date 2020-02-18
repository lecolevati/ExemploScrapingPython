import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup

def main():
    req = requests.get('http://www.leandrocolevati.com.br/materiais?disciplina=4703-010')

    if req.status_code == 200:
        # print('Requisição bem sucedida!')
        content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find(name='table')
    table_str = str(table)
    df = pd.read_html(table_str)[0]
    print(df)
    lista = soup.find(class_='table')
    lista_items = lista.find_all('a')
    for element in lista_items:
        print("idFile in Google Drive: "+element.get("href").split("=")[1].split("&")[0]+" - File: "+ element.get("href").split("=")[2])

if __name__ == '__main__':
    main()
