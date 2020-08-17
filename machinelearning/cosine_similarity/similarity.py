import nltk
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from unidecode import unidecode

# sentence pair
corpus = ["A girl is styling her hair.", "A girl is brushing her hair."]
# for c in range(len(corpus)):
#     corpus[c] = pre_process(c)

def pre_process(corpus):
    # convert input corpus to lower case
    corpus = corpus.lower()

    # collecting a list of stop words from nltk and punctuation form
    # string class and create single array.
    stopset = stopwords.words('english') + list(string.punctuation)

    # remove stop words and punctuations from string.
    # word_tokenize is used to tokenize the input corpus in word tokens.
    corpus = " ".join([i for i in nltk.wordpunct_tokenize(corpus) if i not in stopset])

    # remove non-ascii characters
    corpus = unidecode(corpus)
    return corpus

corpus = pre_process("Sample of non ASCII: Ceñía. How to remove stopwords and punctuations?")
print(corpus)