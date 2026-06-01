# IBM Emotion Detection Application

## Project Description

This is an IBM Emotion Detection Application that uses the Watson Natural Language Processing (NLP) API to analyze emotions in text. The application detects five key emotions: anger, disgust, fear, joy, and sadness.

## Features

- Emotion detection from text using IBM Watson API
- REST API endpoints for emotion analysis
- Comprehensive unit tests
- PEP 8 compliant code
- Flask-based web application
- Error handling for invalid input

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/brovk2008/emotion-detection-project.git
cd emotion-detection-project
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Flask Application

1. Start the Flask server:
```bash
python server.py
```

2. The application will be available at `http://localhost:5000`

3. Test the emotion detector endpoint:
```bash
http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20happy
```

### Using the Emotion Detector Function

```python
from EmotionDetection.emotion_detection import emotion_detector

result = emotion_detector("I am so happy!")
print(result)
# Output: {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95, 'sadness': 0.0, 'dominant_emotion': 'joy'}
```

## Testing

Run the test suite:
```bash
python -m unittest test_emotion_detection.py -v
```

This will run all unit tests including:
- Joy emotion detection
- Anger emotion detection
- Fear emotion detection
- Sadness emotion detection
- Empty string handling

## Flask Deployment

### Local Development
```bash
python server.py
```

### Production Deployment

For production, use a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 server:app
```

## Code Quality

The project maintains PEP 8 compliance and high code quality standards:
- All functions include docstrings
- Error handling for API failures
- Input validation
- Comprehensive test coverage

## API Endpoints

### GET /
Returns: "Emotion Detection App"

### GET /emotionDetector?textToAnalyze=<text>
Returns emotion analysis for the provided text.

**Example Request:**
```
GET /emotionDetector?textToAnalyze=I%20am%20so%20happy
```

**Example Response (Success):**
```
For the given statement, the system response is {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95, 'sadness': 0.0, 'dominant_emotion': 'joy'}
```

**Example Response (Error):**
```
Invalid text! Please try again!
```

## License

This project is part of the IBM and Coursera peer-graded assignment.

## Author

Created as part of the IBM Emotion Detection Course on Coursera.
