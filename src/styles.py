"""
This module contains functions to load CSS styling for the Streamlit app.
"""

def load_css():
    """
    :return: css styling
    """
    css = """
    <style>
    .editable-box {
        background-color: #f0f0f0;
        border: 2px solid #cccccc;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """
    return css
