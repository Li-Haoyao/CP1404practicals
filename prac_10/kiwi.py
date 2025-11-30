"""
Practical 10 - Wikipedia API Example
wiki.py
"""

import wikipedia

def get_page(search_term):
    """Get a Wikipedia page object based on the search term."""
    try:
        # Turn off autosuggest to avoid unexpected suggestions
        page = wikipedia.page(search_term, auto_suggest=False)
        return page
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following:")
        print(e.options[:10])  # show first 10 options
        return None
    except wikipedia.exceptions.PageError:
        print(f'Page "{search_term}" does not match any pages. Try another id!')
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """Main loop to prompt user for search terms."""
    print("Welcome to the Wikipedia search program!")
    while True:
        search_term = input("Enter page title (blank to quit): ").strip()
        if not search_term:
            print("Thank you. Goodbye!")
            break

        page = get_page(search_term)
        if page:
            print("\nTitle:", page.title)
            print("Summary:", page.summary[:500], "...")
            print("URL:", page.url)
        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    main()