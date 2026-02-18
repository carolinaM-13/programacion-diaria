import streamlit as st
import pandas as pd
from datetime import date

st.title("PROGRAMACIÓN DIARIA DE LABORES")

# --- LISTAS PERSONALIZABLES ---

lista_labores = [
    "SIEMBRA MEC",
    "CORTE MEC",
    "SIEMBRA MANUAL",
    "FERTILIZACIÓN",
    "RIEGO",
    "CONTROL MALEZA"
]

lista_operadores = [
    "JUAN PEREZ",
    "PEDRO LOPEZ",
    "CARLOS RAMIREZ",
    "ANDRES GOMEZ"
]

lista_equipos = [
    "COSECHADORA 1",
    "TRACTOR 5",
    "SEMBRADORA 3",
    "RETRO 2"
]

lista_turnos = ["DÍA", "NOCHE"]

# --- DATOS GENERALES ---

st.subheader("Datos Generales")

cabo = st.text_input("Cabo Responsable").upper()
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
contratista = st.text_input("Contratista").upper()

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


