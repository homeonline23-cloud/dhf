import streamlit as st
import pandas as pd

# --- COMMAND CENTER ---
st.sidebar.title("🏛️ Mitrax Command Center")
st.sidebar.write("**Head Chef:** Karel Carty")
st.sidebar.write("**Empire Status:** ONLINE 🟢")
st.sidebar.write("**Universal Compass:** 2620")

# --- THE 2620 REGISTRY (The 14-Soldier Army) ---
st.title("🛰️ Universal Compass Registry")

data = {
    "Soldier": ["1/1", "2/1", "3/1", "4/1", "5/1", "6/1", "7/1", 
                "8/3", "9/3", "10/3", "11/3", "12/3", "13/3", "14/3"],
    "North": [2620]*14,
    "South": [2620]*14,
    "East": [2620]*14,
    "West": [2620]*14
}
df = pd.DataFrame(data)

# --- THE COLOR PROTOCOL (Red 7/1 and Blue 8/3) ---
def apply_colors(row):
    if row['Soldier'] == "7/1":
        return ['background-color: red; color: white; font-weight: bold'] * 5
    if row['Soldier'] == "8/3":
        return ['background-color: blue; color: white; font-weight: bold'] * 5
    return [''] * 5

# Serving the Plate
st.table(df.style.apply(apply_colors, axis=1))

st.success("The Mitrax Empire remains balanced at 2620 across all directions.")