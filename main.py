import streamlit as st
from search import image_search
import os

# App title
st.title("🖼️ Image Search Application with Bridgetower")

# Image Upload Section
st.header("📤 Upload Images")
uploaded_files = st.file_uploader("Upload images to the search directory", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])

if uploaded_files:
    os.makedirs("images", exist_ok=True)
    for uploaded_file in uploaded_files:
        with open(f"images/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption=f"{uploaded_file.name}", use_container_width=True)

# Text Query Section
st.header("🔍 Search by Text Query")
query = st.text_input("Enter your search query:")

if query:
    if not os.path.exists("images") or not os.listdir("images"):
        st.warning("Please upload images first!")
    else:
        result = image_search(query, "images/")
        st.write("✅ **Best Matching Image:**")
        st.image(result, caption="Best Match", use_container_width=True)