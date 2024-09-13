"""
This module provides functions to interact with the Google API for generating content
using the Vertex AI generative model.
"""

import json

import vertexai
from vertexai.generative_models import GenerativeModel

with open('credentials/config.json', 'r',encoding='utf-8') as file:
    config = json.load(file)

MODEL_ID = config["google-flash"]['modelId']
PROJECT_ID = config["google-flash"]['projectID']
LOCATION = config["google-flash"]['location']

vertexai.init(project=PROJECT_ID, location=LOCATION)


def generate_blog_google(prompt, audio_text, alt_text):
    """
    Generate a blog post based on a prompt, audio text, and alt text.
    Args:
        prompt (str): The prompt for the blog post.
        audio_text (str): The audio text for the blog post.
        alt_text (str): The alt text for the blog post.
    Returns:
        str: The generated blog post.
    """
    model = GenerativeModel(MODEL_ID)
    response = model.generate_content([prompt, audio_text, alt_text])
    # print(response.text)
    return response.text


def generate_description_from_labels(labels):
    """
    Generate a detailed description based on a list of labels.
    Args:
        labels (list): A list of strings representing the labels.
    Returns:
        str: The generated description.
    """
    model = GenerativeModel(MODEL_ID)
    labels_text = ", ".join(labels)
    response = model.generate_content(
        ["Generate a detailed alt text for an image that contains",
         labels_text]
    )
    # print(response.text)
    return response.text
