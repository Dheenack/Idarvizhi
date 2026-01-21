# =========================================================
# IDARVIZHI - DISASTER INTELLIGENCE SYSTEM (FINAL - ORDERED)
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import json
import random
from fpdf import FPDF
from gtts import gTTS
import tempfile
import os
from disaster_ai import DisasterAI, DisasterContext
from multilingual import translations as T_dict
from utils.theme import set_theme
# ---------------------------------------------------------
# LOAD CSV FILES (DO NOT REMOVE)
# ---------------------------------------------------------
df = pd.read_csv("disaster_data.csv")
df_hist = pd.read_csv("historical_disaster.csv")
district_df = pd.read_csv("district_data.csv")


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="IdarVizhi - Disaster Intelligence System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# if "theme" not in st.session_state:
#     st.session_state.theme = "light"

# with st.sidebar:
#     theme_toggle = st.toggle(
#         "🌗 Dark mode",
#         value=st.session_state.theme == "dark"
#     )

# st.session_state.theme = "dark" if theme_toggle else "light"
# set_theme(st.session_state.theme)

if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Toggle
dark = st.sidebar.toggle("🌗 Dark mode")

new_theme = "dark" if dark else "light"

# reload only if changed
if st.session_state.theme != new_theme:
    st.session_state.theme = new_theme
    st.query_params["theme"] = new_theme
    st.rerun()


# ---------------------------------------------------------
# 🌪️🔥 DISASTER HEADER + DYNAMIC LOTTIE (FIRST)
# ---------------------------------------------------------

