import streamlit as st
import pandas as pd
import yfinance as yf
import investpy as inv
import seaborn as sns 
import matplotlib.pyplot as plt
from datetime import date
import MetaTrader5 as mt5
from bcb import sgs 



def Atividade():
      st.title('PIB')

      
      pib = sgs.get({'PIB':7326})

      st.bar_chart(pib,)

      st.markdown('-----')

      st.title('PIB SERVIÇOS')

      PS = sgs.get({'PS':7329})
      
      st.bar_chart(PS)

      st.markdown('--')

      st.title('IBC_br')

      ibc = sgs.get({'ibc':7329})

      st.bar_chart(ibc)

      st.markdown('----')

      st.title('População')

      populacao = sgs.get({'populacao':21774})

      st.area_chart(populacao)


#primeira parte do dash


def main():
    st.title('Mapa Econômico')
    st.markdown('-----')
    Indicadores = ['Atividade','Inflação','Dívida']
    escolha = st.sidebar.radio('Indicadores',Indicadores)
    st.image('brasil.jpg',caption='Mapa Econômico')


    if escolha == 'Atividade':
        Atividade()

    if escolha == 'Inflação':
        Inflação()

    if escolha == 'Dívida':
        Dívida()

main()


   
     


def Inflação():
    Inflação = sgs.get({'IPCA',7478})    


def Dívida():
    Dívida = sgs.get({'DIVIDA',11420})  
      