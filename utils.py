import re
import nltk
from nltk.corpus import stopwords

def description_to_words(raw_description):
    no_urls = re.sub("(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)", "", raw_description)
    no_mentions = re.sub("@[A-Za-z0-9]+","", no_urls)
    letters_only = re.sub("[^a-zA-Zñéáíóúü]", " ", no_mentions)
    letters_only = clean_accents(letters_only)
    words = letters_only.lower().split()
    stops = set(stopwords.words('spanish'))
    meaningful_words = [word for word in words if not word in stops]
    return " ".join(meaningful_words)

def clean_accents(sentence):
    return sentence.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó','o').replace('ú', 'u')