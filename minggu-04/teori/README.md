# 6. Modules
*Module* merupakan file yang memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam instance interpreter yang interaktif (kumpulan variabel yang dapat diakses dalam skrip yang dijalankan di tingkat atas dan dalam mode kalkulator). Berikut ini merupakan contoh penggunaan module, dibuat file bernama `fibo.py` :
```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```
Untuk memanggil file dapat menggunakan perintah :
```python
import fibo
```
File modul `fibo` dapat diakses dengan fungsi :
```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```
## 6.1. Lebih Lanjut tentang Modules
Module dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya saat pertama kali nama modul ditemukan dalam pernyataan impor.

Module dapat mengimport module lain. Terdapat varian dari pernyataan [import](https://docs.python.org/3/reference/simple_stmts.html#import) yang mengimport nama dari module langsung ke tabel simbol module pengimport, contohnya :
```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Terdapat pula varian untuk mengimport semua nama yang didefinisikan module :
```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Jika nama modul diikuti oleh `as`, maka nama berikut `as` terikat langsung ke modul yang diimpor.
```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Efek serupa dapat ditimbulkan ketika menggunakan [from](https://docs.python.org/3/reference/simple_stmts.html#from) :
```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
**Catatan** : Untuk alasan efisiensi, setiap modul hanya diimpor sekali per sesi juru bahasa. Oleh karena itu, jika modul diubah, harus memulai ulang penerjemah – atau, jika hanya satu modul yang ingin diuji secara interaktif, gunakan [importlib.reload()](https://docs.python.org/3/library/importlib.html#importlib.reload), mis. `import importlib`; `importlib.reload(modulename)`.
### 6.1.1. Menjalankan Module sebagai Script
Ketika menjalankan module python, dapat menggunakan :
```python
python fibo.py <arguments>
```
Kode dalam module akan dieksekusi, sama seperti ketika diimport, tetapi dengan `__name__`diset ke `"__main__"`.
```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
File dapat digunakan sebagai script dan juga sebagai module yang dapat diimport, karena kode yang di*parse* pada command line hanya berjalan jika module dieksekusi sebagai file "main" :
```python
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```
Jika module diimpor, kode tidak dapat berjalan:
```python
>>> import fibo
>>>
```
### 6.1.2. Jalur Pencarian Module
Ketika sebuah modul bernama `spam` diimpor, interpreter pertama mencari modul built-in dengan nama itu. Jika tidak ditemukan, maka akan mencari file bernama `spam.py` dalam daftar direktori yang diberikan oleh variabel [sys.path.](https://docs.python.org/3/library/sys.html#sys.path). `sys.path` diinisialisasi dari lokasi berikut :
* Direktori yang berisi script input
* PYTHONPATH
* Instalasi default

Setelah inisialisasi, program Python dapat memodifikasi file `sys.path`. Direktori yang berisi skrip yang sedang dijalankan ditempatkan di awal jalur pencarian, di depan jalur standar pustaka. Ini berarti bahwa skrip di direktori itu akan dimuat alih-alih modul dengan nama yang sama di direktori perpustakaan.
### 6.1.3. File Python "Dikompilasi"
Untuk mempercepat pemuatan modul, Python menyimpan versi kompilasi dari setiap modul dalam `__pycache__` direktori dengan nama, di mana versi tersebut mengkodekan format file yang dikompilasi; biasanya berisi nomor versi Python. 

Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah itu kedaluwarsa dan perlu dikompilasi ulang. Ini adalah proses yang sepenuhnya otomatis.

Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, tidak memeriksa cache jika tidak ada modul sumber. 

Beberapa tips untuk ahli :

* Gunakan switch -0 dan -00 pada Python command untuk mengurangi ukuran modul yang dikompilasi.
* Sebuah program tidak berjalan lebih cepat saat dibaca dari `.pyc` file daripada saat dibaca dari `.py` file; satu-satunya hal yang lebih cepat tentang file `.pyc` adalah kecepatan pemuatannya.
* Modul `compileall` dapat membuat file `.pyc` untuk semua modul dalam direktori.
* Ada lebih detail tentang proses ini, termasuk diagram alir keputusan, di [PEP 3147](https://www.python.org/dev/peps/pep-3147/).

## 6.2. Module Standar
Python hadir dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah. Beberapa modul dibangun ke dalam juru bahasa; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, module [winreg](https://docs.python.org/3/library/winreg.html#module-winreg) hanya disediakan pada sistem Windows. Terdapat juga module yang sudah dibuat di setiap bahasa Python yaitu [sys](https://docs.python.org/3/library/sys.html#module-sys). Variabel `sys.ps1` dan `sys.ps2` mendefinisikan string yang digunakan sebagai prompt primer dan sekunder :
```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```
Kedua variabel ini hanya ditentukan jika interpreter dalam mode interaktif.

Variabel `sys.path` adalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkungan [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH), atau dari default bawaan jika  `PYTHONPATH` tidak diatur. Dapat memodifikasinya menggunakan operasi daftar standar :
```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```
## 6.3. Fungsi [dir()](https://docs.python.org/3/library/functions.html#dir)
Fungsi bawaan `dir()` digunakan untuk mengetahui nama mana yang didefinisikan oleh module. Ini mengembalikan daftar string yang diurutkan :
```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```
Tanpa argumen, `dir()` dapat membuat list dengan nama yang telah ditentukan :
```python 
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```
Dapat dilihat bahwa ini mencantumkan semua jenis nama: variabel, modul, fungsi, dll.

`dir()` tidak mencantumkan nama fungsi dan variabel bawaan. Jika list dibutuhkan, dapat didefinisikan dengan module standar [builtins](https://docs.python.org/3/library/builtins.html#module-builtins) :
```python
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```
## 6.4. Packages
adalah cara menyusun namespace modul Python dengan menggunakan "nama modul bertitik". Misalnya, nama modul `A.B` menunjuk sebuah sub modul yang dinamai `B` dalam sebuah paket bernama `A`.

Berikut adalah kemungkinan struktur untuk paket (dinyatakan dalam bentuk sistem file hierarkis) :
```python
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```
Saat mengimpor paket, Python mencari melalui direktori untuk `sys.path` mencari subdirektori paket.

File`__init__.py` dibutuhkan untuk membuat Python menganggap direktori berisi file sebagai package. Pada beberapa kasus, `__init__.py` bisa hanya sekedar file kosong, tetapi juga bisa mengeksekusi insialisasi kode untuk package atau juga bisa men-set variabel `__all__`.

Pengguna package dapat mengimport modul individual dari package, contohnya :
```python
import sound.effects.echo
```
import di atas memuat sub module `sound.effects.echo` yang harus direferensikan dengan penamaan lengkap.
```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```
Alternatif untuk mengimport module :
```python
from sound.effects import echo
```
Ini juga memuat sub module echo, dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut :
```python
echo.echofilter(input, output, delay=0.7, atten=4)
```
Namun variasi lain adalah mengimpor fungsi atau variabel yang diinginkan secara langsung :
```python
from sound.effects.echo import echofilter
```
Sekali lagi, ini memuat sub module echo, tetapi ini membuat fungsinya `echofilter()` tersedia secara langsung :
```python
echofilter(input, output, delay=0.7, atten=4)
```
Dapat dilihat  bahwa saat menggunakan , item dapat berupa submodul (atau subpaket) paket, atau nama lain yang ditentukan dalam paket, seperti fungsi, kelas, atau variabel.
### 6.4.1 Mengimport * dari Packages
Apa yang akan terjadi ketika pengguna menulis `from sound.effects import *`? Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke sistem file, menemukan sub module mana yang ada dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor sub-module mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika sub-module diimpor secara eksplisit.

Satu-satunya solusi adalah bagi pembuat paket untuk memberikan indeks eksplisit dari paket tersebut. Pernyataan `import` menggunakan konvensi berikut: jika kode paket `__init__.py` mendefinisikan daftar bernama `__all__`, itu dianggap sebagai list nama module yang harus diimpor ketika ditemui. Misalnya, file dapat berisi kode berikut: `from package import *sound/effects/__init__.py`
```python
__all__ = ["echo", "surround", "reverse"]
```
Jika `__all__` tidak didefinisikan, pernyataan `from sound.effects import *` tidak mengimpor semua sub module dari paket ke namespace saat ini; itu hanya memastikan bahwa paket telah diimpor (mungkin menjalankan kode inisialisasi apa pun di`__init__.py`) dan kemudian mengimpor nama apa pun yang ditentukan dalam paket. Lihat kode berikut : 
```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```
Pada kode di atas, module `echo` dan `surround` diimpor di dalam current namespace karena modules tersebut didefinisikan pada package `sound.effects` ketika statement `from...import` dijalankan.
### 6.4.2. Referensi Intra-Package
Ketika paket disusun menjadi sub paket, kita dapat melakukan impor absolut untuk untuk me-refer ke submodul package sibling. Misalnya, jika module `sound.filters.vocoder` perlu menggunakan echomodul dalam `sound.effects` paket, itu dapat menggunakan `.from sound.effects import echo`.
```python
from . import echo
from .. import formats
from ..filters import equalizer
```
Dapat dilihat bahwa impor relatif didasarkan pada nama module saat ini. Karena nama module utama selalu `"__main__"`, modul yang dimaksudkan untuk digunakan sebagai module utama aplikasi Python harus selalu menggunakan impor absolut.
### 6.4.3. Package di Beberapa Direktori
Package mendukung satu atribut khusus lagi, [__path__](https://docs.python.org/3/reference/import.html#path__). Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan paket `__init__.py` sebelum kode dalam file itu dieksekusi. Variabel ini dapat dimodifikasi; hal itu akan memengaruhi pencarian module dan sub paket di masa mendatang yang terdapat dalam paket.

Meskipun fitur ini tidak sering diperlukan, fitur ini dapat digunakan untuk memperluas kumpulan module yang ditemukan dalam sebuah package.