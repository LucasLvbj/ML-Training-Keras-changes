# First attempt at feature extraction
# Leads to an error, can you tell why?

import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\blv\PycharmProjects\ML-Training-Keras\scikit\tweets.csv')
target = df['is_there_an_emotion_directed_at_a_brand_or_product']
text = df['tweet_text']

from sklearn.feature_extraction.text import CountVectorizer

count_vect=CountVectorizer()
print(text[:9])
#count_vect.fit(text)
