# Import Translator from the translate library
from translate import Translator

# Create a Translator object with the target language set to Hindi
translator = Translator(to_lang="hi")

# Get the text to translate from the user
text = input("Enter the text to translate: ")

# Translate the text and print the result
translation = translator.translate(text)

print(f"Translated text: {translation}")