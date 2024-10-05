# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Bike Sharing Analysis", layout="wide")

st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# Display project information
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🚴 Proyek Analisis Data: Bike Sharing Dataset</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)
st.write("**Nama:** Jenny Rahma Hidaya")
st.write("**Email:** m191b4kx2057@bangkit.academy")
st.write("**ID Dicoding:** jennyrhmaa")

st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)

## ---- Data Wrangling ----

### Gathering Data

# Load dataset
df = pd.read_csv('day.csv')

# Display dataset with improved visuals
st.subheader("📊 Dataset")
st.dataframe(df)  # Menampilkan DataFrame
st.write("-Dataset terdiri dari beberapa fitur seperti hari, musim, suhu, kelembaban, dan jumlah sepeda yang disewa per hari.")
st.write("-Anda dapat melihat beberapa variabel yang mungkin mempengaruhi penyewaan, seperti cuaca dan musim.")

### Assessing Data

# Tampilkan head dataset
st.subheader("📋 5 Baris Pertama dari Dataset:")
st.write(df.head())
if df.isnull().sum().sum() == 0:
    st.success("✅ Tidak ada missing values pada dataset.")
else:
    st.error("❌ Ada missing values pada dataset.")
# Insight
st.write("Insight: Beberapa fitur numerik seperti 'temp' (suhu) dan 'cnt' (jumlah sepeda) mungkin perlu divisualisasikan lebih lanjut untuk melihat distribusi data.")

# Check for outliers
st.subheader("📈 Statistik Deskriptif:")
st.write(df.describe())

### Cleaning Data

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

### Pertanyaan 1:
# Correlation Analysis
st.subheader('📊 Analisis Korelasi')
correlation = df[['atemp', 'hum', 'windspeed', 'cnt']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='YlGnBu', fmt=".2f")  # Changed color palette
plt.title('Korelasi antara Variabel Cuaca dan Penyewaan Sepeda', fontsize=16)
st.pyplot(plt.gcf())

### Pertanyaan 2
# Monthly bike rentals
df['mnth'] = pd.to_datetime(df['dteday']).dt.month
st.subheader('📅 Tren Penyewaan Sepeda per Bulan')
month_fig = plt.figure(figsize=(10, 6))
sns.lineplot(x='mnth', y='cnt', data=df, marker='o', color='orange')  # Added markers and color
plt.title('Tren Penyewaan Sepeda per Bulan', fontsize=16)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(month_fig)

## Analisis Lanjutan (Opsional)
# ---- RFM Analysis ----
# Add header and title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🚴 Analisis Lanjutan: Bike Sharing Dataset</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# Load dataset
df = pd.read_csv('day.csv')

# ---- RFM Analysis ----
st.subheader("📊 RFM Analysis")
st.markdown("""
    **RFM Analysis** membantu memahami perilaku penyewaan sepeda berdasarkan tiga faktor utama:
    - **Recency**: Seberapa baru penyewaan terakhir.
    - **Frequency**: Frekuensi penyewaan sepeda.
    - **Monetary**: Jumlah penyewaan sepeda per hari.
""")

# Menghitung Recency, Frequency, Monetary
current_date = pd.to_datetime(df['dteday'].max())  # Tanggal terakhir dalam dataset
df['dteday'] = pd.to_datetime(df['dteday'])
df['Recency'] = (current_date - df['dteday']).dt.days
df['Frequency'] = 1  # Karena data per hari
df['Monetary'] = df['cnt']  # Jumlah penyewaan per hari

# Menggabungkan nilai RFM
rfm_df = df[['dteday', 'Recency', 'Frequency', 'Monetary']]

# Tampilkan DataFrame RFM dengan format yang lebih menarik
st.subheader("📊 RFM Analysis")
st.markdown("""
    **RFM Analysis** membantu memahami perilaku penyewaan sepeda berdasarkan tiga faktor utama:
    - **Recency**: Seberapa baru penyewaan terakhir.
    - **Frequency**: Frekuensi penyewaan sepeda.
    - **Monetary**: Jumlah penyewaan sepeda per hari.
""")

# Tampilkan DataFrame RFM
st.write("Tabel RFM Analysis:")
st.dataframe(rfm_df.head().style.applymap(lambda x: 'background-color: #4CAF50' if x == rfm_df['Recency'].min() else '', subset=['Recency']))  # Highlight Recency terendah

# Menambahkan informasi tambahan
st.markdown("""
    **Insight**: 
    - **Recency** menunjukkan berapa lama sejak penyewaan terakhir, di mana nilai lebih rendah berarti penyewaan lebih baru.
    - **Frequency** mencerminkan berapa kali penyewaan terjadi.
    - **Monetary** mewakili jumlah total penyewaan sepeda per hari, memberikan gambaran tentang tren penyewaan.
""")

# ---- Geoanalysis ----
st.subheader("🗺️ Geoanalysis berdasarkan Musim")
st.markdown("Visualisasi penyewaan sepeda berdasarkan musim:")

# Plot Geoanalysis
plt.figure(figsize=(10, 6))
sns.scatterplot(x='season', y='cnt', size='cnt', sizes=(20, 200), data=df, alpha=0.6, palette='coolwarm')
plt.title('Penyewaan Sepeda Berdasarkan Musim', fontsize=16)
plt.xlabel('Musim', fontsize=12)
plt.ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(plt.gcf())

# Insight Geoanalysis
st.markdown("""
    **Insight Geoanalysis**:
    - Penyewaan sepeda sangat dipengaruhi oleh musim.
    - Tingkat penyewaan tertinggi terjadi selama musim panas dan terendah pada musim dingin.
    - Pemilik bisnis dapat merencanakan persediaan dan promosi musiman dengan lebih efektif.
""")

# ---- Clustering ----
st.subheader("🔍 Clustering Berdasarkan Suhu dan Kelembapan")
st.markdown("Kita menggunakan **clustering** untuk mengelompokkan data berdasarkan suhu dan kelembapan.")

# Mengambil dua fitur untuk clustering
data = df[['atemp', 'hum']]

# Menentukan jumlah cluster
num_clusters = 3  # Misalkan kita ingin 3 cluster

# Menghitung centroid secara manual (gunakan rata-rata)
centroids = data.groupby(np.floor(data.index / (len(data) / num_clusters))).mean().reset_index(drop=True)

# Menetapkan cluster ke setiap data
data['Cluster'] = (data.index // (len(data) // num_clusters))

# Plot Clustering
plt.figure(figsize=(10, 6))
sns.scatterplot(x='atemp', y='hum', hue='Cluster', data=data, palette='Set1', alpha=0.6)
plt.scatter(centroids['atemp'], centroids['hum'], color='black', marker='X', s=100, label='Centroids')
plt.title('Clustering Penyewaan Sepeda Berdasarkan Suhu dan Kelembapan', fontsize=16)
plt.xlabel('Suhu (atemp)', fontsize=12)
plt.ylabel('Kelembapan (hum)', fontsize=12)
plt.legend()
st.pyplot(plt.gcf())

# Insight Clustering
st.markdown("""
    **Insight Clustering**:
    - Pengguna cenderung lebih aktif pada hari-hari yang hangat dan tidak terlalu lembap.
    - Faktor cuaca ini dapat digunakan untuk memprediksi permintaan penyewaan sepeda.
""")

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
st.markdown("📊 *Data diambil dari Bike Sharing Dataset*")
