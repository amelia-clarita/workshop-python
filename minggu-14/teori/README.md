# Scikit-Learn
Scikit-learn merupakan library machine learning berbasis open source yang mensupport pembelajaran yang diawasi dan tidak diawasi. Scikit-learn juga menyediakan berbagai tools untuk pemasangan model, pra-pemrosesan data, pemilihan model, evaluasi model, dan banyak utilitas lain.

Untuk instalasi scikit-learn sendiri dapat menggunakan packager pip ataupun conda. Berikut ini merupakan langkah instalasi scikit-learn menggunakan anaconda pada sistem operasi windows.
* Pada anaconda prompt jalankan `conda create -n sklearn-env -c conda-forge scikit-learn`
* Selanjutnya mengaktifkan scikit-learn dengan menjalankan `conda activate sklearn-env`
* Untuk mengecek instalasi dapat menggunakan perintah
	```python
	>>> conda list scikit-learn  # to see which scikit-learn version is installed
	
	>>> conda list  # to see all packages installed in the active conda environment
	
	>>> python -c "import sklearn; sklearn.show_versions()"
	```
* Catatan : Untuk menghindari potensi package yang bertentangan, dapat menggunakan virtual environment (venv) atau conda environment.

## Pengenalan Machine Learning Menggunakan Scikit-Learn
Secara umum, permasalahan pembelajaran ialah tentang mempertimbangkan satu set sampel data n dan kemudian mencoba untuk memprediksi properti dari data yang tidak diketahui.

Machine learning adalah adalah tentang mempelajari beberap properti dari kumpulan data dan kemudian menguji properti tersebut terhadap kumpulan data lainnya.

### Memperoses Contoh Dataset
Scikit-learn terdiri dari beberapa kumpulan data standar, misalnya kumpulan data iris dan angka untuk klasifikasi dan kumpulan dataset untuk regresi.

Konvensi notasi pada prompt shell untuk memulai interpreter adalah `$` dan `>>>` menunjukan prompt juru bahasa Python.
```python
$ python
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> digits = datasets.load_digits()
```
Dataset adalah objek seperti kamus yang menyimpan semua data dan beberapa metadata. Data ini disimpan dalam format .data, yang merupakan array. Misalnya, dalam kasus kumpulan data digit, `digits.data` memberikan akses ke fitur yang dapat digunakan untuk mengklasifikasikan sampel digit:
```python
>>> print(digits.data)
[[ 0.   0.   5. ...   0.   0.   0.]
 [ 0.   0.   0. ...  10.   0.   0.]
 [ 0.   0.   0. ...  16.   9.   0.]
 ...
 [ 0.   0.   1. ...   6.   0.   0.]
 [ 0.   0.   2. ...  12.   0.   0.]
 [ 0.   0.  10. ...  12.   1.   0.]]
 ```
 Dan `digits.target` memberikan kebenaran dasar untuk kumpulan data digit, yaitu angka yang sesuai dengan setiap gambar digit.
 ```python
 >>> digits.target
array([0, 1, 2, ..., 8, 9, 8])
```
#### Bentuk Array Data
Data selalu berupa bentuk 2D, meskipun data asli mungkin memiliki bentuk yang berbeda. Dalam hal digit, setiap sampel asli adalah gambar bentuk dan dapat diakses menggunakan: `(n_samples, n_features)(8, 8)`.
```python
>>> digits.images[0]
array([[  0.,   0.,   5.,  13.,   9.,   1.,   0.,   0.],
       [  0.,   0.,  13.,  15.,  10.,  15.,   5.,   0.],
       [  0.,   3.,  15.,   2.,   0.,  11.,   8.,   0.],
       [  0.,   4.,  12.,   0.,   0.,   8.,   8.,   0.],
       [  0.,   5.,   8.,   0.,   0.,   9.,   8.,   0.],
       [  0.,   4.,  11.,   0.,   1.,  12.,   7.,   0.],
       [  0.,   2.,  14.,   5.,  10.,  12.,   0.,   0.],
       [  0.,   0.,   6.,  13.,  10.,   0.,   0.,   0.]])
```

### Mempelajari dan Memprediksi
Dalam kasus kumpulan data digit, tugas/task adalah memprediksi. Dalam scikit-learn, estimator untuk klasifikasi adalah objek Python yang mengimplementasikan metode `.fit(X, y)` dan `predict(T)`.

