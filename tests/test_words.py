import re

from fraise import words


class TestWords:

    # Should return a single lowercase word
    def test_get_random_word(self):
        word = words.get_random_word()
        match = re.match(r'^[a-z]+$', word)
        print("Generated word: {}".format(word))
        assert match
