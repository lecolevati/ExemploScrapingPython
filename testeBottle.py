import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup
from bottle import route, run, request, get

def scrap(codigo):
    site = 'http://www.leandrocolevati.com.br/materiais?disciplina='+codigo
    print(site)
    req = requests.get(site)

    if req.status_code == 200:
        # print('Requisição bem sucedida!')
        content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find(name='table')
    table_str = str(table)
    df = pd.read_html(table_str)[0]
    # print(df)
    lista = soup.find(class_='table')
    lista_items = lista.find_all('a')
    elementos = ""
    for element in lista_items:
        elementos = elementos + "idFile in Google Drive: "+element.get("href").split("=")[1].split("&")[0]+" - File: "+ element.get("href").split("=")[2]
        elementos = elementos+"</br>"
    return elementos

@get('/scrap')
def message():

    codigo = request.query.codigo
    return scrap(codigo)

run(host='localhost', port=8080, debug=True)
