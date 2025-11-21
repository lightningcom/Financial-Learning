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


def generate_volume_trend(price, trend_direction=1):
    """Generates synthetic volume data correlated with price movement."""
    change = np.diff(price, prepend=price[0])
    
    # Base volume with noise
    vol = np.random.normal(1000, 100, len(price))
    
    if trend_direction == 1:
        # Healthy: Volume expands on up-moves (change > 0)
        vol += np.where(change > 0, 500, -200)
        
    return np.clip(vol, 100, None)



st.title("Dow Theory and application")

st.write("**Let's learn the Dow Theory and its application in cool way**")

st.write("The market is not a random casino; it is a barometer of the global economy. By understanding the **tides** of this barometer, one can align with the major economic currents rather than swimming against them.")

tab1, tab2, tab3, tab4, tab5, tab6, tab7= st.tabs(["The Origin and all", "Tenet 1","Tenet 2","Tenet 3","Tenet 4","Tenet 5","Tenet 6"])


with tab1:

    st.subheader("The Origin Story: An Accidental System", divider=True)

    st.markdown("""

    It is a great irony of financial history that the father of technical analysis, **Charles H. Dow**, never wrote a book on the subject, nor did he ever use the term "Technical Analysis."\n

    In the late 19th century, Wall Street was a chaotic, unregulated environment. Charles Dow, a journalist and co-founder of Dow Jones & Company, sought to bring transparency to this chaos. In 1884, he created the first stock average (composed mostly of railroads), and in 1896, he created the **Dow Jones Industrial Average (DJIA).**\n

    Dow's goal was not to create a system for trading stocks. His goal was to create an index that measured the health of the American economy. He published his observations in a series of editorials for The Wall Street Journal between 1900 and his death in 1902.\n

    It was his successors who organized these thoughts into a trading discipline. S.A. Nelson first coined the term "Dow's Theory" in 1902. Later, William Peter Hamilton (in The Stock Market Barometer, 1922) and Robert Rhea (in The Dow Theory, 1932) refined these editorials into the axioms we study today.

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
                fig.add_trace(go.Scatter(x=t, y=with_secondary, mode='lines', name='Primary + Secondary', line=dict(color='orange', width=2)))
                current_view = with_secondary

            if show_minor:
                # Total Price
                fig.add_trace(go.Scatter(x=t, y=total, mode='lines', name='Final Price (Composite)', line=dict(color='yellow', width=1)))

            fig.update_layout(title="Deconstructing Price Action", height=500, xaxis_title="Time", yaxis_title="Price")
            st.plotly_chart(fig, use_container_width=True)



with tab4:

    st.subheader("Mainly! the market trends have 3 Phases", divider=True)

    st.write("Just as a story has a beginning, middle, and the end. In same manner, a Primary Trend has three distinct psychological phases.")

    tab1, tab2= st.tabs(["Bull Market Phase", "Bear Market Phase"])
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
        fig_bear.add_vrect(x0=6.6, x1=10, fillcolor="yellow", opacity=0.1, annotation_text="Despair", annotation_position="bottom left")

        fig_bear.update_layout(title="Anatomy of a Bear Market", height=400, showlegend=False)
        st.plotly_chart(fig_bear, use_container_width=True)

with tab5:
    st.subheader("Indices Must Confirm Each Other", divider=True)
    st.markdown("""
    This is the most unique and industrial-centric aspect of Dow Theory. Dow believed you could nove have a healthy economy unless goods were being manufactured and shipped. 
    * **The Industrial Average:** Measures the performance of the largest, most industrialized companies.
    * **The Transportation Average (earlier Railroad Average):** Measures the performance of the largest transportation companies. 
    """)
    st.success("**The Rule is simple:** If the Industrials hit a new high, the Transports must also hit a new high to **confirm** the trend. The Warning: If Industrials break out to a new high but Transports sluggishly fail to follow (a Divergence), the trend is suspect. It implies factories are making goods that aren't being shipped—a prelude to a recession.")
    st.divider()
    scenario = st.radio("**Select a market scenario**",["Healthy Confirmation","Bearish Non-Confirmation (Divergence)"])
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Dow Jones Industrial Average (DJIA)", "Dow Jones Transportation Average (DJTA)"))
    
    days = 100
    t = np.arange(days)
    
    if scenario == "Healthy Confirmation":
        # Both go up
        djia = 100 + t * 0.5 + np.random.normal(0, 2, days)
        djta = 100 + t * 0.5 + np.random.normal(0, 2, days)
        msg = "✅ **CONFIRMED:** Both averages are making higher highs. The economy is producing AND shipping goods."
    else:
        # Divergence
        djia = 100 + t * 0.5 + np.random.normal(0, 2, days) # Goes up
        djta = 100 + t * 0.2 
        djta[70:] = djta[70] - (np.arange(30) * 0.4) # Crash at end
        djta += np.random.normal(0, 2, days)
        msg = "⚠️ **NON-CONFIRMATION:** Industrials are making new highs, but Transports are failing. This is a major warning signal."
        
    fig.add_trace(go.Scatter(x=t, y=djia, mode='lines', name='Industrials', line=dict(color='blue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=t, y=djta, mode='lines', name='Transports', line=dict(color='orange')), row=2, col=1)
    
    st.plotly_chart(fig, use_container_width=True)
    st.success(msg)

with tab6:
    st.subheader("Volume Must Confirm the Trend", divider=True)
    st.markdown("""
    Volume is the secondary indicator. Dow believed volume should expand in the direction of the major trend.\n
    
    * **Bullish Confirmation:** Volume expands as price moves up, and dries up when price pulls back.\n
    * **Bearish Confirmation:** Volume contracts in the direction of the trend.\n
    If prices rise to a new high but volume is lower than on the previous rally, the trend is running out of fuel.
    """)
    st.error("**Basically!** Volume is the Polygraph Test. It tells us if the price move is true or fake.")
    st.divider()
    
    trend_type = st.radio("Simulate Scenario:", ["Healthy Uptrend", "Weak Uptrend (Divergence)"])
    
    days = 100
    t = np.arange(days)
    
    # Create a zigzag price pattern (Uptrend)
    price = 100 + t + 5 * np.sin(t * 0.2)
    
    # Calculate Volume
    if trend_type == "Healthy Uptrend":
        vol = generate_volume_trend(price, trend_direction=1)
        msg = "✅ **Healthy:** Volume expands as price moves up, and dries up when price pulls back."
    else:
        # Weak Uptrend: Volume decreases as price goes up
        vol = np.linspace(2000, 500, days) + np.random.normal(0, 100, days)
        msg = "⚠️ **Weak/Divergence:** Price is rising, but Volume is dropping. Smart money is not participating. Danger of reversal."

    # Plotting Price and Volume
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[0.7, 0.3])
    
    # Price Trace
    fig.add_trace(go.Scatter(x=t, y=price, mode='lines', name='Price', line=dict(color='yellow')), row=1, col=1)
    
    # Volume Trace (Color code bars)
    colors = ['green' if price[i] >= price[i-1] else 'red' for i in range(len(price))]
    fig.add_trace(go.Bar(x=t, y=vol, name='Volume', marker_color=colors), row=2, col=1)
    
    fig.update_layout(height=500, title=f"Volume Analysis: {trend_type}", showlegend=False)
    
    st.plotly_chart(fig, use_container_width=True)
    st.info(msg)

with tab7:
    st.subheader("A Trend Is Assumed to Be in Effect Until It Gives a Definite Signal of Reversal", divider=True)

    st.info("This is the application of Newton's Law of Motion to finance: A trend in motion continues in motion.")
    st.markdown("""A common mistake is trying to pick the "top" or "bottom" of a market prematurely. Dow Theory dictates that you must assume the current trend is still valid until the weight of evidence—specifically price breaking a previous significant low (in an uptrend) or high (in a downtrend)—proves otherwise. The technician does not predict the reversal; they identify it after it has begun.""")

    # Create price pattern showing reversal
    price_pattern = [
        10, 12, 11, 14, 13, 16, 15, 19, 17, 22,
        18,
        20,
        19, 17, 15, 14, 12, 10, 8]
    t = np.arange(len(price_pattern))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=price_pattern, mode='lines+markers', line=dict(color='orange')))
        
    fig.add_annotation(x=9, y=22, text="Highest High", showarrow=True, arrowhead=1)
    fig.add_annotation(x=10, y=18, text="Key Support (Low)", showarrow=True, arrowhead=1, ay=40)
    fig.add_annotation(x=12, y=20, text="Lower High (Failure)", showarrow=True, arrowhead=1)
    fig.add_annotation(x=13, y=17, text="Break of Structure!", showarrow=True, arrowhead=1, ay=40, ax=40, font=dict(color="red", size=14))
        
    # Add Support Line
    fig.add_shape(type="line", x0=9, y0=18, x1=14, y1=18, line=dict(color="green", dash="dash"))
        
    fig.update_layout(title="Anatomy of a Reversal (Failure Swing)", height=500, xaxis_title="Time", yaxis_title="Price")
    st.plotly_chart(fig, use_container_width=True)
        
    st.error("The trend is technically UP until the price breaks that red dashed line (The previous Low).")