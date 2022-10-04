import requests
import json
import pandas as pd
import time
import os

data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []

while True:
    for informacoes in json_data['cand']:
    
         candidato.append(informacoes['nm'])
         votos.append(informacoes['vap'])
         porcentagem.append(informacoes['pvap'])
    
    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=['candidato', 'N° Votos', 'Porcentagem'])
    
    print(df_eleicao)
    
    print("Urnas Apuradas: " + json_data['pst'] + "%")
    candidato.clear()
    partido.clear()
    votos.clear()
    porcentagem.clear()
    time.sleep(30)
    os.system('clear')
