import nltk 
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

sample_text = input("Enter a sentence: ")
tokens = word_tokenize(sample_text)

unigrams = list(ngrams(tokens, 1))

