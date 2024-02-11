import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#import nltk
#import streamlit as st 
#import re
#import string
import numpy as np

#from typing import List
#from pandas import DataFrame
#from wordcloud import WordCloud
from google_play_scraper import app
#from nltk.tokenize import word_tokenize
#from nltk.tokenize import RegexpTokenizer
#from nltk.corpus import stopwords
#from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
#from text_analysis import TextAnalysis
#from nltk.tokenize import word_tokenize
#from nltk.probability import FreqDist 


#import nltk
#nltk.download('punkt')
#nltk.download('stopwords')



st.set_page_config(
    page_title="Analisa Sentimen Mobile JKN",
    layout="wide"
)

#Persiapan parameter konfigurasi
path_dataset = st.secrets.path_configuration.path_dataset
filename = "scrapped_mobile_jkn.csv"

#baca data
df_jkn = pd.read_csv(f"{path_dataset}{filename}")
#df.drop(['kode_provinsi','nama_provinsi','satuan'],axis=1,inplace=True)
df = df_jkn[['userName','content','score','at']].copy()

#container title
with st.container(border=True):
    st.title("Analisa Sentimen Mobile JKN ")
    st.text("Muhammad Okidarsyah")

#tampilkan data
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
    )


polarity_counts = df['score'].value_counts()

def create_pie_chart(polarity_counts):
                fig, ax = plt.subplots()
                ax.pie(polarity_counts, labels=polarity_counts.index, startangle=80)
                ax.axis('equal')
                return fig
st.subheader("Diagram Pie Scoring Pengguna Mobile JKN")
st.pyplot(create_pie_chart(polarity_counts))


st.markdown("Diagram 1. Melihat diagram pie diatas terlihat bahwa untuk scoring '5' masih dominan, namun untuk penilaian kurang baik (score 1 & 2) juga cukup banyak")



sentimen = []
for index, row in df.iterrows():
  if row['score'] > 3 :
    sentimen.append('Positif')
  elif row['score'] == 3 :
    sentimen.append('Netral')
  else :
    sentimen.append('Negatif')
df['sentimen'] = sentimen


polarity_counts = df['sentimen'].value_counts()

def create_pie_chart(polarity_counts):
                fig, ax = plt.subplots()
                ax.pie(polarity_counts, labels=polarity_counts.index, startangle=80)
                ax.axis('equal')
                return fig
st.subheader("Diagram Pie Analisa Sentimen")
st.pyplot(create_pie_chart(polarity_counts))

st.markdown("Diagram 2. Untuk labelisasi kita memanfaatkan scoring pengguna karena ini akan lebih kontekstual dari pada menggunakan dari hasil kelolaan content yang tekstual. untuk skore 1 dan 2 diberi label Negatif, untuk score 3 diberi label netral dan sisanya di beri label positif")


#old_stopwords = stopwords.words('indonesian')
#new_stopwords = ["aplikasi", "app", "nya", "yg", "ya", "bank", "jenius", "neo", "raya", "tmrw", 
 #                "dbs", "line bank", "linebank", "livin", "wokee", "seabank", "jago", "blu", "yng",
 #                'aolikasi', 'apliksix', 'aja', 'apk', 'apps', 'dgn', 'ane', 'sy', 'gua', 'gwa', 'si',
 #                'smpai', 'bgt', 'banget', 'bangettt', 'tu', 'ama', 'utk', 'udh', 'btw', 'ntar', 'lol',
 #                'ttg', 'emg', 'aj', 'tll', 'sih', 'kalo', 'klo', 'trsa', 'mnrt', 'nih', 'ma', 'dr', 'ajaa',
 #                'tp', 'akan', 'bs', 'bikin', 'kta', 'pas', 'pdahl', 'bnyak', 'guys', 'tnx', 'bang', 'nang',
 #                'mas', 'amat', 'tjoy', 'hemm', 'haha', 'sllu', 'hrs', 'lanjut', 'bgtu', 'sbnrnya', 'trjadi',
 #                'pdhl', 'sm', 'plg', 'skrg', 'ny', 'bca', 'mandiri', 'bri', 'btpn', 'dbs', 'brimo']

#new_stopwords = new_stopwords + old_stopwords

#def cleaningText(text):
#    text = re.sub(r'@[A-Za-z0-9]+', '', text) # remove mentions
#    text = re.sub(r'#[A-Za-z0-9]+', '', text) # remove hashtag
#    text = re.sub(r"http\S+", '', text) # remove link
#    text = re.sub(r'[0-9]+', '', text) # remove numbers

 #   text = text.replace('\n', ' ') # replace new line into space
 #   text = text.translate(str.maketrans('', '', string.punctuation)) # remove all punctuations
 #   text = text.strip(' ') # remove characters space from both left and right text
 #   return text

#def casefoldingText(text): # Converting all the characters in a text into lower case
#    text = text.lower() 
#    return text

#def tokenizingText(text): # Tokenizing or splitting a string, text into a list of tokens
#    text = word_tokenize(text) 
#    return text

#def filteringText(text): # Remove stopwords in a text
 #   listStopwords = set(new_stopwords)
  #  filtered = []
   # for txt in text:
    #    if txt not in listStopwords:
     #       filtered.append(txt)
    #text = filtered 
    #return text

#def stemmingText(text): # Reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words
#    factory = StemmerFactory()
#    stemmer = factory.create_stemmer()
#    text = [stemmer.stem(word) for word in text]
#    return text

#def  toSentence(list_words): # Convert list of words into sentence
#    sentence = ' '.join(word for word in list_words)
#    return sentence

#df['text_clean'] =df['content'].apply(cleaningText)
#df['case_folding'] = df['text_clean'].apply(casefoldingText)

#df['tokenizing'] = df['case_folding'].apply(tokenizingText)
#df['filter'] = df['tokenizing'].apply(filteringText)
#df['text_preprocessed'] = df['filter'].apply(stemmingText)


#st.dataframe(
#    df,
#    use_container_width=True,
#    hide_index=True
#     )

#akurasi = [[90,10,80.29,72.57,85.63],[80,20,80.87,72.09,85.62],[70,30,80.79,70.19,84.98],[60,40,79.59,71.13,84.43],[50,50,79.31,69.60,83.99],[40,60,79.59,71.13,84.43],[30,70,75.64,66.78,80.09],[20,80,70.14,59.06,74.86],[10,90,64.71,49.74,65.90]]

##Membuat data frame
#df_hasil = pd.DataFrame(akurasi, columns=['data_train', 'data_tes', 'SVM', 'Naive', 'R_Forest'])

#st.dataframe(
 #   df_hasil,
  #  use_container_width=True,
   # hide_index=True
    # )
