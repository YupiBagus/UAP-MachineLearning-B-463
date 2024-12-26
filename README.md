# Face Recognition
## Overview Project
Proyek ini adalah sistem klasifikasi untuk mengenali gender berdasarkan citra gambar wajah dengan menggunakan _ResNet50v2_dan _VGG16_

## Overview Dataset
Dataset yang digunakan berasal dari kaggle [Gender Classification](https://www.kaggle.com/datasets/gpiosenka/gender-classification-from-an-image)
dengan jumlah data train 3491 data citra

## Langkah Instalasi
### Persiapan
Python version>= 3.10  
PDM  
Streamlit  
Model H5  
VScode  
### Langkah-langkah
Masuk pada terminal lalu ketikkan :  
1. install PDM
   '(Invoke-WebRequest -Uri https://pdm-project.org/install-pdm.py -UseBasicParsing).Content | python -'  
2. inisialisasi pdm
   'pdm init'  
3. Buat virtual env
   'python -m venv myenv'
4. aktivkan Virtual env
   'myenv\scripts\ctivate'
5. Install paket yang di butuhkan
   'pdm add tensorflow'
   'pdm add numpy'
Lalu run dengan Mengetikkan perintah :
'pdm run streamlit run app.py'

# Local Web Deployment
## Tampilan HomePage
![My Screenshot (189)](UAP-MachineLearning-B-463/assets
/Screenshot (189).png)
## Tampilan HomePage Setelah Upload Image
![Alt Text](UAP-MachineLearning-B-463/assets
/Screenshot (190).png)
## Tampilan Prediction Result
![Alt Text](UAP-MachineLearning-B-463/assets
/Screenshot (191).png)

