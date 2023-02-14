# INTRODUCTION

**Natural Language Processing (NLP)** adalah cabang dari ilmu komputer yang mempelajari bagaimana komputer dapat memahami, memanipulasi, dan membuat persepsi terhadap bahasa alami manusia. Ini mencakup berbagai bidang seperti pemrosesan bahasa, analisis sentimen, pengenalan vokal, dan banyak lagi.

Berikut adalah beberapa **komponen utama** dari NLP:

1.  **Tokenisasi**: Proses memecah teks menjadi bagian-bagian lebih kecil seperti kata, frase, klausa, dan lain-lain. Ini memungkinkan kita untuk memproses data teks secara lebih mudah dan efisien.

> Contoh: Jika ada teks "Saya sedang belajar NLP", maka setelah melalui proses tokenisasi akan menghasilkan: **["Saya", "sedang", "belajar", "NLP"]**
    
2.  **Stopword Removal**: Proses menghapus kata-kata yang sering muncul dan tidak memiliki makna yang signifikan, seperti "the", "a", "an", dan", "atau", "yang", dll.
    
3.  **Stemming**: Proses mengubah kata yang berbeda menjadi kata dasar yang sama, seperti "running" menjadi "run".
    
4.  **Named Entity Recognition (NER)**: Proses mengidentifikasi entitas nama seperti nama orang, tempat, organisasi, dan lain-lain. 
> Contoh: Jika ada teks "Barack Obama adalah presiden Amerika Serikat", maka setelah melalui proses Named Entity Recognition akan menghasilkan: **[(Barack Obama, PERSON), (Amerika Serikat, GPE)]**
    
5.  **Part-of-Speech Tagging (POS)**: Proses mengidentifikasi posisi kata dalam kalimat, seperti subjek, objek, kata sifat, dan lain-lain. Contoh: Jika kita memiliki ["Say"a, "sedang", "belajar", "NLP"], setelah melalui proses Part-of-Speech Tagging akan menghasilkan: **[(Saya, Noun), (sedang, Verb), (belajar, Verb), (NLP, Noun)]**
    
6.  **Dependency Parsing**: Proses menentukan hubungan antar kata dalam kalimat dan membentuk pohon dependensi (menganalisis hubungan gramatika). Ini membantu memahami struktur dan makna teks secara lebih mendalam.

> Contoh: Jika ada teks **"Barack Obama adalah presiden Amerika Serikat"**, maka setelah melalui proses **Dependency Parsing** akan menghasilkan representasi grafik seperti ini:

[Barack Obama] 
|
|--------- [adalah presiden] 
|
|------ [Amerika Serikat]
    
8.  **Sentiment Analysis**: Proses menentukan sentimen atau perasaan yang terkandung dalam teks, seperti positif, negatif, atau netral. 
> Contoh: Jika ada teks "Film ini sangat bagus", maka setelah melalui proses Sentiment Analysis akan menghasilkan sentimen **positif**.

9. **Topic Modelling** adalah proses menentukan topik atau tema yang terkandung dalam teks. Ini membantu memahami isi teks secara keseluruhan dan mengidentifikasi topik utama dalam dokumen-dokumen yang besar.

> Contoh: Jika kita memiliki kumpulan dokumen tentang berbagai topik seperti teknologi, bisnis, dan olahraga, maka setelah melalui proses Topic Modeling kita akan mendapatkan topik-topik seperti **teknologi, bisnis, dan olahraga yang mewakili setiap dokumen** 
    

# ROADMAP
Berikut adalah roadmap untuk belajar **NLP**

1.  Pelajari dasar-dasar pemrograman dan bahasa pemrograman seperti **Python**.
    
2.  Pelajari dasar-dasar ilmu data dan machine learning, seperti **statistik dan algoritma**.
    
3.  Pelajari tentang representasi teks seperti **bag-of-words, TF-IDF, dan word embeddings**.
    
4.  Pelajari NLP pemrosesan dasar seperti **tokenisasi, stopword removal, stemming, dan NER**.
    
5.  Pelajari teknik-teknik NLP lanjutan seperti **sentiment analysis, machine translation, dan text summarization**.
    
6.  Pelajari bagaimana mengaplikasikan teknik-teknik NLP menggunakan **bibliotek Python seperti NLTK, spaCy, dan PyTorch**.
    
7.  Pelajari bagaimana membangun proyek NLP sendiri dan membuat mode NLP yang berguna.
  
# CONT.

### Statistika
Dalam NLP, penting untuk memahami dasar-dasar ilmu data dan machine learning karena NLP sering menggunakan metodologi dan teknik-teknik dari kedua bidang tersebut.

Berikut adalah penjelasan lengkap tentang dasar-dasar ilmu data dan machine learning:

