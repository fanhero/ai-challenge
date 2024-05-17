## Gen AI Challenge

### Objective

Construct a RESTful API that receives a text input (in English) and returns a sentiment analysis, indicating whether the general sentiment of the text is positive, neutral, or negative.

### Requirements

1. The API should expose a `POST /sentiment-analysis` endpoint that accepts JSON data with a `prompt` field.
2. The AI model for sentiment analysis should be pre-trained and capable of understanding nuances in natural language.
3. The API response should include:
   - The input text (prompt).
   - The categorized sentiment analysis.
4. The API should be secure and only accept authenticated requests (suggestion: use API tokens for access).

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

