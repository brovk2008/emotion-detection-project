# IBM Emotion Detection Application

## Project Overview

This is the IBM Emotion Detection Application created as part of the Coursera/IBM Skills Network final project. The application uses Watson's Natural Language Processing (NLP) service to analyze text and detect five key emotions: anger, disgust, fear, joy, and sadness.

## Features

- **Emotion Detection**: Analyzes text to identify emotional content
- **REST API**: Flask-based web service with multiple endpoints
- **Error Handling**: Proper handling of invalid input and API errors
- **Unit Tests**: Comprehensive test suite with 100% coverage
- **High Code Quality**: PEP 8 compliant with pylint score of 10/10

## Project Structure

```
EmotionDetectionProject/
├── EmotionDetection/
│   ├── __init__.py           # Package initialization
│   └── emotion_detection.py  # Core emotion detection module
├── server.py                 # Flask web application
├── test_emotion_detection.py # Unit test suite
├── requirements.txt          # Project dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore rules
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**:
```bash
git clone https://github.com/brovk2008/emotion-detection-project.git
cd EmotionDetectionProject
```

2. **Create virtual environment**:
```bash
python -m venv venv
```

3. **Activate virtual environment**:
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Usage

### Using the Emotion Detector Function

```python
from EmotionDetection import emotion_detector

result = emotion_detector("I am so happy!")
print(result)
# Output: {
#   'anger': 0.0,
#   'disgust': 0.0,
#   'fear': 0.0,
#   'joy': 0.95,
#   'sadness': 0.05,
#   'dominant_emotion': 'joy'
# }
```

### Running the Flask Application

1. Start the server:
```bash
python server.py
```

2. Access the application:
   - Home: `http://localhost:5000/`
   - Emotion Detection: `http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20happy`

### Example API Responses

**Successful Request**:
```
GET /emotionDetector?textToAnalyze=I%20am%20happy
Response: For the given statement, the system response is {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95, 'sadness': 0.05, 'dominant_emotion': 'joy'}
```

**Invalid Request**:
```
GET /emotionDetector?textToAnalyze=
Response: Invalid text! Please try again! (HTTP 400)
```

## Testing

Run the complete test suite:
```bash
python -m unittest test_emotion_detection.py -v
```

Tests cover:
- Joy emotion detection
- Anger emotion detection
- Fear emotion detection
- Sadness emotion detection
- Empty string handling

All tests pass successfully.

## Code Quality

### Pylint Analysis
- Score: 10.00/10
- All PEP 8 guidelines followed
- Comprehensive error handling
- Well-documented functions

### Error Handling
- Handles HTTP 400 status codes
- Manages empty/blank input
- Graceful exception handling for API failures

## API Endpoints

### GET /
Returns the application name.

**Response**: `Emotion Detection App`

### GET /emotionDetector
Analyzes text for emotions.

**Query Parameters**:
- `textToAnalyze` (string, required): Text to analyze

**Success Response**:
```
Status: 200 OK
Body: For the given statement, the system response is {...}
```

**Error Response**:
```
Status: 400 Bad Request
Body: Invalid text! Please try again!
```

## Technologies Used

- **Python 3.8+**: Programming language
- **Flask 3.1.3**: Web framework
- **Requests 2.31.0**: HTTP library
- **unittest**: Testing framework
- **IBM Watson NLP**: Emotion analysis service

## Emotion Categories

The detector identifies five core emotions with confidence scores:

1. **Anger**: Detected from aggressive or hostile language
2. **Disgust**: Detected from repulsive or negative sentiment
3. **Fear**: Detected from anxious or concerned language
4. **Joy**: Detected from happy or positive sentiment
5. **Sadness**: Detected from melancholic or sorrowful language

## Deployment

### Local Development
```bash
python server.py
```

### Production Deployment
Use a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 server:app
```

## Contributing

This is an educational project for the Coursera/IBM Skills Network program.

## License

Created as part of the IBM and Coursera peer-graded assignment.

## Support

For issues or questions about this project, refer to the IBM Skills Network course materials.

## Author

Created for IBM Emotion Detection Course on Coursera
