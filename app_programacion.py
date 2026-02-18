import streamlit as st
import pandas as pd
from datetime import date
import io

# --- Lista de opciones ---
lista_cabos = ["CARLOS PÉREZ", "YAINER ESCOBAR", "ANDRÉS ZAMBRANO",  "MARLON ALARCÓN", "YERSON GUERRERO","JAMES RODRÍGUEZ"]
lista_contratistas = ["QUINCORA", "SERVIAGRÍCOLA MÉNDEZ","AMEZQUITA","SOCIEDAD AZCÀRATE"]
lista_labores = ["SIEMBRA MECÀNICA", "CORTE MECÀNICO"]
lista_operadores = ["JUAN", "PABLO"]
lista_equipos = ["COSECHADORA 9467", "TRACTOR 7401"]
lista_turnos = ["50", "51"]

# --- Título ---
st.title("PROGRAMACIÓN DIARIA DE LABORES")

# --- Datos generales ---
cabo = st.selectbox("Cabo Responsable", lista_cabos)
contratista = st.selectbox("Contratista", lista_contratistas)
hacienda = st.text_input("Hacienda").upper()
suerte = st.text_input("Suerte").upper()
fecha = st.date_input("Fecha", date.today())

# --- Detalle de labores ---
if "labores" not in st.session_state:
    st.session_state.labores = []

actividad = st.selectbox("Actividad Programada", lista_labores)
area = st.number_input("Área Programada", min_value=0.0)
operador = st.selectbox("Operador", lista_operadores)
equipo = st.selectbox("Equipo", lista_equipos)
turno = st.selectbox("Turno", lista_turnos)

if st.button("Agregar Labor"):
    nueva_labor = {
        "Fecha": fecha.strftime("%d/%m/%Y"),
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
    st.success("Labor agregada correctamente")

# --- Mostrar datos ---
if st.session_state.labores:
    df = pd.DataFrame(st.session_state.labores)
    st.dataframe(df)

    # --- Botón de descarga ---
    towrite = io.BytesIO()
    df.to_excel(towrite, index=False, engine='xlsxwriter')
    towrite.seek(0)

    st.download_button(
        label="📥 Descargar Excel con todas las labores",
        data=towrite,
        file_name="programacion_diaria.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )




