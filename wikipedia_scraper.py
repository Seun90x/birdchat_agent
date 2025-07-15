import wikipedia

def get_bird_description(scientific_name):
    try:
        summary = wikipedia.summary(scientific_name, sentences=3, auto_suggest=False, redirect=True)
        return f"📚 Wikipedia summary for {scientific_name}:\n{summary}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"⚠️ Multiple entries found for '{scientific_name}': {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return f"❌ No Wikipedia page found for '{scientific_name}'"
    except Exception as e:
        return f"❌ Wikipedia error: {str(e)}"

if __name__ == "__main__":
    print(get_bird_description("Turdus migratorius"))