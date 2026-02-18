import streamlit as st
import pandas as pd
from datetime import date

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

st.subheader("Datos Generales")

cabo = st.selectbox("Cabo Responsable", lista_cabos)
hacienda = st.text_input("Hacienda").upper()
suerte = st.text_input("Suerte").upper()
fecha = st.date_input("Fecha", date.today())

# --- LABORES ---

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
    nueva_labor = {
        "Fecha": fecha,
        "Cabo": cabo,
        "Hacienda": hacienda,
        "Suerte": suerte,
        "Actividad": actividad,
        "Área": area,
        "Operador": operador,
        "Equipo": equipo,
        "Turno": turno,
        "Contratista": contratista
    }
    st.session_state.labores.append(nueva_labor)

if st.session_state.labores:
    df = pd.DataFrame(st.session_state.labores)
    st.dataframe(df)

    if st.button("Guardar en Excel"):
        df.to_excel("programacion_diaria.xlsx", index=False)
        st.success("Archivo guardado correctamente")


