# Sentiment Analysis API

## Objective

The objective of this project is to construct a RESTful API that receives a text input (in English) and returns a sentiment analysis, indicating whether the general sentiment of the text is positive, neutral, or negative.

## Requirements

- The API should expose a `POST /sentiment-analysis` endpoint that accepts JSON data with a `prompt` field.
- The AI model for sentiment analysis should be pre-trained and capable of understanding nuances in natural language.
- The API response should include:
  - The input text (prompt).
  - The categorized sentiment analysis.
- The API should be secure and only accept authenticated requests (suggestion: use API tokens for access).

## Implementation

The API is implemented using Python Flask framework and utilizes the OpenAI API for sentiment analysis.

### Endpoints

- **POST /sentiment-analysis**: This endpoint accepts JSON data with a `prompt` field in the request body. It performs sentiment analysis on the provided text prompt using the OpenAI model and returns a JSON response containing the prompt and the categorized sentiment analysis.

### Installation and Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file in the root directory and add the following:

    ```plaintext
    API_KEY=<your-openai-api-key>
    ```

    Replace `<your-openai-api-key>` with your actual OpenAI API key, you can get one by accessing: https://platform.openai.com/api-keys.

4. Run the Flask server:

    ```bash
    python app.py
    ```

    The server will start running on `http://localhost:5000` by default.

### Usage

- Send a POST request to `http://localhost:5000/sentiment-analysis` with the following JSON payload:

    ```json
    {
        "prompt": "Text for sentiment analysis."
    }
    ```

- Include the Authorization header with the value `Bearer <your-openai-api-key>`.

- The API will perform sentiment analysis on the provided text and return a JSON response containing the input text (prompt) and the categorized sentiment analysis.

### License

- Link to the license: https://github.com/fanhero/ai-challenge/blob/main/LICENSE

### Contributing

- Link to the contributing: https://github.com/fanhero/ai-challenge/blob/main/CONTRIBUTING.md