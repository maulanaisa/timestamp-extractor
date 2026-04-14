# Memulai

Modul ini digunakan untuk ekstraksi titik koordinat di gambar dengan timestamp menggunakan OPENAI API.

## Persyaratan

Instal Python 3.14 di sistem anda.

## Instalasi virtual evironment dan library

Buka command prompt.

Lalu buka lokasi file modul yang disimpan.

Contoh : Misal modul disimpan di C:\Users\PLN\Documents\Teknik, maka ketik 
```bash
cd C:\Users\PLN\Documents\Teknik
```

Buat virtual environment.
```bash
python -m venv myenv
```

Lalu aktifkan virtual environment tersebut
```bash
myenv\Scripts\activate
```

Install kebutuhan library di requirements.txt menggunakan pip.
```bash
pip install -r requirements.txt
```

## Penggunaan

Open settings.py file to configure parameters.
Buka settings.py untuk melakukan konfigurasi parameter.

### Modul OpenAI API
Gunakan openai_api.py untuk ekstraksi koordinat dari gambar dengan timestamp. Ubah IMAGES_PATH sesuai dengan lokasi folder yang dikehendaki.

Lalu jalankan script nya.
```bash
python openai_api.py
```
ini akan menghasilkan output_open_ai.csv berisi filename, latitude, longitude.

### Modul Utama
Gunakan main.py untuk eksport workbook file (.xlsx) berisi gambar di IMAGES_PATH yang juga kebetulan sudah di list di output_openai_api.csv. File excel akan disimpan di EXPORT_PATH. Modul ini juga mampu memberikan lokasi berdasarkan file di LOCATION_COORDINATES.
```bash
python main.py
```
