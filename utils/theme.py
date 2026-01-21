import streamlit as st

def set_theme(theme):

    if theme == "dark":
        st.markdown("""
        <style>

        .stApp {
            background-color: #0e1117;
            color: #fafafa;
        }

        div[data-baseweb="input"] input,
        div[data-baseweb="input"] textarea {
            background-color: #262730 !important;
            color: white !important;
            border-radius: 10px !important;
            border: 1px solid #3a3a3a !important;
        }

        div[data-baseweb="select"] > div {
            background-color: #262730 !important;
            color: white !important;
            border-radius: 10px !important;
            border: 1px solid #3a3a3a !important;
        }

        div[data-baseweb="select"] svg {
            fill: white !important;
        }

        ul[role="listbox"] {
            background-color: #262730 !important;
            color: white !important;
        }

        </style>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <style>

        .stApp {
            background-color: #ffffff;
            color: black;
        }

        div[data-baseweb="input"] input,
        div[data-baseweb="input"] textarea {
            background-color: #f5f6f7 !i    mportant;
            color: black !important;
            border-radius: 10px !important;
            border: 1px solid #cccccc !important;
        }

        div[data-baseweb="select"] > div {
            background-color: #f5f6f7 !important;
            color: black !important;
            border-radius: 10px !important;
            border: 1px solid #cccccc !important;
        }

        div[data-baseweb="select"] svg {
            fill: black !important;
        }

        ul[role="listbox"] {
            background-color: #ffffff !important;
            color: black !important;
        }

        </style>
        """, unsafe_allow_html=True)
