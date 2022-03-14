# 7. Input dan Output
Terdapat beberapa cara untuk menampilkan output dari sebuah program, data dapat di*print* dalam format *human-readable*, atau ditulis dalam sebuah file untuk digunakan nanti.
## 7.1. Pemformatan Output yang Lebih Menarik
Sejauh ini telah dipelajari dua cara untuk menulis values: *expression statements* dan fungsi `print()`. (Cara ketiga adalah menggunakan metode  `write()` dari objek file; dengan standar output `sys.stdout`).

Terdapat beberapa bentuk pemformatan output :
* Menggunakan [string literals berformat](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings), dimulai dengan string `f` atau `F` sebelum tanda kutip pembuka. Di dalam string, dapat ditulis variabel atau karakter di antara tanda `{` dan `}`.
```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```
* Metode string `str.format()`. Dapat menggunakan `{` dan `}` untuk memberi tanda variabel dan dapat memberi pemformatan detail.
```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```
* Terakhir, dapat menggunakan *slicing* dan operasi *concatenation* untuk membuat layout yang diinginkan.

Untuk menampilkan output secara cepat dari beberapa variabel, dapat menggunakan fungsi [repr()](https://docs.python.org/3/library/functions.html#repr) atau [str()](https://docs.python.org/3/library/stdtypes.html#str) untuk mengkonversi nilai apapun menjadi string.

Fungsi `str()` digunakan untuk mengembalikan representasi nilai yang cukup dibaca manusia, sedangkan `repr()` untuk menghasilkan representasi yang dapat dibaca oleh interpreter.

Contoh :
```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```
Modul `string` berisi kelas `Template` yang memberikan cara lain untuk mengganti nilai menjadi string.
### 7.1.1. Literal String Terformat
Disebut juga f-string memungkinkan kita memasukan nilai ekspresi Python dalam string dengan `f` atau `F` dan menulis ekspresi sebagai `{expression}`.

Contoh berikut membulatkan pi ke tiga tempat setelah desimal :
```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```
Dengan `':'` dapat membuat field menjadi jumlah karakter minimum. Ini berguna untuk membuat kolom tersusun.
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```
Selain itu, untuk mengonversi nilai dapat menggunakan modifier lain, seperti `!r` pada `repr()`.
```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```
### 7.1.2. Metode Format String()
Penggunaan dasar metode `str.format()` seperti berikut :
```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```
Tanda kurung dan karakter di dalam (format field) diganti dengan objek yang diteruskan ke metode `str.format()`. Angka dalam kurung merujuk ke posisi objek yang dilewatkan ke dalam `str.format()`.
```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```
Apabila argumen merupakan kata kunci, maka nilai dirujuk menggunakan nama argumen.
```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```
Posisi argumen dan kata kunci dapat digabungkan :
```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.
```
Apabila format string sangat panjang dan tidak bisa dipisahkan, kita dapat mereferensikan variabel yang akan diformat berdasarkan nama, bukan berdasarkan posisi menggunakan kurung siku `[]`.
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
Dapat juga menggunakan notasi `**`.
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
Contoh, baris program berikut menghasilkan kumpulan kolom yang tersusun rapi dengan bilangan bulat, kuadrat, dan kubus.
```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
### 7.1.3. Pemformatan String Manual
Berikut merupakan tabel kubus yang sama dnegan format manual :
```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
Tiap satu spasi di antara setiap kolom ditambahkan dengan cara `print()`.

Metode `str.rjust()` string objek membenarkan string di bidang dengan lebar tertentu dengan mengisinya dengan spasi di sebelah kiri. Ada metode serupa, yaitu `str.ljust()` dan `str.center()`. Terdapat metode lain pula, `str.zfill()` yang mengisi string numerik di sebelah kiri dengan nol dan mengerti tentang tanda plus dan minus:
```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```
### 7.1.4. Pemformatan String Lama
Operator % (modulo) juga dapat digunakan untuk pemformatan string. Dengan `'string'%values`, instance dari `%` di dalam `%` diubah dengan nol atau elemen dari `values`. Operasi ini disebut juga dengan interpolasi string. Contoh :
```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```
## 7.2. Membaca dan Menulis File
`open()` mengembalikan `file objek`, dan pada umumnya digunakan bersama dua argumen: `open(filename, mode)`.
```python
>>> f = open('workfile', 'w')
```
Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menjelaskan cara file akan digunakan. Mode `r` hanya akan dibaca, mode `w` hanya menulis, dan `a` membuka file untuk ditambahkan.

Berikut adalah praktik menggunakan kata kunci [with](https://docs.python.org/3/reference/compound_stmts.html#with) ketika berhadapan dengan objek file.
```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```
Jika menggunakan kata kunci `with`, maka `f.close()` harus dipanggil untuk menutup file.
Setelah objek file ditutup, baik pernyataan `with` atau dengan memanggil `f.close()`, upaya untuk menggunakan objek file secara otomatis akan gagal.
```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```
### 7.2.1. Metode Objek File
Untuk membaca konten file, digunakan `f.read(size)`, yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). *Size* adalah argumen numerik opsional. Jika akhir file telah tercapai, `f.read()` akan mengembalikan string kosong (` ''`).
```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```
`f.readline()` membaca satu baris dari file; karakter baris baru (`\n`) ditinggalkan di akhir string, dan hanya dihilangkan pada baris terakhir file jika file tidak diakhiri dengan baris baru. 
```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```
Untuk membaca baris dari file, kita dapat mengulang objek file. 
```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```
Jika Anda ingin membaca semua baris file dalam daftar, Anda juga dapat menggunakan `list(f)` atau `f.readlines()`.

`f.write(string)` menulis isi string ke file, mengembalikan jumlah karakter yang ditulis.
```python
>>> f.write('This is a test\n')
15
```
Jenis objek lain perlu dikonversi – baik menjadi string atau objek byte - sebelum ditulis.
```python
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
```
Untuk mengubah posisi objek file, menggunakan `f.seek(offset, whence)`. Posisi dihitung dari penambahan offset ke titik referensi;
```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```
Objek file memiliki beberapa metode tambahan, seperti `isatty()` dan `truncate()` yang lebih jarang digunakan.
### 7.2.2. Menyimpan Data Terstruktur dengan Json
String dapat dengan mudah ditulis dan dibaca dalam sebuah file. Di dalam python, terdapat format pertukaran data yang disebut dengan [JSON(JavaScript Object Notation)](https://www.json.org/json-en.html). Modul standar yang dipanggil `json`dapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string; proses ini disebut `serialisasi`. Merekonstruksi data dari representasi string disebut `deserializing`.

Representasi string JSON sederhana :
```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```
Jenis lain dari fungsi `dumps()`, yang disebut `dump()`, hanya membuat serial objek ke file teks. Sehingga, jika objek `f` file teks dibuka untuk ditulis, kita bisa melakukan ini:
```python
json.dump(x, f)
```
Untuk memecahkan kode objek lagi, jika `f` adalah objek file teks yang telah dibuka untuk dibaca:
```python
x = json.load(f)
```
Teknik serialisasi sederhana ini dapat menangani daftar dan kamus, tetapi membuat serialisasi instance kelas arbitrer di JSON membutuhkan sedikit usaha ekstra.