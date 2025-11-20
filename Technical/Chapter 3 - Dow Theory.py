import streamlit as st
import numpy as np
import pandas as pd

import plotly.graph_objects as go

from plotly.subplots import make_subplots



def generate_trends(days=365, primary_slope=0.1, sec_freq=0.05, sec_amp=5, noise_level=1):

    """Generates synthetic price data composed of Primary, Secondary, and Minor trends."""

    t = np.arange(days)
    

    # Primary Trend (The Tide) - Linear or slight curve

    primary = 100 + (primary_slope * t)
    

    # Secondary Trend (The Waves) - Sine wave

    secondary = sec_amp * np.sin(2 * np.pi * sec_freq * t)
    

    # Minor Trend (The Ripples) - Random Noise

    np.random.seed(42)

    minor = np.random.normal(0, noise_level, days)
    

    # Composite Price

    total_price = primary + secondary + minor
    

    return t, primary, secondary, minor, total_price



st.title("Dow Theory and application")

st.write("**Let's learn the Dow Theory and its application in cool way**")

st.write("The market is not a random casino; it is a barometer of the global economy. By understanding the **tides** of this barometer, one can align with the major economic currents rather than swimming against them.")

tab1, tab2, tab3, tab4, tab5, tab6, tab7= st.tabs(["The Origin and all", "Tenet 1","Tenet 2","Tenet 3","Tenet 4","Tenet 5","Tenet 6"])


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

with tab2:

    st.subheader("The Averages Discount Everything", divider=True)

    st.write("This is the premise of **Efficient Markets** before the term existed. Dow argued that the closing price of the market averages represents the sum total of all hopes, fears, and knowledge of market participants.")

    st.markdown("""

    * Interest rate hikes? Priced in.

    * War in Europe? Priced in

    * Expected earnings? Priced in \n


    Because the **"smart money"** acts on information before it becomes public news, the price movement itself is the news. The chart leads; the headlines follow.

    """)


with tab3:

        st.subheader("The Market Has Three Movements", divider=True)

        st.write("Dow proposed that the market acts exactly like the ocean. To understand the price, you must distinguish between the tide, the waves, and the ripples.")

        st.markdown("""

    So, basically Dow compared the market to ocean. Price action is a composite of 3 distinct movements occuring simultaneously, which are nothing basically the above 3 ones:

    1.  **Primary Trend (The Tide):** Long-term direction (Years).

    2.  **Secondary Trend (The Waves):** Intermediate corrections (Weeks/Months).

    3.  **Minor Trend (The Ripples):** Day-to-day fluctuations (Noise).

    """)
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.subheader("Simulation Controls")
            slope = st.slider("Primary Trend Slope (Bull/Bear)", -0.2, 0.2, 0.1, 0.01)
            amp = st.slider("Secondary Trend Volatility", 0, 20, 5)
            noise = st.slider("Minor Trend Noise", 0.0, 5.0, 1.0)
            
            show_primary = st.checkbox("Show Primary (Tide)", True)
            show_secondary = st.checkbox("Show Secondary (Waves)", True)
            show_minor = st.checkbox("Show Minor (Ripples)", True)
            
        with col2:
            t, p, s, m, total = generate_trends(days=200, primary_slope=slope, sec_amp=amp, noise_level=noise)
            
            fig = go.Figure()
            
            # Calculate components for visualization (centering secondary/minor around primary for visual clarity)
            if show_primary:
                fig.add_trace(go.Scatter(x=t, y=p, mode='lines', name='Primary Trend', line=dict(color='blue', width=4, dash='dash')))
                
            current_view = p.copy() # Start with primary as baseline
            
            if show_secondary:
                # We add the sine wave to the primary
                with_secondary = p + s
                # To visualize just the wave distinct from price, we can plot it, but here we want to show composition
                # Let's plot the "Idealized" price (Primary + Secondary)
                fig.add_trace(go.Scatter(x=t, y=with_secondary, mode='lines', name='Primary + Secondary', line=dict(color='green', width=2)))
                current_view = with_secondary

            if show_minor:
                # Total Price
                fig.add_trace(go.Scatter(x=t, y=total, mode='lines', name='Final Price (Composite)', line=dict(color='black', width=1)))

            fig.update_layout(title="Deconstructing Price Action", height=500, xaxis_title="Time", yaxis_title="Price")
            st.plotly_chart(fig, use_container_width=True)



with tab4:

    st.subheader("Mainly! the market trends have 3 Phases", divider=True)

    st.write("Just as a story has a beginning, middle, and a Primary Trend has three distinct psychological phases.")

    tab1, tab2= st.tabs(["Bull Market phase", "Bear Market Phases"])
    with tab1:
        st.markdown("### The Bull Market Cycle")
        st.markdown("""
        1.  **Accumulation:** Informed investors buy low. Market is quiet. "Smart Money" enters.
        2.  **Public Participation:** Trend becomes visible. Earnings improve. The crowd joins.
        3.  **Excess:** Euphoria. "Stocks only go up." Smart money sells to the public.
        """)
        x = np.linspace(0, 10, 100)
        y = 1 / (1 + np.exp(-x + 5)) * 100  # Sigmoid
        y += np.random.normal(0, 1, 100) # Noise
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='green', width=3)))
        fig.add_vrect(x0=0, x1=3.3, fillcolor="green", opacity=0.1, annotation_text="Accumulation", annotation_position="top left")
        fig.add_vrect(x0=3.3, x1=6.6, fillcolor="blue", opacity=0.1, annotation_text="Participation", annotation_position="top left")
        fig.add_vrect(x0=6.6, x1=10, fillcolor="red", opacity=0.1, annotation_text="Excess", annotation_position="top left")
        
        fig.update_layout(title="Anatomy of a Bull Market", height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.markdown("### The Bear Market Cycle")
        st.markdown("""
        1.  **Distribution:** Smart money offloads positions. Market stalls despite "good news."
        2.  **Panic:** Price breaks support. Fear takes over. Steepest declines.
        3.  **Despair (Capitulation):** Everyone who wanted to sell has sold. Market hits bottom.
        """)
        
        # Generate Bear Market Curve
        y_bear = 100 - (1 / (1 + np.exp(-x + 5)) * 100)
        y_bear += np.random.normal(0, 1, 100)

        fig_bear = go.Figure()
        fig_bear.add_trace(go.Scatter(x=x, y=y_bear, mode='lines', line=dict(color='red', width=3)))
        
        # Annotations
        fig_bear.add_vrect(x0=0, x1=3.3, fillcolor="orange", opacity=0.1, annotation_text="Distribution", annotation_position="bottom left")
        fig_bear.add_vrect(x0=3.3, x1=6.6, fillcolor="red", opacity=0.1, annotation_text="Panic", annotation_position="bottom left")
        fig_bear.add_vrect(x0=6.6, x1=10, fillcolor="gray", opacity=0.1, annotation_text="Despair", annotation_position="bottom left")

        fig_bear.update_layout(title="Anatomy of a Bear Market", height=400, showlegend=False)
        st.plotly_chart(fig_bear, use_container_width=True)


    


        


