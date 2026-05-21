from translate import Translator

translator = Translator(to_lang="hi")

text = input("Enter the text to translate: ")

translation = translator.translate(text)

print(f"Translated text: {translation}")