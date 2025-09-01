
import streamlit as st

# Título de la app
st.title("Diagnóstico Veterinario para Perros")
st.subheader("Simulador de diagnóstico veterinario basado en síntomas")

# Entradas del usuario
edad = st.number_input("Edad del perro (en años)", min_value=0.0, step=0.5)
raza = st.text_input("Raza del perro")
genero = st.selectbox("Género del perro", ["Macho", "Hembra"])
sintomas = st.text_area("Describe los síntomas que presenta el perro")

# Lógica simulada para diagnóstico
def diagnostico_veterinario(edad, raza, genero, sintomas):
    sintomas = sintomas.lower()

    if not sintomas:
        return "Por favor ingresa los síntomas para generar un diagnóstico."

    if "vomito" in sintomas and "diarrea" in sintomas:
        return "Posible gastroenteritis. Se recomienda hidratación y consulta médica urgente."
    elif "cojera" in sintomas or "dolor al caminar" in sintomas:
        return "Posible lesión musculoesquelética. Se sugiere reposo y revisión radiológica."
    elif "comezon" in sintomas or "erupciones" in sintomas:
        return "Posible reacción alérgica o problema dermatológico. Revisar alimentación y ambiente."
    elif "tos" in sintomas and edad > 8:
        return "Posible problema respiratorio crónico. Evaluación pulmonar recomendada."
    elif "letargo" in sintomas and "fiebre" in sintomas:
        return "Puede tratarse de una infección sistémica. Acudir al veterinario lo antes posible."
    else:
        return "Síntomas generales detectados. Se recomienda una revisión veterinaria completa."

# Botón para generar diagnóstico
if st.button("Generar diagnóstico"):
    resultado = diagnostico_veterinario(edad, raza, genero, sintomas)
    st.markdown(f"### 🩺 Diagnóstico:\n{resultado}")
