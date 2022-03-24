import pandas as pd
import numpy as np
import re

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.preprocessing import FunctionTransformer



lemmatizer = WordNetLemmatizer()

def text_clean(text):
    '''Takes a string and returns a string of space-separated words
    that have been made lower-case and lemmatized, with stop words removed'''

    out_text = text
    stop_words = stopwords.words('english')

    # Remove hyperlinks
    out_text = re.sub(r'http\S+', '', out_text)

    # Remove punctuation
    for punct in punctuation:
        out_text = out_text.replace(punct, '')

    # Make lowercase
    out_text = out_text.lower()

    # Make list of lemmatized word tokens excluding all stopwords
    out_text_token = word_tokenize(out_text)
    out_text_token = [lemmatizer.lemmatize(word) for word in out_text_token if word not in stop_words]

    # Join text together again so we return a string of space-separated
    # lemmatized words
    out_text = ' '.join(out_text_token)

    return out_text

def transform_func(feature_data):
    # Trim to just the text (feature_data['text']) and apply text_clean
    return feature_data['text'].apply(text_clean)

text_clean_tran = FunctionTransformer(transform_func)
