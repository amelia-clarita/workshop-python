# 9. Kelas
Kelas memberikan sarana untuk menggabungkan data dan fungsionalitas bersamaan. Kelas baru yang dibuat akan membuat tipe objek baru, yang memungkinkan *instance* baru dari tipe objek yang dibuat. Setiap *instance* kelas dapat memiliki atribut yang terikat untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode (didefinisikan oleh kelasnya) untuk memodifikasi statusnya.

Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme turunan/warisan kelas memungkinkan adanya beberapa kelas *base*, kelas *derived* yang dapat meng-*override* semua metode milik kelas *base* atau kelas yang lain, dan sebuah metode dapat memanggil metode dari kelas *base* dengan nama yang sama. Objek dapat berisi jumlah dan jenis data yang berubah-ubah.

## 9.1. Sekilas Tentang Nama dan Objek
Objek memiliki individualitas, dan beberapa nama (dalam beberapa cakupan) dapat terikat ke objek yang sama. Dikenal juga dengan nama *aliasing*. Hal ini bisa diabaikan ketika berhadapan dengan angka, string, atau tupel. Meskipun demikian, aliasing memeiliki kemampuan atau efek pada kode semantik Python seperti objek *mutable*, antara lain kamus, list, dsb.

## 9.2. Scope dan Namespace Python
*Namespace* merupakan pemetaan dari nama ke objek. Contohnya: kumpulan nama bawaan (berisi fungsi seperti [abs()](https://docs.python.org/3/library/functions.html#abs)), dan nama *exception* bawaan; nama global dalam modul; dan nama lokal di invokasi fungsi. Hal yang patut diperhatikan pada *namespace* merupakan tidak ada hubungan antara setiap nama pada *namespace* yang berbeda. Misalnya, dua modul berbeda bisa mendefinisikan sebuah fungsi `maximize` tanpa terjadi kekeliruan.

`Attribute` untuk nama dapat digunakan setelah titik. Contohnya, ekspresi `z.real`, `real` merupakan atribut dari objek `z`. Pada ekspresi `modname.funcname`, `modname` merupakan objek modul dan `funcname` merupakan atributnya. Pada kasus tersebut ada proses *mapping* di antara atribut modul dan nama global yang didefinisikan di dalam modul: dua hal tersebut memiliki *namespace* yang sama.

Atribut dapat bersifat *read-only* atau *writable*. Pada kasus *writable*, dapat ditulis `modname.the*answer = 42`. Atribut *writable* juga bisa dihapus dengan statement [del](https://docs.python.org/3/reference/simple*stmts.html#del). Contohnya, `del modname.the_answer` akan menghapus atribut the_answer dari objek yang bernama `modname`.

*Namespace* dibuat pada waktu yang berbeda. Namespace yang berisi nama-nama *built-in* dibuat ketika Python interpreter dijalankan, dan tidak pernah dihapus. Namespace global untuk modul dibuat ketika definisi modul dimasukkan; umumnya, *namespace* modul bertahan hingga interpreter berhenti. Statement yang dieksekusi oleh invokasi *top-level* interpreter, yang dibaca dari file script atau secara interaktif, akan dianggap sebagai bagian dari modul bernama `__main__`, sehingga statement tersebut memiliki namespace global sendiri.

*Scope* merupakan bagian tekstual dari program Python dimana *namespace* dapat langsung diakses. "dapat langsung diakses" berarti referensi yang tidak dikualifikasi pada sebuah nama mencoba untuk menemukan nama di dalam *namespace*.

Walaupun scope ditentukan secara statis, scope digunakan secara dinamis. Pada proses eksekusi, ada 3 atau 4 *nested scope* yang *namespace*-nya dapat langsung diakses:
- Scope *innermost*, dicari pertama dan berisi nama lokal.
- Scope dari fungsi *enclosing*, diproses pencariannya dimulai dari *enclosing scope* terdekat, berisi nama non-lokal dan nama non-global.
- Scope *next-to-last*, berisi nama global modul terbaru.
- Scope *outermost* dicari paling akhir. Scope ini merupakan *namespace* yang berisi nama-nama bawaan.

Apabila nama dideklarasikan secara global, maka semua referensi dan *assignment* langsung berpindah ke *middle scope* yang berisi nama global modul. Untuk menyatukan ulang variabel yang ada di luar *innermost scope*, statement [nonlocal](https://docs.python.org/3/reference/simple*stmts.html#nonlocal) dapat digunakan; jika tidak dideklarasikan secara nonlokal, maka variabel tersebut bersifat *read-only*.

Statement `global` dapat digunakan untuk menunjukkan variabel tertentu yang ada di dalam scope global dan harus *rebound* di sana; statement `nonlocal` menunjukkan variabel tertentu yang ada di dalam *enclosing scope* dan harus *rebound* dari sana.

### 9.2.1. Contoh Scope dan Namespace
Berikut merupakan contoh demonstrasi untuk mereferensikan scope dan namespace yang berbeda, dan bagaimana `global` dan `nonlocal` mempengaruhi pengikatan variabel:
```python
def scope*test():
    def do*local():
        spam = "local spam"

    def do*nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do*global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do*local()
    print("After local assignment:", spam)
    do*nonlocal()
    print("After nonlocal assignment:", spam)
    do*global()
    print("After global assignment:", spam)

scope*test()
print("In global scope:", spam)
```
Output dari contoh:
```python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```
**Note** : *assignment* lokal tidak mengganti *binding* (pengikatan) *scope-test* milik *spam*. *Assignment* `nonlocal` mengganti *binding* *scope-test* milik *spam*, dan *assignment* global mengganti *binding* dari *module-level*.

## 9.3. Tampilan Pertama Kelas
Kelas memperkenalkan sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.

### 9.3.1. Sintaks Definisi Kelas
Bentuk paling sederhana dari definisi kelas:
```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
Definisi kelas, harus dieksekusi sebelum definisi kelas memberi efek saat dijalankan. Statement di dalam definisi kelas biasanya akan menjadi definisi fungsi, tetapi statement lain juga diperbolehkan, dan bisa berguna.

Ketika definisi kelas dimasuki, *namespace* baru dibuat dan digunakan sebagai scope lokal, semua *assignment* yang menuju variabel lokal akan berpindah ke *namespace* baru tersebut. Pada praktik tersebut, definisi fungsi mengikat nama dari fungsi baru.

Ketika definisi kelas ditinggalkan, maka objek kelas dibuat. Hal ini pada dasarnya merupakan *wrapper* (pembungkusan) diantara konten dari *namespace* yang dibuat oleh definisi kelas. Scope lokal original dipulihkan, dan objek kelas terikat ke nama kelas yanf ada di *header* definisi kelas. (Contohnya: *ClassName*).

### 9.3.2. Objek Kelas
Kelas objek mendukung dua jenis operasi: referensi atribut dan instansiasi.

Referensi atribut menggunakan sintaks standar yang digunakan untuk seluruh referensi atribut Python: `obj.name`. Nama atribut valid merupakan semua nama yang ada di dalam *namespace* kelas ketika objek kelas dibuat. Contoh:
```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
`MyClass.i` dan `MyClass.f` merupakan referensi atribut valid yang me-return integer dan objek fungsi. Atribut kelas juga bisa ditetapkan, jadi nilai milik `MyClass.i` dapat diganti dengan *assignment*. `__doc__` juga merupakan atribut valid yang me-return docstring milik kelas: `"A simple example class"`.

Instansiasi kelas menggunakan notasi fungsi. Pada dasarnya, objek kelas merupakan fungsi tanpa parameter yang me-return *instance* baru milik kelas. Contoh:
```python
x = MyClass()
```
Kode tersebut menciptakan *instance* baru milik kelas dan memasukkan objek ke variabel lokal x.

Operasi instansiasi ("memanggil" objek kelas) menciptakan objek kosong. Sebuah kelas bisa mendefinisikan metode istimewa bernama `__init__()`, seperti ini:
```python
def __init__(self):
    self.data = []
```
Ketika sebuah kelas mendefinisikan metode `__init__()`, instansiasi kelas secara otomatis membangkitkan `__init__()` untuk *instance* kelas yang baru dibuat. *instance* baru yang diinisialisasi bisa diperoleh dengan:
```python
x = MyClass()
```
Metode `__init__()` bisa memiliki argumen untuk fleksibilitas yang lebih baik. Pada kasus seperti itu, argumen yang diberikan ke operator instansiasi kelas diteruskan ke `__init__()`. Contoh:
```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```
### 9.3.3. Objek Instance
Terdapat dua jenis nama atribut valid: atribut data dan metode. 

Atribut data tidak perlu dideklarasikan; seperti variabel lokal, atribut data muncul ketika pertama kali dipanggil. Sebagai contoh, jika x merupakan *instance* dari `MyClass`, potongan kode berikut akan mencetak value `16`, tanpa menyisakan jejak:
```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```
Jenis lain dari referensi atribut *instance* merupakan metode. metode merupakan fungsi yang "dimiliki" oleh sebuah objek.

Menurut definisi, semua atribut dari kelas yang merupakan objek fungsi mendefinisikan metode yang sesuai dari *instance*-nya. Contoh, `x.f` merupakan sebuah referensi metode valid karena `MyClass.f` merupakan fungsi, tapi `x.i` bukan referensi metode valid karena `MyClass.i` bukan sebuah fungsi. Tetapi, `x.f` bukanlah hal yang sama dengan `MyClass.f` — `x.f` merupakan objek metode, bukan objek fungsi.

### 9.3.4. Objek Metode
Biasanya, sebuah metode dipanggil setelah metode tersebut 'terikat':
```python
x.f()
```
Pada contoh `MyClass`, hal tersebut akan me-return string `'hello world'`. Kita tidak perlu langsung memanggil metode: `x.f ` merupakan objek metode, dan bisa disimpan dan dipanggil suatu saat. Contoh:
```python
xf = x.f
while True:
    print(xf())
```
Kode di atas akan terus mencetak `'hello world'` tanpa henti.

Hal istimewa tentang metode merupakan objek *instance* diteruskan sebagai argumen pertama dari fungsi. Pada contoh tersebut, `x.f()` setara dengan `MyClass.f(x)`. Secara umum, memanggil metode dengan list berisi argumen `n` setara dengan memanggil fungsi yang sesuai dengan list argumen yang dibuat dengan memasukkan *instance* metode sebelum argumen pertama.

Ketika atribut non-data dari sebuah instance direferensikan, kelas dari instance akan dicari. Jika namanya menunjukkan atribut kelas valid yang merupakan objek fungsi, objek metode dibuat dengan membungkus objek instance dan objek fungsi yang ditemukan bersama dalam objek abstrak. Ketika objek metode dipanggil dengan list argumen, list argumen baru dibuat dari objek instance dan list argumen, dan objek fungsi dipanggil dengan list argumen baru tersebut.

### 9.3.5. Kelas dan Variabel Instance
Secara umum, variabel instance ditujukan untuk data yang unik terhadap setiap *instance* dan  variabel kelas untuk atribut dan metode yang dibagikan oleh semua instance kelas:
```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
Data bersama dapat memiliki efek mengejutkan dengan menyertakan objek [mutable](https://docs.python.org/3/glossary.html#term-mutable) seperti list dan dictionary. Sebagai contoh, list *tricks* pada kode berikut tidak seharusnya digunakan sebagai variabel kelas karena satu list saja bisa dibagikan oleh instance *Dog*:
```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```
Sebagai ganti, desain kelas yang benar harus menggunakan variabel instan:
```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add*trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add*trick('roll over')
>>> e.add*trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```
## 9.4. Keterangan Acak
Jika nama atribut yang sama muncul dalam sebuah instance dan dalam sebauh kelas, maka pencarian atribut memprioritaskan instance:
```python
>>> class Warehouse:
        purpose = 'storage'
        region = 'west'

>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```
Atribut data bisa direferensikan dengan metode atau oleh "client" dari objek. Kelas tidak bisa digunakan untuk mengimplementasikan tipe data abstrak.

Client harus menggunakan atribut data dengan hati-hati — client bisa mengacaukan invarian yang dimaintain oleh metode dengan memberi *stamp* (cap) pada atribut datanya. Client dapat menambahkan atribut data mereka sendiri ke objek instan tanpa memengaruhi validitas metode, selama konflik nama bisa dihindari.

Seringkali argumen pertama bernama `self`. Hal tersebut hanyalah konvensi: nama `self` tidak memiliki arti spesial.

Objek fungsi apa pun yang merupakan atribut kelas mendefinisikan metode untuk instance kelas itu. Definisi fungsi tidak perlu secara tekstual dilampirkan dalam definisi kelas: menetapkan objek fungsi ke variabel lokal di kelas juga tidak masalah. Contoh:
```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```
`f`,`g`, dan `h` merupakan atribut milik kelas C yang me-refer ke objek fungsi, yang membuat atribut-atribut tersebut menjadi metode *instance* milik C — dengan `h` menjadi setara dengan `g`.

Metode dapat memanggil metode lain dengan atribut metode milik argumen `self`:
```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```
Metode dapat mereferensikan nama global dengan cara yang sama seperti fungsi biasa. Scope global yang diasosiasikan dengan metode merupakan modul yang berisi definisi.

Setiap value merupakan objek yang memiliki kelas yang disimpan dengan nama `object.__class__`.

## 9.5. Inheritance
Tampilan sintaks dari kelas turunan:
```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Nama `BaseClassName` harus didefinisikan di dalam scope yang mengandung definisi subclass. Kita juga bisa menuliskan ekspresi lain di tempat `BaseClassName`. Hal ini bisa berguna ketika base class didefinisikan di dalam modul lain:
```python
class DerivedClassName(modname.BaseClassName):
```
Eksekusi definisi derived class (subclass) berlangsung sama seperti base class. Ketika objek kelas dibentuk, case class akan diingat. Hal tersebut berguna untuk mengatasi referensi atribut.

`DerivedClassName()` membuat *instance* baru pada kelas. Referensi metode diatasi dengan cara berikut: atribut kelas dicari, dan referensi metode valid jika proses ini menghasilkan objek fungsi.

Derived class bisa meng-override metode milik base class. Karena metode tidak memiliki hak istimewa ketika memanggil objek lain milik objek yang sama, metode milik base class yang memanggil metode lain yang didefinisikan di dalam base class yang sama bisa memanggil metode milik derived class yang meng-override metode.

Ada cara sederhana untuk memanggil metode base class yaitu dengan memanggil `BaseClassName.metodename(self, arguments)`.

Python memiliki dua fungsi built-in pada inheritance:
- Gunakan [isinstance()](https://docs.python.org/3/library/functions.html#isinstance) untuk memeriksa tipe *instance*: `isinstance(obj, int)` akan bernilai `True` jika `obj.__class__ is` bertipe int atau ada derived class dari int.
- Gunakan [issubclass()](https://docs.python.org/3/library/functions.html#issubclass) untuk memeriksa inheritance: `issubclass(bool, int)` bernilai `True` karena `bool` merupakan subclass dari `int`. Tetapi `issubclass(float, int)` bernilai False karena `float` bukanlah subclass dari `int`.

### 9.5.1. Multiple Inheritance
Python mendukung bentuk multiple inheritance (pewarisan banyak/ganda). Berikut tampilan definisi kelas dengan beberapa base class:
```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Pengurutan dinamis diperlukan karena semua kasus pewarisan berganda menunjukkan satu atau lebih hubungan. Misalnya, semua kelas mewarisi dari `object`, jadi setiap kasus pewarisan berganda menyediakan lebih dari satu jalur untuk mencapai `object`.
## 9.6. Variabel Privat
Di Python, tidak ada variabel *instance* "privat" yang tidak bisa diakses kecuali dari dalam objek. Walau begitu, ada konvensi yang diikuti oleh kebanyakan kode Python: nama yang di-prefix atau diawali dengan underscore (Contoh: `*spam`) harus diperlakukan sebagai bagian non-public dari API. Hal tersebut harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.

Pembagian/pemotongan (mangling) nama digunakan untuk memungkinkan subclass untuk meng-override metode tanpa memengaruhi pemanggilan metode intraclass. Contoh:
```python
class Mapping:
    def __init__(self, iterable):
        self.items*list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items*list.append(item)

    __update = update   # private copy of original update() metode

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items*list.append(item)
```
Contoh di atas dapat bekerja bahkan jika `MappingSubclass` memperkenalkan identifier `__update` karena diganti dengan `_Mapping__update` di dalam `Mapping class` dan `_MappingSubclass__update` di dalam `MappingSubclass`.

Perhatikan bahwa kode yang diteruskan ke `exec()` atau `eval()` tidak menganggap classname kelas yang di-invoke untuk menjadi current class; hal ini mirip dengan efek statement global.

## 9.7. Odds dan Ends
Terkadang berguna untuk memiliki tipe data yang mirip dengan "record" Pascal atau "struct" C, yang menggabungkan beberapa item data bernama. Definisi kelas empty:
```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```
Kode Python yang memerlukan tipe data tertentu dapat diteruskan ke kelas yang meniru metode dari tipe data tersebut. Misalnya, jika kita memiliki fungsi yang mem-format beberapa data dari objek file, kita bisa mendefinisikan sebuah kelas dengan metode `read()` dan `readline()` yang mendapatkan data dari string buffer, dan meneruskannya sebagai argumen.

Objek metode *instance* juga memiliki atribut: `m.__self__` merupakan objek *instance* dengan metode `m()`, dan `m.__func__` merupakan objek fungsi yang sesuai dengan metode.

## 9.8. Iterator
Sebagian besar objek kontainer dapat diulang menggunakan statement [for](https://docs.python.org/3/reference/compound*stmts.html#for):
```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```
Gaya akses tersebut jelas, ringkas, dan mudah dibuat. Penggunaan iterator meliputi dan menyatukan Python. Statement `for` memanggil [iter()](https://docs.python.org/3/library/functions.html#iter) pada objek container. Fungsi me-return objek iterator yang mendefinisikan metode `__next__()` yang mengakses elemen di dalam container. Ketika tidak ada lagi elemen, `__next__()`memunculkan *exception* [StopIteration](https://docs.python.org/3/library/exceptions.html#StopIteration) yang memberi tahu loop `for` untuk mengakhiri proses. Kita bisa memanggil metode `__next__()` menggunakan fungsi built-in `__next__()`, contoh:
```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```
Setelah melihat cara kerja protokol iterator, kita dapat dengan mudah menambahkan behavior iterator ke kelas. Definisikan metode `__iter__()` yang me-return objek dengan metode `__next__()`. Jika kelas mendefinisikan `__next__()`, maka `__iter__()` dapat hanya me-return `self`:
```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```
```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

## 9.9. Generator
[Generator](https://docs.python.org/3/glossary.html#term-generator) merupakan tool untuk membuat iterator. Tool tersebut ditulis seperti fungsi pada umumnya menggunakan statement [yield](https://docs.python.org/3/reference/simple*stmts.html#yield) kapanpun generator ingin me-return data. Setiap kali `next()` dipanggil, generator melanjutkan dari titik yang ditinggalkan. Contoh membuat generator:
```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```
Apapun yang bisa dilakukan dengan generator juga bisa dilakukan dengan iterator class-based. Yang membuat generator sangat *compact* merupakan metode `__iter__()` dan `__next__()` dibuat secara otomatis.

Fitur utama lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan di antara panggilan. Hal ini membuat fungsi dapat ditulis dengan lebih mudah dan jelas daripada menggunakan variabel *instance* seperti `self.index` dan `self.data`.

## 9.10. Ekspresi Generator
Ekspresi generator lebih ringkas tetapi kurang fleksibel jika dibandingkan dengan definisi generator lengkap dan cenderung lebih ramah memori. Contoh:
```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```