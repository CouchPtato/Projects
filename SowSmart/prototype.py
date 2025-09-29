import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from gtts import gTTS
import base64
from streamlit_extras.metric_cards import style_metric_cards

# -------------------------
# COLOR PALLETE
# -------------------------
colorPallete = ["#F0F0F0", "#E6D8C3", "#C2A68C", "#5D866C"]

# -------------------------
# SAMPLE CROPS DATA
# -------------------------
def recommend_crops(soil, ph, rainfall, temp, prev_crop):
    return random.sample(crops, 3)  # random for demo

def fetch_soil_types():
    return ["Alluvial", "Black", "Red", "Sandy", "Laterite"]

def text_to_speech(text, lang="hi"):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    with open(filename, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f'<audio autoplay controls><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'

def fetch_sustainability():
    return random.randint(1, 10)

crops = [
    {"name": "Wheat", "yield": 3.2, "cp": 34, "sp": 52, "risk": 0.25, "sustainability": fetch_sustainability(), "rotation": ["Pulses", "Mustard"]},
    {"name": "Rice", "yield": 2.8, "cp": 43, "sp": 55, "risk": 0.40, "sustainability": fetch_sustainability(), "rotation": ["Pulses", "Vegetables"]},
    {"name": "Mustard", "yield": 2.5, "cp": 37, "sp": 42, "risk": 0.20, "sustainability": fetch_sustainability(), "rotation": ["Wheat", "Vegetables"]},
    {"name": "Barley", "yield": 2.0, "cp": 29, "sp": 34, "risk": 0.30, "sustainability": fetch_sustainability(), "rotation": ["Maize", "Mustard"]},
    {"name": "Maize", "yield": 3.0, "cp": 42, "sp": 57, "risk": 0.22, "sustainability": fetch_sustainability(), "rotation": ["Potato", "Pulses"]},
]

# -------------------------
# STREAMLIT PAGE CONFIG
# -------------------------
st.set_page_config(page_title="SowSmart", page_icon="🌱", layout="wide")
st.markdown(
    f"""
    <style>
        /* Background */
        .main, .block-container {{
            background-color: {colorPallete[0]} !important;
        }}

        /* Headers */
        h1, h2, h3, h4, h5, h6 {{
            color: {colorPallete[3]} !important;
        }}

        /* Streamlit primary buttons */
        button[kind="primary"] {{
            background-color: {colorPallete[2]} !important;
            color: {colorPallete[0]} !important;
            border: 1px solid {colorPallete[1]} !important;
        }}

        /* Streamlit secondary buttons */
        button[kind="secondary"] {{
            background-color: {colorPallete[1]} !important;
            color: {colorPallete[3]} !important;
            border: 1px solid {colorPallete[2]} !important;
        }}

        /* Hover effect */
        button:hover {{
            opacity: 0.85 !important;
        }}
        .stSelectbox label, .stNumberInput label {{
            color: {colorPallete[3]} !important;  /* your dark green */
            font-weight: 600 !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# HOME TAB
# -------------------------
def Home():
    st.subheader("📈 Top 3 Crops Trending in Market / शीर्ष 3 फसलें")
    trending = sorted(crops, key=lambda x: (x["sp"] + x["sustainability"]), reverse=True)[:3]
    
    for crop in trending:
        card_html = f"""
            <div style="
                background-color:{colorPallete[1]};
                border-radius: 12px;
                padding: 15px;
                margin-bottom: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
            <h3 style="margin:0; color:{colorPallete[3]}; font-size:22px;">🌱 {crop['name']}</h3>
            <p style="margin:6px 0; font-size:16px; color:#333;">
                💰 Selling Price: <b>₹{crop['sp']}/kg</b><br>
                🌿 Sustainability: <b>{crop['sustainability']}/10</b>
            </p>
            </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📊 Factor Analysis / कारक विश्लेषण")
    factor = st.selectbox("Select Factor / कारक चुनें",
                          ["Temperature", "Rainfall", "Cloud Percentage", "Crop Price Prediction"])
    
    fig, ax = plt.subplots(figsize=(10, 3), dpi=100)
    if factor == "Temperature":
        values = [random.randint(0, 40) for _ in range(119)]
        ylabel = "Temperature (°C)"
        ax.set_title("Temperature Trends (°C)", color=colorPallete[3])
        c = colorPallete[2]
    elif factor == "Rainfall":
        values = [random.randint(50, 200) for _ in range(119)]
        ylabel = "Rainfall (mm)"
        ax.set_title("Rainfall Trends (mm)", color=colorPallete[3])
        c = colorPallete[3]
    elif factor == "Cloud Percentage":
        values = [random.randint(10, 90) for _ in range(119)]
        ylabel = "Cloud %"
        ax.set_title("Cloud Coverage (%)", color=colorPallete[3])
        c = colorPallete[1]
    else:
        current_crop = st.selectbox("Select Crop / फसल चुनें", [crop["name"] for crop in crops])
        values = [random.randint(30, 60) for _ in range(119)]
        ylabel = "Predicted Price (₹)"
        ax.set_title("Crop Price Prediction (₹)", color=colorPallete[3])
        c = colorPallete[2]
    
    ax.plot(range(len(values)), values, color=c, linewidth=2)
    ax.set_xlabel("Weeks", color=colorPallete[3])
    ax.set_ylabel(ylabel, color=colorPallete[3])
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig, use_container_width=True)

# -------------------------
# RECOMMEND TAB
# -------------------------
def Recommend():
    st.subheader("🌱 AI Crop Recommendation / फसल अनुशंसा")
    col1, col2 = st.columns(2)
    with col1:
        soil = st.selectbox("Soil Type / मिट्टी का प्रकार", fetch_soil_types())
        ph = st.number_input("Soil pH / मिट्टी का pH", min_value=3.5, max_value=9.0, value=6.5, step=0.1)
        rainfall = st.number_input("Rainfall (mm) / वर्षा (mm)", 0, 500, 120)
    with col2:
        temp = st.number_input("Temperature (°C) / तापमान (°C)", 5, 45, 25)
        prev_crop = st.selectbox("Previous Crop / पिछली फसल", 
                                 ["None", "Wheat", "Rice", "Maize", "Mustard", "Barley"])
    run = st.button("🚀 Recommend Crops / फसल सुझाएँ")

    if run:
        results = recommend_crops(soil, ph, rainfall, temp, prev_crop)
        df = pd.DataFrame(results)

        sub_tabs = st.tabs([
            "🌾 Recommendations / अनुशंसाएँ",
            "📊 Smart Economics / स्मार्ट अर्थशास्त्र",
            "🌍 Crop Rotation / फसल चक्र",
            "🔊 Voice Assistant / वॉयस असिस्टेंट"
        ])

        # ========== Recommendations ==========
        with sub_tabs[0]:
            st.subheader("🌾 Recommended Crops for You / आपके लिए अनुशंसित फसलें")
            for crop in results:
                crop_card = f"""
                <div style="
                    background: linear-gradient(135deg, {colorPallete[0]}, {colorPallete[1]});
                    border-radius: 12px;
                    padding: 16px;
                    margin-bottom: 16px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                ">
                    <h3 style="margin:0; color:{colorPallete[3]};">🌱 {crop['name']}</h3>
                    <p style="margin:6px 0; font-size:14px; color:#333;">
                        📦 Yield: <b>{crop['yield']} t/ha</b><br>
                        💰 Selling Price: <b>₹{crop['sp']} /kg</b><br>
                        🌿 Sustainability: <b>{crop['sustainability']}/10</b>
                    </p>
                </div>
                """
                st.markdown(crop_card, unsafe_allow_html=True)

        # ========== Smart Economics ==========
        with sub_tabs[1]:
            st.subheader("📊 Smart Economics Insights / स्मार्ट अर्थशास्त्र अंतर्दृष्टि")
            for crop in results:
                if crop["risk"] < 0.25:
                    risk_level = "🟢 Low / कम"
                elif crop["risk"] < 0.4:
                    risk_level = "🟡 Medium / मध्यम"
                else:
                    risk_level = "🔴 High / उच्च"

                score = round(crop["sp"] / (crop["risk"]*100), 2)

                with st.container():
                    col1, col2, col3 = st.columns(3)
                    col1.metric("💰 Profit %", round(((crop["sp"] - crop["cp"]) * 100 / crop["cp"]), 3))
                    col2.metric("⚠️ Risk", risk_level)
                    col3.metric("📈 Smart Score", score)

            style_metric_cards(
                background_color=colorPallete[1],
                border_color=colorPallete[2],
                border_left_color=colorPallete[3]
            )

        # ========== Crop Rotation ==========
        with sub_tabs[2]:
            st.subheader("🌍 Smart Crop Rotation Planner / स्मार्ट फसल चक्र योजनाकार")
            for crop in results:
                rotation_list = ", ".join(crop["rotation"])
                html_card = f"""
                <div style="padding:16px;border-radius:12px;border:1px solid {colorPallete[2]};
                            margin-bottom:12px;background-color:{colorPallete[1]};
                            box-shadow:0 2px 6px rgba(0,0,0,0.05);">
                    <h4 style="margin:0;color:{colorPallete[3]};">🌱 {crop['name']}</h4>
                    <p style="margin:6px 0;color:#333">🔄 After harvesting <b>{crop['name']}</b>, rotate with → <b>{rotation_list}</b></p>
                    <p style="margin:6px 0;font-size:13px;color:#555;">✅ This improves soil fertility and reduces pest risk.</p>
                </div>"""
                st.markdown(html_card, unsafe_allow_html=True)

        # ========== Voice Assistant ==========
        with sub_tabs[3]:
            st.subheader("🔊 Voice Assistant")
            response_text = f"आपके खेत के लिए सबसे अच्छे फसल हैं {results[0]['name']}, {results[1]['name']} और {results[2]['name']}."
            st.markdown(text_to_speech(response_text, lang="hi"), unsafe_allow_html=True)

# -------------------------
# MAIN NAVIGATION
# -------------------------
pg = st.navigation([Home, Recommend], position='top')
pg.run()
