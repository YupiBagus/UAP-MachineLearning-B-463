# Face Recognition
## Overview Project
Proyek ini adalah sistem klasifikasi untuk mengenali gender berdasarkan citra gambar wajah dengan menggunakan _ResNet50v2_ dan _VGG16_
## Model ResNet50v2
![Screenshot 2024-12-26 114139](https://github.com/user-attachments/assets/fc0e9c6e-8ae1-4420-b7a4-3df1e2bc95d0)  
bisa diketahui dari classification report dimana acuracy yang didapat dari model resnet sebesar 99
## Model VGG16
![Screenshot 2024-12-26 114052](https://github.com/user-attachments/assets/01129c26-7d99-47da-ac51-3ad836d2d7ff)
bisa diketahui dari classification report dimana acuracy yang didapat dari model resnet sebesar 99
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
   '(Invoke-WebRequest -Uri https://pdm-project.or![Screenshot 2024-12-26 114139](https://github.com/user-attachments/assets/c5f0b535-f379-4380-8242-9207006ded8b)
g/install-pdm.py -UseBasicParsing).Content | python -'  
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
![Screenshot (189)](https://github.com/user-attachments/assets/d03bf9fb-16d3-4e6f-aa38-c38b6ef711f8)
## Tampilan HomePage Setelah Upload Image
![Screenshot (190)](https://github.com/user-attachments/assets/ad0fdc2f-d00d-477e-ae7c-a3ace087a276)
## Tampilan Prediction Result
![Screenshot (191)](https://github.com/user-attachments/assets/08bf3d07-14d5-4d9e-b9d5-9fb4c0a02949)






