import plotly.express as px
import plotly.graph_objects as go
from collections import Counter


def sentiment_chart(sentiments):

    counts=Counter(sentiments)

    fig=px.pie(

        names=list(counts.keys()),

        values=list(counts.values()),

        hole=0.4,

        title="Sentiment Distribution",

        color=list(counts.keys()),

        color_discrete_map={

            "POSITIVE":"#00ff9c",

            "NEGATIVE":"#ff4b4b"

        }

    )

    fig.update_layout(template="plotly_dark")

    return fig


def gauge_chart(conf):

    fig=go.Figure(go.Indicator(

        mode="gauge+number",

        value=conf,

        title={'text':"Average Confidence"},

        gauge={'axis':{'range':[0,1]}}

    ))

    fig.update_layout(template="plotly_dark")

    return fig


def scatter_chart(df):

    df=df.copy()

    df["Sentiment_num"]=df["Sentiment"].apply(

        lambda x:1 if x=="POSITIVE" else -1

    )

    fig=px.scatter_3d(

        df,

        x=df.index,

        y="Confidence",

        z="Sentiment_num",

        color="Sentiment",

        title="Customer Feedback Analysis"

    )

    fig.update_layout(template="plotly_dark")

    return fig