"""Emotion detection module using IBM Watson API."""
import requests


def emotion_detector(text_to_analyze):
    """
    Analyze text and return emotion predictions from IBM Watson.

    Args:
        text_to_analyze (str): Text to analyze for emotions.

    Returns:
        dict: Dictionary with emotion scores and dominant emotion.
              Returns None values on error.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        response.raise_for_status()
        response_data = response.json()

        # Extract emotion scores from the response
        emotions = response_data.get("emotionPredictions", [{}])[0].get("emotion", {})

        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get) if emotions else None

        return {
            "anger": emotions.get("anger"),
            "disgust": emotions.get("disgust"),
            "fear": emotions.get("fear"),
            "joy": emotions.get("joy"),
            "sadness": emotions.get("sadness"),
            "dominant_emotion": dominant_emotion
        }
    except requests.RequestException:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
