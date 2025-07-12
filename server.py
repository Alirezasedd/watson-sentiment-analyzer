"""Flask web server for BERT-based sentiment analysis using Watson NLP."""

from flask import Flask, request, render_template
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask(__name__)

@app.route('/')
def index():
    """
    Serve the main HTML page containing the sentiment analysis form.
    """
    return render_template('index.html')


@app.route('/sentimentAnalyzer', methods=['GET'])
def analyze_sentiment():
    """
    Handle AJAX GET request for sentiment analysis.
    Extracts text input from query string, analyzes it using Watson NLP,
    and returns formatted results or appropriate error messages.
    """
    text_to_analyze = request.args.get('textToAnalyze', '').strip()

    if not text_to_analyze:
        return "❗ No input text provided. Please enter some text."

    result = sentiment_analyzer(text_to_analyze)

    if not isinstance(result, dict):
        return "❌ Invalid response from sentiment analyzer."

    label = result.get("label")
    score = result.get("score")

    if label is None or score is None:
        return "⚠️ Unable to determine sentiment. Try different text."

    return f"<strong>Sentiment:</strong> {label}<br><strong>Confidence Score:</strong> {score:.2f}"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    