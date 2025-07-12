import requests
import json

def sentiment_analyzer(text_to_analyse):
    # Handle empty or whitespace-only input
    if not text_to_analyse or not text_to_analyse.strip():
        return {'label': None, 'score': None}

    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    headers = { "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock" }

    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"API error: {response.status_code}")
            return {'label': None, 'score': None}

        formatted_response = json.loads(response.text)
        sentiment = formatted_response.get('documentSentiment')
        if sentiment:
            return {'label': sentiment.get('label'), 'score': sentiment.get('score')}
        else:
            print("Unexpected response format:", formatted_response)
            return {'label': None, 'score': None}

    except Exception as e:
        print("Exception occurred:", e)
        return {'label': None, 'score': None}