1.  Statistik: Statistik adalah cabang matematika yang mempelajari tentang pengumpulan, analisis, interpretasi, presentasi, dan organisasi data. Dalam NLP, statistik digunakan untuk memahami distribusi dan hubungan antara variabel dalam data teks.
    
2.  Algoritma: Algoritma adalah urutan langkah-langkah spesifik yang digunakan untuk menyelesaikan masalah. Dalam NLP, beberapa algoritma yang digunakan meliputi algoritma clustering, algoritma classification, dan algoritma regression.
    

Berikut adalah contoh aplikasi dasar-dasar ilmu data dan machine learning dalam NLP:

1.  Statistik: Dalam NLP, statistik digunakan untuk memahami distribusi kata dalam corpus (kumpulan teks). Misalnya, kita dapat menghitung frekuensi kata dan melihat kata apa yang paling sering muncul dalam corpus.
    
2.  Algoritma: Dalam NLP, algoritma machine learning digunakan untuk melakukan berbagai tugas seperti sentiment analysis, named entity recognition, dan text classification. Misalnya, kita dapat menggunakan algoritma Naive Bayes untuk melakukan sentiment analysis pada teks dengan mengklasifikasikan teks sebagai positif, negatif, atau netral.
    

Ini adalah gambaran umum dasar-dasar ilmu data dan machine learning dan bagaimana mereka digunakan dalam NLP. Dalam proses belajar, sangat penting untuk memahami teori dan konsep-konsep ini sebelum mempelajari teknik-teknik NLP lanjutan.


### Bag of Words
1. **Bag-of-Words**: Bag-of-Words adalah representasi dasar dari teks yang mengatakan bahwa sebuah dokumen dapat dinyatakan sebagai urutan kata-kata tanpa memperhatikan urutan kata atau grammar. Dalam model ini, setiap kata dalam dokumen dihitung dan diberikan bobot sesuai dengan frekuensi kemunculannya dalam dokumen tersebut.

Contoh: Jika ada dua dokumen A dan B, masing-masing berisi kata "satu", "dua", "tiga", dan "empat", maka representasi bag-of-words-nya akan menjadi:

Dokumen A: [1, 1, 1, 1] Dokumen B: [1, 1, 1, 1]

2.  **TF-IDF**: TF-IDF (Term Frequency - Inverse Document Frequency) adalah metode untuk menilai pentingnya sebuah kata dalam sebuah dokumen berdasarkan frekuensi kemunculannya dalam dokumen tersebut dan frekuensi kemunculan kata tersebut dalam seluruh dokumen dalam corpus. Dalam model ini, bobot kata yang sering muncul dalam sebuah dokumen akan lebih rendah dibandingkan dengan kata yang jarang muncul dalam dokumen lain.

**TF** (Term Frequency) adalah jumlah kemunculan suatu kata dalam sebuah dokumen. Semakin sering kata tersebut muncul dalam dokumen, maka TF-nya semakin tinggi.

**IDF** (Inverse Document Frequency) adalah logaritma dari jumlah dokumen yang ada dibagi dengan jumlah dokumen yang mengandung kata tersebut. Semakin jarang kata tersebut muncul dalam seluruh dokumen, maka IDF-nya semakin tinggi.

**TF-IDF** dapat ditemukan dengan mengalikan TF dengan IDF. Konsep ini membantu menentukan kepentingan suatu kata dalam dokumen tertentu dibandingkan dengan dokumen lain. Kata-kata yang memiliki nilai TF-IDF tinggi akan memiliki nilai penting yang lebih tinggi dalam dokumen tersebut.

Contoh penggunaan TF-IDF:

1.  Dokumen 1: "Kucing berlari di taman"
2.  Dokumen 2: "Anjing berlari di taman"
3.  Dokumen 3: "Kucing dan anjing berlari bersama di taman"

Kata-kata yang ada dalam korpus (seluruh dokumen) adalah: "kucing", "anjing", "berlari", "di", "taman", "dan", "bersama".

TF untuk setiap kata dalam setiap dokumen:

1.  Dokumen 1:

-   kucing: 1
-   berlari: 1
-   di: 1
-   taman: 1

2.  Dokumen 2:

-   anjing: 1
-   berlari: 1
-   di: 1
-   taman: 1

3.  Dokumen 3:

-   kucing: 1
-   anjing: 1
-   berlari: 1
-   di: 1
-   taman: 1
-   dan: 1
-   bersama: 1

IDF untuk setiap kata dalam korpus:

-   kucing: log(3/2)
-   anjing: log(3/2)
-   berlari: log(3/3)
-   di: log(3/3)
-   taman: log(3/3)
-   dan: log(3/1)
-   bersama: log(3/1)

TF-IDF untuk setiap kata dalam setiap dokumen:

1.  Dokumen 1:

