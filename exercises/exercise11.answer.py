def get_censored_text(text, word):
    """
    Censors a given word in a text by replacing it with asterisks.

    Args:
    text (str): The text to be censored.
    word (str): The word to be censored.

    Returns:
    str: The censored text.
    """
    return text.replace(word, '*' * len(word))

if __name__ == "__main__":
    print(get_censored_text("Censored the word python", "python"))
