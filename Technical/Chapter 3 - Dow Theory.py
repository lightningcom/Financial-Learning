import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("Dow Theory and application")
st.write("**Let's learn the Dow Theory and its application in cool way**")
st.write("The market is not a random casino; it is a barometer of the global economy. By understanding the **tides** of this barometer, one can align with the major economic currents rather than swimming against them.")
tab1, tab2, tab3, tab4, tab5= st.tabs(["Origin and all", "The 3 Phase","Market Phases","Volume Confirmation","Trend Identification" ])

with tab1:
    st.subheader("The Origin Story: An Accidental System", divider=True)
    st.markdown("""
    It is a great irony of financial history that the father of technical analysis, **Charles H. Dow**, never wrote a book on the subject, nor did he ever use the term "Technical Analysis."\n
    In the late 19th century, Wall Street was a chaotic, unregulated environment. Charles Dow, a journalist and co-founder of Dow Jones & Company, sought to bring transparency to this chaos. In 1884, he created the first stock average (composed mostly of railroads), and in 1896, he created the **Dow Jones Industrial Average (DJIA).**\n
    Dow’s goal was not to create a system for trading stocks. His goal was to create an index that measured the health of the American economy. He published his observations in a series of editorials for The Wall Street Journal between 1900 and his death in 1902.\n
    It was his successors who organized these thoughts into a trading discipline. S.A. Nelson first coined the term "Dow’s Theory" in 1902. Later, William Peter Hamilton (in The Stock Market Barometer, 1922) and Robert Rhea (in The Dow Theory, 1932) refined these editorials into the axioms we study today.
    """,unsafe_allow_html=False, width="stretch")
    st.subheader("The Six Tenets of Dow Theory")
    st.write("To practice technical analysis without understanding Dow Theory is like trying to do algebra without understanding arithmetic. These six tenets form the bedrock of trend identification.")
    st.markdown("""
        * **The Averages Discount Everything.**
        * **The Market Has Three Movements.**
        * **Major Trends Have Three Phases.**
        * **The Averages Must Confirm Each Other.**
        * **Volume Must Confirm the Trend.**
        * **A Trend Is Assumed to Be in Effect Until It Gives a Definite Signal of Reversal**
    """)