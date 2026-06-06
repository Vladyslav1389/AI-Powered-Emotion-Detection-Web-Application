from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion_detector():
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    str_response = (f"For the given statement, the system response is")
    counter = 0
    for key, value in response.items():
        if counter == len(response) - 2:
            str_response += f" and '{key}': {value}."
            break
        else:
            str_response += f" '{key}': {value},"
            counter += 1
    str_response += f" The dominant emotion is {response['dominant_emotion']}."

    return str_response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)