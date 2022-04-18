# 10. Mengenal Perpustakaan Standar
## 10.1. Interface Sistem Informasi
Modul [os](https://docs.python.org/3/library/os.html#module-os) menyediakan beragam fungsi untuk berinteraksi dengan sistem operasi :
```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python310'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```
**Note** : gunakan `import os` alih-alih `from os import *`.

Built-in [dir()](https://docs.python.org/3/library/functions.html#dir) dan fungsi [help()](https://docs.python.org/3/library/functions.html#help) berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti `os` :
```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```
Untuk manajemen direktori harian, modul [shutil](https://docs.python.org/3/library/shutil.html#module-shutil) menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan :
```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```
## 10.2. File Wildcard
Modul [glob](https://docs.python.org/3/library/glob.html#module-glob) menyediakan fungsi untuk membuat list file dari directory wildcard :
```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```
## 10.3. Argumen Command Line
Skrip Utility kerap kali perlu memproses argumen baris perintah. Argumen tersebut disimpan dalam bentuk list pada atribut `argv` dalam modul `sys`.
```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```
Modul [argparse](https://docs.python.org/3/library/argparse.html#module-argparse) menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah.
```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```
Pada saat dijalankan di command line dengan `python top.py --lines=5 alpha.txt beta.txt`, skrip mengatur `args.lines` ke `5` dan `args.filenames to ['alpha.txt', 'beta.txt']`.
## 10.4. Pengalihan Kesalahan Output dan Penghentian Program
Modul [sys](https://docs.python.org/3/library/sys.html#module-sys) juga memiliki atribut untuk *stdin*, *stdout*, dan *stderr*. Stdrr berfungsi memunculkan peringatan dan pesan error.
```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```
Cara tercepat untuk menghentikan skrip yaitu dengan menggunakan `sys.exit()`.
## 10.5. Pencocokan Pola String
Modul [re](https://docs.python.org/3/library/re.html#module-re) menyediakan tool ekspresi reguler untuk pemrosesan string tingkat lanjut. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan :
```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```
Untuk kapabilitas sederhana, metode string lebih disukai karena mudah dibaca dan di-debug :
```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```
## 10.6. Matematika
Modul [math](https://docs.python.org/3/library/math.html#module-math) memberikan akses ke fungsi pustaka C yang  mendasari untuk matematika floating point :
```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```
Modul [random](https://docs.python.org/3/library/random.html#module-random) menyediakan tool untuk membuat pilihan acak :
```
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```
Modul [statistics](https://docs.python.org/3/library/statistics.html#module-statistics) digunakan untuk menghitung properti statistik dasar dari data numerik :
```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```
## 10.7. Akses Internet
Terdapat banyak modul untuk mengakses internet dan memproses protokol internet. Dua modul yang sederhana antara lain [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) untuk mengambil data dari URL dan [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib) untuk mengirim email :
```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()             # Konversi bytes ke str
...         if line.startswith('datetime'):
...             print(line.rstrip())         # Hapus newline yang tertinggal
...
datetime: 2022-01-01T01:36:47.689215+00:00

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```
## 10.8. Tanggal dan Waktu
Modul [datetime](https://docs.python.org/3/library/datetime.html#module-datetime) menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus implementasinya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek yang sadar zona waktu.
```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```
## 10.9. Kompresi Data
Pengarsipan data umum dan kompresi format secara langsung didukung oleh modul termasuk : [zlib](https://docs.python.org/3/library/zlib.html#module-zlib), [gzip](https://docs.python.org/3/library/gzip.html#module-gzip), [bz2](https://docs.python.org/3/library/bz2.html#module-bz2), [lzma](https://docs.python.org/3/library/lzma.html#module-lzma), [zipfile](https://docs.python.org/3/library/zipfile.html#module-zipfile) dan [tarfile](https://docs.python.org/3/library/tarfile.html#module-tarfile).
```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```
## 10.10. Pengukuran Kinerja
User Python dapat menggunakan fitur tupel seperti packing dan unpacking selain pendekatan tradisional untuk bertukar argumen. Modul [timeit]() dengan cepat menunjukan keunggulan kinerja sederhana :
```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```
Berbeda dengan `timeit`, modul `profile` dan `pstats` menyediakan alat untuk mengidentifikasi bagian kritis waktu dalam blok kode yang lebih besar.
## 10.11. Kontrol Kualitas
Modul [doctest]() menyediakan tool untuk memindai modul dan memvalidasi tes yang tertanam dalam dokumen program.
```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```
Modul [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) tidak semudah modul [doctest](), tetapi memungkinkan serangkaian pengujian yang lebih komprehensif untuk dipertahankan dalam file terpisah :
```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```
## 10.12. "Termasuk Baterai"
Python memiliki filosofi "termasuk baterai". Ini dapat dilihat melalui package-packagenya. Contohnya :
+ Modul `xmlrpc.client` dan `xmlrpc.server` membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang mudah.
+ Package `email` adalah perpustakaan untuk mengelola pesan email, termasuk MIME dan Dokumen pesan berbasis RFC 2822 lain.

+ Package `json` menyediakan dukungan kuat untuk menguraikan format pertukaran data populer. Modul `csv` mendukung pembacaan dan penulisan file secara langsung dalam format Comma-Separated Value, umumnya didukung oleh database dan spreadsheet.

+ Modul `sqlite3` adalah pembungkus untuk pustaka database SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang tidak standar.

+ Internasionalisasi didukung oleh sejumlah modul termasuk `gettext`, `locale`, dan package `codecs`.

# 11. Mengenal Perpustakaan Standar - Bagian II
Bagian II mencakup modul yang lebih canggih yang mendukung kebutuhan pemrograman profesional. Modul ini jarang muncul dalam skrip kecil.
## 11.1. Pemformatan Output
Modul [reprlib](https://docs.python.org/3/library/reprlib.html#module-reprlib) menyediakan versi [repr()](https://docs.python.org/3/library/functions.html#repr) yang disesuaikan untuk tampilan sederhana dari kontainer besar nested:
```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```
Modul [pprint](https://docs.python.org/3/library/pprint.html#module-pprint) menawarkan kontrol yang lebih canggih dalam pencetakan objek bawaan dan objek yang didefinisikan oleh user dengan cara yang bisa dibaca oleh interpreter. Ketika hasil melebihi satu baris, "pretty printer" menambahkan jeda pada baris dan indentasi untuk menampilkan strukur data dengan lebih jelas :
```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```
Modul [textwrap](https://docs.python.org/3/library/textwrap.html#module-textwrap) memformat paragraf teks agar sesuai dengan lebar layar yang telah diatur :
```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```
Modul [locale](https://docs.python.org/3/library/locale.html#module-locale) mengakses database dengan format data yang spesifik. Atribut pengelompokan fungsi format milik lokal menyediakan cara untuk memformat angka dengan pemisah grup :
```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv() 
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```
## 11.2. Pembuatan Template
Modul [string]() mencakup kelas [Template](https://docs.python.org/3/library/string.html#string.Template) dengan sintaks yang disederhanakan yang cocok untuk pengeditan oleh end-users. Hal ini memungkinkan pengguna untuk menyesuaikan aplikasi tanpa harus mengubah aplikasi.

Format menggunakan nama placeholder yang dibentuk dengan `$` dengan identifier Python yang valid. Mengelilingi placeholder dengan kurung dapat membuat placeholder bisa diikuti dengan lebih banyak huruf alfanumerik tanpa spasi. Menulis `$$` akan membuat single escaped `$` :
```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```
Metode [substitute()](https://docs.python.org/3/library/string.html#string.Template.substitute) memunculkan `KeyError` ketika placeholder tidak disediakan dalam dictionary atau argumen keyword. Untuk aplikasi dengan gaya mail-merge, data yang diberikan user mungkin tidak lengkap, sehingga user perlu menggunakan metode [safe_substitute()](https://docs.python.org/3/library/string.html#string.Template.safe_substitute) — ini dapat membuat placeholder tidak berubah jika data tidak ada :
```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```
Subclass template bisa menentukan pembatas kustom. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file :
```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```
## 11.3. Bekerja dengan Tata Letak Rekaman Data Biner
Modul [struct](https://docs.python.org/3/library/struct.html#module-struct) menyediakan fungsi `pack()` dan `unpack()` untuk bekerja dengan format record biner dengan panjang variabel. Contoh berikut menunjukkan cara untuk melakukan loop pada informasi header di dalam file ZIP tanpa menggunakan modul [zipfile](https://docs.python.org/3/library/zipfile.html#module-zipfile). Kode pack `"H"` dan `"I"` mewakili dua dan empat byte angka yang unsigned. `"<"` menunjukan bahwa kode tersebut adalah ukuran standar dan dalam urutan byte little-endian :
```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):  # menunjukkan 3 header pertama
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size # lewati ke header selanjutnya
```
## 11.4. Multi-threading
Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Thread bisa digunakan untuk meningkatkan daya tangkap aplikasi yang menerima input user ketika pekerjaan lain berjalan di background. 

Kode berikut menunjukkan bagaimana modul [threading](https://docs.python.org/3/library/threading.html#module-threading) high level dapat menjalankan task di background ketika program utama sedang berjalan :
```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()  # menunggu background task selesai
print('Main program waited until background was done.')
```
Pendekatan yang lebih disukai untuk koordinasi tugas adalah memusatkan semua akses ke sumber daya dalam satu thread dan kemudian menggunakan modul [queue](https://docs.python.org/3/library/queue.html#module-queue) untuk mengirimi thread tersebut dengan request dari thread lain. Aplikasi yang menggunakan objek `Queue` untuk komunikasi dan koordinasi inter-thread lebih mudah dirancang, lebih mudah dibaca, dan lebih andal.
## 11.5. Logging
Modul [logging](https://docs.python.org/3/library/logging.html#module-logging) menawarkan sistem logging yang berfitur lengkap dan fleksibel. Paling sederhana, pesan log dikirim ke file atau ke `sys.stderr` :
```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```
Hal ini menghasilkan output :

```python
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```
Sistem logging dapat dikonfigurasi langsung dari Python atau dapat dimuat dari file konfigurasi yang dapat diedit pengguna untuk logging yang disesuaikan tanpa mengubah aplikasi.
## 11.6. Referensi Lemah
Python melakukan manajemen memori otomatis. Memori dibebaskan segera setelah referensi terakhir dihilangkan.

Modul [weakref](https://docs.python.org/3/library/weakref.html#module-weakref) menyediakan tool untuk melacak objek tanpa membuat referensi. Ketika objek tidak lagi diperlukan, objek tersebut secara otomatis dihapus dari tabel weakref dan memicu callback memunculkan untuk objek weakref.
```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10) # membuat reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a  # tidak membuat referensi
>>> d['primary']  # ambil objek jika masih aktif
10
>>> del a # hapus satu referensi tersebut
>>> gc.collect() # jalankan garbage collection
0
>>> d['primary'] # entry dihapus secara otomatis
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary'] # entry dihapus secara otomatis
  File "C:/python310/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```
## 11.7. Tool untuk List
Banyak kebutuhan struktur data yang bisa dipertemukan dengan jenis list built-in. Namun, terkadang ada kebutuhan untuk implementasi alternatif dengan pertukaran kinerja yang berbeda. 

Modul [array](https://docs.python.org/3/library/array.html#module-array) menyediakan objek [array()](https://docs.python.org/3/library/array.html#array.array) yang berbentuk seperti list yang hanya menyimpan data homogen yang disimpan secara compact. Contoh berikut menunjukkan array angka yang disimpan sebagai angka biner unsigned dua byte (typecode `"H"`) :
```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```
Modul [collections](https://docs.python.org/3/library/collections.html#module-collections) menyediakan objek [deque()](https://docs.python.org/3/library/collections.html#collections.deque) seperti list dengan penambahan dan kemunculan yang lebih cepat dari sisi kiri tetapi pencarian yang lebih lambat di tengah. Objek-objek ini cocok untuk mengimplementasikan queue :
```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```
```python
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```
Perpustakaan juga menawarkan tool lain seperti modul [bisect](https://docs.python.org/3/library/bisect.html#module-bisect) dengan fungsi untuk memanipulasi list yang urut :
```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```
Modul [heapq](https://docs.python.org/3/library/heapq.html#module-heapq) menyediakan fungsi untuk mengimplementasikan heap berdasarkan list reguler. Entri bernilai terendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin menjalankan pengurutan list lengkap :
```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data) # mengatur ulang list ke dalam heap urutan
>>> heappush(data, -5) # masukkan entry baru
>>> [heappop(data) for i in range(3)]  # ambil tiga entry terkecil
[-5, 0, 1]
```
## 11.8. Titik Mengambang Desimal Aritmatika
Modul [decimal](https://docs.python.org/3/library/decimal.html#module-decimal) menawarkan tipe data [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal) untuk titik mengambang desimal aritmatika. Dibandingkan dengan `float` built-in dari floating point biner, kelas ini sangat membantu untuk :
+ aplikasi keuangan dan penggunaan lain yang perlu representasi desimal.
+ kontrol presisi.
+ kontrol atas pembulatan untuk memenuhi persyaratan hukum atau regulasi.
+ pelacakan letak desimal yang signifikan. Atau,
+ aplikasi di mana pengguna mengharapkan hasil yang sesuai dengan perhitungan yang dilakukan manual.

Misalnya, menghitung pajak 5% untuk biaya telepon sebesar 70 sen akan memberikan hasil yang berbeda pada floating point desimal dan floating point biner. Perbedaan menjadi signifikan jika hasilnya dibulatkan ke sen terdekat :
```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```
Representasi yang tepat memungkinkan kelas `Decimal` untuk mengimplementasikan perhitungan modulo dan pengujian persamaan yang tidak cocok untuk floating point biner :
```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
```
Modul [decimal](https://docs.python.org/3/library/decimal.html#module-decimal) menyediakan aritmetika dengan presisi sesuai yang diperlukan :
```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```