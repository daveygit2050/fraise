import re

from fraise import words

# Should return a single lowercase word
def test_get_random_word():
    word = words.get_random_word()
    match = re.match("^[a-z]+$", word)
    print("Generated word: {}".format(word))
    assert match
