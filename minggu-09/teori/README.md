# 12. Virtual Environment dan Package

## 12.1. Pengenalan
Python sebagai sebuah aplikasi terkadang tidak menggunakan package dan modul yang berasal dari *standard library*. Aplikasi terkadang akan membutuhkan versi library tertentu untuk dapat mengatasi bug atau mengatasi versi interface yang sudah usang.

Hal ini berarti sebuah instalasi Python tidak dapat memenuhi persyaratan tiap aplikasi berbeda. Untuk mengatasi masalah ini, perlu membuat sebuah *virtual environment*. Virtual environment merupakan direktori mandiri yang dapat berisi berbagai versi Python lengkap dengan package tambahan.

Tiap aplikasi berbeda dapat menggunakan beragam virtual environment yang berbeda pula.

## 12.2. Membuat Virtual Environment
Modul yang digunakan untuk membuat dan mengatur tentang virtual environment bernama [venv](https://docs.python.org/3/library/venv.html#module-venv). Biasanya `venv` akan menginstal versi terbaru dari Python. 

Untuk membuat virtual environment, pilih sebuah direktori untuk menempatkannya, kemudian jalankan skrip modul `venv` :
```python
python3 -m venv tutorial-env
```
Perintah di atas dapat membuat direktori `tutorial-env` dan membuat salinan dari interpreter Python dan support file lainnya di dalam direktori.


Lokasi umum direktori untuk virtual environment adalah `.venv`. Penamaan ini menjaga direktori khususnya yang tersembunyi di *shell* dan mengeluarkannya dari jalur sambil memberikannya nama yang menjelaskan alasan direktori ini ada.

Setelah membuat sebuah *virtual environment*, langkah selanjutnya adalah mengaktifkannya. Pada windows, jalankan :
```python
tutorial-env\Scripts\activate.bat
```
Pada Unix atau MacOS, jalankan :
```python
source tutorial-env/bin/activate
```

Aktifnya virtual environment dapat mengubah shell prompt untuk jenis virtual environment yang digunakan dan memodifikasi environment agar ketika menjalankan `python` kita akan mendapatkan versi tertentu dari Python. Sebagai contoh :
```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

## 12.3. Mengatur Package menggunakan pip
Kita dapat menginstal, mengupgrade, dan menghapus package menggunakan program **pip**. Secara default `pip` akan menginstal package dari *Python Package Index*, <https://pypi.org>.

`pip` mempunyai sejumlah perintah bawaan : "install", "uninstall", "freeze", dll. Kita dapat menginstal versi terbaru dari package dengan menetapkan nama package :
```python
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```
Kita dapat juga menginstal versi tertentu dari package dengan memberi nama pada package menggunakan `==` dan nomor versi :
```python
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```
Jika kita menjalankan ulang perintah di atas, `pip` akan menyadari bahwa versi yang diminta sudah terinstal dan `pip` tidak akan melakukan apapun. Untuk mengupgrade ke versi terbaru, dapat menggunakan perintah `pip install --upgrade` :
```python
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```
Perintah `pip uninstall` dapat menghapus satu atau lebih nama package dari virtual environment.

perintah `pip show` akan menampilkan informasi tentang package tertentu :
```python
(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```
Perintah `pip list` berfungsi menampilkan semua package yang terinstal pada virtual environment :
```python
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```
Perintah `pip freeze` akan menghasilkan daftar serupa dari package yang terinstal, tetapi outputnya menggunakan format dari `pip install`. Contohnya adalah memasukan daftar berikut pada file `requirements.txt` :
```python
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```
File `requirements.txt` dapat terikat pada versi kontrol dan terkirim sebagai bagian dari aplikasi. Pengguna dapat menginstall semua package yang diperlukan dengan perintah `install -r` :
```python
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```

# Praktik Menggunakan Virtual Environment (Conda)
Conda merupakan package manajemen sistem berbasis *open-source* dan manajemen environment yang dapat menjadi *package manager* dalam membantu menemukan dan menginstal banyak package.

Conda dapat dengan mudah digunakan. Conda dapat membuat, menyimpan, memuat, dan mengganti antar environment yang berada di dalam komputer lokal. Conda dapat digunakan pada command line dari Anaconda Prompt.

## Mengelola Conda
Untuk memverifikasi instalasi conda dapat menjalankan perintah `conda --version`. Conda akan menampilkan nomor versi yang sudah terinstal.
```python
(base) C:\Users\USER>conda --version
conda 4.10.3
```

Untuk mengupdate versi conda dapat menggunakan perintah `conda update conda`.
```python
(base) C:\Users\USER>conda update conda
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: E:\Anaconda

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-4.12.0               |   py39haa95532_0        14.5 MB
    ------------------------------------------------------------
                                           Total:        14.5 MB

The following packages will be UPDATED:

  conda                               4.10.3-py39haa95532_0 --> 4.12.0-py39haa95532_0
  conda-package-han~                   1.7.3-py39h8cc25b3_1 --> 1.8.1-py39h8cc25b3_0
```
Jika terdapat versi terbaru yang perlu diupdate, akan muncul pertanyaan `Proceed ([y]/n)?`, masukan `y` untuk melanjutkan.
```python
Proceed ([y]/n)? y


Downloading and Extracting Packages
conda-4.12.0         | 14.5 MB   | ###################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

## Mengelola Environment
Conda dapat digunakan untuk membuat environment terpisah. Ketika memulai conda, default environment yang muncul bernama `base`.

### 1. Membuat environment baru dan menginstal package di dalamnya.
Environment pada praktik ini menggunakan nama `rusa` dan menginstal package BioPython dengan perintah `conda create --name rusa biopython`.
```python
(base) C:\Users\USER>conda create --name rusa biopython
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: E:\Anaconda\envs\rusa

  added / updated specs:
    - biopython


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    biopython-1.78             |   py39h2bbff1b_0         2.1 MB
    ca-certificates-2022.3.29  |       haa95532_1         122 KB
    certifi-2021.10.8          |   py39haa95532_2         152 KB
    numpy-1.21.5               |   py39h7a0a035_1          25 KB
    numpy-base-1.21.5          |   py39hca35cd5_1         4.4 MB
    openssl-1.1.1n             |       h2bbff1b_0         4.8 MB
    python-3.9.12              |       h6244533_0        17.1 MB
    setuptools-61.2.0          |   py39haa95532_0         1.0 MB
    six-1.16.0                 |     pyhd3eb1b0_1          18 KB
    sqlite-3.38.2              |       h2bbff1b_0         807 KB
    tzdata-2022a               |       hda174b7_0         109 KB
    wheel-0.37.1               |     pyhd3eb1b0_0          33 KB
    ------------------------------------------------------------
                                           Total:        30.7 MB

The following NEW packages will be INSTALLED:

  biopython          pkgs/main/win-64::biopython-1.78-py39h2bbff1b_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_1
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py39h2bbff1b_0
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py39h277e83a_0
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py39hf11a4ad_0
  numpy              pkgs/main/win-64::numpy-1.21.5-py39h7a0a035_1
  numpy-base         pkgs/main/win-64::numpy-base-1.21.5-py39hca35cd5_1
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_1
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2
```
Conda akan melakukan pengecekan untuk melihat package yang tersedia.
```python
Proceed ([y]/n)? y


Downloading and Extracting Packages
numpy-1.21.5         | 25 KB     | ###################################### | 100%
six-1.16.0           | 18 KB     | ###################################### | 100%
biopython-1.78       | 2.1 MB    | ###################################### | 100%
tzdata-2022a         | 109 KB    | ###################################### | 100%
wheel-0.37.1         | 33 KB     | ###################################### | 100%
ca-certificates-2022 | 122 KB    | ###################################### | 100%
setuptools-61.2.0    | 1.0 MB    | ###################################### | 100%
certifi-2021.10.8    | 152 KB    | ###################################### | 100%
openssl-1.1.1n       | 4.8 MB    | ###################################### | 100%
numpy-base-1.21.5    | 4.4 MB    | ###################################### | 100%
sqlite-3.38.2        | 807 KB    | ###################################### | 100%
python-3.9.12        | 17.1 MB   | ###################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate rusa
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```
### 2. Penggunaan atau "pengaktifan" environment baru.
Untuk mengaktifkan menggunakan perintah `conda activate rusa`.
```python
(base) C:\Users\USER>conda activate rusa

(rusa) C:\Users\USER>
```
Dari output di atas, environment default `base` sudah berubah nama menjadi `rusa`.
### 3. Melihat daftar lengkap environment.
Untuk melihat daftar lengkap environment menggunakan perintah `conda info --envs`.
```python
(rusa) C:\Users\USER>conda info --envs
# conda environments:
#
base                     E:\Anaconda
rusa                  *  E:\Anaconda\envs\rusa
```
### 4. Mengubah environment saat ini ke default (base).
Environment `rusa` dapat dinonaktifkan menggunakan perintah `conda deactivate`.
```python
(rusa) C:\Users\USER>conda deactivate

(base) C:\Users\USER>
```
Setelah dinonaktifkan, conda secara otomatis akan kembali ke environment default yaitu `base`.