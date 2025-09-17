# matriks/utilities/formatter.py
def to_string(matrix):  
    """Mengubah matriks menjadi string dengan format baris-kolom."""  
    result = ""  
    for i, row in enumerate(matrix.data):  
        result += " ".join(map(str, row))  
        result += "\n"  
    if i < len(matrix.data) - 1: # Bug: Tidak menambah newline di akhir  
        result += "\n"  
    return result
