import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# ================================
# LOAD DATASET
# ================================
# Pastikan file CSV berada di folder yang sama dengan file ini
data = pd.read_csv("DATA KEPUASAN PELANGGAN.csv")

# ================================
# PREPROCESSING / ENCODING
# ================================
le = LabelEncoder()

data['Gender'] = le.fit_transform(data['Gender'])
data['Pelayanan'] = le.fit_transform(data['Pelayanan'])
data['Kebersihan'] = le.fit_transform(data['Kebersihan'])
data['Harga produk'] = le.fit_transform(data['Harga produk'])
data['Rekomendasi'] = le.fit_transform(data['Rekomendasi'])

# ================================
# SPLIT FITUR & TARGET
# ================================
X = data.drop('Rekomendasi', axis=1)
y = data['Rekomendasi']

# ================================
# SPLIT TRAIN & TEST
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================================
# TRAIN MODEL
# ================================
model = LogisticRegression()
model.fit(X_train, y_train)

# ================================
# SAVE MODEL
# ================================
joblib.dump(model, "model.pkl")

print("✅ Model berhasil dibuat dan disimpan sebagai model.pkl")
