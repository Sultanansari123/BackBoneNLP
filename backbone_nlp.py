# -*- coding: utf-8 -*-
"""Backbone NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19QlBA-T9er3o7uu-WtcHqGyuOzhrBmGY

#NLP

Tokenization is the process of breaking up text into word,phrases,symbols or other meaningful element which is called as tokens.
"""

import nltk
nltk.download('punkt')
text=" Hi, I am Sultan Ansari and i am looking  as a job opportunity as a data science and data analyst"
from nltk.tokenize import word_tokenize
tokens=word_tokenize(text)
print(tokens)

"""Stopwords is the most comman words in the language that are to be filtered out before processing the data."""

nltk.download('stopwords')

from nltk.corpus import stopwords
stop_words=stopwords.words('english')
filtered_tokens= [ token for token in tokens if not token in stop_words]
print(filtered_tokens)

"""Lemmatization is the process of reducing the words to its base words or root form with some meaning to it."""

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
Lemmatizer=WordNetLemmatizer()
words=["history","historical"]
for word in words:
  lemmatized_words=Lemmatizer.lemmatize(word)
  print(f"{word}:{lemmatized_words}")

"""Stemming is the process of reducing words to its base words or root form without meaning to it"""

from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
words=["history","historical"]
for word in words:
  stemmed_word=stemmer.stem(word)
  print(f"{word}:{stemmed_word}")

"""Parts of speech is the process of labeling words in a sentences with their appropriate parts of speech."""

from nltk import pos_tag
import nltk
nltk.download('averaged_perceptron_tagger')
pos_tags=pos_tag(tokens)
print(pos_tags)

"""Sentiment analysis is the process of determining sentiment or emotions of piece of a text.

ner is the process of locating name entities in text and transforming them into the predefined categories.

Embedding is a technique used to represent words or phrases as a vectors in high dimensional space capturing sentiment or syntatic relationships.


1-TF-IDF-TF-IDF works on a statical measure of finding word relevance in the text.That can be used in single single document or various documents.Such task as a information retrieval,stopwords removal,keyword extraction and basic text analysis.

2-Bag of Words-is a technique to convert each an every words some number or extract feature from the text.

for example tokenize text into sentences and further tokenize words.eliminate any stopwords and convert upper case to lower case.


3-Word2Vec-each and every words convert some vectors and find sentiment information and provide relationships between words.
"""

