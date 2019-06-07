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

    def test_word_is_capitalised_on_request(self):
        """When capitalized is True, the first letter should be upper case and the rest lower"""
        word = words.get_random_word(capitalized=True)
        assert word[0].isupper()
        for letter in word[1:]:
            assert letter.islower()

    def test_word_is_not_capitalised_by_default(self):
        """When capitalized is False or omitted, all letters should be lower case"""
        non_capitalized_word = words.get_random_word(capitalized=False)
        default_word = words.get_random_word()
        for letter in non_capitalized_word:
            assert letter.islower()
        for letter in default_word:
            assert letter.islower()
