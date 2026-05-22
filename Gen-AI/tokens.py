# Import nltk libraries
import nltk

# Download the 'punkt_tab' tokenizer models
nltk.download('punkt_tab')

# Import necessary libraries for tokenization and n-grams
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# Get input text from the user
sample_text = input("Enter your text: ")
tokens = word_tokenize(sample_text)

# Print the tokens
print("Tokens:", tokens)

# Generate bigrams from the tokens
bigrams = list(ngrams(tokens, 2))
print("Bigrams:", bigrams)