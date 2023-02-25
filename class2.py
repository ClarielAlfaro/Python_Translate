import urllib.request
import re
import nltk
from inscriptis import get_text
from googletrans import Translator

#nltk.download()
translator = Translator()

#enlace = "https://en.wikipedia.org/wiki/PlayStation"
enlace = "https://www.quantamagazine.org/giant-genetic-map-reveals-lifes-hidden-links-20161025/"
html = urllib.request.urlopen(enlace).read().decode('utf-8')
text = get_text(html)
article_text = text
article_text = article_text.replace("[ edit ]","")
print("########################")

from nltk import word_tokenize,sent_tokenize

article_text = re.sub(r'\[[0-9]*\]',' ',article_text)
article_text = re.sub(r'\s+',' ',article_text)

formatted_article_text = re.sub('[^a-zA-Z]',' ',article_text)
formatted_article_text = re.sub(r'\s+',' ',formatted_article_text)

sentence_list = nltk.sent_tokenize(article_text)


stopwords = nltk.corpus.stopwords.words('english')



word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

#CALCULA LAS FRASES QUE MAS SE REPITEN
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]


#REALIZAR EL RESUMEN CON LAS MEJORES FRASES Y TRADUCIR

import heapq
summary_sentence = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentence)

translation = translator.translate(summary, dest='es')
print(translation.text)
#print(summary)

from nltk.corpus import treebank
#t = treebank.parsed_sents('wsj_0001.mrg')[0]
#t.draw()

