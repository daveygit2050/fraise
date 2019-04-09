import re

from fraise import words


class TestWords:

    # Should return a single lowercase word
    def test_get_random_word(self):
        word = words.get_random_word()
        match = re.match(r'^[a-z]+$', word)
        print("Generated word: {}".format(word))
        assert match

    # Should always return a word of four characters or fewer
    def test_get_random_word_with_max_word_length(self):
        for _ in range(10):
            word = words.get_random_word(max_word_length=4)
            if len(word) > 4:
                assert False
        assert True


