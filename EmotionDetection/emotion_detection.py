import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    json_response = json.loads(response.text)
    formatted_response = json_response["emotionPredictions"][0]["emotion"]

    anger_score = formatted_response["anger"]
    disgust_score = formatted_response["disgust"]
    fear_score = formatted_response["fear"]
    joy_score = formatted_response["joy"]
    sadness_score = formatted_response["sadness"]
    
    dominant_emotion = max(formatted_response, key=formatted_response.get)

    collected_dictionay = {'anger': anger_score,
                            'disgust': disgust_score,
                            'fear': fear_score,
                            'joy': joy_score,
                            'sadness': sadness_score,
                            'dominant_emotion': dominant_emotion}

    return collected_dictionay