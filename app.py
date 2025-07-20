import streamlit as st
from PIL import Image
import base64
import io

# ----------------- Styling CSS + Background -----------------
image_path = "Web nackground.png"
with open(image_path, "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .title {{
            color: #ffffff;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            text-shadow: 2px 2px 4px #000000;
        }}
        .sub {{
            text-align: center;
            font-size: 18px;
            color: #f0f0f0;
            text-shadow: 1px 1px 2px #000000;
        }}
        .kelompok-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: 20px;
        }}
        .kelompok-text {{
            text-align: center;
            font-size: 18px;
            color: #ffffff;
            font-family: 'Comic Sans MS', cursive;
            text-shadow: 1px 1px 2px #000000;
        }}
        .divider {{
            border-top: 2px solid white;
            width: 100%;
            margin-top: 30px;
            margin-bottom: 20px;
        }}
        .info, .warning {{
            text-shadow: 1px 1px 2px #000000;
        }}
        .element-container .stMarkdown p,
        .element-container .stMarkdown h1,
        .element-container .stMarkdown h2,
        .element-container .stMarkdown h3,
        .element-container .stMarkdown h4,
        .element-container .stMarkdown h5,
        .element-container .stMarkdown h6,
        .element-container .stMarkdown li {{
            text-shadow: 1px 1px 2px #000000 !important;
        }}
        .stRadio > div {{
            text-shadow: 1px 1px 2px #000000;
        }}
    </style>
""", unsafe_allow_html=True)

# Tambahan fungsi konversi

def bv_to_ppm(bv, density):
    return bv * density * 10

def vv_to_ppm(vv, density):
    return vv * density * 10

def bb_to_ppm(bb, density):
    return bb * density * 10

# Halaman konversi dari % ke PPM

def halaman_konversi_bb_bv_vv():
    st.markdown("## 🔄 Konversi dari % ke PPM")

    kategori = st.selectbox("Pilih jenis %:", ["% b/v", "% b/b", "% v/v"])

    persen = st.number_input("Masukkan nilai persen:", step=0.01)
    dens = st.number_input("Masukkan densitas larutan (g/mL):", step=0.001)

    if st.button("Konversi ke PPM"):
        if kategori == "% b/v":
            hasil = bv_to_ppm(persen, dens)
            st.success(f"Hasil: {hasil:.2f} ppm")
            st.latex(r"PPM = \%b/v \times densitas \times 10")
        elif kategori == "% b/b":
            hasil = bb_to_ppm(persen, dens)
            st.success(f"Hasil: {hasil:.2f} ppm")
            st.latex(r"PPM = \%b/b \times densitas \times 10")
        elif kategori == "% v/v":
            hasil = vv_to_ppm(persen, dens)
            st.success(f"Hasil: {hasil:.2f} ppm")
            st.latex(r"PPM = \%v/v \times densitas \times 10")

# Menu utama yang ditambahkan

def halaman_menu():
    st.markdown("<h2 class='title'>📂 Menu Utama</h2>", unsafe_allow_html=True)
    menu = st.radio("Silahkan pilih menu:", ["Konversi % ke PPM"])

    if menu == "Konversi % ke PPM":
        halaman_konversi_bb_bv_vv()

if _name_ == '_main_':
    halaman_menu()
