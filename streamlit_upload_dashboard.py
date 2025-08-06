import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📤 Upload je meetgegevens")

uploaded_file = st.file_uploader("Kies een CSV-bestand", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Bestand succesvol ingelezen")

        grens = st.sidebar.slider("Grens EC", 100, 1500, 800)

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(df["tijd"], df["temperatuur"], label="Temperatuur (°C)")
        ax.plot(df["tijd"], df["geleidbaarheid"], label="Geleidbaarheid (µS/cm)")
        ax.axhline(y=grens, color="red", linestyle="--", label=f"Grens EC = {grens}")
        ax.set_xlabel("Tijd")
        ax.set_ylabel("Waarde")
        ax.set_title("Geüploade sensordata")
        ax.legend()
        ax.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        st.pyplot(fig)

        if df["geleidbaarheid"].max() > grens:
            st.error("⚠️ Geleidbaarheid overschreden!")
        else:
            st.success("✅ Alles onder controle.")
    except Exception as e:
        st.error(f"Fout bij inlezen bestand: {e}")
else:
    st.info("⬆️ Upload een CSV-bestand om te starten.")
foutief bestand verwijderd
