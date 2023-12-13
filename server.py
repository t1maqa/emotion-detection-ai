""" Import Flask, render_template, request from the flask pramework package """
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """ This function analyzes given text and outputs its emotion """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is not None:
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']

        # Display the response in the desired format
        response_message = (
            f"For the given statement, the system response is "
            f"'anger':{anger},'disgust':{disgust},'fear':{fear},'joy':{joy},and'sadness':{sadness}."
            f"The dominant emotion is {dominant_emotion}."
        )

        return response_message

    return "Invalid text! Please try again."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
