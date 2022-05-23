# Pemrograman Web - Flask
Flask merupakan framework web pada Python yang dapat digunakan untuk membangun sebuah web terstruktur. Fungsi utama dari flask sendiri adalah sebagai kerangka kerja aplikasi dan tampilan dari suatu web.

Untuk menginstal Flask, direkomendasikan menggunakan versi terbaru dari Python. Flask sendiri sudah mendukung Python 3.7 dan versi terbaru. Berikut ini merupakan distribusi yang secara otomatis terinstal ketika Flask terunduh.
- `Werkzeug` mengimplementasikan WSGI, antarmuka Python standar antara aplikasi dan server.
- `Jinja` adalah bahasa template yang merender halaman yang dilayani aplikasi.
- `MarkupSafe` termuat bersama dengan Jinja, hadir dari input yang tidak tepercaya saat merender template untuk menghindari serangan injeksi.
- `ItsDangerous` menandatangani data dengan aman untuk memastikan integritasnya. Ini digunakan untuk melindungi cookie sesi Flask.
- `Click` adalah kerangka kerja untuk menulis aplikasi baris perintah. Ini memberikan flask perintah dan memungkinkan menambahkan perintah manajemen kustom.

Untuk mengelola dependensi, dapat menggunakan *virtual envinronment*. Virtual envinronment merupakan grup independen dari pustaka python, satu untuk setiap proyek.

