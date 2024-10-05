# 🚴 Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini merupakan bagian dari analisis data yang bertujuan untuk memahami pola dan faktor-faktor yang memengaruhi penggunaan sepeda di layanan berbagi sepeda (bike sharing). Dengan menggunakan **Bike Sharing Dataset**, proyek ini menjawab dua pertanyaan utama:

1. **Apa faktor-faktor yang paling memengaruhi jumlah penyewaan sepeda harian?**
2. **Bagaimana pola penggunaan sepeda bervariasi berdasarkan waktu (musim, bulan, hari)?**

### Link ke Proyek
Anda dapat mengakses aplikasi ini di Streamlit: [**Bike Sharing Analysis**](#link-ke-streamlit-atau-repository).

---

## 📁 Struktur Proyek
- `day.csv` - Dataset bike-sharing harian.
- `proyek_analisis_data.py` - Script utama untuk analisis dan dashboard menggunakan Streamlit.
- `README.md` - Dokumentasi proyek.

---

## 📊 Data Wrangling & Pembersihan Data

Dataset **Bike Sharing** terdiri dari berbagai fitur, seperti:
- **Hari** (`dteday`): Tanggal penyewaan.
- **Musim** (`season`): Musim saat penyewaan dilakukan.
- **Suhu** (`temp`, `atemp`): Suhu saat penyewaan.
- **Kelembapan** (`hum`): Tingkat kelembapan saat penyewaan.
- **Jumlah sepeda** (`cnt`): Jumlah penyewaan sepeda per hari.

### Tahap 1: Pengumpulan Data
Dataset bike-sharing diambil dari file `day.csv` dan dimuat ke dalam program menggunakan `pandas`.

### Tahap 2: Penilaian dan Pembersihan Data
- Data diperiksa untuk **missing values** dan **outliers**. Berdasarkan hasil analisis, tidak ada missing values yang ditemukan di dataset.
- Fitur kategorikal seperti `season` diubah menjadi tipe data `category` untuk memudahkan visualisasi.

---

## 🔍 Exploratory Data Analysis (EDA)

### 1. **Penyewaan Sepeda Berdasarkan Musim**
Melalui visualisasi **boxplot**, kami menemukan bahwa penyewaan sepeda tertinggi terjadi selama musim panas, sedangkan penyewaan terendah terjadi di musim dingin.

### 2. **Analisis Korelasi**
Kami melakukan **analisis korelasi** antara variabel cuaca seperti `atemp` (suhu terasa), `hum` (kelembapan), `windspeed` (kecepatan angin), dan `cnt` (jumlah sepeda). Hasil korelasi menunjukkan bahwa suhu memiliki hubungan positif yang kuat terhadap jumlah penyewaan sepeda, sedangkan kecepatan angin memiliki hubungan negatif yang lebih lemah.

### 3. **Tren Penyewaan Sepeda per Bulan**
Analisis tren penyewaan sepeda per bulan menunjukkan fluktuasi musiman yang jelas, dengan puncak penyewaan terjadi di bulan-bulan musim panas.

---

## 🚴 Analisis Lanjutan

### 1. **RFM Analysis**
Kami menggunakan **RFM Analysis** untuk memahami perilaku penyewaan sepeda berdasarkan tiga faktor:
- **Recency**: Seberapa baru penyewaan terakhir.
- **Frequency**: Frekuensi penyewaan sepeda.
- **Monetary**: Jumlah penyewaan sepeda per hari.

Insight yang diperoleh:
- Nilai **Recency** yang lebih rendah menunjukkan bahwa pengguna lebih aktif baru-baru ini.
- **Monetary** memberikan gambaran tren penyewaan berdasarkan jumlah penyewaan harian.

### 2. **Geoanalysis Berdasarkan Musim**
Kami melakukan **geoanalysis** untuk melihat distribusi penyewaan berdasarkan musim. Hasil analisis menunjukkan bahwa penyewaan sepeda sangat dipengaruhi oleh musim, dengan musim panas sebagai periode paling sibuk.

### 3. **Clustering Berdasarkan Suhu dan Kelembapan**
Kami melakukan **clustering** untuk mengelompokkan data berdasarkan suhu dan kelembapan. Hasil clustering menunjukkan bahwa pengguna cenderung lebih aktif pada hari-hari yang hangat dan tidak terlalu lembap. Faktor cuaca ini dapat membantu memprediksi permintaan penyewaan sepeda di masa depan.

---

## 📝 Kesimpulan

### Pertanyaan 1: Apa faktor-faktor yang paling memengaruhi jumlah penyewaan sepeda harian?
- Faktor cuaca, seperti **suhu** dan **musim**, memiliki pengaruh besar terhadap jumlah penyewaan sepeda.
- Suhu yang lebih tinggi dan kondisi cuaca yang lebih nyaman cenderung meningkatkan penggunaan sepeda.

### Pertanyaan 2: Bagaimana pola penggunaan sepeda bervariasi berdasarkan waktu?
- Penggunaan sepeda tertinggi terjadi di **musim panas**, sementara penggunaan terendah terjadi di **musim dingin**.
- Tren musiman dan cuaca memengaruhi perilaku penyewaan sepeda, dan pola ini dapat digunakan untuk merencanakan operasional bisnis dan promosi.

---

## 📚 Teknologi yang Digunakan

- **Python**: Untuk analisis data dan machine learning.
- **Streamlit**: Untuk membangun dashboard interaktif.
- **Pandas**: Untuk pembersihan dan manipulasi data.
- **Matplotlib & Seaborn**: Untuk visualisasi data.
- **Scikit-learn**: Untuk clustering dan analisis lanjutan.

---

## 🚀 Cara Menjalankan Proyek

### 1. Clone Repository
```bash
git clone https://github.com/username/bike-sharing-analysis.git
cd bike-sharing-analysis

### 2. Install Requirements
```bash
pip install -r requirements.txt

### 3. Menjalankan Aplikasi Streamlit
streamlit run proyek_analisis_data.py
