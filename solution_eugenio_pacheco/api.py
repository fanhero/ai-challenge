# Dependencies
from flask import Flask, request, jsonify, current_app
from joblib import load
import tensorflow as tf
import traceback
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import jwt
from functools import wraps
import sys
import os
import dotenv
import openai

# Your API definition
app = Flask(__name__)

dotenv.load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

def preprocess_text(text):
    text = re.sub(r"https?://\S+|www\.\S+"," ",text)
    text = re.sub(r"<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});"," ",text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\w*\d\w*", " ", text)
    text = re.sub(r"[0-9]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            data=jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user=data['user_id']
            if current_user is None:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return {
                "message": "Invalid data!",
                "data": None,
                "error": "Bad Request"
            }, 400
        if data['email'] == 'admin@admin.com' and data['password'] == 'admin':
            try:
                token = jwt.encode({"user_id": data["email"]}, current_app.config["SECRET_KEY"], algorithm="HS256")
                return {
                    "message": "Login successful!",
                    "data": token,
                    "error": None
                }, 200
            except Exception as e:
                return {
                    "message": "Something went wrong",
                    "data": None,
                    "error": str(e)
                }, 500
    except:
        return {
            "message": "Something went wrong",
            "data": None,
            "error": "Internal Server Error"
        }, 500

@app.route('/sentiment-analysis', methods=['POST'])
@token_required
def sentiment_analysis(current_user):
    if model and vectorizer:
        try:
            json_ = request.json
            prediction = model.predict(vectorizer.transform(pd.Series(preprocess_text(json_['prompt']))))
            
            if prediction[0][1] > 0.5:
                prediction_response = 'Positive'
            else:
                prediction_response = 'Negative'
            return jsonify({
                'prompt': json_['prompt'],
                'prediction': prediction_response,
            })

        except:
            return jsonify({'trace': traceback.format_exc()})


@app.route('/image-generation', methods=['POST'])
@token_required
def image_generation(current_user):
    if openai.api_key:
        try:
            json_ = request.json
            response = openai.OpenAI().images.generate(
                model="dall-e-2",
                prompt=json_['prompt'],
                size="256x256",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url
            return jsonify({
                'prompt': json_['prompt'],
                'image_url': image_url,
            })

        except:
            return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = 5000

    vectorizer = load("vectorizer.joblib")
    model = tf.keras.models.load_model('model.keras')
    print ('Models loaded')

    app.run(port=port, debug=True)