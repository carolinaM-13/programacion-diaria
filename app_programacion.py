import streamlit as st
import pandas as pd
from datetime import date
import gspread
from google.oauth2.service_account import Credentials

st.title("PROGRAMACIÓN DIARIA DE LABORES")

# --- LISTAS PERSONALIZABLES ---

lista_cabos = [
    "CARLOS PEREZ",
    "YAINER ESCOBAR",
    "JAMES RODRIGUEZ",
    "MARLON ALARCON",
    "YERSON GUERRERO",
    "ANDRES ZAMBRANO"
]

lista_contratistas = [
    "QUINCORA",
    "SOCIEDAD AZCÀRATE",
    "AMEZQUITA",
    "MANUELITA",
    "SERVIAGRÌCOLA MENDEZ"
]

lista_labores = [
    "SIEMBRA MECÀNICA",
    "CORTE MECÀNICO",
    "CORTE MANUAL",
    "SIEMBRA MANUAL",
    "DESCEPADA 1",
    "DESCEPADA 2",
    "NIVELACIÒN",
    "SUBSUELO",
    "RASTROARADO",
    "RASTRILLO",
    "SURCO"
]

lista_operadores = [
    "JUAN",
    "PABLO",
    "JAMES",
    "ESCOBAR"
]

lista_equipos = [
    "COSECHADORA 9467",
    "TRACTOR 7401",
    "SEMBRADORA 1002",
    "TRACTOR 7402"
]

lista_turnos = ["50", "51", "63"]

# --- DATOS GENERALES ---

cabo = st.selectbox("Cabo Responsable", lista_cabos)
contratista = st.selectbox("Contratista", lista_contratistas)
hacienda = st.text_input("Hacienda").upper()
suerte = st.text_input("Suerte").upper()
fecha = st.date_input("Fecha", date.today())

# --- DETALLE DE LABORES ---

actividad = st.selectbox("Actividad Programada", lista_labores)
area = st.number_input("Área Programada", min_value=0.0)
operador = st.selectbox("Operador", lista_operadores)
equipo = st.selectbox("Equipo", lista_equipos)
turno = st.selectbox("Turno", lista_turnos)

# --- CONEXIÓN GOOGLE SHEETS ---

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Cambia "credenciales.json" por el nombre exacto de tu archivo JSON
creds = Credentials.from_service_account_file("credenciales.json", scopes=scope)
client = gspread.authorize(creds)

# Reemplaza con el nombre exacto de tu Google Sheet
sheet = client.open("Programacion Diaria de Labores").sheet1

# --- AGREGAR LABOR ---

if st.button("Agregar Labor"):
    nueva_labor = [
        fecha.strftime("%d/%m/%Y"),
        cabo,
        hacienda,
        suerte,
        actividad,
        area,
        operador,
        equipo,
        turno,
        contratista
    ]
    sheet.append_row(nueva_labor)
    st.success("Labor agregada correctamente y guardada en el Sheet central")
