import spacy
from textblob import TextBlob

from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# API code for Named Entity Recognition

# Load the spaCy model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

def ner(text):
    # Process the text using the spaCy model
    doc = nlp(text)

    # Extract entities from the processed text
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    # Return the extracted entities
    return entities


# API code for Sentiment Analysis
def sentiment_analysis(text):
    # Process the text using TextBlob
    blob = TextBlob(text)

    # Get the sentiment polarity (-1 to 1) and subjectivity (0 to 1)
    sentiment = {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    }

    # Return the sentiment analysis
    return sentiment


# API code for Language Analysis
DetectorFactory.seed = 0

def language_detection(text):
    try:
        # Detect the language of the text
        lang = detect(text)
    except LangDetectException:
        # Handle case where language detection fails
        lang = "Unknown"

    # Return the detected language
    return {"language": lang}

