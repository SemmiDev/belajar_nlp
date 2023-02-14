## PREPROCESSING

### TEXT CLEANING

```python
import re

def text_cleaning(text):
    # Menghapus tanda baca dan angka
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    # Menghapus spasi ganda
    text = re.sub(r'\s+', ' ', text)
    # Menormalkan teks menjadi huruf kecil
    text = text.lower()
    return text

# Contoh teks yang akan dicleaning
text = "Berikut adalah contOh tEks 123 untUK TExt clEANing!!"

# Menjalankan text cleaning
text = text_cleaning(text)

print("Hasil text cleaning:", text)


# UNTUK BAHASA INDONESIA

        def text_cleaning(text):
            # Tokenisasi teks
            words = word_tokenize(text)
            # Menghapus stopword
            # englis, indonesian (di, dan, dan lain-lain)
            stop_words = set(stopwords.words("indonesian"))
            words = [word for word in words if word.lower() not in stop_words]
            # Menggabungkan kembali kata-kata yang sudah dicleaning menjadi teks
            text = " ".join(words)
            return text

        # Contoh teks yang akan dicleaning
        text = "Berikut adalah contOh di tEks 123 untUK TExt clEANing!!"

        # Menjalankan text cleaning
        text = text_cleaning(text)

        print("Hasil text cleaning:", text) # -> hasil text cleaning: contOh tEks 123 TExt clEANing ! !

```


### TEXT CLEANING

Setelah melakukan text cleaning, langkah berikutnya dalam proses text normalization adalah mengonversikan teks menjadi bentuk yang lebih standar. Proses ini dapat meliputi beberapa tahap, seperti:

- Menghapus karakter yang tidak diperlukan seperti tanda baca, angka, dan simbol.
- Menkonversi teks menjadi huruf kecil atau huruf besar.
- Menghapus spasi yang berlebihan.
- Menghapus kata-kata yang sama.

```python
import re

def normalize_text(text):
    text = text.lower() # konversi teks menjadi huruf kecil
    text = re.sub(r'[^a-zA-Z\s]', '', text) # hapus karakter yang tidak diperlukan
    text = re.sub(r'\s+', ' ', text) # hapus spasi yang berlebihan
    return text
```

Dengan kode di atas, kita melakukan konversi teks menjadi huruf kecil dengan menggunakan method lower(). Kemudian, kita menghapus karakter yang tidak diperlukan dengan menggunakan regular expression (regex) dan re.sub(). Regex [^a-zA-Z\s] berarti hapus semua karakter selain huruf besar atau kecil dan spasi. Regex \s+ berarti hapus spasi yang berlebihan.

Contoh menggunakan library sastrawi

```python
from Sastrawi.Normalizer.NormalizerFactory import NormalizerFactory

normalizer = NormalizerFactory().create_normalizer()

def normalize_text(text):
    return normalizer.normalize(text)
```
