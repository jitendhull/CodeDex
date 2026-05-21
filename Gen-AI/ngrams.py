import nltk 
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

sample_text = input("Enter a sentence: ")
tokens = word_tokenize(sample_text)


unigrams = list(ngrams(tokens, 1))

bigrams = list(ngrams(tokens, 2))

trigrams = list(ngrams(tokens, 3))

ngrams = list(ngrams(tokens, 4))

print("Token:", tokens)
print("Unigrams:", unigrams)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
print("N-grams:", ngrams)