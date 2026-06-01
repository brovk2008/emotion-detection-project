"""Flask application for emotion detection."""
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Return application name."""
    return "Emotion Detection App"


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Emotion detector endpoint.

    Query parameter: textToAnalyze
    Returns: Emotion analysis result or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    return f"For the given statement, the system response is {result}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
