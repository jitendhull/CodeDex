from textblob import TextBlob

text = input("Enter a sentence: ")

blob = TextBlob(text)

corrected_text = blob.correct()

print("Original sentence:", text)
print("Corrected sentence:", corrected_text)