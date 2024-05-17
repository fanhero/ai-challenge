## Gen AI Challenges

### Objective Challenge 1: Sentiment Analysis API

Construct a RESTful API that receives a text input (in English) and returns a sentiment analysis, indicating whether the general sentiment of the text is positive, neutral, or negative.

### Requirements

1. The API should expose a `POST /sentiment-analysis` endpoint that accepts JSON data with a `prompt` field.
2. The AI model for sentiment analysis should be pre-trained and capable of understanding nuances in natural language.
3. The API response should include:
   - The input text (prompt).
   - The categorized sentiment analysis.
4. The API should be secure and only accept authenticated requests (suggestion: use API tokens for access).

### Objective Challenge 2: Image Generation API

Develop a RESTful API that, given a descriptive text prompt, generates an image corresponding to the description using AI.

### Requirements

1. The API should expose a POST /image-generation endpoint that accepts JSON data with a prompt field.
2. Utilize a generative AI model capable of crafting images from text descriptions.
3. The API's response should include either a URL to the generated image or the image itself encoded in base64.
4. Ensure the API adequately handles requests and usage limits, potentially introducing a queuing system for resource-intensive requests.
5. Include authentication to ensure that only authorized users can request image generation.

### About
The API and the Sentiment Analysis AI model were developed using Python.

The Sentiment Analysis Model uses Tensorflow and Scikit-learn, and it was trained using part of the dataset at https://www.kaggle.com/datasets/kazanova/sentiment140.

The Image Generation API uses OpenAI API and needs an OpenAI API Key to work.

The Web API was created using Flask Framework.


### Installation Instructions
```bash
pip install -r requirements.txt
python app.py PORT
```

If no PORT is passed, the server will start on `http://localhost:5000`

### Secret Key and Open AI API Key
Rename .env.example to .env and include your Open AI API Key and a random string to serve as a secret key in token generation.

### Authentication Request

```json
POST /login
Content-Type: application/json

{
  "email": "admin@admin.com",
  "password": "admin"
}
```

### Authentication Response

```json
{
    "data": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW5AYWRtaW4uY29tIn0.EF8_q8ku-fMbKcQgKlGnprQqrgYAODEu72DzhPM43G8",
    "error": null,
    "message": "Login successful!"
}
```

### Sentiment Analysis API Example Request

```json
POST /sentiment-analysis
Content-Type: application/json
Authorization: Bearer "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW5AYWRtaW4uY29tIn0.EF8_q8ku-fMbKcQgKlGnprQqrgYAODEu72DzhPM43G8"

{
  "prompt": "I had a wonderful experience at the new café in the city center. The ambiance was perfect."
}
```

### Sentiment Analysis API Example Response

```json
{
  "prompt": "I had a wonderful experience at the new café in the city center. The ambiance was perfect.",
  "sentiment": "Positive"
}
```

### Image Generation API Example Request

```json
POST /sentiment-analysis
Content-Type: application/json
Authorization: Bearer "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW5AYWRtaW4uY29tIn0.EF8_q8ku-fMbKcQgKlGnprQqrgYAODEu72DzhPM43G8"

{
  "prompt": "a white siamese cat"
}
```

### Image Generation API Example Response

```json
{
  "prompt": "a white siamese cat",
  "image_url": "http://example.com/path/to/generated/image.png"
}
```

