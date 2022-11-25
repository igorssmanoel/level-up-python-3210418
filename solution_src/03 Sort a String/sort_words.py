
def sort_words(words):
    return sorted(words.split(), key=lambda x: x[0].lower())


# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
