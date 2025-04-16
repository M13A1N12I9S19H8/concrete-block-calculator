# app.py
import streamlit as st
from calculation import calculate_materials, get_block_dimensions

st.set_page_config(page_title="Block Calculator", layout="centered")

st.title("🧱 Concrete Block Material Calculator")

block_types = [
    "Splitface Block", "Bullnose Block", "Partition Block", "Fly Ash Block",
    "Aerated Autoclaved Block", "Paving Block", "Cellular Lightweight Block",
    "Expanded Block", "Solid Concrete Block", "Hollow Concrete Block",
    "Stretcher Block", "Pillar Block", "Lintel Block", "Jamb Block",
    "Column Block", "Corner Block"
]

block_type = st.selectbox("Select Block Type", block_types)

length, width, height = get_block_dimensions(block_type)

st.image(f"assets/{block_type.replace(' ', '_').lower()}.png", caption=block_type, width=200)

st.subheader("Block Dimensions (in mm)")
length = st.number_input("Length", value=length)
width = st.number_input("Width", value=width)
height = st.number_input("Height", value=height)

st.subheader("Concrete Strength")
strength = st.slider("Select Strength (MPa)", min_value=10, max_value=35, value=20)

formwork_thickness = st.number_input("Formwork Thickness (mm)", value=10)

if st.button("Calculate Materials"):
    results = calculate_materials(length, width, height, strength, formwork_thickness)

    report = f"""
    <div style='background-color:#f9f9f9;padding:20px;border-radius:10px;'>
        <h3>Calculation Report</h3>
        <p><b>Block Type:</b> {block_type}</p>
        <p><b>Dimensions (L×W×H):</b> {length} × {width} × {height} mm</p>
        <p><b>Concrete Strength:</b> {strength} MPa</p>
        <p><b>Formwork Thickness:</b> {formwork_thickness} mm</p>
        <ul>
            <li><b>Volume:</b> {results['Volume (m³)']} m³</li>
            <li><b>Cement:</b> {results['Cement (kg)']} kg</li>
            <li><b>Sand:</b> {results['Sand (kg)']} kg</li>
            <li><b>Aggregate:</b> {results['Aggregate (kg)']} kg</li>
            <li><b>Water:</b> {results['Water (kg)']} kg</li>
        </ul>
    </div>
    """
    st.markdown(report, unsafe_allow_html=True)
