# 8. Errors dan Exceptions
Terdapat setidaknya bentuk kesalahaan yang dapat dibedakan, yaitu sintaks error dan exception.
## 8.1. Sintaks Error
Sintaks error atau error parsing, mungkin merupakan keluhan yang paling umum dalam python :
```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```
*Parser* mengulangi baris yang menyinggung dan menampilkan 'panah' kecil yang menunjuk pada titik paling awal di baris tempat kesalahan terdeteksi. Dari contoh, error terdeteksi pada fungsi `print()`, karena titit dua (`':'`) hilang. Nama file dan nomor baris dicetak sehingga pemrogram tahu letak pencariannya Apabila input berasal dari skrip.
## 8.2. Exception
*Exception* merupakan error yang terdeteksi ketika program dieksekusi dan bukan merupakan kesalahan fatal. Kebanyakan exception tidak ditangani oleh program, namun pesan error akan tampil seperti berikut :
```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
Exception tampil dalam tipe yang berbeda, dan tipe tersebut dicetak dengan pesan: tipe dalam contoh adalah `ZeroDivisionError`, `NameError` dan `TypeError`. Sisa baris memberikan detail berdasarkan jenis exception dan apa yang menyebabkannya. 
## 8.3. Menangani Exception
Contoh berikut, meminta pengguna untuk menginput integer yang valid, tetapi juga memungkinkan pengguna untuk menginterupsi program.
```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

Pernyataan statement `try` bekerja dengan cara berikut.
+ Pertama, klausa `try` dieksekusi
+ Apabila tidak ditemukan exception, klausa `except` dilewati dan statement `try` yang dieksekusi akan berakhir.
+ apabila pada eksekusi klausa `try` muncul exception, klausa yang tersisa akan dilewati.
+ Apabila exception dari klausa `except` tidak cocok dengan exception, exception tersebut akan diteruskan ke statement `try` luar.

Sebuah statement `try` mungkin mempunyai lebih dari satu klausa *except*, untuk menangani exception yang berbeda. Klausa exception dapat menyebutkan beberapa exception sebagai tupel dalam kurung, misalnya:
```python
... except (RuntimeError, TypeError, NameError):
...     pass
```
Kelas dalam klausa `except` kompatibel dengan exception apabila berada pada kelas yang sama. Misalnya,  kode berikut akan mencetak B, C, D dalam urutan itu:
```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```
Dapat dilihat bahwa Apabila klausa *except* dibalik, akan pertama mencetak `except B`, dan menampilkan B, B, B.

Semua *exception* diwariskan oleh `BaseException`, sehingga dapat digunakan sebagai karakter pengganti. Hal itu juga dapat digunakan untuk mencetak pesan *error* dan menampilkan kembali exception:
```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```
Sebagai alternatif, klausa *exception* terakhir dapat menghilangkan nama exception, namun nilai *exception* kemudian harus diambil dari sys.exc_info().

Pernyataan `try ... except` memiliki klausa `else` yang apabila muncul, maka harus mengikuti semua klausa `except`. Hal ini berguna ketika harus mengeksekusi program dan klausa `try` tidak memunculkan exception. Sebagai contoh:
```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```
Penggunaan klausa `else` lebih baik daripada menambahkan kode pada klausa `try` karena dapat mencegah program menangkap exception yang tidak ditampilkan oleh kode yang dilindungi oleh statement `try ... except`.

