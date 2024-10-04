# -*- coding: utf-8 -*-
"""Proyek Analisis Data: Bike Sharing Dataset
- **Nama:** Jenny Rahma Hidaya
- **Email:** m191b4kx2057@bangkit.academy
- **ID Dicoding:** jennyrhmaa
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
df = pd.read_csv('day.csv')

# Data Wrangling
# Check for missing data
if df.isnull().sum().sum() == 0:
    st.write("Tidak ada missing values pada dataset.")
else:
    st.write("Ada missing values pada dataset.")

# Check for outliers
st.write("Statistik Deskriptif:")
st.write(df.describe())

# Cleaning Data
df['season'] = df['season'].astype('category')

# Exploratory Data Analysis (EDA)
# Visualize bike rentals per season
st.title('Analisis Penyewaan Sepeda')
st.subheader('Penyewaan Sepeda per Musim')
season_fig = plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=df)
plt.title('Bike Rentals by Season')
st.pyplot(season_fig)

# Insight
st.write("Insight: Penggunaan sepeda tampak lebih tinggi selama musim panas dan lebih rendah di musim dingin.")

# Correlation Analysis
st.subheader('Analisis Korelasi')
correlation = df[['atemp', 'hum', 'windspeed', 'cnt']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Korelasi antara Variabel Cuaca dan Penyewaan Sepeda')
st.pyplot(plt.gcf())  

# Monthly bike rentals
df['mnth'] = pd.to_datetime(df['dteday']).dt.month
st.subheader('Tren Penyewaan Sepeda per Bulan')
month_fig = plt.figure(figsize=(10, 6))
sns.lineplot(x='mnth', y='cnt', data=df)
plt.title('Tren Penyewaan Sepeda per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(month_fig)

# Conclusion
st.subheader('Kesimpulan')
st.write(
    "Kesimpulan Pertanyaan 1: Faktor cuaca seperti suhu dan musim memiliki pengaruh besar terhadap penyewaan sepeda."
)
st.write(
    "Kesimpulan Pertanyaan 2: Pola penyewaan sepeda bervariasi berdasarkan musim, dengan penggunaan tertinggi di musim panas dan terendah di musim dingin."
)

