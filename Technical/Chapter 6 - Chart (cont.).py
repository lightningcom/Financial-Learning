import streamlit as st


st.subheader("The Optical Illusion: Arithmetic vs. Logarithmic Scales", divider=True)
st.write("""
This is the most common mistake new traders make, and it usually leads to bad analysis. They look at a chart of Amazon or Apple from 1997 to 2024. On a standard setting, it looks like a completely flat line for 20 years and then suddenly a vertical wall in the last five years. \n
That’s because they are using the wrong scale. They are looking at dollars, not growth. \n

**Arithmetic Scale (Linear)** \n
* **The Logic:** Every dollar is equal. The physical distance on the screen from 10 to 20 is exactly the same as the distance from 100 to 110. \n
* **The Flaw:** This ignores the reality of percentage growth.  
Going from 10 to 20 is a 100% gain. That is a massive doubling of wealth.  
Going from 100 to 110 is only a 10% gain. It's a nice move, but it's not a life-changer.

* **The Result:** On a long-term chart, the linear scale makes the early moves (which actually made people rich) look tiny and irrelevant, while recent moves look scary, volatile, and unsustainable. It distorts your perception of history.

**Logarithmic Scale (Log)** 
* **The Logic:** Every percentage is equal. The physical distance on the screen from 10 to 20 is exactly the same as the distance from 100 to 110. 
* **The Vibe:** This is how money actually works. Compound interest is exponential, not linear. It respects the "Rule of 72."

* **The Rule:**  
**Day Trading:** Use Arithmetic (Linear). You care about the dollar moves for quick scalps.  
**Trend Trading / Investing:** Use Logarithmic. You care about the percentage growth over time.

Go look at a Bitcoin chart. On a Linear scale, the 2017 bull run to 20,000 looks like a tiny, insignificant blip compared to the 2021 run to 69,000. But if you switch to Log scale, you see the truth: the 2017 run was actually more explosive in percentage terms than 2021. The Log scale reveals the true momentum.
""")