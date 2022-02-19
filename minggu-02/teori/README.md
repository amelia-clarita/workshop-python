# Minggu ke-2 : Pengendalian Alur Program - Tutorial Bab 4

## 4.1 If Statements
Dalam penggunaan statements **if**, kata kunci '*elif*' merupakan kependekan
dari 'else if'. Statement If..., elif..., elif... secara berurutan
merupakan pengganti *switch* atau *case* pada bahasa pemrograman lain.


## 4.2 For Statements
Statement **for** dalam pernyataan Python mengulangi item dari urutan 
apa pun (daftar atau string), dalam urutan yang muncul dalam rangkaian.


## 4.3 The Range() Function
Fungsi **range()** berfungsi mengulangi urutan angka. Titik terakhir
dalam urutan bukan merupakan indeks. Indeks dalam *range* merupakan
jumlah item. Contohnya : *range(10)* berarti jumlah item adalah 10 
dengan start angka dimulai dari angka 0.
Dalam *range*, untuk mengulangi indeks urutan dapat menggabungkan
*range()* dan *len()*.


## 4.4 Break and Continue Statements, and Else Clauses on Loops
Klausa **else** dalam praktik digunakan dalam looping *for* dan bukan 
dalam pernyataan *if*. Ketika digunakan dengan loop, klausa *else* 
memiliki lebih banyak kesamaan dengan klausa *else* dari pernyataan
*try* daripada dengan *if*. 


## 4.5 Pass Statements
Pernyataan **pass** tidak melakukan apa-apa. Pernyataan dapat digunakan 
ketika pernyataan diperlukan secara sintaksis tetapi program tidak 
memerlukan tindakan.


## 4.6 Match Statements
Pernyataan **match** mengambil ekspresi dan membandingkan nilainya dengan 
pola berurutan yang diberikan sebagai satu atau lebih blok kasus. Ini sangat 
mirip dengan pernyataan *switch* pada bahasa pemrograman lain (C atau Java).


## 4.7 Defining Functions
Kata kunci **def** memperkenalkan fungsi *definition*. Fungsi harus diikuti
dengan nama fungsi dan daftar parameter formal dalam kurung. Pernyataan-pernyataan
yang membentuk badan fungsi dimulai dari baris berikutnya, dan harus diindentasi.


## 4.8 More on Defining Functions

### 4.8.1 Default Argument Values
**Default argument** merupakan bentuk yang paling berguna adalah untuk
menentukan nilai default untuk satu atau lebih argumen. Bentuk ini menciptakan 
fungsi yang dapat dipanggil dengan argumen yang lebih sedikit daripada yang
ditentukan untuk diizinkan. 
			
### 4.8.2 Keyword Arguments
Fungsi juga dapat dipanggil menggunakan argumen kata kunci dari formulir *kwarg=value*.
Dalam panggilan fungsi, argumen kata kunci harus mengikuti argumen posisi.
Semua argumen kata kunci yang diteruskan harus cocok dengan salah satu argumen
yang diterima oleh fungsi dan urutannya tidak penting.
			
### 4.8.3 Special Parameters
Secara default, argumen dapat diteruskan ke fungsi Python baik dengan posisi atau
secara eksplisit dengan kata kunci. Untuk keterbacaan dan kinerja, masuk akal
untuk membatasi cara argumen dapat diteruskan sehingga pengembang hanya perlu
melihat definisi fungsi untuk menentukan apakah item dilewatkan berdasarkan
posisi, berdasarkan posisi atau kata kunci, atau kata kunci.
			
### 4.8.4 Arbitrary Argument Lists
Suatu fungsi dapat dipanggil dengan sejumlah argumen yang berubah-ubah. Argumen-
argumen ini akan dibungkus dalam sebuah tuple. Sebelum jumlah variabel argumen, 
nol atau lebih argumen normal dapat terjadi.
			
### 4.8.5 Unpacking Argument Lists
Situasi sebaliknya terjadi ketika argumen sudah ada dalam daftar atau tupel
tetapi perlu dibongkar untuk pemanggilan fungsi yang memerlukan argumen
posisi terpisah. Misalnya, fungsi *range()* bawaan mengharapkan argumen
mulai dan berhenti yang terpisah. Jika tidak tersedia secara terpisah,
tulis pemanggilan fungsi dengan operator bintang untuk membongkar argumen
dari daftar atau tuple.
			
### 4.8.6 Lambda Expressions
Fungsi anonim kecil dapat dibuat dengan kata kunci **lambda**. Fungsi ini
mengembalikan jumlah dari dua argumen. Fungsi Lambda dapat digunakan
di mana pun objek fungsi diperlukan. Mereka secara sintaksis terbatas
pada satu ekspresi.
			
### 4.8.7 Documentation Strings
Baris pertama **string** harus selalu merupakan ringkasan singkat dan
ringkas dari tujuan objek. Baris ini harus dimulai dengan huruf kapital
dan diakhiri dengan titik. Jika ada lebih banyak baris dalam string
dokumentasi, baris kedua harus kosong, yang secara visual memisahkan
ringkasan dari deskripsi lainnya. Baris berikut harus berupa satu atau
lebih paragraf yang menjelaskan konvensi pemanggilan objek, efek
sampingnya, dll.
			
### 4.8.8 Function Annotations
**Function annotations** sepenuhnya merupakan informasi metadata
opsional tentang jenis yang digunakan oleh fungsi yang ditentukan
pengguna. Parameter *anotasi* ditentukan oleh titik dua setelah 
nama parameter, diikuti dengan ekspresi yang mengevaluasi nilai *anotasi*.
*Anotasi* pengembalian ditentukan oleh literal -> , diikuti oleh ekspresi,
antara daftar parameter dan titik dua yang menunjukkan akhir pernyataan *def*.
			