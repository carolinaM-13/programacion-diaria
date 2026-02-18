import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# --- Alcance de Google Sheets ---
scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]

# --- Obtener credenciales desde Streamlit Secrets ---
creds_dict = st.secrets["GOOGLE_CREDS"]   # YA es un dict
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)

# --- Conectarse a Google Sheets ---
gc = gspread.authorize(creds)

# Ejemplo: abrir hoja de cálculo por URL
spreadsheet_url = "TU_URL_DE_GOOGLE_SHEETS"
sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.sheet1  # primera hoja

