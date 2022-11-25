def is_palindrome(phrase):
    phrase = "".join([char.lower() for char in phrase if char.isalpha()])
    return phrase[::-1] == phrase


# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    print(is_palindrome('Able was I ere I saw Elba'))  # true
    print(is_palindrome("race car"))  # true
