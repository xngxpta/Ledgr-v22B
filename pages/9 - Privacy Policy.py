import pandas as pd
import streamlit as st
#from pathlib import Path
from streamlit_pdf_viewer import pdf_viewer
# Function to read the content of a markdown file
import base64
import os


direc = os.getcwd()

# Display PDF with custom zoom, alignment, and separators
pdf_viewer(
    f"{direc}/pages/appdata/Privacy_Policy_Final.pdf",
    width=700,
    height=1000,
    zoom_level=1.2,                    # 120% zoom
    viewer_align="center",             # Center alignment
    show_page_separator=True           # Show separators between pages
)
st.write("  ---------------------------------------------------------------  ")
# # ###################################################################
with st.container():
    f9, f10, f11 = st.columns([2, 5, 1])
    with f9:
        st.write(" ")
    with f10:
        st.write(": 2025 - 2026 | All Rights Reserved  ©  Ledgr Inc.")
        st.write(": alphaLedgr.com | alphaLedgr Technologies Ltd. :")
    with f11:
        st.write(" ")

