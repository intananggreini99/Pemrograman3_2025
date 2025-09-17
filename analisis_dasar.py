# analisis_dasar.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def analisis_dasar(file_path: str):
    """
    Fungsi untuk melakukan analisis dasar dataset.
    :param file_path: path ke file CSV
    """

    # Baca dataset
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print(f"❌ Gagal membaca file: {e}")
        sys.exit(1)

    print("===== INFORMASI DATASET =====")
    print(f"Jumlah baris: {data.shape[0]}")
    print(f"Jumlah kolom: {data.shape[1]}\n")

    print("===== 5 DATA TERATAS =====")
    print(data.head(), "\n")

    print("===== INFO DATASET =====")
    print(data.info(), "\n")

    print("===== DESKRIPSI STATISTIK =====")
    print(data.describe(include="all"), "\n")

    print("===== CEK MISSING VALUE =====")
    print(data.isnull().sum(), "\n")

    # Visualisasi distribusi nilai numerik
    num_cols = data.select_dtypes(include=["int64", "float64"]).columns
    if len(num_cols) > 0:
        print("===== DISTRIBUSI DATA NUMERIK =====")
        data[num_cols].hist(bins=20, figsize=(10, 8_]()