-   kucing: 1 * log(3/2)
-   berlari: 1 * log(3/3)
-   di: 1 * log(3/3)
-   taman: 1 * log(3/3)

2.  Dokumen 2:

-   anjing: 1 * log(3/2)
-   berlari: 1 * log(3/3)
-   di: 1 * log(3/3)
-   taman: 1 * log(3/3)

3.  Dokumen 3:

-   kucing: 1 * log(3/2)
-   anjing: 1 * log(3/2)
-   berlari: 1 * log(3/3)
-   di: 1 * log(3/3)
-   taman: 1 * log(3/3)
-   dan: 1 * log(3/1)
-   bersama: 1 * log(3/1)

Dalam contoh ini, kata "dan" dan "bersama" memiliki nilai TF-IDF yang lebih tinggi dibandingkan dengan kata-kata lain, karena hanya muncul pada satu dokumen saja. Sebaliknya, kata-kata seperti "kucing", "anjing", "berlari", "di", dan "taman" memiliki nilai TF-IDF yang lebih rendah karena muncul pada semua dokumen.


3.  **Word Embeddings**: Word Embeddings adalah representasi vektor dari kata-kata dalam teks yang memperhitungkan hubungan semantik antar kata. Dalam model ini, kata-kata dalam teks diwakili oleh vektor yang memperhitungkan konteks dan hubungan antar kata.

Contoh: Jika kata "kucing" dan "anjing" memiliki hubungan yang erat dalam teks, maka kata "kucing" dan "anjing" akan berada dalam jarak yang dekat dalam ruang vektor. Sebaliknya, kata "kucing" dan "gunung" akan berada dalam jarak yang jauh dalam ruang vektor.

Ketiga representasi teks di atas adalah representasi dasar yang digunakan dalam NLP. Bag-of-Words dan TF-IDF digunakan untuk mengolah data teks dengan memperhitungkan frekuensi kata, sedangkan Word Embeddings memperhitungkan hubungan semantik antar kata. Pemahaman yang ba

# CONT.

Tokenisasi adalah proses memecah suatu teks menjadi bagian-bagian yang lebih kecil, biasanya kata-kata atau frasa. Tujuan tokenisasi adalah untuk mempermudah proses analisis teks selanjutnya.

Stopword removal adalah proses menghilangkan kata-kata yang tidak memiliki makna atau tidak memiliki informasi yang signifikan dalam suatu teks. Kata-kata seperti "di", "ke", "dari", "dan", dll, biasanya dianggap sebagai stopword dan dihilangkan dari teks.

Stemming adalah proses mengubah kata-kata menjadi bentuk dasar (root form) mereka. Hal ini dilakukan untuk mengurangi variasi kata-kata yang sama dan mengurangi ukuran data. Misalnya, kata "berlari" dan "berlari-lari" akan direduksi menjadi "lari".

Named Entity Recognition (NER) adalah proses identifikasi dan ekstraksi entitas nama dalam suatu teks. Entitas nama dapat berupa nama orang, organisasi, lokasi, produk, dll. Tujuan NER adalah untuk mempermudah pencarian informasi dalam teks dan mempermudah taks-taks seperti klasifikasi dan sumber.

Contoh NER: Dalam teks berikut: "Barack Obama berbicara di depan konferensi di Washington DC", entitas nama yang terdeteksi adalah "Barack Obama", "Washington DC", dan "konferensi".


# CONT.

**Sentiment Analysis** adalah proses menentukan sentimen atau emosi dalam suatu teks. Tujuannya adalah untuk memahami apakah teks memiliki sentimen positif, negatif, atau netral. Sentiment analysis sering digunakan dalam bidang bisnis untuk menilai sentimen pelanggan terhadap suatu produk atau jasa, atau dalam politik untuk menilai sentimen publik terhadap suatu isu.

**Machine Translation** adalah proses menterjemahkan suatu teks dari satu bahasa ke bahasa lain secara otomatis. Tujuannya adalah untuk mempermudah komunikasi antar bahasa dan mempermudah akses ke informasi dalam bahasa yang berbeda. Meskipun masih belum sempurna, teknologi machine translation telah sangat berkembang dan sering digunakan dalam aplikasi seperti browser web, aplikasi penerjemah, dan aplikasi komunikasi.

**Text Summarization** adalah proses mengurangi ukuran suatu teks dengan menyaring informasi yang tidak penting dan memberikan ringkasan informasi yang penting. Tujuannya adalah untuk mempermudah pemahaman dan mempercepat waktu membaca. Ada dua jenis utama text summarization: extractive summarization dan abstractive summarization. Extractive summarization memilih fragmen teks yang ada dalam teks asli dan menyusunnya menjadi ringkasan. Abstractive summarization membuat ringkasan baru dengan menggunakan konsep dan ide dari teks asli.

