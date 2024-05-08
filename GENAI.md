# FanHero Generative AI Challenge Repository

This repository hosts two primary challenges related to artificial intelligence, focusing on the construction of RESTful APIs that utilize state-of-the-art AI models to perform complex tasks.

## Challenge 1: Sentiment Analysis API

### Objective

Construct a RESTful API that receives a text input (in English) and returns a sentiment analysis, indicating whether the general sentiment of the text is positive, neutral, or negative.

### Requirements

1. The API should expose a `POST /sentiment-analysis` endpoint that accepts JSON data with a `prompt` field.
2. The AI model for sentiment analysis should be pre-trained and capable of understanding nuances in natural language.
3. The API response should include:
   - The input text (prompt).
   - The categorized sentiment analysis.
4. The API should be secure and only accept authenticated requests (suggestion: use API tokens for access).

### Example Request

```json
POST /sentiment-analysis
Content-Type: application/json
Authorization: Bearer YOUR_API_TOKEN

{
  "prompt": "I had a wonderful experience at the new café in the city center. The ambiance was perfect."
}
```

### Example Response

```json{
  "prompt": "I had a wonderful experience at the new café in the city center. The ambiance was perfect.",
  "sentiment": "Positive"
}
```

## Challenge 2: Image Generation API

### Objective

Develop a RESTful API that, given a descriptive text prompt, generates an image corresponding to the description using AI.

### Requirements

1. The API should expose a POST /image-generation endpoint that accepts JSON data with a prompt field.
2. Utilize a generative AI model capable of crafting images from text descriptions.
3. The API's response should include either a URL to the generated image or the image itself encoded in base64.
4. Ensure the API adequately handles requests and usage limits, potentially introducing a queuing system for resource-intensive requests.
5. Include authentication to ensure that only authorized users can request image generation.


### Example Request

```json
POST /image-generation
Content-Type: application/json
Authorization: Bearer YOUR_API_TOKEN

{
  "prompt": "A vivid representation of a futuristic cityscape at sunset, with flying cars and towering skyscrapers."
}
```

### Example Response

```
{
  "prompt": "A vivid representation of a futuristic cityscape at sunset, with flying cars and towering skyscrapers.",
  "image_url": "http://example.com/path/to/generated/image.png"
}
```

### Getting Started

To contribute to these challenges, follow the setup and installation instructions of this repository, check open issues, and submit your pull requests with suggested or implemented solutions. Guidelines for coding and contribution rules are available in the CONTRIBUTING.md[CONTRIBUTING](https://github.com/fanhero/ai-challenge/CONTRIBUTING.md) file.

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.

By participating in the challenges or contributing to this repository, you will be aiding in advancing the field of artificial intelligence by building tools that enable more intelligent and contextual interactions between humans and machines for FanHero Generative AI team.

Please ensure that you replace `YOUR_API_TOKEN` with appropriate instructions for acquiring and using an API token. Also, replace any placeholder URLs or paths with the actual ones users should access. Make sure to include actual paths or links to the `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `LICENSE.md` files if they exist.
