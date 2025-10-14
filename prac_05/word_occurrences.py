"""
Word Occurrences
Estimate: 20 minutes
Actual:20
"""

def main():
    """Count occurrences of words in a given string."""
    text = input("Text: ")
    words = text.split()

    word_to_count = {}
    for word in words:
        word = word.lower()
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    longest_word_length = max(len(word) for word in word_to_count)

    for word in sorted(word_to_count):
        print(f"{word:{longest_word_length}} : {word_to_count[word]}")


if __name__ == "__main__":
    main()
