import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# --- Page Config ---
st.set_page_config(
    page_title="Dow Theory Interactive",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Helper Functions for Data Generation ---

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
    """
    Generates volume that confirms the trend:
    - High volume when price moves IN direction of trend.
    - Low volume when price moves AGAINST trend.
    """
    returns = np.diff(price, prepend=price[0])
    volume = np.abs(np.random.normal(1000, 200, len(price)))
    
    # Add volume spikes based on trend agreement
    for i in range(len(returns)):
        if trend_direction == 1: # Uptrend
            if returns[i] > 0: # Moving with trend
                volume[i] *= 1.5 # Expand volume
            else: # Pullback
                volume[i] *= 0.7 # Contract volume
        else: # Downtrend
            if returns[i] < 0: # Moving with trend
                volume[i] *= 1.5
            else: # Rally (against trend)
                volume[i] *= 0.7
                
    return volume

def identify_pivots(price, window=5):
    """Simple local extrema finder for Highs and Lows."""
    highs = []
    lows = []
    
    for i in range(window, len(price) - window):
        slice_data = price[i-window : i+window+1]
        if price[i] == max(slice_data):
            highs.append((i, price[i]))
        if price[i] == min(slice_data):
            lows.append((i, price[i]))
            
    return highs, lows

# --- Sidebar ---
st.sidebar.title("Dow Theory Explorer")
st.sidebar.markdown("Explore the 6 Tenets of Charles Dow's market theory.")
selection = st.sidebar.radio("Go to Module:", 
    ["1. The Three Movements", "2. Phases of the Market", "3. Volume Confirmation", "4. Trend Identification"])

st.sidebar.info(
    "**Tip:** Dow Theory is the ancestor of modern technical analysis, focusing on market psychology and trends."
)

# --- Main Content ---

st.title("📉 The Dow Theory Interactive Guide")

# --- MODULE 1: THE THREE MOVEMENTS ---
if selection == "1. The Three Movements":
    st.header("Tenet: The Market has Three Movements")
    st.markdown("""
    Dow compared the market to the ocean. Price action is a composite of three distinct movements occurring simultaneously:
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

# --- MODULE 2: PHASES OF THE MARKET ---
elif selection == "2. Phases of the Market":
    st.header("Tenet: Primary Trends have Three Phases")
    
    tab1, tab2 = st.tabs(["Bull Market Phases", "Bear Market Phases"])
    
    with tab1:
        st.markdown("### The Bull Market Cycle")
        st.markdown("""
        1.  **Accumulation:** Informed investors buy low. Market is quiet. "Smart Money" enters.
        2.  **Public Participation:** Trend becomes visible. Earnings improve. The crowd joins.
        3.  **Excess:** Euphoria. "Stocks only go up." Smart money sells to the public.
        """)
        
        # Generate a Bull Market Curve (Sigmoid-like)
        x = np.linspace(0, 10, 100)
        y = 1 / (1 + np.exp(-x + 5)) * 100  # Sigmoid
        y += np.random.normal(0, 1, 100) # Noise
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='green', width=3)))
        
        # Annotations
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

# --- MODULE 3: VOLUME CONFIRMATION ---
elif selection == "3. Volume Confirmation":
    st.header("Tenet: Volume Must Confirm the Trend")
    st.markdown("""
    **"Volume is the fuel."**
    * In an **Uptrend**, volume should increase on rallies and decrease on pullbacks.
    * In a **Downtrend**, volume should increase on declines and decrease on rallies.
    * If volume disagrees with price (Divergence), the trend is weak.
    """)
    
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
    fig.add_trace(go.Scatter(x=t, y=price, mode='lines', name='Price', line=dict(color='black')), row=1, col=1)
    
    # Volume Trace (Color code bars)
    colors = ['green' if price[i] >= price[i-1] else 'red' for i in range(len(price))]
    fig.add_trace(go.Bar(x=t, y=vol, name='Volume', marker_color=colors), row=2, col=1)
    
    fig.update_layout(height=500, title=f"Volume Analysis: {trend_type}", showlegend=False)
    
    st.plotly_chart(fig, use_container_width=True)
    st.info(msg)

# --- MODULE 4: TREND IDENTIFICATION ---
elif selection == "4. Trend Identification":
    st.header("Identifying Trends: Higher Highs & Lower Lows")
    st.markdown("Dow Theory defines an uptrend purely by price structure. Indicators are secondary.")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("""
        **The Rules:**
        * **Uptrend:** Series of Higher Highs (HH) and Higher Lows (HL).
        * **Downtrend:** Series of Lower Highs (LH) and Lower Lows (LL).
        * **Reversal:** When the pattern breaks (e.g., price makes a Lower Low in an uptrend).
        """)
        sensitivity = st.slider("Pivot Sensitivity (Window)", 2, 10, 5, help="How many days to look back/forward to define a peak.")
        
    with col2:
        # Generate random walk with a trend
        np.random.seed(10)
        rw = np.cumsum(np.random.normal(0.5, 1, 100)) + 100 # Slight upward bias
        
        # Identify Pivots
        highs, lows = identify_pivots(rw, window=sensitivity)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=np.arange(len(rw)), y=rw, mode='lines', name='Price', line=dict(color='gray')))
        
        # Plot Highs
        hx, hy = zip(*highs)
        fig.add_trace(go.Scatter(x=hx, y=hy, mode='markers', name='Highs', marker=dict(color='green', size=10, symbol='triangle-up')))
        
        # Plot Lows
        lx, ly = zip(*lows)
        fig.add_trace(go.Scatter(x=lx, y=ly, mode='markers', name='Lows', marker=dict(color='red', size=10, symbol='triangle-down')))
        
        # Logic to label HH/LH (Basic simulation)
        annotations = []
        for i in range(1, len(highs)):
            curr = highs[i]
            prev = highs[i-1]
            label = "HH" if curr[1] > prev[1] else "LH"
            annotations.append(dict(x=curr[0], y=curr[1], text=label, showarrow=False, yshift=15))
            
        for i in range(1, len(lows)):
            curr = lows[i]
            prev = lows[i-1]
            label = "HL" if curr[1] > prev[1] else "LL"
            annotations.append(dict(x=curr[0], y=curr[1], text=label, showarrow=False, yshift=-15))

        fig.update_layout(title="Automated Pivot Analysis", annotations=annotations, height=500)
        st.plotly_chart(fig, use_container_width=True)