## Membuat Environment dan Mengaktifkannya
Perintah berikut dapat digunakan untuk membuat environment baru.
```python
(base) C:\Users\USER>conda create --name ameliaenv biopython
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: E:\Anaconda\envs\ameliaenv

  added / updated specs:
    - biopython


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    biopython-1.78             |  py310h2bbff1b_0         2.2 MB
    ca-certificates-2022.4.26  |       haa95532_0         124 KB
    certifi-2022.5.18.1        |  py310haa95532_0         157 KB
    libffi-3.4.2               |       h604cdb4_1          43 KB
    mkl-service-2.4.0          |  py310h2bbff1b_0          48 KB
    mkl_fft-1.3.1              |  py310ha0764ea_0         136 KB
    mkl_random-1.2.2           |  py310h4ed8f06_0         221 KB
    numpy-1.22.3               |  py310h6d2d95c_0          25 KB
    numpy-base-1.22.3          |  py310h206c741_0         4.9 MB
    openssl-1.1.1o             |       h2bbff1b_0         4.8 MB
    pip-21.2.4                 |  py310haa95532_0         1.9 MB
    python-3.10.4              |       hbb2ffb3_0        15.9 MB
    setuptools-61.2.0          |  py310haa95532_0         1.0 MB
    sqlite-3.38.3              |       h2bbff1b_0         806 KB
    tk-8.6.11                  |       h2bbff1b_1         3.3 MB
    wincertstore-0.2           |  py310haa95532_2          15 KB
    xz-5.2.5                   |       h8cc25b3_1         246 KB
    zlib-1.2.12                |       h8cc25b3_2         116 KB
    ------------------------------------------------------------
                                           Total:        35.8 MB

The following NEW packages will be INSTALLED:

  biopython          pkgs/main/win-64::biopython-1.78-py310h2bbff1b_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  bzip2              pkgs/main/win-64::bzip2-1.0.8-he774522_0
  ca-certificates    pkgs/main/win-64::ca-certificates-2022.4.26-haa95532_0
  certifi            pkgs/main/win-64::certifi-2022.5.18.1-py310haa95532_0
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
  libffi             pkgs/main/win-64::libffi-3.4.2-h604cdb4_1
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py310h2bbff1b_0
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py310ha0764ea_0
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py310h4ed8f06_0
  numpy              pkgs/main/win-64::numpy-1.22.3-py310h6d2d95c_0
  numpy-base         pkgs/main/win-64::numpy-base-1.22.3-py310h206c741_0
  openssl            pkgs/main/win-64::openssl-1.1.1o-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py310haa95532_0
  python             pkgs/main/win-64::python-3.10.4-hbb2ffb3_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py310haa95532_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_1
  sqlite             pkgs/main/win-64::sqlite-3.38.3-h2bbff1b_0
  tk                 pkgs/main/win-64::tk-8.6.11-h2bbff1b_1
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py310haa95532_2
  xz                 pkgs/main/win-64::xz-5.2.5-h8cc25b3_1
  zlib               pkgs/main/win-64::zlib-1.2.12-h8cc25b3_2


Proceed ([y]/n)? y


Downloading and Extracting Packages
openssl-1.1.1o       | 4.8 MB    | ############################################################################ | 100%
numpy-base-1.22.3    | 4.9 MB    | ############################################################################ | 100%
mkl-service-2.4.0    | 48 KB     | ############################################################################ | 100%
biopython-1.78       | 2.2 MB    | ############################################################################ | 100%
sqlite-3.38.3        | 806 KB    | ############################################################################ | 100%
setuptools-61.2.0    | 1.0 MB    | ############################################################################ | 100%
pip-21.2.4           | 1.9 MB    | ############################################################################ | 100%
zlib-1.2.12          | 116 KB    | ############################################################################ | 100%
tk-8.6.11            | 3.3 MB    | ############################################################################ | 100%
mkl_fft-1.3.1        | 136 KB    | ############################################################################ | 100%
mkl_random-1.2.2     | 221 KB    | ############################################################################ | 100%
numpy-1.22.3         | 25 KB     | ############################################################################ | 100%
wincertstore-0.2     | 15 KB     | ############################################################################ | 100%
certifi-2022.5.18.1  | 157 KB    | ############################################################################ | 100%
ca-certificates-2022 | 124 KB    | ############################################################################ | 100%
libffi-3.4.2         | 43 KB     | ############################################################################ | 100%
python-3.10.4        | 15.9 MB   | ############################################################################ | 100%
xz-5.2.5             | 246 KB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate ameliaenv
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) C:\Users\USER>
```
Selanjutnya, mengaktifkan environment yang sudah dibuat.
```python
(base) C:\Users\USER>conda activate ameliaenv

(ameliaenv) C:\Users\USER>conda info --envs
# conda environments:
#
base                     E:\Anaconda
ameliaenv             *  E:\Anaconda\envs\ameliaenv
rusa                     E:\Anaconda\envs\rusa


(ameliaenv) C:\Users\USER>
```
Setelah itu, membuat file project untuk instalasi flask.

## Instalasi Flask

```python
(ameliaenv) C:\Users\USER>mkdir myproject

(ameliaenv) C:\Users\USER>cd myproject

(ameliaenv) C:\Users\USER\myproject>
```
Untuk instalasi flask dapat menggunakan perintah berikut.
```python
(ameliaenv) C:\Users\USER\myproject>conda install flask
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: E:\Anaconda\envs\ameliaenv

  added / updated specs:
    - flask


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    click-8.0.4                |  py310haa95532_0         157 KB
    flask-2.0.3                |     pyhd3eb1b0_0          76 KB
    jinja2-3.0.3               |     pyhd3eb1b0_0         106 KB
    markupsafe-2.0.1           |  py310h2bbff1b_0          24 KB
    werkzeug-2.0.3             |     pyhd3eb1b0_0         221 KB
    ------------------------------------------------------------
                                           Total:         583 KB

The following NEW packages will be INSTALLED:

  click              pkgs/main/win-64::click-8.0.4-py310haa95532_0
  colorama           pkgs/main/noarch::colorama-0.4.4-pyhd3eb1b0_0
  dataclasses        pkgs/main/noarch::dataclasses-0.8-pyh6d0b6a4_7
  flask              pkgs/main/noarch::flask-2.0.3-pyhd3eb1b0_0
  itsdangerous       pkgs/main/noarch::itsdangerous-2.0.1-pyhd3eb1b0_0
  jinja2             pkgs/main/noarch::jinja2-3.0.3-pyhd3eb1b0_0
  markupsafe         pkgs/main/win-64::markupsafe-2.0.1-py310h2bbff1b_0
  werkzeug           pkgs/main/noarch::werkzeug-2.0.3-pyhd3eb1b0_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
markupsafe-2.0.1     | 24 KB     | ############################################################################ | 100%
click-8.0.4          | 157 KB    | ############################################################################ | 100%
jinja2-3.0.3         | 106 KB    | ############################################################################ | 100%
flask-2.0.3          | 76 KB     | ############################################################################ | 100%
werkzeug-2.0.3       | 221 KB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

(ameliaenv) C:\Users\USER\myproject>
```
Setelah proses instalasi flask, selanjutnya membuat project menggunakan flask.

