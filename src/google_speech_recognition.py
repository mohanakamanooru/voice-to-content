"""
This script provides functionality to convert video files to text using speech recognition.
It uses the moviepy library to extract the audio from the video
file and the speech_recognition library

"""
import os

import moviepy.editor as mp
import speech_recognition as sr


def audio_to_text(audio_file):
    """
    :param audio_file:
    :return: audio transcript
    """
    recognizer = sr.Recognizer()
    audio = sr.AudioFile(audio_file)

    with audio as source:
        audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)

    return text


def video_to_text(video_file):
    """
    :param video_file:
    :return: transcript of video file
    """
    # Step 1: Extract audio from video
    video = mp.VideoFileClip(video_file)
    audio_file = "extracted_audio.wav"
    video.audio.write_audiofile(audio_file)

    transcript = audio_to_text(audio_file)
    # Optionally, clean up by deleting the temporary audio file
    os.remove(audio_file)

    return transcript
