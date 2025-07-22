import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re
import streamlit as st
import time

nltk.download('vader_lexicon')

from googleapiclient.discovery import build

api_key = 'AIzaSyA9Q5L1W-8avZACOi-7QKz1Ukgpqp8o9ns'
youtube = build('youtube', 'v3', developerKey=api_key)

def predict(video_id):
    
    sia=SentimentIntensityAnalyzer()
    request = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id,
        maxResults=100
    )

    comments = []
    while request is not None:
        response = request.execute()
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                'author': comment['authorDisplayName'],
                'text': comment['textDisplay'],
                'likes': comment['likeCount'],
                'published': comment['publishedAt'],
                'updated': comment['updatedAt']
            })
            if 'replies' in item.keys():
                for reply in item['replies']['comments']:
                    reply_text = reply['snippet']['textDisplay']
                    comments.append({
                        'author': reply['snippet']['authorDisplayName'],
                        'text': reply_text,
                        'likes': reply['snippet']['likeCount'],
                        'published': reply['snippet']['publishedAt'],
                        'updated': reply['snippet']['updatedAt']
                    })
        request = youtube.commentThreads().list_next(request, response)
    result=[]

    for i in comments:
        score=sia.polarity_scores(i['text'])
        if score['compound']>0:
            result.append('Positive')
        elif score['compound']<0:
            result.append('Negative')
        else:
            result.append('Neutral')

    total_results={
        'pos':result.count("Positive"),
        'neu':result.count('Neutral'),
        'neg':result.count('Negative')
    }
    plt.figure(figsize=(12,4))
    plt.bar(total_results.keys(),total_results.values(),color=['green','blue','red'])
    with st.spinner('Getting comments'):
        time.sleep(2)
    with st.spinner('Analysing all the comments'):
        time.sleep(2)
    with st.spinner('Preparing the Results'):
        time.sleep(2)
    st.pyplot(plt)
    positive_count = total_results.get("pos", 0)
    neutral_count = total_results.get("neu", 0)
    negative_count = total_results.get("neg", 0)
    
    if positive_count > negative_count:
        return "Positive Video"
    elif negative_count > positive_count:
        return "Negative Video"


st.title("Sentiment Analysis For YouTube Video")
url=st.text_input("Paste your YouTube link here")
if st.button("Predict"):
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([^&]+)',
        r'(?:https?:\/\/)?youtu\.be\/([^?&]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([^?&]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/v\/([^?&]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            link=match.group(1)
    st.subheader('Analysis')
    result=predict(link)
    if result=='Positive Video':
        st.success(result)
    elif result=='Negative Video':
        st.error(result)
    else:
        st.info(result)