### TEXT SUMMARIZATION

Text summarization adalah salah satu bagian penting dari NLP yang berguna untuk mempermudah pemahaman dan mempercepat waktu membaca teks panjang dan kompleks. Ada dua jenis text summarization yaitu extractive summarization dan abstractive summarization.

Extractive summarization adalah proses memilih fragmen teks yang ada dalam teks asli dan menyusunnya menjadi ringkasan. Ini biasanya dilakukan dengan memilih fragmen teks yang paling penting berdasarkan beberapa metrik seperti frekuensi kata, informasi yang disampaikan, dan relevansi terhadap topik utama.

Abstractive summarization adalah proses membuat ringkasan baru dengan menggunakan konsep dan ide dari teks asli. Ini dilakukan dengan memahami makna dan konteks teks dan menggunakan konsep dan informasi yang penting untuk membuat ringkasan yang berbeda dari teks asli.

Untuk belajar text summarization, berikut adalah roadmap yang dapat Anda ikuti:

1.  Pelajari teori dasar text summarization, termasuk extractive summarization dan abstractive summarization.
2.  Pelajari bagaimana memilih fragmen teks untuk extractive summarization, termasuk menggunakan metrik seperti frekuensi kata, informasi yang disampaikan, dan relevansi terhadap topik utama.
3.  Pelajari bagaimana memahami makna dan konteks teks untuk abstractive summarization.
4.  Belajar menggunakan teknik NLP seperti tokenisasi, stopword removal, stemming, dan Named Entity Recognition untuk mempersiapkan teks untuk text summarization.
5.  Pelajari bagaimana membuat model text summarization menggunakan teknologi machine learning seperti deep learning atau reinforcement learning.
6.  Praktikkan teori dan teknik yang Anda pelajari dengan menggunakan dataset teks yang tersedia.
7.  Evaluasi hasil ringkasan Anda dan perbaiki model jika perlu.

### LIBRARY

Berikut adalah beberapa library populer Python untuk NLP yang dapat digunakan untuk memproses bahasa Indonesia:

1.  Sastrawi: Library NLP untuk bahasa Indonesia yang menyediakan fitur seperti stemming dan stopword removal.
    
2.  PySastrawi: Versi Python dari library Sastrawi.
    
3.  Bahasa: Library NLP yang menyediakan fitur seperti tokenisasi, stopword removal, dan Named Entity Recognition untuk bahasa Indonesia.
    
4.  Indonesian NLP: Library NLP yang menyediakan fitur seperti stemming, stopword removal, dan koreksi ejaan untuk bahasa Indonesia.
    
5.  Polyglot: Library NLP yang menyediakan fitur seperti tokenisasi, Named Entity Recognition, dan sentiment analysis untuk bahasa Indonesia.
    
6.  IndicNLP: Library NLP untuk bahasa India, termasuk bahasa Indonesia, yang menyediakan fitur seperti tokenisasi, Named Entity Recognition, dan text classification.
    

Semua library ini dapat membantu Anda memproses bahasa Indonesia dan mengatasi masalah NLP seperti tokenisasi, stopword removal, stemming, dan Named Entity Recognition. Anda dapat memilih library yang paling sesuai dengan kebutuhan Anda dan memulai menggunakannya untuk membuat aplikasi NLP untuk bahasa Indonesia.




### BEST PRACTICE FLOW

Berikut adalah langkah-langkah umum dalam pemrosesan NLP yang banyak digunakan dan dianggap sebagai best practice:

Text Preprocessing:

Text Cleaning: Menghapus tanda baca, angka, dan simbol yang tidak relevan.
Text Normalization: Menormalkan kata-kata dalam teks, seperti mengubah huruf besar menjadi huruf kecil.
Text Tokenization: Membagi teks menjadi token atau bagian-bagian yang lebih kecil, seperti kalimat atau kata.
Text Preprocessing Lanjutan:

Stopword Removal: Menghapus kata-kata yang sering muncul dalam bahasa, tetapi tidak memberikan informasi penting bagi pemahaman teks.
Stemming: Menghilangkan imbuhan pada akhir kata untuk mengurangi dimensi data dan memperkuat analisis.
Text Representation: Mengubah teks menjadi representasi numerik yang dapat digunakan oleh mesin untuk melakukan analisis.

Text Analysis: Melakukan analisis teks menggunakan teknik seperti sentiment analysis, text classification, named entity recognition (NER), dan lainnya.

Text Visualization: Menampilkan hasil analisis teks dalam bentuk visual untuk mempermudah interpretasi dan analisis.

Langkah-langkah ini bisa saja berbeda tergantung pada tujuan dan konteks analisis NLP yang digunakan. Namun, langkah-langkah ini menjadi dasar yang umum dan sering digunakan dalam pemrosesan NLP.

### LET'S DO IT


