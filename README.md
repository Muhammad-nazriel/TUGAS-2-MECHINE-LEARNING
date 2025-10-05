# 📚 Prediksi Nilai Matematika - Machine Learning Project

Project machine learning untuk memprediksi nilai matematika siswa berdasarkan jam belajar per minggu menggunakan Linear Regression.

## 🎯 Deskripsi Project

Aplikasi web berbasis Flask yang menggunakan model Linear Regression untuk memprediksi nilai matematika siswa berdasarkan jumlah jam belajar per minggu. Dataset yang digunakan adalah Student Scores yang berisi data performa akademik siswa.

## 📊 Dataset

- **Source**: Student Scores Dataset
- **Features**: 
  - `weekly_self_study_hours` (Jam belajar per minggu)
- **Target**: 
  - `math_score` (Nilai matematika)
- **Total Data**: 2000 records (setelah filtering: 1930 records)

## 🔍 Model Performance

- **R² Score**: 0.1333
- **RMSE**: 10.352

## 🛠️ Teknologi yang Digunakan

- **Backend**: Flask
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Frontend**: Bootstrap 5, HTML, CSS

## 📁 Struktur Project

```
TUGAS-2-MECHINE-LEARNING/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── data/
│   └── student-scores.csv  # Dataset
├── models/
│   └── model.pkl          # Trained model
├── notebooks/
│   ├── ta2.ipynb          # Training notebook
│   └── tp2.ipynb          # Additional notebook
├── static/                # Visualizations
│   ├── ta2_regression.png
│   ├── ta2_scatter.png
│   ├── ta2_residual.png
│   ├── ta2_heatmap.png
│   ├── ta2_histogram_x.png
│   └── ta2_histogram_y.png
└── templates/
    └── index.html         # Web interface
```

## 🚀 Cara Menjalankan

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Training Model (Opsional)

Jika ingin melatih ulang model, jalankan notebook:

```bash
jupyter notebook notebooks/ta2.ipynb
```

### 3. Jalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di `http://127.0.0.1:5000`

## 📈 Visualisasi

Aplikasi menampilkan 6 grafik visualisasi:

1. **Grafik Regresi Linear** - Hubungan antara jam belajar dan nilai
2. **Scatter Plot** - Sebaran data
3. **Residual Plot** - Analisis residual model
4. **Heatmap Korelasi** - Korelasi antar variabel
5. **Distribusi Jam Belajar** - Histogram jam belajar
6. **Distribusi Nilai Matematika** - Histogram nilai

## 💡 Cara Menggunakan

1. Buka aplikasi di browser
2. Masukkan jumlah jam belajar per minggu (contoh: 25)
3. Klik tombol "Prediksi Nilai Matematika"
4. Lihat hasil prediksi dan visualisasi data

## 📝 Catatan

- Model ini menggunakan Simple Linear Regression
- R² Score 0.1333 menunjukkan bahwa jam belajar memiliki korelasi positif namun lemah dengan nilai matematika
- Terdapat faktor lain yang mempengaruhi nilai matematika selain jam belajar

## 👨‍💻 Author

Tugas 2 - Machine Learning

## 📄 License

MIT License
