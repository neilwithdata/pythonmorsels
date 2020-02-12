import string


# simple implementation using split and manually counting
def count_words(sentence):
    word_counts = {}

    sentence = sentence.lower()
    for word in sentence.split():
        word = word.strip(string.punctuation)
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts
