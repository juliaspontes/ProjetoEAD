# -*- coding: utf-8 -*-
"""ProjetoPython.ipynb

Projeto em Python com análise de dados.

1 - Importando bibliotecas
"""

import os
import pandas as pd

lista_arquivos = os.listdir("/content/drive/MyDrive/ProjetoPyhton/Vendas")
print(lista_arquivos)
display(lista_arquivos)

from google.colab import drive
drive.mount('/content/drive')

"""2 - Importar base de dados"""

tabela_total = pd.DataFrame() #tabelavazia

for arquivo in lista_arquivos:
  #if not "Devolucoes" in arquivo: outra forma de pesquisar
  #if "Vendas" in arquivo.lower(): tranforma todos em letra minuscula
  if "Vendas" in arquivo: 
    tabela = pd.read_csv(f"/content/drive/MyDrive/ProjetoPyhton/Vendas/{arquivo}")
    tabela_total = tabela_total.append(tabela) #append = adicionando informação na tabela

display(tabela_total)

"""3 - Calculando os indicadores (agrupando grupo de itens e somando os valores)"""

tabela_produtos = tabela_total.groupby('Produto'). sum() #tabela de produtos agrupando os itens pelo group by 
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
display(tabela_produtos)

"""4 - Produto que mais faturou"""

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total ["Preco Unitario"]
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento [["Faturamento"]].sort_values(by="Faturamento", ascending=False)
display(tabela_faturamento)

"""5 - Loja que mais faturou"""

tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
display(tabela_lojas)

"""6 - Gráfico"""

import plotly.express as px #biblioteca que cria os gráficos

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento")
grafico.show()
