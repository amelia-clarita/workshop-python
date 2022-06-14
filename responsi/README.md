# Responsi Workshop Python
Pada responsi ini dipraktikan mendownload dan menampilkan data dari url menggunakan python. Untuk praktik dilakukan bukan pada default environment conda (base), sehingga perlu mengaktifkan terlebih dahulu environment yang mau digunakan. Berikut cara mengaktifkannya
**Catatan** : environment berikut sudah pernah dibuat sebelumnya, sehingga hanya perlu diaktifkan untuk penggunaannya.
```python
(base) C:\Users\USER>conda info --envs
# conda environments:
#
base                  *  E:\Anaconda
ameliaenv                E:\Anaconda\envs\ameliaenv
rusa                     E:\Anaconda\envs\rusa


(base) C:\Users\USER>conda activate ameliaenv
```
Setelah aktif, tampilan anaconda shell akan seperti berikut.
```python
(ameliaenv) C:\Users\USER>
```
Untuk menampilkan data, terlebih dahulu menginstall pandas dan module requests pada environment dengan perintah berikut.
```python
(ameliaenv) C:\Users\USER>conda install pandas

(ameliaenv) C:\Users\USER>conda install requests
Collecting package metadata (current_repodata.json): done
Solving environment: done
```
Untuk memperoses download dan extract pandas, akan muncul pertanyaan `Proceed ([y]/n)?` masukan `y` untuk melanjutkan.

Selanjutnya, masuk ke python shell.
```python
(ameliaenv) C:\Users\USER>python
Python 3.10.4 | packaged by conda-forge | (main, Mar 30 2022, 08:38:02) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Untuk menampilkan data menggunakan perintah berikut.
```python
import pandas as pd
import io
import requests

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

data_negara = requests.get(url).content
read_data = pd.read_csv(io.StringIO(data_negara.decode('utf-8')))
print(read_data)
```
Data yang tampil adalah berikut ini.
```python
(ameliaenv) C:\Users\USER>python responsi.py
       Country         Region
0      Algeria         AFRICA
1       Angola         AFRICA
2        Benin         AFRICA
3     Botswana         AFRICA
4      Burkina         AFRICA
..         ...            ...
189   Paraguay  SOUTH AMERICA
190       Peru  SOUTH AMERICA
191   Suriname  SOUTH AMERICA
192    Uruguay  SOUTH AMERICA
193  Venezuela  SOUTH AMERICA

[194 rows x 2 columns]
```