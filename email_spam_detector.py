from flask import Flask, request, jsonify
import spacy
import string
import re
import json
from io import BytesIO
from spacy.lang.pt.stop_words import STOP_WORDS

# Load the spaCy model

nlp = spacy.load("./spam_model")

# Create a Flask application
app = Flask(__name__)


# Define a route to handle text queries
@app.route('/api/email_spam/email_spam_detector', methods=['POST'])
def email_spam_detector():
    data = json.loads(BytesIO(request.data).read().decode('utf-8'))
    if 'text' in data:
        text = data['text']
        preprocessed_text = preprocessing(text)
        doc = nlp(preprocessed_text)
        response = {'sentiment': doc.cats}
        return jsonify(response)
    else:
        return jsonify({'error': 'Invalid request format'})


def preprocessing(text):
    text = text.lower()

    tokens = [token.text for token in nlp(text)]

    tokens = [t for t in tokens if
              t not in STOP_WORDS and
              t not in string.punctuation and
              len(t) > 3]

    tokens = [t for t in tokens if not t.isdigit()]

    tokens = [t for t in tokens if not t.isdigit()]

    return " ".join(tokens)


if __name__ == '__main__':
    app.run()
