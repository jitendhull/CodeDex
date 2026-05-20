import nltk

nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sample_text = input("Enter your text: ")
tokens = word_tokenize(sample_text)

print("Tokens:", tokens)

bigrams = list(ngrams(tokens, 2))
print("Bigrams:", bigrams)