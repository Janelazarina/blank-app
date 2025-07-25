import streamlit as st
import pandas as pd

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="MindTrack", page_icon="🧠")

# Menu Sidebar
menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda", "Latihan Soal", "Catatan Kuliah", "Riwayat Jawaban", "Tentang"])

# Halaman Beranda
if menu == "Beranda":
    st.title("🧠 MindTrack")
    st.write("Selamat datang di **MindTrack**, platform latihan soal dan catatan kuliah 👋")
    st.info("Gunakan menu di sebelah kiri untuk mulai belajar.")

# Halaman Latihan Soal
elif menu == "Latihan Soal":
    st.title("✏️ Latihan Soal")
    st.write("Halaman ini nanti akan menampilkan soal-soal dari berbagai mata kuliah.")

elif menu == "Catatan Kuliah":
    st.title("📒 Catatan Kuliah")
    # Judul Aplikasi
st.title("Materi Praktik Kimia Organik ")

# Subjudul
st.header("Pembuatan")

# Teks materi
st.write("""
# file: app.py

import streamlit as st

# Judul Aplikasi
st.title("Materi Praktik Kimia Organik ")

# Subjudul
st.header("Rangkuman")

# Teks materi
st.write("""
1. Metana : 1 sendok sodalime dan 1 sendok (COONa3)
prinsip : pemanasan COONa3 akan menghasilkan metana yang akan bereaksi dengan larutan iodhubl membentuk tetra iodin metana,yang ditandai dengan memudarnya larutan iodhubl.
hasil uji : dari jingga ke memudar


(CH4 + I2 = CI4 + 4HI)
""")
pengamatan : positif hanya dengan larutan iodhubl
menggunakan reaksi substitusi

2. Heksana 
prinsip : heksana dapat bereaksi dengan larutan iodhubl yang membentuk 1 iodheksana yang ditandai dengan memudarnya larutan iodhubl 
hasil uji : dari jingga ke memudar
Reaksi :


# Penjelasan tambahan
st.subheader("Faktor yang Mempengaruhi Fotosintesis")
st.markdown("""
1. **Intensitas cahaya**
2. **Konsentrasi karbon dioksida**
3. **Suhu**
4. **Ketersediaan air**
""")

# Tambahan interaktif
if st.checkbox("Tampilkan kesimpulan"):
    st.success("Fotosintesis sangat penting karena menghasilkan oksigen dan menyediakan energi bagi makhluk hidup.")



    if "show_notes" not in st.session_state:
        st.session_state.show_notes = False

    tingkat = st.radio("Pilih Tingkat", ["Tingkat 1", "Tingkat 2"], horizontal=True)
    blok = st.selectbox("Pilih Blok", ["Blok 1", "Blok 2"])
    matkul = st.selectbox("Pilih Mata Kuliah", ["Kimia Fisika", "Spektrofotometri", "Biokimia"])

    if st.button("✅ simpan"):
        st.session_state.show_notes = True
        st.session_state.selected_tingkat = tingkat
        st.session_state.selected_blok = blok
        st.session_state.selected_matkul = matkul

    if st.session_state.show_notes:
        st.subheader(f"📘 Catatan untuk {st.session_state.selected_matkul} - {st.session_state.selected_tingkat} {st.session_state.selected_blok}")
        st.info("Belum ada catatan yang ditambahkan.")

# Halaman Riwayat Jawaban
elif menu == "Riwayat Jawaban":
    st.title("🗂️ Riwayat Jawaban")
    st.write("Di sini akan ditampilkan jawaban-jawaban soal yang pernah kamu kerjakan.")

# Halaman Tentang
elif menu == "Tentang":
    st.title("ℹ️ Tentang MindTrack")
    st.write("Website ini dibuat untuk latihan soal dan mencatat materi perkuliahan.")
    st.header("Tentang Pendiri")
    st.write("Zulfikar Syahid")
    st.write("Rizmi Maitri Nurgianti")
    st.write("Nafisah Nailalhusna I.")
    st.write("Jane Lazarina Bora Isu")
