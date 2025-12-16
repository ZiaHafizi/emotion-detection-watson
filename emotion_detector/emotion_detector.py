def emotion_detector(text_to_analyze):
    """
    Returns a mock emotion detection output
    without connecting to any API.
    """

    if not text_to_analyze:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Mock output
    return {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.9,
        "sadness": 0.1,
        "dominant_emotion": "joy"
    }
