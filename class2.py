import urllib.request
import re
import nltk
from inscriptis import get_text
from googletrans import Translator

#nltk.download()
translator = Translator()

texto = "Genes are located on chromosomes. Chromosomes are in pairs and genes, or their alleles, are located on each of these pairs. When the cell divides in half, each chromosome ends up in a different cell. This is seen during meiosis in formation of egg cells of sperms. The genes also split into two halves. These are called alleles. Meiotic products have one of each homologous chromosome but not both. Meiosis is a series of cell divisions that creates haploid cells with half of the total number of chromosomes. Once the egg and sperm meet, the pairs are restored but now the genetic combination of the pair is altered. One of the alleles thus comes from the mother and another from the father. This is how a defective gene causing a genetic disorder is also inherited by offspring. As per the Mendelian principles of inheritance genes need to be inherited independently of each other. However, there are far more genes than chromosome pairs. It is found that all of the genes on a chromosome are physically inherited together as a single linked group. Only genes that are located on different chromosomes have independent assortment during meiosis. According to the chromosomal theory 25% would resemble one parent, 25%, the second parent, 25% would have one trait from one parent and one from the other parent and 25% would have also have the other traits from each parent. Since each chromosome is a diploid, or occurs in pairs, genes on different chromosomes assort independently during sexual reproduction, recombining to form new combinations of genes. Genes on the same chromosome would theoretically never recombine. However, genes do undergo cross over. During crossover, chromosomes exchange stretches of DNA, effectively shuffling the gene alleles between the chromosomes. This process of chromosomal crossover generally occurs during meiosis. The probability of crossover occurring between two given points on the chromosome is related to the distance between the points. If the distance is long there is a higher chance of a crossover. For genes that are closer together, however, the lower probability of crossover means that the genes demonstrate genetic linkage that means that the alleles for the two genes tend to be inherited together. The amounts of linkage between a series of genes can be combined to form a linear linkage map."
#enlace = "https://www.quantamagazine.org/giant-genetic-map-reveals-lifes-hidden-links-20161025/"
#html = urllib.request.urlopen(enlace).read().decode('utf-8')
#text = get_text(html)
#article_text = text
#article_text = article_text.replace("[ edit ]","")
print("########################")

from nltk import word_tokenize,sent_tokenize

#article_text = re.sub(r'\[[0-9]*\]',' ',article_text)
#article_text = re.sub(r'\s+',' ',article_text)

#formatted_article_text = re.sub('[^a-zA-Z]',' ',article_text)
#formatted_article_text = re.sub(r'\s+',' ',formatted_article_text)

sentence_list = nltk.sent_tokenize(texto)


stopwords = nltk.corpus.stopwords.words('english')



word_frequencies = {}
for word in nltk.word_tokenize(texto):
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

