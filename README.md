# Video Summarizer #

This repository contains a Streamlit-based web application that summarizes YouTube videos using OpenAI’s language model. The application extracts the transcript of a YouTube video and generates a concise summary.

## Features ##

- URL Input: Users can input a YouTube video URL.
- Transcript Extraction: The application fetches the video transcript using the youtube_transcript_api.
- Summary Generation: Utilizes OpenAI’s language model to generate a 100-word summary of the video.
- Thumbnail Display: Shows the video thumbnail.
- Progress Bar: Displays a progress bar while generating the summary.
- Full Transcript Option: Users can view the entire transcript if desired.

## Installation ##

#### 1. Clone the repository: ####
```bash
git clone https://github.com/yourusername/video-summarizer.git
cd video-summarizer
```

#### 2. Install the required packages: ####
```bash
pip install -r requirements.txt

```

#### 3. Set up environment variables: ####

* Create a `.env` file and add your OpenAI API key:
```Python
OPENAI_API_KEY=your_openai_api_key

```

## Usage ##
1.**Run the Streamlit app**:
```Python
streamlit run app.py

```

2.**Enter the YouTube video URL** in the input box.

3.**View the summary** and other details such as the video thumbnail and full transcript.

## Libraries ##
```Python

import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as yta
from dotenv import load_dotenv
from openai import OpenAI
import time
```

- `streamlit`: For creating the web application.
- `youtube_transcript_api`: To fetch the transcript of YouTube videos.
- `dotenv`: To load environment variables.
- `openai`: To interact with OpenAI’s API.
- `time`: For adding delays (used in the progress bar).

## Experience ##

Initially thought it was a tough project but it was managable and also a fun one
