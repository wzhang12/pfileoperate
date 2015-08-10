# coding=utf-8
from gensim import corpora, models, similarities
from gensim.models import hdpmodel, ldamodel,Doc2Vec
from itertools import izip
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#
# documents = ["Human machine interface for lab abc computer applications",
#               "A survey of user opinion of computer system response time",
#               "The EPS user interface management system",
#               "System and human system engineering testing of EPS",
#               "Relation of user perceived response time to error measurement",
#               "The generation of random binary unordered trees",
#               "The intersection graph of paths in trees",
#               "Graph minors IV Widths of trees and well quasi ordering",
#               "Graph minors A survey"]
texts=[]
with open('C:\Users\DELL\Desktop\segmented1.txt') as sourcefile:
        for line in sourcefile:
           texts.append([word for word in line.split(' ')])

model = Doc2Vec(texts, size=100, window=8, min_count=5, workers=4)

print("ok1")

#remove words that appear only once
print("ok2")
dictionary = corpora.Dictionary(texts)
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(once_ids) # remove stop words and words that appear only once
dictionary.compactify()
corpus = [dictionary.doc2bow(text) for text in texts]

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

# I can print out the topics for LSA
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
corpus_lsi = lsi[corpus]
print("ok")
#for l,t in izip(corpus_lsi,corpus):
  #print l,"#",t
#print
#for top in lsi.print_topics(2):
  #print top

# I can print out the documents and which is the most probable topics for each doc.
lda = ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=500)
corpus_lda = lda[corpus]

for l,t in izip(corpus_lda,corpus):
  print l,"#",t
print

for top in lda.print_topics(num_topics=30, num_words=15):
  print top