import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gestor de Metas", page_icon="🎯", layout="centered")

st.title("🎯 Gestor de Metas Personales")
st.write("Version web de tu proyecto de consola")

if "metas" not in st.session_state:
    st.session_state.metas = []

col1, col2 = st.columns([3, 1])
with col1:
    nueva_meta = st.text_input("Escribe una nueva meta")
with col2:
    st.write("")
    st.write("")
    if st.button("Agregar", use_container_width=True):
        if nueva_meta.strip() != "":
            st.session_state.metas.append({"descripcion": nueva_meta, "cumplida": False})
            st.rerun()

st.divider()
st.subheader("Tus metas")

if len(st.session_state.metas) == 0:
    st.info("Aun no tienes metas registradas. Agrega la primera arriba.")

for i, meta in enumerate(st.session_state.metas):
    col1, col2 = st.columns([4, 1])
    with col1:
        cumplida = st.checkbox(meta["descripcion"], value=meta["cumplida"], key=f"chk{i}")
        st.session_state.metas[i]["cumplida"] = cumplida
    with col2:
        if st.button("🗑️", key=f"del{i}"):
            st.session_state.metas.pop(i)
            st.rerun()

if len(st.session_state.metas) > 0:
    st.divider()
    st.subheader("Progreso")
    total = len(st.session_state.metas)
    cumplidas = sum(1 for m in st.session_state.metas if m["cumplida"])
    st.progress(cumplidas / total)
    st.write(f"{cumplidas} de {total} metas cumplidas ({cumplidas/total*100:.0f}%)")
    
    df = pd.DataFrame({
        "Estado": ["Cumplidas", "Pendientes"],
        "Cantidad": [cumplidas, total - cumplidas]
    })
    st.bar_chart(df.set_index("Estado"))