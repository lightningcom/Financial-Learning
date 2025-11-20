import streamlit as st
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Financial Analysis Learning Platform",
    page_icon="📈",
    layout="centered"
)

def home_page():
    st.title("Learn your way to Financial Analysis")
    st.subheader("Select a module to begin")
    st.write("---")
    
    # Custom CSS to ensure equal height boxes and consistent padding
    st.markdown("""
    <style>
    div[data-testid="stVerticalBlockBorderWrapper"] {
        padding: 20px !important;
        height: 300px !important;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Using a container to create a visual "box" effect
        with st.container(border=True):
            st.markdown("### 📊 Fundamentals")
            st.write("Learn about intrinsic value, financial statements, and long-term investing.")
            if st.button("Start Fundamentals", use_container_width=True, type="primary"):
                st.switch_page("pages/1_Fundamentals.py")
            
    with col2:
        with st.container(border=True):
            st.markdown("### 📈 Technical")
            st.write("Master charts, trends, indicators, and price action trading.")
            if st.button("Start Technical", use_container_width=True, type="primary"):
                st.switch_page("pages/2_Technical.py")

if __name__ == "__main__":
    home_page()