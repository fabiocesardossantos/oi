import pandas as pd
import csv
import streamlit as st


tabela = pd.read_csv("planilhadolar.csv", sep = ",")


print(tabela)

st.write(tabela)
a = tabela.Date.Variacao
print(a)
st.write(a)
st.bar_chart(a)