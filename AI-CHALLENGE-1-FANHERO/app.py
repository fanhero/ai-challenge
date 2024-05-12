from flask import Flask, request, jsonify
import dotenv, os, openai

app = Flask(__name__)

dotenv.load_dotenv()

openai.api_key = os.getenv('API_KEY', None)

def analyze_sentiment(text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f'Respond in a single word, being positive, negative, or neutral the sentiment contained in the following text: {text}',
        max_tokens=25,
        stop= None
    )
    sentiment = response.choices[0].text.strip().lower()
    return sentiment

@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'Authorization token is missing'}), 401
    
    if request.headers['Authorization'] != f'Bearer {openai.api_key}':
        return jsonify({'error': 'Invalid Authorization token'}), 401

    if not request.json or 'prompt' not in request.json:
        return jsonify({'error': 'Request must be in JSON format and include a "prompt" field'}), 400

    prompt = request.json['prompt']
    sentiment = analyze_sentiment(prompt)

    return jsonify({'prompt': prompt, 'sentiment': sentiment.capitalize()})


if __name__ == '__main__':
    app.run(debug=True)