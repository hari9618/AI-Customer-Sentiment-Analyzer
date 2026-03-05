from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


def generate_wordcloud(texts):

    texts=[str(t) for t in texts if pd.notna(t)]

    if len(texts)==0:

        fig,ax=plt.subplots(figsize=(10,5))

        ax.text(0.5,0.5,"No Feedback Data",ha="center",va="center",fontsize=20)

        ax.axis("off")

        return fig


    text=" ".join(texts)


    extra_words={"product","service","order","delivery"}

    stopwords=STOPWORDS.union(extra_words)


    wordcloud=WordCloud(

        width=1200,

        height=500,

        background_color="black",

        colormap="plasma",

        stopwords=stopwords,

        max_words=120

    ).generate(text)


    fig,ax=plt.subplots(figsize=(12,6))

    ax.imshow(wordcloud,interpolation="bilinear")

    ax.axis("off")

    plt.tight_layout()

    return fig