from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model hasil training
model = joblib.load("model.pkl")

# Inisialisasi FastAPI
app = FastAPI(
    title="API Prediksi Kepuasan Pelanggan",
    description="API sederhana untuk memprediksi kepuasan pelanggan",
    version="1.0"
)

# Format input data
class InputData(BaseModel):
    features: list

# Endpoint root
@app.get("/")
def root():
    return {"message": "API Kepuasan Pelanggan berhasil dijalankan"}

# Endpoint prediksi
@app.post("/predict")
def predict(data: InputData):
    data_array = np.array(data.features).reshape(1, -1)
    hasil = model.predict(data_array)
    return {"hasil_prediksi": int(hasil[0])}
