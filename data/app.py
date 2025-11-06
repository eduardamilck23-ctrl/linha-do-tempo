import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime
import base64

st.set_page_config(page_title="Linha do Tempo", page_icon="📸", layout="centered")

# === Estilo CSS ===
st.markdown("""
    <style>
    body {
        background-color: #fafafa;
        color: #333;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .polaroid {
        background-color: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        display: inline-block;
        margin: 15px;
        padding: 10px 10px 25px 10px;
        text-align: center;
        border-radius: 6px;
        transition: transform 0.2s ease;
    }
    .polaroid:hover {
        transform: scale(1.02);
    }
    .caption {
        font-size: 14px;
        color: #555;
        margin-top: 5px;
    }
    .date {
        font-size: 12px;
        color: #999;
    }
    .recado {
        background-color: #fffef9;
        border: 1px solid #f3eacb;
        padding: 30px;
        border-radius: 10px;
        width: 80%;
        margin: 40px auto;
        font-family: 'Courier New', monospace;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# === Cabeçalho ===
st.title("📸 Linha do Tempo")
st.write("Um passeio por momentos marcantes, acompanhados de música e lembranças.")

# === Música ===
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

try:
    autoplay_audio("assets/music.mp3")
except:
    st.warning("🔈 Adicione o arquivo 'music.mp3' na pasta assets para ativar a trilha sonora.")

# === Fotos ===
df = pd.read_csv("data/photos.csv")
df['date'] = pd.to_datetime(df['date'], format="%d/%m/%Y")
df = df.sort_values(by="date")

for _, row in df.iterrows():
    st.markdown(f"""
        <div class="polaroid">
            <img src="assets/images/{row['filename']}" width="250">
            <div class="caption">{row['caption']}</div>
            <div class="date">{row['date'].strftime('%d/%m/%Y')}</div>
        </div>
        """, unsafe_allow_html=True)

# === Recado ===
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("💌 Recado Final")
recado_text = st.text_area("Escreva seu recado aqui:", "Algumas memórias não precisam de legenda...")
st.markdown(f"<div class='recado'>{recado_text}</div>", unsafe_allow_html=True)
