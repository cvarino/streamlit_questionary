import streamlit as st

st.title("¿Cuánto conoces a Marta?")

cumple = st.radio(
    "¿Qué día es mi cumpleaños?",
    ["13 de marzo", "3 de mayo", "13 de mayo", "3 de marzo"],
)

acertadas = 0
if cumple == "13 de mayo":
    acertadas = 1

animal = st.radio(
    "¿Cuál es mi animal favorito?",
    ["Los conejos", "Los caballos", "Los defines", "Las jirafas"],
)

if animal == "Las jirafas":
    acertadas = acertadas + 1

flor = st.radio(
    "¿Cuál es mi flor favorita?",
    ["La Lavanda", "Las rosas", "Las petunias", "Las margaritas"],
)

if flor == "La Lavanda":
    acertadas = acertadas + 1


estación = st.radio(
    "¿Cuál es mi estación del año favorita?",
    ["El verano", "El invierno", "La primavera", "El otoño"],
)

if estación == "La primavera":
    acertadas = acertadas + 1


prenda = st.radio(
    "¿Cuál es mi prenda de vestir favorita?",
    ["Las faldas", "Los monos", "Los jerséis", "Las cardigans"],
)

if prenda == "Los monos":
    acertadas = acertadas + 1

print(f"Has acertado {acertadas}/5")

