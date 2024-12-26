import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image



@st.cache_resource
def load_model(model_name):
    if model_name == 'ResNet50V2':
        return tf.keras.models.load_model('ResNet50V2_cv_gender_classification.h5')
    elif model_name == 'VGG16':
        return tf.keras.models.load_model('VGG16_cv_gender_classification2.h5')
    else:
        st.error("Model tidak ditemukan.")
        return None

def prepare_image(img):
    img = img.resize((224, 224))  
    img_array = np.array(img)  
    img_array = img_array / 255.0  
    return np.expand_dims(img_array, axis=0)  

st.title('Gender Classification')


model_option = st.selectbox(
    "Pilih model yang ingin digunakan:",
    ("ResNet50V2", "VGG16")
)


model = load_model(model_option)


st.markdown("""
    *Selamat datang di aplikasi Klasifikasi Gender!*  
    Di sini, Anda dapat mengupload gambar untuk mengklasifikasikan gender.
""")


uploaded_files = st.file_uploader("Pilih gambar untuk prediksi (bisa lebih dari satu)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        img = Image.open(uploaded_file)
        st.image(img, caption=f"Gambar yang diupload: {uploaded_file.name}", use_container_width=True)

        img_array = prepare_image(img)

        if model is not None:
            prediction = model.predict(img_array)

            st.write(f"Shape Prediksi: {prediction.shape}")
            st.write(f"Nilai Probabilitas: {prediction}")

            if prediction[0][0] >= 0.5:
                predicted_class = "Male"
                confidence = prediction[0][0] * 100
            else:
                predicted_class = "Female"
                confidence = (1 - prediction[0][0]) * 100

            st.write(f" Prediksi: {confidence:.2f}%")

            st.markdown(f"""
            <div style="text-align: center; font-size: 24px; font-weight: bold; color: #4CAF50;">
                <h2>Prediksi Gender: {predicted_class}</h2>
                <p>Prediksi: {confidence:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Model tidak dimuat. Silakan pilih model yang valid.")
