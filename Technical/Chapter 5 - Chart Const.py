import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from numpy.random import default_rng as rng
import random as rand
def generate_dummy_data(days=100):
    """Generates dummy OHLC data for chart demonstrations."""
    np.random.seed(42)
    dates = pd.date_range(start="2024-01-01", periods=days)
    price = 100
    data = []
    
    for date in dates:
        change = np.random.normal(0, 1.5)
        open_p = price
        close_p = price + change
        high_p = max(open_p, close_p) + abs(np.random.normal(0, 0.5))
        low_p = min(open_p, close_p) - abs(np.random.normal(0, 0.5))
        
        data.append([date, open_p, high_p, low_p, close_p])
        price = close_p
        
    df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close'])
    return df
def plot_candlestick(df, title="Market Structure"):
    fig = go.Figure(data=[go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name="Price"
    )])
    fig.update_layout(
        title=title,
        yaxis_title='Price',
        xaxis_title='Date',
        template="plotly_dark",
        height=500
    )
    return fig

def plot_line(df, title="Line Chart View"):
    fig = go.Figure(data=[go.Scatter(
        x=df['Date'], 
        y=df['Close'], 
        mode='lines', 
        name='Close Price',
        line=dict(color='#00CC96', width=2)
    )])
    fig.update_layout(
        title=title,
        yaxis_title='Price',
        template="plotly_dark",
        height=500
    )
    return fig

st.title("The Interface (Chart Construction & Setup)")
st.markdown("""
Ok! Imaging trying to play **Call of Duty** or **Elder Ring** with your monitor turned off. Yo're mashing buttons, hoping for the best, but' you're flying blind.That is exactly what trading is like without a chart. You are just guessing based on vibes. \n
But here is the catch: not all screens are created equal. Just having a chart isn't enough. If your interface is cluttered, uses the wrong data, or is zoomed out too far, you might as well be blind. John Murphy wrote about "Bar Charts" and "Line Charts" back when people had to draw them by hand on graph paper at the end of the trading day. Today, you have a supercomputer in your pocket connected to the global financial mainframe. You have too much data. \n
Your job isn't just to look at a chart; it's to curate it. You need to set up your **Heads-Up Display (HUD)** to filter out the infinite noise and highlight the few signals that actually matter. This chapter isn't just about "how to draw a chart." It's about Data Visualization Strategy. \n
Your job isn't just to look at a chart; it's to curate it. You need to set up your Heads-Up Display (HUD) to filter out the infinite noise and highlight the few signals that actually matter. This chapter isn't just about "how to draw a chart." It's about **Data Visualization Strategy**.

""")

st.subheader("Types of Chart", divider=True)
st.write("""
***Picking your weapon of choice.***
""")
st.markdown("""
So, well, you do ask what is chart? \n
In **definitioin terms**, A chart is the fundamental working surface of the technical analyst, serving as a graphical interface that translates complex streams of market data into a comprehensible visual narrative. More than just a record of historical prices, it is a multidimensional map of supply and demand that captures the collective psychology of all market participants at any given moment. By plotting price against time, the chart acts as a lie detector for the market, filtering out the noise of news and rumors to reveal the true conviction of buyers and sellers. It provides the necessary context to identify trends, spot reversals, and manage risk, ultimately transforming raw statistics into actionable market intelligence.\n


Well, the charts are divided into basically 3 types : 
* **Time Based Chart** - Standard One
* **Price Based Chart** - Filter Noise
* **Volume Based Chart**
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Time Based Chart", "Price Based Chart", "Volume Based Chart"])

df = generate_dummy_data(100)

with tab1:
    st.subheader("Time Based Chart")
    st.write("""
    These plot price over fixed time intervals (e.g., Daily, Hourly).  \n
    Check around below tabs to discover more!
    """)
    tab_1, tab_2, tab_3, tab_4 = st.tabs(["Line Chart", "Bar Chart (OHLC)", "Candlestick Chart", "Heikin Ashi Chart"])
    
    with tab_1:
        st.write("""
        ***"TThe Big Picture Guy"*** \n
        
        Think of the line chart as the "executive summary" of the market. It cuts out all the noise and drama of the day and just tells you the bottom line: where the price ended up. It connects the closing prices with a single, clean line. It’s perfect when you want to step back and see the overall trend without getting a headache from too many details. It’s not great for timing a precise entry, but it’s fantastic for answering the question, "Is this thing generally going up or down?"
        """)
        st.plotly_chart(plot_line(df), use_container_width=True)

    with tab_2:
        st.write("""
        ***"The Blueprint"*** \n
        If the line chart is an executive summary, the bar chart is the engineer’s blueprint. It gives you the "Open, High, Low, and Close" (OHLC) for every single period. It’s rigid, mechanical, and gives you the cold, hard facts. You can see how volatile the day was (the height of the bar) and who won at the end of the day (the little notch on the right). It’s not pretty to look at, but purists love it because it doesn’t try to influence your emotions with colors.
        """)

    with tab_3:
        st.write("""
        ***"The Drama Queen"*** \n
        The absolute standard for modern trading. Like bar charts, they show the full OHLC data, but they use thick, color-coded "Bodies" to show the distance between the Open and Close.  
        Visual dominance. It turns raw data into an immediate story about momentum.

        * **Green (or White) Candle**: The Bulls won the round. The price closed higher than it opened. The buyers were in control.
        * **Red (or Black) Candle (Bearish)**: The Bears won. The price closed lower than it opened. The sellers pushed the market down.
        * **The Wicks (Shadows)**: These thin lines sticking out of the body are the most important part. They are the battle scars.

        * **Long Upper Wick**: It means the Bulls tried to push the price up to a new high, but the Bears slapped them back down. It screams "Rejection!"

        * **Long Lower Wick**: It means the Bears tried to crash the price, but the Bulls stepped in and bought the dip. It screams "Resilience!"

        **Why Candlesticks Win:**
        They turn a spreadsheet into a narrative. A line chart shows price going up. A candlestick chart might show price going up but struggling, leaving long upper wicks that signal the buyers are running out of ammo. That visual cue of "Exhaustion" is often the only warning you get before a reversal. We will deep dive into specific Candle patterns later—think of them as the Emoji language of the market.
                """)
        st.plotly_chart(plot_candlestick(df), use_container_width=True)
    
    with tab_4:
        st.write("The ***Autotune*** for Charts")
        st.markdown("""
        "Heikin-Ashi" means "Average Bar" in Japanese. It takes standard candlestick data and smooths it out using a formula. \n
        **It’s like putting noise-canceling headphones on your trading.**\n
        * In a normal candlestick chart, an uptrend might look like: Green, Green, Red, Green, Red, Green. It looks choppy.
       * In Heikin-Ashi, that same uptrend looks like: Green, Green, Green, Green, Green. It smooths out the red candles during an uptrend to keep you focused on the primary direction.
       **The Verdict:** Excellent for staying in a trend without getting shaken out by minor pullbacks. If the Heikin-Ashi candles are green with no lower wicks, you simply do not sell.
        """)


st.subheader("The Optical Illusion: Arithmetic vs. Logarithmic Scales", divider=True)
st.write("""
This is the most common mistake new traders make, and it usually leads to bad analysis. They look at a chart of Amazon or Apple from 1997 to 2024. On a standard setting, it looks like a completely flat line for 20 years and then suddenly a vertical wall in the last five years. \n
That’s because they are using the wrong scale. They are looking at dollars, not growth. \n

""")






