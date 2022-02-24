# 5. Struktur Data
## 5.1. Membuat List
Tipe data list memiliki beberapa metode, antara lain :

list.**append**(*x*)

Menambahkan item ke akhir list. Setara dengan `a[len(a):] = [x]`
	
list.**extend**(*iterable*)

Memperluas list dengan menambahkan semua item dari iterable. Setara dengan `a[len(a):] = iterable`

list.**insert**(*i, x*)

Memasukan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang akan disisipkan sebelumnya, setara dengan `a.insert(0,x)a.insert(len(a), x)a.append(x)`

list.**remove**(*x*)

Menghapus item pertama dari list yang nilainya sama dengan *x*. Hal ini menimbulkan [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) jika item tidak ditemukan.

list.**pop**([*i*])

Menghapus item pada pada posisi yang diberikan dari list dan dikembalikan. Jika tidak ada indeks yang ditentukan, `a.pop()` akan menghapus dan mengembalikan item terakhir dari list.

list.**clear**()

Menghapus semua item dari list. Setara dengan `del a[:]`.

list.**index**(*x[, start[, end]]*)

Mengembalikan indeks berbasis nol dalam list item pertama yang nilainya sama dengan *x*. Muncul [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) jika tidak ditemukan item.

list.**count**(*x*)

Mengembalikan jumlah *x* yang muncul pada list.

list.**sort**(*, key=None, reverse=False)

