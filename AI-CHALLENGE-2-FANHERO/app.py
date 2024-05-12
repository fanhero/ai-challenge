from flask import Flask, jsonify, request
import dotenv, os, openai

app = Flask(__name__)

dotenv.load_dotenv()

openai.api_key = os.getenv('API_KEY')

def generate_image(text):
    response = openai.Image.create(
        prompt=f'Generate an image corresponding to the description: {text}',
        n=1,
        size='256x256'
    )
    return response['data'][0]['url']

@app.route('/image-generation', methods=['POST'])
def image_generation():
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'Authorization token is missing'}), 401
    
    if request.headers['Authorization'] != f'Bearer {openai.api_key}':
        return jsonify({'error': 'Invalid Authorization token'}), 401

    if not request.json or 'prompt' not in request.json:
        return jsonify({'error': 'Request must be in JSON format and include a "prompt" field'}), 400

    prompt = request.json['prompt']
    image = generate_image(prompt)

    return jsonify({'prompt': prompt, 'image_url': image})

if __name__ == '__main__':
    app.run(debug=True, port=8080)