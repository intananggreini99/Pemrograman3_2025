# ... (kode impor lainnya) 
from exporters.csv_exporter import export_to_csv   
 
if __name__ == "__main__":   
    # ... (kode demonstrasi lainnya)   
    matriks_c = Matrix([[10, 20], [30, 40]])   
    print("Menyimpan Matriks C ke file CSV")   
    export_to_csv(matriks_c, "matriks_c.csv")   
