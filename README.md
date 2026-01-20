Customer Satisfaction Prediction System 📊

Final Project Machine Learning (UAS)
Aplikasi berbasis Web untuk memprediksi kepuasan pelanggan menggunakan algoritma Random Forest Classifier.

⸻

📖 Deskripsi Proyek (Laporan Teknis)

Proyek ini bertujuan untuk membantu perusahaan dalam memahami tingkat kepuasan pelanggan berdasarkan data historis pelanggan. Dengan memanfaatkan pendekatan Machine Learning, sistem ini mampu melakukan analisis data secara objektif dan menghasilkan prediksi kepuasan pelanggan yang dapat digunakan sebagai dasar pengambilan keputusan bisnis.

Sistem dibangun menggunakan pendekatan End-to-End Machine Learning, mulai dari pengolahan dataset, pelatihan model, hingga implementasi model ke dalam aplikasi berbasis web menggunakan FastAPI.

⸻

1️⃣ Dataset & Fitur

Sumber Data:
Dataset Kepuasan Pelanggan yang diperoleh dari platform Kaggle.

Fitur Input (X):
Beberapa atribut pelanggan seperti:
	•	Gender
	•	SeniorCitizen
	•	Partner
	•	Dependents
	•	Tenure
	•	PhoneService
	•	InternetService
	•	OnlineSecurity
	•	TechSupport
	•	Contract
	•	PaperlessBilling
	•	PaymentMethod
	•	MonthlyCharges
	•	TotalCharges

Target Output (y):
	•	Churn (indikator kepuasan pelanggan: bertahan atau tidak)

⸻

2️⃣ Metodologi (Preprocessing)

Agar model dapat bekerja secara optimal, dilakukan beberapa tahapan preprocessing pada file train.py, yaitu:
	•	Data Cleaning: Menghapus atau menangani data kosong (missing values)
	•	Encoding Data: Mengubah data kategorikal menjadi numerik
	•	Feature Selection: Memilih fitur yang relevan terhadap kepuasan pelanggan
	•	Data Splitting: Membagi dataset menjadi 80% data latih (training) dan 20% data uji (testing)

⸻

3️⃣ Algoritma & Model

Algoritma:
Random Forest Classifier

Alasan Pemilihan:
Algoritma ini merupakan metode ensemble yang mampu:
	•	Menangani data dengan banyak fitur
	•	Mengurangi risiko overfitting
	•	Memberikan performa klasifikasi yang cukup baik

Evaluasi Model:
Model dievaluasi menggunakan:
	•	Akurasi
	•	Precision
	•	Recall
	•	F1-Score

Hasil evaluasi menunjukkan bahwa model mampu memprediksi kepuasan pelanggan dengan performa yang cukup baik.

⸻

👤 Identitas Mahasiswa
	Nama: Jihan Revalien Wahyudi
	NIM: 2441017
	Mata Kuliah: Machine Learning

⸻

📂 Struktur Project

Berikut adalah penjelasan komponen teknis dalam repository ini:
	•	train.py
Script untuk membaca dataset CSV, melakukan preprocessing data, melatih model Machine Learning menggunakan Random Forest Classifier, dan menyimpan model ke dalam file .pkl.
	•	main.py
Backend aplikasi menggunakan FastAPI yang bertugas memuat model dan melayani request prediksi kepuasan pelanggan.
	•	index.html
Tampilan antarmuka web sederhana yang digunakan untuk memasukkan data pelanggan dan menampilkan hasil prediksi.
	•	requirements.txt
Daftar library Python yang dibutuhkan agar aplikasi dapat dijalankan dengan baik.

⸻

🛠️ Cara Menjalankan Aplikasi (Installation Guide)

1️⃣ Persiapan Data
	•	Download repository ini
	•	Pastikan file dataset CSV berada dalam satu folder dengan train.py

2️⃣ Install Library
Buka terminal di folder project, lalu jalankan:
pip install -r requirements.txt

3️⃣ Training Model
Jalankan perintah berikut untuk melatih model:
python train.py
Pastikan file model.pkl berhasil dibuat.

4️⃣ Jalankan Server
Setelah model terbentuk, jalankan server FastAPI:
uvicorn main:app --reload

5️⃣ Buka Aplikasi
Buka browser dan akses:
http://127.0.0.1:8000

Atau untuk dokumentasi API:
http://127.0.0.1:8000/docs

Output Prediksi (Hasil Akhir Sistem)
Contoh Output JSON:
{
  "prediction": "Pelanggan Puas"
}

atau

{
  "prediction": "Pelanggan Tidak Puas"
}
