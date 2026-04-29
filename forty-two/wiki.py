import wikipedia

print(wikipedia.summary("Lenovo Laptop"))

wikipedia.set_lang("en")

def get_wikipedia_summary(topic):
    try:
        summary = wikipedia.summary(topic)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"