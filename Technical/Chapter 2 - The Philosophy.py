import streamlit as st

st.title("The Philosophy: The Three Pillars")

st.write("""
If you want to be a technical analyst, you have to buy into a specific philosophy. There are three core assumptions that act as the "pillars" holding up everything we do. \n""" , unsafe_allow_html=True)
st.subheader("**Pillar 1 - Price Discounts Everything**", divider=True)
st.write("""This is the big one. The "Efficient Market" theory. \n
It implies that **the current price of a stock already reflects all known information about that stock**. \n
* **The Fundamental Analyst** (we’ll talk about them in a moment) worries about the company’s earnings report, the CEO’s scandal, the interest rates, and the supply chain issues in China. \n
* **The Technical Analyst** says: "I don't need to read the news reports. The price already knows." \n
Think of it this way: Imagine a company is about to announce bad news. Before the news is public, insiders might start selling. Then, analysts who crunch the numbers might start selling. The price starts to drop before the headline hits your news feed. \n
By the time you read "Company X Misses Earnings" on a news site, the price has usually already reacted. Technical analysts focus on the price chart because it acts as a leading indicator. We trust the chart more than the news.
""" , unsafe_allow_html=True)
st.subheader("**Pillar 2 - Price Moves in Trends**", divider=True)
st.write("""
Newton’s First Law of Motion states that an object in motion stays in motion unless acted upon by a force. Markets are the same. \n
Prices don't just jump around randomly like a grasshopper. They move in trends. \n
**If a stock is going up, it is more likely to keep going up than it is to suddenly turn around and crash.** \n
**Our entire job as analysts is to:** \n
* Spot the trend early (get on the train). \n
* Ride the trend (stay on the train). \n
* Spot when the trend is bending (get off the train before it crashes).
""" , unsafe_allow_html=True)
st.success("If markets were truly random (Random Walk Theory), technical analysis would be impossible. The goal of the technician is to identify the trend in its early stages and ride it until the weight of evidence suggests a reversal.")

st.subheader("**Pillar 3: History Repeats Itself**", divider=True)
st.write("""
Why? Because humans don't change. \n
We have charts going back hundreds of years. The technology has changed—we went from trading rice coupons in Japan in the 1700s to trading Bitcoin on iPhones today—but the brains pushing the buttons haven't changed. \n
People still panic when they lose money. People still get greedy when they make money. Because human psychology is constant, the patterns on the charts—like "Head and Shoulders" or "Double Tops"—appear over and over again. A chart pattern that signaled a crash in 1929 looks almost identical to a pattern that signaled a crash in 2008.
""" , unsafe_allow_html=True)
st.subheader("**The Great Debate: Fundamental vs. Technical Analysis**", divider=True)
st.write("""
You will often hear traders arguing about which method is better: Fundamental or Technical analysis. Let's settle this argument right now.\n
Imagine you are buying a house.\n

**The Fundamental Analyst** is like a home inspector. They look at the "health" of the house. They check the foundation, the roof, the plumbing, the school district, and the crime rate. They want to know the intrinsic value of the house. They ask: "Is this house worth the price?" \n
**The Technical Analyst** is like a real estate flipper. They don't care as much about the plumbing. They look at the sales data. They say: "Three other houses on this street sold for $500k last week, and prices in this neighborhood have been trending up for six months. There is a line of buyers out the door." They ask: "Will someone buy this house from me for a higher price?" \n
**Who is right? Well! They both are!** \n
* Fundamental Analysis tells you WHAT to buy (a strong, healthy company). \n
* Technical Analysis tells you WHEN to buy (when the market is trending up). \n

""" , unsafe_allow_html=True)

st.subheader("**Setting Expectations: The Random Walk Critic**", divider=True)
st.markdown("""
There is an academic theory called the Random Walk Hypothesis. It states that price movements are totally random and unpredictable, like a drunk person stumbling down the street. It argues that you cannot predict the next step based on the previous step.\n
If the Random Walk theory is 100% true, then this book is useless, and you should just buy an index fund and never look at it again.\n
**But here is why we disagree:** If markets were purely random, we wouldn't see the same geometric patterns appearing for 100 years. We wouldn't see prices bounce perfectly off specific "support" levels time and time again.\n
However, this leads to a very important warning: ***Technical Analysis is about Probability, not Certainty.***

""")
