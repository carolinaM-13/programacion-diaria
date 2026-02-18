import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import date

# --- Listas personalizables ---
lista_cabos = ["CARLOS PEREZ", "YAINER ESCOBAR", "JAMES RODRIGUEZ", "MARLON ALARCON", "YERSON GUERRERO", "ANDRES ZAMBRANO"]
lista_contratistas = ["QUINCORA", "SOCIEDAD AZCÀRATE", "AMEZQUITA", "MANUELITA", "SERVIAGRÌCOLA MENDEZ"]
lista_labores = ["SIEMBRA MECÀNICA","CORTE MECÀNICO","CORTE MANUAL","SIEMBRA MANUAL","DESCEPADA 1","DESCEPADA 2","NIVELACIÒN","SUBSUELO","RASTROARADO","RASTRILLO","SURCO"]
lista_operadores = ["JUAN","PABLO","JAMES","ESCOBAR"]
lista_equipos = ["COSECHADORA 9467","TRACTOR 7401","SEMBRADORA 1002","TRACTOR 7402"]
lista_turnos = ["50","51","63"]

# --- Datos generales ---
st.title("PROGRAMACIÓN DIARIA DE LABORES")
st.subheader("Datos Generales")
cabo = st.selectbox("Cabo Responsable", lista_cabos)
hacienda = st.text_input("Hacienda").upper()
suerte = st.text_input("Suerte").upper()
fecha = st.date_input("Fecha", date.today())

# --- Conexión a Google Sheets ---
scope = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credenciales.json", scopes=scope)
gc = gspread.authorize(creds)
spreadsheet_url = "TU_URL_DE_GOOGLE_SHEETS"  # <--- pon aquí la URL de tu hoja de cálculo
sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.sheet1

# --- Detalle de labores ---
st.subheader("Detalle de Labores")
if "labores" not in st.session_state:
    st.session_state.labores = []

actividad = st.selectbox("Actividad Programada", lista_labores)
area = st.number_input("Área Programada", min_value=0.0)
operador = st.selectbox("Operador", lista_operadores)
equipo = st.selectbox("Equipo", lista_equipos)
turno = st.selectbox("Turno", lista_turnos)
contratista = st.selectbox("Contratista", lista_contratistas)

if st.button("Agregar Labor"):
    nueva_labor = [str(fecha), cabo, hacienda, suerte, actividad, area, operador, equipo, turno, contratista]
    worksheet.append_row(nueva_labor)
    st.success("Labor agregada en Google Sheets correctamente!")

# --- Mostrar tabla local ---
if st.button("Ver Tabla"):
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    st.dataframe(df)