Mengurutkan item dari list di tempat ( argumen dapat digunakan untuk penyesuaian pengurutan, penjelasan lebih dalam lihat [sorted()](https://docs.python.org/3/library/functions.html#sorted) ).

list.**reverse**()

Membalikan elemen dari list tempat.

list.**copy**()

Mengembalikan salinan list. Setara dengan `a[:]`.

Contoh penggunaan sebagian besar metode list :
```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```
Metode seperti `insert`, `remove`, atau `sort` yang hanya mengubah list tidak memiliki nilai kembali `none`. Tidak semua data dapat diurutkan atau dibandingkan.
### 5.1.1. Menggunakan Lists sebagai Stacks
Metode list dapat digunakan sebagai stack, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil. Untuk menambahkan item ke bagian atas tumpukan, gunakan `append()`. Untuk mengambil item dari atas tumpukan, gunakan `pop()` tanpa indeks eksplisit.
```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```
### 5.1.2. Menggunakan Lists sebagai Queues
Metode list juga dapat digunakan sebagai queue, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil. Namun, list tidak efisien untuk tujuan ini. Untuk implementasi queue, dapat menggunakan [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) yang dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya.
```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```
### 5.1.3. List Comprehensions
List comprehensions menyediakan cara ringkas untuk membuat list. Secara umum, pengaplikasiannya adalah untuk membuat list baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau untuk membuat sub urutan dari elemen-elemen yang memenuhi kondisi tertentu. Berikut contoh membuat list kotak :
```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
Note : ini membuat variabel bernama `x`  masih ada setelah loop selesai. 

Untuk menghitung list kotak tanpa efek samping dapat menggunakan :
```python
squares = list(map(lambda x: x**2, range(10)))
```
atau, ekuivalen dengan :
```python
squares = [x**2 for x in range(10)]
```
List comprehensions terdiri dari tanda kurung yang berisi ekspresi diikuti oleh klausa `for`, kemudian 0 atau lebih `for` atau  klausa `if`. Hasilnya adalah list baru yang dihasilkan dari evaluasi ekspresi dalam konteks `for` dan klausa `if` yang mengikutinya. Contohnya, listcomp berikut menggabungkan elemen dari dua list jika sama :
```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
atau, ekuivalen dengan :
```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
Urutan pernyatan `for` dan `if` sama di kedua cuplikan program di atas. Apabila ekspresi adalah tuple, harus diberi kurung `(x, y)`.
```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Pemahaman list dapat berisi ekspresi kompleks dan fungsi bersarang :
```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```
### 5.1.4. Nested List Comprehensions
Ekspresi awal dalam list comprehension dapat berupa ekspresi arbitrary, termasuk list comprehension lain. Berikut conto dari matriks 3x4 yang diimplementasikan sebagai 3 list dengan panjang 4 :
```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```
Daftar berikut akan mengubah baris dan kolom :
```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Seperti pada bagian sebelumnya, listcomp bersarang dievaluasi dalam konteks `for` yang mengikutinya, jadi contoh ini ekuivalen dengan :
```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
berikutnya, sama dengan :
```python
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Fungsi [zip()](https://docs.python.org/3/library/functions.html#zip) dapat membuat pekerjaan menjadi lebih baik dalam kasus ini :
```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```
Dapat dilihat pada [Membongkar Daftar Argumen](https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments) untuk lebih detail tentang tanda bintang pada baris program di atas.
## 5.2. Pernyataan `del`
Terdapat cara untuk menghapus item dari list yang diberikan indeksnya alih-alih nilainya : pernyatan `del`. Ini berbeda dengan metode `pop()` yang mengembalikan nilai. Pernyataan `del` juga dapat digunakan untuk menghapus irisan dari list atau menghapus seluruh list. Contoh :
```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```
`del` juga dapat digunakan untuk menghapus seluruh variabel :
```python
>>> del a
```
## 5.3. Tuples dan Sequences
List dan String memiliki banyak properti umum, seperti operasi pengindeksan dan pengirisan. Keduanya merupakan contoh tipe data urutan. Tedapat tipe data urutan standar lain : *tuple*. Tuple terdiri dari sejumlah nilai yang dipisah dengan koma, misalnya :
```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```
Dari program dapat dilihat pada keluaran tuple selalu diapit tanda kurung, sehingga interpretasi tupel bersarang benar. Meskipun tuple mirip dengan list, keduanya digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuple tidak dapat diubah dan pada umumnya berisi urutan elemen heterogen yang diakses melalui pembongkaran atau pengindeksan. List dapat diubah dan elemennya pada umumnya homogen dan diakses dengan mengulangi list. Tuple kosong dibangun oleh sepasang tanda kurung kosong; tuple dengan satu item dibangun dengan mengikuti nilai dengan koma. Kurang bagus, tapi efektif. Sebagai contoh :
```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```
Operasi sebaliknya dimungkinkan dengan : `t = 12345, 54321, 'hello!'1234554321'hello!'`
```python
>>>x, y, z = t
```
## 5.4. Set
Di dalam python juga terdapat tipe data *set*. Set adalah kumpulan tidak berurutan tanpa elemen duplikat. Kurung kurawal atau fungsi `set()` dapat digunakan untuk membuat himpunan. 

Note : untuk membuat set kosong harus menggunakan `st()`, bukan `{}`.

Demonstrasi singkat :
```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```
Sama seperti `list comprehension`, set juga didukung :
```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```
## 5.5. Kamus
Tipe data lain yang berguna yang dibangun di dalam Python adalah `dictionary` (dapat dilihat pada [Mapping Types - dict](https://docs.python.org/3/library/stdtypes.html#typesmapping). Kamus terkadang menemukan bahasa yang berbeda sebagai "memori asosiatif" atau "array asosiatif". Seperti halnya *sequences*, yang mana diindeks berdasarkan rentang angka, kamus diindeks oleh *kunci* yang dapat berupa tipe apapun yang tidak dapat diubah; String dan angka dapat menjadi kunci.

Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci tersebut. Dimungkinkan juga untuk menghapus pasangan key:value dengan `del`. Jika menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci tersebut akan terlupakan. Ini adalah kesalahan untuk mengekstrak nilai menggunakan kunci yang tidak ada. Contoh penggunaan kamus :
```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```
Konstruksi `dict()` membangun kamus langsung dari urutan pasangan nilai kunci :
```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```
Selain itu, pemahaman `dict` dapat digunakan untuk membuat kamus dari kunci arbitrer dan ekspresi nilai :
```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```
Jika kuncinya adalah string sederhana, terkadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci :
```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```
## 5.6. Teknik Perulangan
Saat mengulang melalui kamus, kunci dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan metode `items()`.
```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```
Saat mengulang melalui urutan, indeks posisi dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan fungsi `enumerate()`.
```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```
Untuk mengulang dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan fungsi `zip()`.
```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```
Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi `reversed()`.
```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```
Untuk mengulang urutan dalam urutan terurut, gunakan fungsi `sorted()` yang mengembalikan list terurut baru sambil membiarkan sumbernya tidak berubah.
```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```
Menggunakan `set()` pada urutan menghilangkan duplikasi elemen. Penggunaan `sorted()` dalam kombinasi dengan `set()` lebih dari urutan adalah cara idiomatik untuk mengulang elemen unik dari sequence dalam urutan.
```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```
Membuat list baru lebih mudah dan aman dibanding mengubah daftar ketika mengulangnya.
```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```
## 5.7. Lebih Lanjut tentang Kondisi
Kondisi menggunakan `while` dan pernyatan `if` dapat berisi banyak operasi, tidak hanya perbandingan.

Operasi perbandingan `in` dan `not in` adalah bagian dari tes keanggotaan apakah suatu nilai ada atau tidak di dalam wadah. Semua operator pembanding memiliki prioritas yang sama, yaitu lebih rendah dari semua operator numerik.`not in` `is` `is not`.

Perbandingan dapat dirantai. Misalnya, menguji apakah kurang dari dan sama dengan.`a < b == c` `a` `b` `b` `c`

Perbandingan dapat digabungkan menggunakan operator Boolean `and` dan `or`, dan hasil perbandingan dapat dinegasikan dengan `not`. Tanda kurung dapat digunakan untuk menyatakan komposisi yang diinginkan. `A and not B or C` `(A and (not B)) or C`.

Operator Boolean `and` dan `or` yang disebut operator hubung singkat: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel, contoh :
```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```
Di dalam python, penugasan di dalam ekspresi harus dilakukan secara eksplisit dengan [operator walrus](https://docs.python.org/3/faq/design.html#why-can-t-i-use-an-assignment-in-an-expression) `:=`. Hal ini menghindari kelas umum dari masalah pemrograman seperti mengetik ekspresi `=` padahal yang dimaksud adalah `==`.
## 5.8. Membandingkan Urutan dan Jenis Lainnya
Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingannya menggunakan `leksikografis` pemesanan: pertama, dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis. Jika dua item yang akan dibandingkan merupakan urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama. Jika satu barisan merupakan sub-urutan awal dari yang lain, barisan yang lebih pendek adalah yang lebih kecil. Urutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan karakter individual. Beberapa contoh perbandingan antara urutan dari jenis yang sama :
```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
Perhatikan bahwa membandingkan objek dari jenis yang berbeda dengan `<` atau `>` legal, asalkan objek tersebut memiliki metode perbandingan yang sesuai. Misalnya, tipe numerik campuran dibandingkan menurut nilai numeriknya, jadi 0 sama dengan 0.0, dll. Jika tidak, alih-alih memberikan pengurutan arbitrer, akan memunculkan pengecualian `TypeError`.