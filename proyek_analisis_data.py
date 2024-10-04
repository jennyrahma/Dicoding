# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Bike Sharing Analysis", layout="wide")

# Display project information with styling
st.title("🚴 Proyek Analisis Data: Bike Sharing Dataset")
st.markdown("**Nama:** Jenny Rahma Hidaya")
st.markdown("**Email:** [m191b4kx2057@bangkit.academy](mailto:m191b4kx2057@bangkit.academy)")
st.markdown("**ID Dicoding:** jennyrhmaa")

# Load dataset
df = pd.read_csv('day.csv')

# Sidebar for user inputs
st.sidebar.header("Pengaturan")
selected_season = st.sidebar.selectbox("Pilih Musim", options=df['season'].unique())
st.sidebar.text("Penggunaan sepeda berdasarkan musim.")

# Display dataset
st.subheader("Dataset")
st.dataframe(df.style.highlight_max(axis=0))  # Highlight maximum values
st.write("- Dataset terdiri dari beberapa fitur seperti hari, musim, suhu, kelembaban, dan jumlah sepeda yang disewa per hari.")
st.write("- Anda dapat melihat beberapa variabel yang mungkin mempengaruhi penyewaan, seperti cuaca dan musim.")

# Tampilkan head dataset
st.subheader("5 Baris Pertama dari Dataset:")
st.write(df.head())

# Data Wrangling
if df.isnull().sum().sum() == 0:
    st.write("✅ Tidak ada missing values pada dataset.")
else:
    st.write("❌ Ada missing values pada dataset.")

# Check for outliers
st.subheader("Statistik Deskriptif:")
st.write(df.describe())

# Cleaning Data
df['season'] = df['season'].astype('category')

# Exploratory Data Analysis (EDA)
st.title('🔍 Analisis Penyewaan Sepeda')
st.subheader('📊 Penyewaan Sepeda per Musim')
season_fig = plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=df, palette="Set2")  # Added color palette
plt.title('Penyewaan Sepeda Berdasarkan Musim', fontsize=16)
plt.ylabel('Jumlah Penyewaan', fontsize=12)
plt.xlabel('Musim', fontsize=12)
st.pyplot(season_fig)

# Insight
st.write("Insight: Penggunaan sepeda tampak lebih tinggi selama musim panas dan lebih rendah di musim dingin.")

# Correlation Analysis
st.subheader('📈 Analisis Korelasi')
correlation = df[['atemp', 'hum', 'windspeed', 'cnt']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='YlGnBu', fmt=".2f")  # Changed color palette
plt.title('Korelasi antara Variabel Cuaca dan Penyewaan Sepeda', fontsize=16)
st.pyplot(plt.gcf())

# Monthly bike rentals
df['mnth'] = pd.to_datetime(df['dteday']).dt.month
st.subheader('📅 Tren Penyewaan Sepeda per Bulan')
month_fig = plt.figure(figsize=(10, 6))
sns.lineplot(x='mnth', y='cnt', data=df, marker='o', color='orange')  # Added markers and color
plt.title('Tren Penyewaan Sepeda per Bulan', fontsize=16)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(month_fig)

# Conclusion
st.subheader('📝 Kesimpulan')
st.write(
    "Kesimpulan Pertanyaan 1: Faktor cuaca seperti suhu dan musim memiliki pengaruh besar terhadap penyewaan sepeda."
)
st.write(
    "Kesimpulan Pertanyaan 2: Pola penyewaan sepeda bervariasi berdasarkan musim, dengan penggunaan tertinggi di musim panas dan terendah di musim dingin."
)

# Add a footer
st.markdown("---")
st.write("📊 *Data diambil dari Bike Sharing Dataset*")
