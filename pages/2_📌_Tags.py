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

def get_tags(transcript):
    tgs=client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages=[
            {'role':'journalist','content':'you are a journalist'},
            {"role" : "assistant","content" :"given a list of tags for the blog post in the format [item 1, item 2, item 3]"},
            {"role" : "user","content" :transcript}
        ]
    )
    return tgs

st.header('Tagger')
url = st.text_input("Enter Video Url")

video_id = url.replace('https://www.youtube.com/watch?v=','')
if video_id:
    st.write('The video id is  ',video_id)
    output = yta.get_transcript(video_id)
    transcript=''
    for x in output:
        temp = x['text']
        transcript+=f'{temp}\n'
    #progress bar
    iurl='https://img.youtube.com/vi/'+video_id+'/maxresdefault.jpg'
    st.image(iurl,"Thumbnail")
    st.subheader('The Tags are')
    st.write(get_tags(transcript))
st.write('\n')
ri= st.checkbox("Wanna take a photo")
if ri:
    photo= st.camera_input("Smile 📸")