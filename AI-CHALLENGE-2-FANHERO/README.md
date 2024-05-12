# AI Image Generator API

## Objective

The objective of this project is to develop a RESTful API that generates an image corresponding to a descriptive text prompt using Artificial Intelligence (AI).

## Requirements

- The API should expose a `POST /image-generation` endpoint that accepts JSON data with a `prompt` field.
- Utilize a generative AI model capable of crafting images from text descriptions.
- The API's response should include either a URL to the generated image or the image itself encoded in base64.
- Ensure the API adequately handles requests and usage limits, potentially introducing a queuing system for resource-intensive requests.
- Include authentication to ensure that only authorized users can request image generation.

## Implementation

The API is implemented using Python Flask framework and utilizes the OpenAI API for generating images based on text prompts.

### Endpoints

- **POST /image-generation**: This endpoint accepts JSON data with a `prompt` field in the request body. It generates an image based on the provided prompt using the OpenAI model and returns a JSON response containing the prompt and the URL of the generated image.

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

    The server will start running on `http://localhost:8080` by default.

### Usage

- Send a POST request to `http://localhost:8080/image-generation` with the following JSON payload:

    ```json
    {
        "prompt": "Description of the image you want to generate."
    }
    ```

- Include the Authorization header with the value `Bearer <your-openai-api-key>`.

- The API will generate an image based on the provided prompt and return a JSON response containing the prompt and the URL of the generated image.

### License

- Link to the license: https://github.com/fanhero/ai-challenge/blob/main/LICENSE

### Contributing

- Link to the contributing: https://github.com/fanhero/ai-challenge/blob/main/CONTRIBUTING.md