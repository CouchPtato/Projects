import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from gtts import gTTS
import base64


crops = [
    {"name": "Wheat", "yield": 3.2, "profit": 45000, "sustainability": 8, "risk": 0.25, "rotation": ["Pulses", "Mustard"]},
    {"name": "Rice", "yield": 2.8, "profit": 38000, "sustainability": 6, "risk": 0.40, "rotation": ["Pulses", "Vegetables"]},
    {"name": "Mustard", "yield": 2.5, "profit": 50000, "sustainability": 9, "risk": 0.20, "rotation": ["Wheat", "Vegetables"]},
    {"name": "Barley", "yield": 2.0, "profit": 30000, "sustainability": 7, "risk": 0.30, "rotation": ["Maize", "Mustard"]},
    {"name": "Maize", "yield": 3.0, "profit": 42000, "sustainability": 8, "risk": 0.22, "rotation": ["Potato", "Pulses"]},
]

def recommend_crops(soil, ph, rainfall, temp, prev_crop):
    return random.sample(crops, 3)  # random for demo

def text_to_speech(text, lang="hi"):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    with open(filename, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f'<audio autoplay controls><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'

#UI

st.set_page_config(page_title="AI Crop Advisor", page_icon="🌱", layout="wide")

st.title("🌱 AI-Powered Crop Recommendation System")
st.markdown("### 🤖 Personalized, science-guided advice for Indian farmers")

# Input Sidebar
st.sidebar.header("🌍 Farm Details")
soil = st.sidebar.selectbox("Soil Type", ["Alluvial", "Black", "Red", "Sandy", "Laterite"])
ph = st.sidebar.slider("Soil pH", 3.5, 9.0, 6.5)
rainfall = st.sidebar.number_input("Rainfall (mm)", 0, 500, 120)
temp = st.sidebar.number_input("Temperature (°C)", 5, 45, 25)
prev_crop = st.sidebar.selectbox("Previous Crop", ["None", "Wheat", "Rice", "Maize", "Mustard", "Barley"])

if st.sidebar.button("🚀 Recommend Crops"):
    results = recommend_crops(soil, ph, rainfall, temp, prev_crop)
    df = pd.DataFrame(results)

    # Tabs
    tabs = st.tabs(["🌾 Recommendations", "📊 Smart Economics", "🌍 Crop Rotation", "🔊 Voice Assistant"])


    with tabs[0]:
        st.subheader("🌾 Recommended Crops for You")
        for crop in results:
            col1, col2, col3, col4 = st.columns(4)
            with col1: st.metric("Crop", crop["name"])
            with col2: st.metric("Yield (t/ha)", crop["yield"])
            with col3: st.metric("Profit (₹)", f"{crop['profit']}")
            with col4: st.metric("Sustainability", f"{crop['sustainability']}/10")

        # Profit Chart
        st.markdown("### 💰 Profit Comparison")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(df["name"], df["profit"], color=["#2e8b57", "#3cb371", "#66cdaa"])
        ax.set_ylabel("Profit (₹/hectare)")
        ax.set_title("Crop Profitability")
        st.pyplot(fig)


    with tabs[1]:
        st.subheader("📊 Smart Economics Insights")
        for crop in results:
            risk_level = "🟢 Low" if crop["risk"] < 0.25 else "🟡 Medium" if crop["risk"] < 0.4 else " 🔴 High"
            score = round(crop["profit"] / (crop["risk"]*100000), 2)
            st.write(f"**{crop['name']}** → Profit: ₹{crop['profit']} | Risk: {risk_level} | Smart Score: {score}")


    with tabs[2]:
        st.subheader("🌍 Smart Crop Rotation Planner")
        for crop in results:
            st.info(f"After **{crop['name']}**,  grow  →  {' ,  '.join(crop['rotation'])}")


    with tabs[3]:
        st.subheader("🔊 Voice Assistant")
        response_text = f"आपके खेत के लिए सबसे अच्छे फसल हैं {results[0]['name']}, {results[1]['name']} और {results[2]['name']}."
        st.markdown(text_to_speech(response_text, lang="hi"), unsafe_allow_html=True)
