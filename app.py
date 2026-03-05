import streamlit as st
import pandas as pd
import os
from gtts import gTTS

from sentiment_model import predict_sentiment, explain_sentiment
from analytics import sentiment_chart, gauge_chart, scatter_chart
from utils import generate_wordcloud


# ---------------------------
# Page Config
# ---------------------------

st.set_page_config(
    page_title="AI Customer Sentiment Analyzer",
    layout="wide"
)


# ---------------------------
# Custom CSS
# ---------------------------

st.markdown("""
<style>

body {
background: radial-gradient(circle,#0f0c29,#302b63,#24243e);
color:white;
}

.stButton>button{
background: linear-gradient(90deg,#ff00cc,#3333ff);
color:white;
border-radius:12px;
height:50px;
width:220px;
font-size:18px;
font-weight:bold;
box-shadow:0px 0 20px #ff00cc;
}

</style>
""",unsafe_allow_html=True)


# ---------------------------
# Title
# ---------------------------

st.markdown(
"<h1 style='text-align:center;color:#00ffcc'>AI Customer Sentiment Analyzer</h1>",
unsafe_allow_html=True
)


CSV_FILE="feedback_history.csv"


# ---------------------------
# Session State
# ---------------------------

if "history" not in st.session_state:

    st.session_state.history=[]

    if os.path.exists(CSV_FILE):

        df=pd.read_csv(CSV_FILE)

        st.session_state.history=df.values.tolist()


# ---------------------------
# Save History
# ---------------------------

def save_history(text,label,score):

    df=pd.DataFrame(
        [[text,label,score]],
        columns=["Text","Sentiment","Confidence"]
    )

    if os.path.exists(CSV_FILE):

        df.to_csv(CSV_FILE,mode="a",header=False,index=False)

    else:

        df.to_csv(CSV_FILE,index=False)


# ---------------------------
# Voice Feedback
# ---------------------------

def speak_text(text):

    try:

        tts=gTTS(text=text,lang="en")

        file="voice.mp3"

        tts.save(file)

        st.audio(file)

    except:
        pass


# ---------------------------
# Sidebar History
# ---------------------------

st.sidebar.header("Recent Feedback")

if os.path.exists(CSV_FILE):

    df_history=pd.read_csv(CSV_FILE)

    st.sidebar.dataframe(df_history.tail(10))

else:

    st.sidebar.write("No data")


if st.sidebar.button("Clear History"):

    if os.path.exists(CSV_FILE):

        os.remove(CSV_FILE)

    st.session_state.history=[]

    st.rerun()


# ---------------------------
# CSV Upload
# ---------------------------

uploaded=st.file_uploader("Upload CSV",type=["csv"])

if uploaded:

    df=pd.read_csv(uploaded)

    column=st.selectbox("Select text column",df.columns)

    if st.button("Analyze CSV"):

        for text in df[column]:

            label,score=predict_sentiment(str(text))

            st.session_state.history.append((text,label,score))

            save_history(text,label,score)

        st.success("CSV Analysis Completed")


# ---------------------------
# Input
# ---------------------------

user_text=st.text_area("Enter Customer Feedback")


# ---------------------------
# Analyze
# ---------------------------

if st.button("Analyze Sentiment"):

    text=user_text.strip()

    if text=="":

        st.warning("Please enter feedback")

        st.stop()

    label,score=predict_sentiment(text)

    st.session_state.history.append((text,label,score))

    save_history(text,label,score)


    # Emoji

    if label=="POSITIVE":
        emoji="😊"
        color="#00ff9c"

    else:
        emoji="😡"
        color="#ff4b4b"


    # Result Card

    st.markdown(f"""

    <div style='
    padding:30px;
    border-radius:20px;
    background:rgba(255,255,255,0.05);
    text-align:center;
    border:2px solid {color};
    box-shadow:0 0 20px {color}'>

    <h1 style="color:{color}">{emoji} {label.title()} Sentiment</h1>

    <h3>Confidence {score:.3f}</h3>

    </div>

    """,unsafe_allow_html=True)


    speak_text(f"The sentiment detected is {label}. Confidence score is {score:.2f}")


    explanation=explain_sentiment(text,label)

    st.markdown("### AI Explanation")

    st.info(explanation)


# ---------------------------
# Charts
# ---------------------------

if st.session_state.history:

    df=pd.DataFrame(

        st.session_state.history,

        columns=["Text","Sentiment","Confidence"]

    )


    col1,col2=st.columns(2)


    with col1:

        st.plotly_chart(

            sentiment_chart(df["Sentiment"]),

            use_container_width=True

        )


    with col2:

        st.plotly_chart(

            gauge_chart(df["Confidence"].mean()),

            use_container_width=True

        )


    st.plotly_chart(

        scatter_chart(df),

        use_container_width=True

    )


    st.pyplot(

        generate_wordcloud(df["Text"])

    )


# ---------------------------
# AI Insights
# ---------------------------

if st.session_state.history:

    df=pd.DataFrame(

        st.session_state.history,

        columns=["Text","Sentiment","Confidence"]

    )


    pos=len(df[df.Sentiment=="POSITIVE"])

    neg=len(df[df.Sentiment=="NEGATIVE"])

    total=len(df)

    avg=df.Confidence.mean()


    st.markdown(f"""

### AI Insights

Total Feedback: **{total}**

Positive Feedback: **{pos}**

Negative Feedback: **{neg}**

Average Confidence: **{avg:.2f}**

""")