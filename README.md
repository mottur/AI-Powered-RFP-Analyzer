# Welcome to APRA, an AI-Powered RFP Analyzer tool!

## Main features:
### Analyze a Request for Proposal (RFP) document with just one click of a button.
* APRA uses a SetFit Transformer model on HuggingFace to classify sections of text into 5 distinct categories: Scope, Deliverables, Company Info, Timeline, and Technologies.
* Next, it tags relevant keywords using spaCy's NER model.
* Finally, it uses the Llama 3 70B LLM to summarize each category and provide actionable insights and next steps.

### Want a more personalized experience? Fine-tune the classifier model with your own data.
* Upload your own RFP documents or pre-labeled json files to train the classifier model and improve accuracy.

## Try it out for yourself:
Retrieve an OpenRouter API key of your own: https://openrouter.ai/. 

Install Docker if you haven't already: https://docs.docker.com/get-started/get-docker/.

Then, after launching Docker Desktop, execute the following commands in your terminal:

1. Download the public Docker images:
```bash
docker pull mottur/apra-client:latest
docker pull mottur/apra-api:latest
```
1. Download the `.env.example` file in the root folder and the frontend folder.
2. Replace the API_KEY in the `.env.example` file with your own API_KEY.
3. Run: ```cp .env.example .env```
4. Finally, run: ```docker-compose up```

Navigate to https://localhost/8000 to try out the app!