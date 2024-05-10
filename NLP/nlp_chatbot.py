from flask import Flask, request, jsonify, render_template
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('nlp_chatbot.html')

@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    content = request.json['text']
    response_text = ""

    tokens = word_tokenize(content)
    pos_tags = pos_tag(tokens)
    blob = TextBlob(content)
    sentiment = blob.sentiment
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(content)

    response_text += "Here's the analysis of your text:\n"
    response_text += f"Tokens: {tokens}\n"
    response_text += f"POS Tags: {pos_tags}\n"
    response_text += f"Sentiment Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}\n"
    response_text += f"VADER Scores: {sentiment_scores}\n"

    return jsonify({
        'response': response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
