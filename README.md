
# Blog Generator from Text, Audio, and Image Inputs using Google Gemini Flash

This project allows users to input an audio file, an image, and text prompts to generate a blog. It leverages Google Gemini Flash along with other Google Cloud services for speech and image recognition to transform multimedia into well-structured blog content.

## Features
- **Text Input (Required)**: Users can add additional textual prompts for personalized blog creation.
- **Audio Input (Optional)**: Converts speech from an audio file into text using Google Speech-to-Text.
- **Image Input (Optional)**: Recognizes objects or scenes from an image using Google Vision API.
- **Blog Generation**: Synthesizes a blog based on the audio, image, and text inputs.

## Project Structure
```bash
├── src/
│   ├── app.py                    # Main application file using Streamlit
│   ├── google_image_recognition.py # Handles image recognition using Google Vision API
│   ├── google_speech_recognition.py # Converts speech to text using Google Speech API
│   ├── google_api_platform.py     # Utility functions for interacting with Google APIs
│   ├── styles.py                  # Contains styles for blog formatting
├── assets/
│   ├── desk-chair-study-env.jpg   # Sample image for testing
│   ├── public-speaking-audio.mp3  # Sample audio for testing
```

## Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.10+
- Google Cloud SDK with proper credentials set up for the Vision and Speech APIs

You will also need to enable the following Google Cloud services:
- [Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text)
- [Google Cloud Vision API](https://cloud.google.com/vision)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/voice-to-content.git
   cd voice-to-content
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Lint the code** (optional but recommended):
   ```bash
   pylint src/*.py
   ```

## Running the Application

To run the application, execute the following command:
```bash
streamlit run src/app.py
```

This will start a local Streamlit server where you can upload audio, image, and text inputs to generate your blog.

## Usage

1. Enter User prompt in the text field.
2. Upload an audio file if needed (e.g., `public-speaking-audio.mp3`).
3. Upload an image file if needed (e.g., `desk-chair-study-env.jpg`).
4. Click the "Generate Blog" button.

The application will process the inputs and generate a blog in real-time, displaying it on the web interface.

## Google Cloud Setup

Ensure you have a Google Cloud project set up with the necessary API keys and credentials for using the Speech and Vision APIs. The file `google_api_platform.py` handles the authentication and interaction with the APIs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