st.markdown("""
<h1 style='text-align:center; color:#ff5252;'>🌪️🔥 IDARVIZHI 🌊🛡️</h1>
<h4 style='text-align:center; color:#ffa726;'>
Disaster Intelligence • Risk Prediction • Life Saving Dashboard
</h4>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# LANGUAGE CODES
# ---------------------------------------------------------
LANG_CODE = {
    "English": "en", "Tamil": "ta", "Hindi": "hi", "Telugu": "te",
    "Kannada": "kn", "Malayalam": "ml", "Marathi": "mr",
    "Bengali": "bn", "Gujarati": "gu", "Punjabi": "pa",
    "Odia": "or", "Assamese": "as"
}

# ---------------------------------------------------------
# VOICE MESSAGE
# ---------------------------------------------------------
def generate_voice_message(lang, disaster, district, state, risk):
    msgs = {
        "English": f"Warning! {disaster} risk is {risk} in {district}, {state}.",
        "Tamil": f"எச்சரிக்கை! {district} மாவட்டத்தில் {disaster} அபாயம் {risk}.",
        "Hindi": f"चेतावनी! {district}, {state} में {disaster} का खतरा {risk} है।",
        "Telugu": f"హెచ్చరిక! {district}, {state} లో {disaster} ప్రమాదం {risk}.",
        "Kannada": f"ಎಚ್ಚರಿಕೆ! {district}, {state} ನಲ್ಲಿ {disaster} ಅಪಾಯ {risk}.",
        "Malayalam": f"മുന്നറിയിപ്പ്! {district}, {state} ൽ {disaster} അപകടം {risk}.",
        "Marathi": f"इशारा! {district}, {state} मध्ये {disaster} धोका {risk}.",
        "Bengali": f"সতর্কতা! {district}, {state} এ {disaster} ঝুঁকি {risk}.",
        "Gujarati": f"ચેતવણી! {district}, {state} માં {disaster} જોખમ {risk}.",
        "Punjabi": f"ਚੇਤਾਵਨੀ! {district}, {state} ਵਿੱਚ {disaster} ਦਾ ਖਤਰਾ {risk}.",
        "Odia": f"ଚେତାବନୀ! {district}, {state} ରେ {disaster} ଝୁମ୍ପ {risk}.",
        "Assamese": f"সতৰ্কবাণী! {district}, {state} ত {disaster} বিপদ {risk}."
    }
    return msgs.get(lang, msgs["English"])

def play_voice_alert(text, lang):
    tts = gTTS(text=text, lang=LANG_CODE.get(lang, "en"))
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.save(f.name)
        st.audio(f.name)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
lang = st.sidebar.selectbox("🌐 Language", list(T_dict.keys()),key="langbox")
T = T_dict[lang]

state = st.sidebar.selectbox(T["select_state"], sorted(df["State"].unique()))
district = st.sidebar.selectbox(T["select_district"], sorted(df[df["State"] == state]["District"].unique()))
year = st.sidebar.selectbox(T["select_year"], sorted(df["Year"].unique(), reverse=True))
disaster = st.sidebar.selectbox(T["select_disaster"], sorted(df["Disaster_Type"].unique()))

# ---------------------------------------------------------
# RISK CALCULATION
# ---------------------------------------------------------
filtered = df[
    (df["State"] == state) &
    (df["District"] == district) &
    (df["Year"] == year) &
    (df["Disaster_Type"] == disaster)
]

print("filtered-score:", filtered["Risk_Score"])
district_filtered = district_df[district_df["state"].str.lower() == state.lower()].copy()
district_filtered["risk_score"] = (district_filtered["risk_base"].fillna(50) * 1.2).clip(0, 100)

print("district_filtered:", district_filtered)

overall_risk = round(
    ((filtered["Risk_Score"].mean() if not filtered.empty else 0) +
     district_filtered["risk_score"].mean()) / 2,
    2 
)

print("overall_risk:", overall_risk)

# ---------------------------------------------------------
# 🚨 REAL-TIME RISK SUMMARY
# ---------------------------------------------------------
st.subheader("🚨 Real-Time Risk Summary")
c1, c2, c3 = st.columns(3)

def risk_card(t, v, c):
    st.markdown(f"""
    <div style="background:{c};padding:20px;border-radius:15px;text-align:center;color:white">
    <h3>{t}</h3><h1>{v}</h1></div>
    """, unsafe_allow_html=True)

with c1: risk_card("Overall Risk", overall_risk, "#e53935")
with c2: risk_card("District", district, "#1e88e5")
with c3: risk_card("Disaster", disaster, "#6a1b9a")

# ---------------------------------------------------------
# 🔊 AUTO VOICE ALERT
# ---------------------------------------------------------
if st.sidebar.toggle("🔊 Auto Disaster Voice Alert", True):
    play_voice_alert(
        generate_voice_message(lang, disaster, district, state, overall_risk),
        lang
    )

# ---------------------------------------------------------
# AI REPORT
# ---------------------------------------------------------
st.subheader(T["ai_report"])
for i in range(1, 11):
    st.write(f"{i}. Risk factor analysis generated.")

# ---------------------------------------------------------
# PDF
# ---------------------------------------------------------
def save_pdf(points):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "IDARVIZHI - Disaster Risk Intelligence Report", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", "", 12)
    for p in points:
        pdf.multi_cell(0, 8, p)
    pdf.output("AI_Report.pdf")
    return "AI_Report.pdf"

if st.button("📄 Download AI Report PDF"):
    st.download_button("Download PDF", open(save_pdf(["Report - generated"]), "rb"))


# =========================================================
# IDARVIZHI - DISASTER INTELLIGENCE SYSTEM (FINAL - ORDERED)
# =========================================================
# ---------------------------------------------------------
# VOICE MESSAGE
# ---------------------------------------------------------
def generate_voice_message(lang, disaster, district, state, risk):
    msgs = {
        "English": f"Warning! {disaster} risk is {risk} in {district}, {state}.",
        "Tamil": f"எச்சரிக்கை! {district} மாவட்டத்தில் {disaster} அபாயம் {risk}.",
        "Hindi": f"चेतावनी! {district}, {state} में {disaster} का खतरा {risk} है।",
        "Telugu": f"హెచ్చరిక! {district}, {state} లో {disaster} ప్రమాదం {risk}.",
        "Kannada": f"ಎಚ್ಚರಿಕೆ! {district}, {state} ನಲ್ಲಿ {disaster} ಅಪಾಯ {risk}.",
        "Malayalam": f"മുന്നറിയിപ്പ്! {district}, {state} ൽ {disaster} അപകടം {risk}.",
        "Marathi": f"इशारा! {district}, {state} मध्ये {disaster} धोका {risk}.",
        "Bengali": f"সতর্কতা! {district}, {state} এ {disaster} ঝুঁকি {risk}.",
        "Gujarati": f"ચેતવણી! {district}, {state} માં {disaster} જોખમ {risk}.",
        "Punjabi": f"ਚੇਤਾਵਨੀ! {district}, {state} ਵਿੱਚ {disaster} ਦਾ ਖਤਰਾ {risk}.",
        "Odia": f"ଚେତାବନୀ! {district}, {state} ରେ {disaster} ଝୁମ୍ପ {risk}.",
        "Assamese": f"সতৰ্কবাণী! {district}, {state} ত {disaster} বিপদ {risk}."
    }
    return msgs.get(lang, msgs["English"])

def play_voice_alert(text, lang):
    tts = gTTS(text=text, lang=LANG_CODE.get(lang, "en"))
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.save(f.name)
        st.audio(f.name)


# ---------------------------------------------------------
# MAP
# ---------------------------------------------------------


st.subheader("🗺️ Live District Risk Map")
# --------------------------------------------------------- 
# MAP STYLE SWITCHER 
# --------------------------------------------------------- 
map_styles = [ "basic", "carto-darkmatter", "carto-darkmatter-nolabels", 
"carto-positron", "carto-positron-nolabels", "carto-voyager", "carto-voyager-nolabels", 
"dark", "light", "open-street-map", "outdoors", "satellite", "satellite-streets", "streets", "white-bg" ] 
# User selects map style 
selected_style = st.selectbox("🗺️ Choose Map Style", map_styles, index=9) # default index=9 → "open-street-map"

# classify risk levels
def classify_risk(score):
    if score*100 >= 80:
        return "High risk"
    elif score*100 >= 60:
        return "Moderate risk"
    else:
        return "Low risk"

district_filtered["risk_level"] = district_filtered["risk_score"].apply(classify_risk)

# define custom colors for risk levels
risk_colors = {
    "High risk": "red",       # 🔴
    "Moderate risk": "orange",# 🟠
    "Low risk": "green"       # 🟢
}

# plot with discrete colors
fig = px.scatter_map(
    district_filtered,
    lat="lat",
    lon="lon",
    map_style=selected_style,
    size="risk_score",
    color="risk_level",
    color_discrete_map=risk_colors,
    hover_name="district",
    hover_data={
        "risk_score": True,
        "risk_base": True,
        "lat": False,
        "lon": False
    },
    zoom=5,
)

fig.update_layout(
    # map_style="satellite-streets",
    margin={"r":0,"t":0,"l":0,"b":0},
    height=520
)

st.plotly_chart(fig, width="stretch")


# ---------------------------------------------------------
# CHATBOT
# ---------------------------------------------------------
# st.subheader("🤖 Disaster Assistant")
# q = st.text_input("Ask your question")
# if q:
#     st.info("Please stay calm and follow official alerts.")

import streamlit as st
from hf_blend import *

st.subheader("🤖 Disaster Assistant (Hybrid)") 
if "chat" not in st.session_state: 
    st.session_state.chat = [] 

# Context inputs 

disaster_type = disaster
risk_score = overall_risk
ctx = DisasterContext(disaster_type=disaster_type, state=state, district=district, risk_score=risk_score) 



q = st.text_input("Ask your disaster question")
if q:
    resp = blended_answer_online(q, ctx)
    st.markdown("### AI Perspective (Online AI: model-mistralai/Mistral-7B-Instruct-v0.2)")
    st.write(resp["api_text"])

    st.markdown(f"**{resp['title']}**")
    st.write(resp['summary'])

    st.markdown("### Structured Guidance")
    for b in resp["kb_bullets"]:
        st.write(b)
    st.write("Sources:", ", ".join(resp["kb_links"]))
