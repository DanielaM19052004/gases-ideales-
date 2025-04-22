import streamlit as st

# Constante universal de los gases en L·atm/(mol·K)
R = 0.0821

st.title("Calculadora de la Ecuación de los Gases Ideales")

st.markdown("Ecuación:  **PV = nRT**")

# Opción para seleccionar qué calcular
opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Moles (n)")
)

# Campos de entrada dependiendo de la selección
if opcion == "Presión (P)":
    volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.3f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.2f")
    moles = st.number_input("Cantidad de sustancia (mol)", min_value=0.0, format="%.3f")
    if st.button("Calcular Presión"):
        if volumen > 0:
            presion = (moles * R * temperatura) / volumen
            st.success(f"Presión: {presion:.3f} atm")
        else:
            st.error("El volumen debe ser mayor que cero.")

elif opcion == "Volumen (V)":
    presion = st.number_input("Presión (atm)", min_value=0.0, format="%.3f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.2f")
    moles = st.number_input("Cantidad de sustancia (mol)", min_value=0.0, format="%.3f")
    if st.button("Calcular Volumen"):
        if presion > 0:
            volumen = (moles * R * temperatura) / presion
            st.success(f"Volumen: {volumen:.3f} L")
        else:
            st.error("La presión debe ser mayor que cero.")

elif opcion == "Temperatura (T)":
    presion = st.number_input("Presión (atm)", min_value=0.0, format="%.3f")
    volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.3f")
    moles = st.number_input("Cantidad de sustancia (mol)", min_value=0.0, format="%.3f")
    if st.button("Calcular Temperatura"):
        if moles > 0:
            temperatura = (presion * volumen) / (moles * R)
            st.success(f"Temperatura: {temperatura:.2f} K")
        else:
            st.error("La cantidad de moles debe ser mayor que cero.")

elif opcion == "Moles (n)":
    presion = st.number_input("Presión (atm)", min_value=0.0, format="%.3f")
    volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.3f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.2f")
    if st.button("Calcular Moles"):
        if temperatura > 0:
            moles = (presion * volumen) / (R * temperatura)
            st.success(f"Moles: {moles:.3f} mol")
        else:
            st.error("La temperatura debe ser mayor que cero.")
