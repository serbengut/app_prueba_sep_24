import pandas as pd
import seaborn as sns
import streamlit as st

df = sns.load_dataset('tips')

seleccion = st.selectbox('Elige:',['Male','Female'])

g = sns.displot(data = df.loc[df.sex == seleccion], x = 'total_bill',kind= 'kde')

st.pyplot(g)