Klausa `except` dapat menentukan variabel setelah nama exception. Variabel tersebut terikat ke exception instance dengan argumen yang disimpan di `instance.args`. Instance tersebut mendefinisikan `__str__()` sehingga argumen dapat dicetak tanpa harus mereferensikan `.args`. 
```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```
Pengendali exception tidak hanya menangani exception yang muncul ketika klausa *try*, tetapi juga ketika fungsi yang dipanggil di dalam klausa *try*. Sebagai contoh:
```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

## 8.4. Menampilkan Exception
Pernyataan [raise](https://docs.python.org/3/reference/simple_stmts.html#raise) memungkinkan programmer untuk memaksa exception tertentu terjadi. Contohnya:
```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```
Satu-satunya argumen `raise` menunjukan exception yang akan diajukan. Apabila kelas exception dilanjutkan, akan secara implisit dipakai dengan memanggil konstruktornya tanpa argumen:
```python
raise ValueError  # shorthand for 'raise ValueError()'
```
Apabila ingin menentukan apakah exception harus dimunculkan tetapi juga tidak ingin menanganinya, maka dapat menggunakan bentuk sederhana dari statement `raise` untuk memunculkan ulang sebuah exception:
```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```
## 8.5. Rantai Exception
Pernyataan `raise` memungkinkan sebuah optional `from` untuk mengaktifkan rantai exception. Contoh:
```python
# exc must be exception instance or None.
raise RuntimeError from exc
```
Hal ini dapat berguna ketika mentranform exception. Contoh:
```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```
Rantai exception secara otomatis terjadi ketika sebuah exception tampil dalam sebuah [except](https://docs.python.org/3/reference/compound_stmts.html#except) atau [finally](https://docs.python.org/3/reference/compound_stmts.html#finally). Hal ini dapat dinonaktifkan dengan idiom `none`:
```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```
## 8.6. Exception yang Ditentukan Pengguna
Program dapat memberi nama exception mereka sendiri dengan membuat kelas exception baru. Exception biasanya harus diturunkan dari kelas `Exception`, baik secara langsung maupun tidak langsung.

Kelas exception dapat didefinisikan sebagai yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk exception.

Sebagian besar exception didefinisikan dengan nama yang diakhiri dengan "Kesalahan", mirip dengan penamaan pengecualian standar.
## 8.7. Mendefinisikan Tindakan Pembersihan
Pernyataan `try` memiliki klausa opsional lain yang dimaksudkan untuk mendefinisikan tindakan pembersihan yang harus dilakukan dalam semua keadaan. Sebagai contoh:
```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```
Klausa `finally` akan dieksekusi sebagai perintah terakhir sebelum statemen `try` selesai dieksekusi. Klausa `finally` berjalan saat pernyataan `try` menghasilkan ataupun juga saat tidak menghasilkan sebuah exception. Poin-poin berikut membahas tentang apa saja yang terjadi saat exception muncul:
+ Apabila exception muncul ketika klausa `try` dieksekusi, exception dapat ditangani oleh sebuah klausa except.
+ Sebuah exception dapat muncul saat proses eksekusi klausa `except` atau `else`.
+ Apabila klausa `finally` mengeksekusi pernyataan [break](https://docs.python.org/3/reference/simple_stmts.html#break), [continue](https://docs.python.org/3/reference/simple_stmts.html#continue), atau [return](https://docs.python.org/3/reference/simple_stmts.html#return), maka exception tidak dimunculkan kembali.
+ Apabila pernyataan `try` sampai pada `break`, `continue`, atau `return`, maka klausa `finally` akan dieksekusi sebelum eksekusi pernyataan `break`, `continue`, atau `return`.
+ Apabila klausa `finally` mengandung pernyataan `return`, maka nilai yang di-return adalah nilai dari pernyataan `return` milik `finally`, bukan nilai dari pernyataan `return` milik `try`.

Sebagai contoh:
```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```
Contoh yang lebih rumit:
```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```
Dapat dilihat, klausa `finally` dieksekusi pada semua kejadian. [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError) muncul  karena ada operasi pembagian dua string yang tidak ditangani oleh klausa `except` sehingga `TypeError` dimunculkan ulang setelah klausa `finally` selesai dieksekusi.
## 8.8. Tindakan Pembersihan yang Sudah Didefinisikan
Beberapa objek menentukan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Contoh berikut mencoba membuka file dan mencetak isinya.
```python
for line in open("myfile.txt"):
    print(line, end="")
```
Masalah kode ini adalah membiarkan file terbuka untuk waktu yang lama setelah bagian kode ini selesai dieksekusi. Hal ini bukanlah masalah pada sebuah skrip sederhana, tetapi dapat menjadi masalah pada aplikasi yang berukuran besar. Pernyataan [with](https://docs.python.org/3/reference/compound_stmts.html#with) memungkinkan objek seperti file dapat digunakan dan memastikan objek tersebut selalu dibersihkan dengan cepat dan benar.
```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```
Setelah pernyataan dieksekusi, file *f* selalu ditutup, bahkan jika ada masalah saat memproses baris.