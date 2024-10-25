from app import app
from flask import request, render_template

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get_emotion", methods=["POST"])
def get_emotion():
    image_value = request.form['image_value']
    
    emotion_messages = {
        "happy": "It's great to see you happy! Keep it up!",
        "loved": "It's wonderful to know you feel loved!",
        "amazing": "Good to know you're feeling amazing!",
        "sad": "It seems you're going through a tough time. Remember, better days are ahead, and you're not alone in this!",
        "angry": "We understand that you might be feeling frustrated. Don't worry, everything will be okay, and you'll find a solution!"
    }

    text = emotion_messages.get(image_value)
        
    return render_template('show_emotion.html', value=text, image_value=image_value)