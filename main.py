# text preprocessing

# text cleaning
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("stopwords")
nltk.download("punkt")

def text_cleaning(text):
    # Tokenisasi teks
    words = word_tokenize(text)
    # Menghapus stopword
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.lower() not in stop_words]
    # Menggabungkan kembali kata-kata yang sudah dicleaning menjadi teks
    text = " ".join(words)
    return text

# Contoh teks yang akan dicleaning
text = "Berikut adalah contOh tEks 123 untUK TExt clEANing!!"

# Menjalankan text cleaning
text = text_cleaning(text)

print("Hasil text cleaning:", text)