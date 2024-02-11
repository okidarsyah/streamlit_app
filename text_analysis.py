from pandas import DataFrame
import pandas as pd
from typing import List
import matplotlib.pyplot as plt
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk import ngrams
from wordcloud import WordCloud

class TextAnalysis:
    def __init__(self) -> None:
        pass

    def word_frequency(self, data:DataFrame)->List:
        _ = pd.DataFrame()
        _['token'] = data.apply(lambda x: word_tokenize(str(x)))
        tokens = [word for sentence in _['token'] for word in sentence] #data flatening
        token_freq = FreqDist(tokens)
        most_common_words = token_freq.most_common(100)
        return most_common_words
    
    def ngram_dist(self, data:DataFrame, n_grams = 2):
        tokens = data.apply(lambda x: word_tokenize(str(x)))
        _ = [word for sentence in tokens for word in sentence]
        result = ngrams(_,n_grams)
        token_freq = FreqDist(result)
        most_ngram = token_freq.most_common(25)
        return result

    def create_wordcloud(self, data:DataFrame):
        '''
        Ini adalah fungsi yang digunakan untuk membuat wordcloud dari data yang dimasukkan.
        input --> dataDataFrame[Teks]
        output --> image
        '''

        tokens = data.apply(lambda x: word_tokenize(str(x)))
        _ = [word for sentence in tokens for word in sentence]

        wcloud = WordCloud(width=1600, height=1600, max_font_size=200).generate(' '.join(_))
        plt.figure(figsize=(16,16))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

        wc_vis(df["tweet_stopword"])
