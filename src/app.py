"""
This is a Streamlit app that allows users to input a prompt,
upload an audio file (optional), and upload an image file (optional).
The app then generates a blog post based on the input and the uploaded media (if provided).
The generated blog is displayed in a text area
"""

import os
from io import BytesIO
import tempfile

import streamlit as st
from pydub import AudioSegment
from google_speech_recognition import audio_to_text
from google_api_platform import generate_blog_google
from google_image_recognition import generate_image_description
from styles import load_css

st.title("Voice-to-Blog Generator")

st.markdown(load_css(), unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

# Initialize session state
if 'blog_content' not in st.session_state:
    st.session_state['blog_content'] = ""
if 'audio_transcript' not in st.session_state:
    st.session_state['audio_transcript'] = ""
if 'alt_text' not in st.session_state:
    st.session_state['alt_text'] = ""

# Render text areas with session state values
with col1:
    st.text_area(
        "Image Description:",
        value=st.session_state['alt_text'],
        height=50,
        key="alt_text_display"
    )
    st.text_area(
        "Audio Transcription:",
        value=st.session_state['audio_transcript'],
        height=100,
        key="audio_transcript_display"
    )
    st.text_area(
        "Generated Blog (Editable):",
        value=st.session_state['blog_content'],
        height=350,
        key="blog_editor_display"
    )

# User input for prompt, audio, and image
with col2:
    prompt = st.text_input("Enter the Prompt *")
    audio_file = st.file_uploader("Upload Audio (Optional)", type=["wav", "mp3"])
    image_file = st.file_uploader("Upload Image (Optional)", type=["jpg", "png", "jpeg"])
    generate_blog = st.button("Generate Blog")


if generate_blog and prompt:
    # Process audio file if uploaded
    if audio_file:
        audio = AudioSegment.from_file(BytesIO(audio_file.read()))
        audio.export("temp.wav", format="wav")
        st.session_state['audio_transcript'] = audio_to_text("temp.wav")
    else:
        st.session_state['audio_transcript'] = ""

    # Process image file if uploaded
    if image_file:
        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=os.path.splitext(image_file.name)[1]
        )
        temp_file.write(image_file.read())
        temp_file.close()
        st.image(temp_file.name, caption="Uploaded Image", use_column_width=True)
        st.session_state['alt_text'] = generate_image_description(temp_file.name)
    else:
        st.session_state['alt_text'] = ""

    # Combine text for blog generation
    combined_text = (st.session_state['audio_transcript'] + " " + prompt).strip()
    blog = generate_blog_google(prompt, combined_text, st.session_state['alt_text'])

    # Update session state with the new blog content
    st.session_state['blog_content'] += "\n" + blog

elif generate_blog:
    st.write("Please enter a prompt to generate the blog.")