## Project Layout Menggunakan Flask
Sebelum itu, terlebih dahulu dibuat sebuah project direktori.
```python
(ameliaenv) C:\Users\USER\myproject>mkdir flask-tutorial

(ameliaenv) C:\Users\USER\myproject>cd flask-tutorial

(ameliaenv) C:\Users\USER\myproject\flask-tutorial>
```
Sebuah aplikasi Flask dapat berupa sebuah file sederhana. Sebagai contoh file `hello.py` berikut.
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```
Akan tetapi, ketika sebuah proyek semakin besar, menjadi sangat sulit untuk menyimpan semua kode dalam satu file. Proyek Python menggunakan *package* untuk mengatur kode ke dalam beberapa modul yang dapat diimpor jika diperlukan. Direktori proyek tersebut akan berisi :
- `flaskr/`, paket Python yang berisi kode aplikasi dan file.
- `tests/`, direktori yang berisi modul pengujian.
- `venv/`, lingkungan virtual Python tempat Flask dan dependensi lainnya diinstal.
- File instalasi yang memberi tahu Python cara menginstal proyek.
- Konfigurasi kontrol versi, seperti git.
- File proyek lain yang mungkin akan ditambahkan di masa mendatang.

## Aplikasi Flask
Aplikasi flask merupakan turunan dari kelas flask. Segala sesuatu tentang aplikasi, seperti konfigurasi dan URL akan termuat dengan kelas ini. Sebelum memulai pengkodean, dibuat direktori `flaskr` terlebih dahulu kemudian diisi dengan sebuah file `__init__.py`. file `__init__.py` akan berisi *aplication factory* dan memberitahu Python bahwa flaskr direktori harus diperlakukan sebagai sebuah paket.
```python
(ameliaenv) C:\Users\USER\myproject\flask-tutorial>mkdir flaskr
```
Isi dari file `__init__.py` sendiri adalah sebagai berikut.
```python
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```
Untuk menjalankan aplikasi, dapat menggunakan perintah flask dari terminal.
```python
(ameliaenv) C:\Users\USER\myproject\flask-tutorial>set FLASK_APP=flaskr

(ameliaenv) C:\Users\USER\myproject\flask-tutorial>set FLASK_ENV=development

(ameliaenv) C:\Users\USER\myproject\flask-tutorial>flask run
 * Serving Flask app 'flaskr' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 472-972-706
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [24/May/2022 01:01:37] "GET /hello HTTP/1.1" 200 -
127.0.0.1 - - [24/May/2022 01:01:40] "GET /favicon.ico HTTP/1.1" 404 -
```
Setelah itu, untuk membuktikan aplikasi web Flask sudah berjalan, dapat dilakukan pengecekan pada browser melalui link http://127.0.0.1:5000/hello. Jika pada browser menampilkan tulisan "Hello World", maka aplikasi flask sudah berjalan.

**Note** : Tampilan screenshot browser dapat dilihat pada file src pertemuan-11.