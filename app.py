
import streamlit as st
from PIL import Image
import base64
import io

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
            color: #fff;
            text-align: center;
        }}
        .sub {{
            text-align: center;
            font-size: 18px;
            color: #e0e0e0;
        }}
        .kelompok-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: -10px;
            margin-bottom: 10px;
        }}
        .kelompok-text {{
            text-align: center;
            font-size: 18px;
            color: #ffffff;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }}
        hr {{
            border: none;
            height: 2px;
            background-color: white;
            width: 50%;
            margin: 20px auto;
        }}
    </style>
""", unsafe_allow_html=True)

# ----------------- Fungsi konversi tambahan -----------------
def ppm_to_molaritas(ppm, mr):
    try:
        return ppm / (mr * 1000)
    except:
        return None

def ppm_to_normalitas(ppm, eq_weight):
    try:
        return ppm / (eq_weight * 1000)
    except:
        return None

def ppm_to_bv(ppm, density):
    try:
        return ppm / (density * 10)
    except:
        return None

def ppm_to_wv(ppm):
    try:
        return ppm / 10000
    except:
        return None

def ppm_to_bb(ppm, density):
    try:
        return ppm / (density * 10)
    except:
        return None

def ppm_to_vv(ppm, density):
    try:
        return ppm / (density * 10)
    except:
        return None

def molaritas_to_ppm(molaritas, mr):
    try:
        return molaritas * mr * 1000
    except:
        return None

def molaritas_to_bv(molaritas, mr, density):
    try:
        return (molaritas * mr) / (density * 10)
    except:
        return None

def molaritas_to_wv(molaritas, mr):
    try:
        return molaritas * mr / 10
    except:
        return None

def molaritas_to_bb(molaritas, mr, density):
    try:
        return (molaritas * mr) / (density * 10)
    except:
        return None

def molaritas_to_vv(molaritas, mr, density):
    try:
        return (molaritas * mr) / (density * 10)
    except:
        return None

def normalitas_to_ppm(normalitas, eq_weight):
    try:
        return normalitas * eq_weight * 1000
    except:
        return None

def molaritas_to_normalitas(molaritas, valensi):
    try:
        return molaritas * valensi
    except:
        return None

def normalitas_to_molaritas(normalitas, valensi):
    try:
        return normalitas / valensi
    except:
        return None

def normalitas_to_wv(normalitas, eq_weight):
    try:
        return (normalitas * eq_weight) / 10
    except:
        return None

def normalitas_to_bv(normalitas, eq_weight, density):
    try:
        return (normalitas * eq_weight) / (density * 10)
    except:
        return None

def normalitas_to_bb(normalitas, eq_weight, density):
    try:
        return (normalitas * eq_weight) / (density * 10)
    except:
        return None

def normalitas_to_vv(normalitas, eq_weight, density):
    try:
        return (normalitas * eq_weight) / (density * 10)
    except:
        return None


# ----------------- Halaman Konversi -----------------
def halaman_konversi():
    st.markdown("## 🧪 Aplikasi Konversi Konsentrasi")

    kategori = st.selectbox("Pilih kategori konversi:", ["PPM", "Molaritas", "Normalitas"])

    if kategori == "PPM":
        ppm = st.number_input("Masukkan nilai PPM (mg/L):", step=0.1)
        jenis = st.selectbox("Konversi ke:", ["mg/L", "Molaritas", "Normalitas", "% b/v", "% w/v", "% b/b", "% v/v"])
        
        if jenis == "mg/L":
            if st.button("Konversi"):
                st.success(f"Hasil: {ppm} mg/L")
                st.latex(r"PPM = \frac{mg}{L}")
                st.latex(rf"PPM = \frac{{{ppm}}}{{1}} = {ppm} \, mg/L")

        elif jenis == "Molaritas":
            mr = st.number_input("Masukkan Mr:", step=0.01)
            if st.button("Konversi"):
                hasil = ppm_to_molaritas(ppm, mr)
                st.success(f"Hasil: {hasil:.6f} mol/L")
                st.latex(r"M = \frac{PPM}{Mr \times 1000}")
                st.latex(rf"M = \frac{{{ppm}}}{{{mr} \times 1000}} = {hasil:.6f} \, mol/L")

        elif jenis == "Normalitas":
            eq = st.number_input("Masukkan berat ekuivalen:", step=0.01)
            if st.button("Konversi"):
                hasil = ppm_to_normalitas(ppm, eq)
                st.success(f"Hasil: {hasil:.6f} N")
                st.latex(r"N = \frac{PPM}{BE \times 1000}")
                st.latex(rf"N = \frac{{{ppm}}}{{{eq} \times 1000}} = {hasil:.6f} \, N")
            
        elif jenis == "% b/v":
            dens = st.number_input("Masukkan densitas larutan (g/mL):", step=0.001)
            if st.button("Konversi"):
                hasil = ppm_to_bv(ppm, dens)
                st.success(f"Hasil: {hasil:.6f} % b/v")
                st.latex(r"\%b/v = \frac{PPM}{densitas \times 10}")
                st.latex(rf"\%b/v = \frac{{{ppm}}}{{{dens} \times 10}} = {hasil:.6f} \, \%b/v")

        elif jenis == "% w/v":
            if st.button("Konversi"):
                hasil = ppm_to_wv(ppm)
                st.success(f"Hasil: {hasil:.6f} % w/v")
                st.latex(r"\%w/v = \frac{PPM}{10000}")
                st.latex(rf"\%w/v = \frac{{{ppm}}}{{10000}} = {hasil:.6f} \, \%w/v")

        elif jenis == "% b/b":
            dens = st.number_input("Masukkan densitas larutan (g/mL):", step=0.001)
            if st.button("Konversi"):
                hasil = ppm_to_bb(ppm, dens)
                st.success(f"Hasil: {hasil:.6f} % b/b")
                st.latex(r"\%b/b = \frac{PPM}{densitas \times 10}")
                st.latex(rf"\%b/b = \frac{{{ppm}}}{{{dens} \times 10}} = {hasil:.6f} \, \%b/b")

        elif jenis == "% v/v":
            dens = st.number_input("Masukkan densitas larutan (g/mL):", step=0.001)
            if st.button("Konversi"):
                hasil = ppm_to_vv(ppm, dens)
                st.success(f"Hasil: {hasil:.6f} % v/v")
                st.latex(r"\%v/v = \frac{PPM}{densitas \times 10}")
                st.latex(rf"\%v/v = \frac{{{ppm}}}{{{dens} \times 10}} = {hasil:.6f} \, \%v/v")

    elif kategori == "Molaritas":
        mol = st.number_input("Masukkan Molaritas (mol/L):", step=0.001)
        jenis = st.selectbox("Konversi ke:", ["PPM", "Normalitas", "% b/v", "% w/v", "% b/b", "% v/v"])

        if jenis == "PPM":
            mr = st.number_input("Masukkan Mr:", step=0.01)
            if st.button("Konversi"):
                hasil = molaritas_to_ppm(mol, mr)
                st.success(f"Hasil: {hasil:.2f} ppm")
                st.latex(r"PPM = M \times Mr \times 1000")
                st.latex(rf"PPM = {mol} \times {mr} \times 1000 = {hasil:.2f} \, ppm")

        elif jenis == "Normalitas":
            val = st.number_input("Masukkan Valensi:", step=1)
            if st.button("Konversi"):
                hasil = molaritas_to_normalitas(mol, val)
                st.success(f"Hasil: {hasil:.4f} N")
                st.latex(r"N = M \times valensi")
                st.latex(rf"N = {mol} \times {val} = {hasil:.4f} \, N")

        elif jenis == "% b/v":
            mr = st.number_input("Masukkan Mr:", step=0.01)
            dens = st.number_input("Masukkan densitas larutan (g/mL):", step=0.001)
            if st.button("Konversi"):
                hasil = molaritas_to_bv(mol, mr, dens)
                st.success(f"Hasil: {hasil:.6f} % b/v")
                st.latex(r"\%b/v = \frac{M \times Mr}{densitas \times 10}")
                st.latex(rf"\%b/v = \frac{{{mol} \times {mr}}}{{{dens} \times 10}} = {hasil:.6f} \, \%b/v")

        elif jenis == "% w/v":
            mr = st.number_input("Masukkan Mr:", step=0.01)
            if st.button("Konversi"):
                hasil = molaritas_to_wv(mol, mr)
                st.success(f"Hasil: {hasil:.6f} % w/v")
                st.latex(r"\%w/v = \frac{M \times Mr}{10}")
                st.latex(rf"\%w/v = \frac{{{mol} \times {mr}}}{{10}} = {hasil:.6f} \, \%w/v")
            
        elif jenis == "% b/b":
            mr = st.number_input("Masukkan Mr:", step=0.01)
            dens = st.number_input("Masukkan densitas larutan (g/mL):", step=0.001)
            if st.button("Konversi"):
                hasil = (molaritas_to_ppm(mol, mr)) / (dens * 10)
                st.success(f"Hasil: {hasil:.6f} % b/b")

        elif jenis == "% v/v":
            mr = st.number_input("Masukkan Mr:", step=0.01)
            dens = st.number_input("Masukkan densitas larutan (g/mL):", step=0.001)
            if st.button("Konversi"):
                hasil = (molaritas_to_ppm(mol, mr)) / (dens * 10)
                st.success(f"Hasil: {hasil:.6f} % v/v")

    elif kategori == "Normalitas":
        norm = st.number_input("Masukkan Normalitas (N):", step=0.001)
        jenis = st.selectbox("Konversi ke:", ["PPM", "Molaritas", "% b/v", "% w/v", "% b/b", "% v/v"])

        if jenis == "PPM":
            eq = st.number_input("Masukkan berat ekuivalen:", step=0.01)
            if st.button("Konversi"):
                hasil = normalitas_to_ppm(norm, eq)
                st.success(f"Hasil: {hasil:.2f} ppm")
                st.latex(r"PPM = N \times BE \times 1000")
                st.latex(rf"PPM = {norm} \times {eq} \times 1000 = {hasil:.2f} \, ppm")

        elif jenis == "Molaritas":
            val = st.number_input("Masukkan Valensi:", step=1)
            if st.button("Konversi"):
                hasil = normalitas_to_molaritas(norm, val)
                st.success(f"Hasil: {hasil:.4f} M")
                st.latex(r"M = \frac{N}{valensi}")
                st.latex(rf"M = \frac{{{norm}}}{{{val}}} = {hasil:.4f} \, M")

        elif jenis == "% w/v":
            eq = st.number_input("Masukkan berat ekuivalen:", step=0.01)
            if st.button("Konversi"):
                hasil = normalitas_to_wv(norm, eq)
                st.success(f"Hasil: {hasil:.6f} % w/v")
                st.latex(r"\%w/v = \frac{N \times BE}{10}")
                st.latex(rf"\%w/v = \frac{{{norm} \times {eq}}}{{10}} = {hasil:.6f} \, \%w/v")

        elif jenis == "% b/v":
            eq = st.number_input("Masukkan berat ekuivalen:", step=0.01)
            dens = st.number_input("Masukkan densitas larutan (g/mL):", step=0.001)
            if st.button("Konversi"):
                hasil = normalitas_to_bv(norm, eq, dens)
                st.success(f"Hasil: {hasil:.6f} % b/v")
                st.latex(r"\%b/v = \frac{N \times BE}{densitas \times 10}")
                st.latex(rf"\%b/v = \frac{{{norm} \times {eq}}}{{{dens} \times 10}} = {hasil:.6f} \, \%b/v")
            
        elif jenis == "% b/b":
            eq = st.number_input("Masukkan berat ekuivalen:", step=0.01)
            dens = st.number_input("Masukkan densitas larutan (g/mL):", step=0.001)
            if st.button("Konversi"):
                hasil = (normalitas_to_ppm(norm, eq)) / (dens * 10)
                st.success(f"Hasil: {hasil:.6f} % b/b")

        elif jenis == "% v/v":
            eq = st.number_input("Masukkan berat ekuivalen:", step=0.01)
            dens = st.number_input("Masukkan densitas larutan (g/mL):", step=0.001)
            if st.button("Konversi"):
                hasil = (normalitas_to_ppm(norm, eq)) / (dens * 10)
                st.success(f"Hasil: {hasil:.6f} % v/v")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅ Kembali ke Menu", on_click=lambda: st.session_state.update({"halaman": "menu"}))
    with col2:
        st.button("🏠 Halaman Utama", on_click=lambda: st.session_state.update({"halaman": "utama"}))

# ----------------- Halaman lainnya -----------------
# ... (tetap sesuai dengan isi sebelumnya tanpa perubahan)


# ----------------- Halaman lainnya -----------------
def halaman_utama():
    st.markdown("<h1 class='title'>⚗ Selamat Datang di My Concentration ⚗</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p class='sub'>
            🔍 Bingung konversi PPM ke Molaritas atau Normalitas? <br>
            🚀 Yuk, gunakan <strong>My Concentration</strong> – aplikasi kimia interaktif yang membantu kamu menghitung dan memahami berbagai satuan konsentrasi dengan cepat dan akurat! <br><br>
            🎯 Cocok untuk pelajar, mahasiswa, guru, atau siapapun yang ingin belajar atau bekerja di dunia kimia. <br>
            💡 Ayo eksplor dan konversi satuan kimia hanya dalam beberapa klik! 
        </p>
        <hr class='divider'>
        <div class='kelompok-container'>
            <p class='kelompok-text'>🤖 Dibuat oleh <b>Kelompok 11</b> 💙</p>
            <p class='kelompok-text'>Arsal 🎩, Danish ✨, Hanna 🌸, Raffi 🎮, Yasifa 🎀</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Selanjutnya ➡"):
        st.session_state["halaman"] = "menu"



def halaman_menu():
    st.markdown("<h2 class='title'>📂 Menu Utama</h2>", unsafe_allow_html=True)
    menu = st.radio("Silahkan pilih menu:", ["Penjelasan Konsentrasi", "Penggunaan Aplikasi", "Aplikasi Konversi", "Tabel Periodik"])

    if menu == "Penjelasan Konsentrasi":
        halaman_penjelasan()
    elif menu == "Penggunaan Aplikasi":
        halaman_penggunaan()
    elif menu == "Aplikasi Konversi":
        halaman_konversi()
    elif menu == "Tabel Periodik":
        halaman_periodik()

def halaman_penjelasan():
    st.markdown("## 🧪 Penjelasan Konsentrasi Kimia")
    st.info("""
    Dalam ilmu kimia, **konsentrasi** menunjukkan seberapa banyak zat terlarut terdapat dalam sejumlah pelarut atau larutan. Berikut adalah tiga satuan konsentrasi utama yang sering digunakan:

    🔹 **PPM (Parts Per Million)**
    - Mengukur jumlah zat dalam satu juta bagian larutan.
    - Umumnya digunakan saat konsentrasi sangat kecil, seperti dalam air minum, limbah, atau uji lingkungan.
    - 1 PPM setara dengan 1 mg zat dalam 1 liter larutan.

    🔹 **Molaritas (M)**
    - Mengukur jumlah mol zat terlarut dalam setiap 1 liter larutan.
    - Digunakan dalam banyak perhitungan kimia seperti stoikiometri reaksi, titrasi, atau persiapan larutan.
    - Contoh: 1 M = 1 mol zat per liter larutan.

    🔹 **Normalitas (N)**
    - Mirip dengan molaritas, tetapi mempertimbangkan jumlah ekuivalen (berdasarkan reaksi kimia tertentu).
    - Cocok untuk reaksi asam-basa atau redoks.
    - Contoh: 1 N HCl berarti 1 mol ion H⁺ per liter larutan.

    ⚗️ Dengan memahami perbedaan dan kegunaannya, kamu bisa memilih satuan yang paling tepat sesuai dengan kebutuhan percobaan atau perhitungan kimia yang dilakukan.
    """)
    st.button("⬅ Kembali ke Menu", on_click=lambda: st.session_state.update({"halaman": "menu"}))
    st.button("🏠 Halaman Utama", on_click=lambda: st.session_state.update({"halaman": "utama"}))

def halaman_penggunaan():
    st.markdown("## 📘 Cara Menggunakan Aplikasi My Concentration")
    st.info("""
    🎯 **My Concentration** adalah alat bantu pintar untuk menghitung dan mengonversi berbagai satuan konsentrasi larutan kimia — seperti **PPM**, **Molaritas**, dan **Normalitas** — dengan cepat, akurat, dan mudah dipahami.

    🧠 Baik untuk pelajar, pendidik, maupun profesional laboratorium, aplikasi ini menyederhanakan proses perhitungan dengan antarmuka yang ramah pengguna dan visualisasi rumus yang jelas.

    📌 **Cara Menggunakan:**
    1. Pilih kategori konversi yang ingin digunakan (PPM, Molaritas, Normalitas)
    2. Masukkan nilai dan parameter yang diminta, seperti Mr, berat ekuivalen, valensi, atau densitas
    3. Pilih bentuk satuan tujuan yang ingin dikonversi
    4. Klik tombol KONVERSI untuk menampilkan hasil dan penjelasan matematisnya

    ✅ Cocok untuk:
    - 🧑‍🎓 Pelajar dan Mahasiswa Kimia, Farmasi, Biologi
    - 👩‍🏫 Guru dan Dosen untuk visualisasi materi ajar
    - 🧪 Laboratorium atau praktisi kimia yang butuh perhitungan cepat dan akurat
    """)
    st.button("⬅ Kembali ke Menu", on_click=lambda: st.session_state.update({"halaman": "menu"}))
    st.button("🏠 Halaman Utama", on_click=lambda: st.session_state.update({"halaman": "utama"}))

def halaman_periodik():
    st.markdown("## 🧬 Tabel Periodik Unsur Kimia")
    st.image("https://gurubelajarku.com/wp-content/uploads/2019/12/Tabel-Periodik-Unsur-Kimia.jpg", caption="Sumber: gurubelajarku.com")
    st.button("⬅ Kembali ke Menu", on_click=lambda: st.session_state.update({"halaman": "menu"}))
    st.button("🏠 Halaman Utama", on_click=lambda: st.session_state.update({"halaman": "utama"}))

# ----------------- Routing -----------------
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "utama"

if st.session_state["halaman"] == "utama":
    halaman_utama()
elif st.session_state["halaman"] == "menu":
    halaman_menu()