Contoh estimator adalah kelas `sklearn.svm.SVC`, yang mengimplementasikan klasifikasi vektor pendukung . Konstruktor estimator mengambil parameter model sebagai argumen.
```python
>>> from sklearn import svm
>>> clf = svm.SVC(gamma=0.001, C=100.)
```

### Konvensi
scikit-learn estimator mengikuti aturan tertentu untuk membuatnya lebih prediktif.
#### Tipe Casting
```python
>>> import numpy as np
>>> from sklearn import kernel_approximation

>>> rng = np.random.RandomState(0)
>>> X = rng.rand(10, 2000)
>>> X = np.array(X, dtype='float32')
>>> X.dtype
dtype('float32')

>>> transformer = kernel_approximation.RBFSampler()
>>> X_new = transformer.fit_transform(X)
>>> X_new.dtype
dtype('float64')
```
Dalam contoh di atas, `X` adalah `float32`, yang dilemparkan `float64` oleh `fit_transform(X)`.
```python
>>> from sklearn import datasets
>>> from sklearn.svm import SVC
>>> iris = datasets.load_iris()
>>> clf = SVC()
>>> clf.fit(iris.data, iris.target)
SVC()

>>> list(clf.predict(iris.data[:3]))
[0, 0, 0]

>>> clf.fit(iris.data, iris.target_names[iris.target])
SVC()

>>> list(clf.predict(iris.data[:3]))
['setosa', 'setosa', 'setosa']
```
Penjelasan untuk contoh di atas, yang pertama `predict()` mengembalikan array integer, karena `iris.target` (array integer) digunakan dalam `fit`. Yang kedua `predict()` mengembalikan array string, karena `iris.target_names` untuk pemasangan.
#### Memasang Kembali dan Memperbaharui Parameter
Hyper-parameter estimator dapat diperbarui setelah dibangun melalui metode `set_params()`.
```python
>>> import numpy as np
>>> from sklearn.datasets import load_iris
>>> from sklearn.svm import SVC
>>> X, y = load_iris(return_X_y=True)

>>> clf = SVC()
>>> clf.set_params(kernel='linear').fit(X, y)
SVC(kernel='linear')
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])

>>> clf.set_params(kernel='rbf').fit(X, y)
SVC()
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])
```
#### Pemasangan Multiclass dan Multilabel
Saat digunakan, tugas mempelajari dan memprediksi yang dilakukan bergantung pada format data target yang sesuai dengan `multiclass classifiers`.
```python
>>> from sklearn.svm import SVC
>>> from sklearn.multiclass import OneVsRestClassifier
>>> from sklearn.preprocessing import LabelBinarizer

>>> X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
>>> y = [0, 0, 1, 1, 2]

>>> classif = OneVsRestClassifier(estimator=SVC(random_state=0))
>>> classif.fit(X, y).predict(X)
array([0, 0, 1, 1, 2])
```
Dalam kasus di atas, pengklasifikasi cocok pada larik 1d dari label multiclass dan oleh `predict()`, karena itu metode ini menyediakan prediksi multikelas yang sesuai. Dimungkinkan juga untuk menyesuaikan pada array 2d indikator label biner:
```python
>>> y = LabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 0, 0],
       [1, 0, 0],
       [0, 1, 0],
       [0, 0, 0],
       [0, 0, 0]])
```
Di sini, pengklasifikasi berada `fit()` pada representasi label biner 2d dari `y`, menggunakan `LabelBinarizer`. Dalam hal ini `predict()` mengembalikan array 2d yang mewakili prediksi multilabel yang sesuai.
```python
>>> from sklearn.preprocessing import MultiLabelBinarizer
>>> y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
>>> y = MultiLabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 1, 0, 0, 0],
       [1, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 0, 1, 0, 0]])
```
Dalam hal ini, pengklasifikasi cocok pada masing-masing instance yang diberi beberapa label. Digunakan untuk binerisasi array 2d `MultiLabelBinarizer` dari multilabel ke fitatas. Akibatnya, `predict()` mengembalikan larik 2d dengan beberapa label yang diprediksi untuk setiap instance.