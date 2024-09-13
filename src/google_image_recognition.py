"""
This code uses the Google Cloud Vision API to extract labels from an image and
then uses a language model to generate a descriptive text for the image based on those labels.
Step 1: get_image_labels
Step 2: generate_image_description

"""
from google.cloud import vision

from google_api_platform import generate_description_from_labels


def get_image_labels(image_path):
    """
    :param image_path:
    :return: image labels
    """
    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image) # pylint: disable=no-member

    labels = response.label_annotations
    return [label.description for label in labels]

def generate_image_description(image_path):
    """
    :param image_path:
    :return: image description
    """
    labels = get_image_labels(image_path)

    if not labels:
        return "No descriptive information found for the image."

    # Step 2: Generate a description using the language model
    description = generate_description_from_labels(labels)
    return description
