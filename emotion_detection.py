import requests

WATSON_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze: str) -> dict:
    """
    Sends text to the Watson NLP EmotionPredict API and returns the emotion scores.
    Returns a dictionary with emotions or an error message.
    """

    if not text_to_analyze or not text_to_analyze.strip():
        return {"error": "No text provided"}

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(WATSON_URL, headers=HEADERS, json=payload, timeout=10)

        if response.status_code != 200:
            return {"error": f"Watson API returned status {response.status_code}"}

        data = response.json()

        # Extract the emotion scores from the response
        emotions = data.get("emotionPredictions", [{}])[0].get("emotion", {})

        return emotions

    except requests.exceptions.Timeout:
        return {"error": "Request to Watson API timed out"}

    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
