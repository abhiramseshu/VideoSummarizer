import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as yta
from dotenv import load_dotenv
from openai import OpenAI
import time
load_dotenv()
client = OpenAI()
st.set_page_config(
    page_title="Self Gpt",
    page_icon="📈"
)

def get_summary(transcript):
    summary=client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages=[
            {'role':'journalist','content':'you are a journalist'},
            {"role" : "assistant","content" :"write a 100 word summary for the video"},
            {"role" : "user","content" :transcript}
        ]
    )
    return summary

st.header('Video Summarizer')
url = st.text_input("Enter Video Url")

video_id = url.replace('https://www.youtube.com/watch?v=','')
if video_id:
    st.write('The video id is  ',video_id)
    output = yta.get_transcript(video_id)
    iurl='https://img.youtube.com/vi/'+video_id+'/maxresdefault.jpg'
    st.image(iurl,"Thumbnail")
    transcript=''
    for x in output:
        temp = x['text']
        transcript+=f'{temp}\n'
    #progress bar
    st.subheader('Summary :')
    st.write(get_summary(transcript))
    p=st.progress(0)
    for i in range(100):
        p.progress(i+1)
        time.sleep(0.05)
    al=st.checkbox("Want to view the whole transcript??")
    if al:
        st.write(transcript)
