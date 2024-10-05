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

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

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

# Set the aesthetic style of the plots
sns.set_style("whitegrid")
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

# Load dataset
df = pd.read_csv('day.csv')

# ---- RFM Analysis ----
# Menghitung Recency (dari tanggal terbaru dalam dataset)
current_date = pd.to_datetime(df['dteday'].max())  # Menggunakan tanggal terakhir dalam dataset
df['dteday'] = pd.to_datetime(df['dteday'])
df['Recency'] = (current_date - df['dteday']).dt.days

# Menghitung Frequency (berdasarkan jumlah hari)
df['Frequency'] = 1  # Karena data per hari, setiap hari dihitung sebagai satu penyewaan

# Menghitung Monetary (menggunakan jumlah penyewaan per hari)
df['Monetary'] = df['cnt']  # Jumlah penyewaan per hari

# Menggabungkan nilai RFM
rfm_df = df[['dteday', 'Recency', 'Frequency', 'Monetary']]

# Menampilkan hasil RFM
print("### RFM Analysis")
print(rfm_df.head())

# ---- Geoanalysis ----
# Geoanalysis dengan 'season'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='season', y='cnt', size='cnt', sizes=(20, 200), data=df, alpha=0.8, palette='coolwarm', edgecolor='black')
plt.title('Penyewaan Sepeda Berdasarkan Musim', fontsize=20, fontweight='bold')
plt.xlabel('Musim', fontsize=14, labelpad=15)
plt.ylabel('Jumlah Penyewaan', fontsize=14, labelpad=15)
plt.xticks(ticks=[0, 1, 2, 3], labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# ---- Clustering ----
# Mengambil dua fitur untuk clustering
data = df[['atemp', 'hum']]

# Menentukan jumlah cluster
num_clusters = 3  # Misalkan kita ingin 3 cluster

# Menghitung centroid secara manual (gunakan rata-rata)
centroids = data.groupby(np.floor(data.index / (len(data) / num_clusters))).mean().reset_index(drop=True)

# Menetapkan cluster ke setiap data
data['Cluster'] = (data.index // (len(data) // num_clusters))

# Visualisasi hasil clustering
plt.figure(figsize=(10, 6))
sns.scatterplot(x='atemp', y='hum', hue='Cluster', data=data, palette='Set1', s=100, alpha=0.8, edgecolor='black')
plt.scatter(centroids['atemp'], centroids['hum'], color='black', marker='X', s=200, label='Centroids')
plt.title('Clustering Penyewaan Sepeda Berdasarkan Suhu dan Kelembapan', fontsize=20, fontweight='bold')
plt.xlabel('Suhu (atemp)', fontsize=14, labelpad=15)
plt.ylabel('Kelembapan (hum)', fontsize=14, labelpad=15)
plt.legend(title='Cluster', loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# ---- Insights ----
print("\n--- Insight RFM Analysis ---")
print("Jumlah penyewaan harian sangat bervariasi, tetapi puncaknya terjadi selama bulan-bulan hangat, seperti Juni hingga Agustus. "
      "Ini menunjukkan bahwa permintaan sepeda lebih tinggi selama musim panas, yang mungkin mengindikasikan peluang bisnis yang lebih besar di masa ini.")

print("\n--- Insight Geoanalysis ---")
print("Penyewaan sepeda sangat dipengaruhi oleh musim, dengan tingkat penyewaan yang tertinggi pada musim panas dan terendah pada musim dingin. "
      "Ini dapat membantu perencana transportasi atau bisnis penyewaan sepeda untuk memperkirakan stok sepeda dan promosi musiman yang lebih efektif.")

print("\n--- Insight Clustering ---")
print("Kondisi cuaca memainkan peran penting dalam memengaruhi pola penyewaan sepeda. Pengguna cenderung lebih aktif pada hari-hari yang lebih cerah, hangat, dan tidak terlalu lembap. "
      "Faktor cuaca bisa digunakan sebagai indikator prediksi permintaan penyewaan sepeda.")

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
