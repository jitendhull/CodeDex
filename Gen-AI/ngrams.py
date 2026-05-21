# Import nltk library and its tokenize and ngrams modules
import nltk 
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# Take user input for conversion into token
sample_text = input("Enter a sentence: ")

# Use nltk's word_tokenize function to split the input text into tokens
tokens = word_tokenize(sample_text)

# Generate unigrams, bigrams, trigrams, and n-grams using the ngrams function from nltk
unigrams = list(ngrams(tokens, 1))

bigrams = list(ngrams(tokens, 2))

trigrams = list(ngrams(tokens, 3))

ngrams = list(ngrams(tokens, 4))

# Print the tokens and the generated n-grams
print("Token:", tokens)
print("Unigrams:", unigrams)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
print("N-grams:", ngrams)