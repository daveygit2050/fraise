import re
import fraise


class TestPhrases:

    # Should return four space seperated lowercase words
    def test_generate_with_no_parameters(self):
        passphrase = fraise.generate()
        match = re.match(r'^([a-z]+\s){3}[a-z]+$', passphrase)
        print("Generated passphrase: {}".format(passphrase))
        assert match

    # Should return eight space seperated lowercase words
    def test_generate_with_word_count(self):
        passphrase = fraise.generate(word_count=8)
        match = re.match(r'^([a-z]+\s){7}[a-z]+$', passphrase)
        print("Generated passphrase: {}".format(passphrase))
        assert match

    # Should return a passphrase of at least 128 characters
    def test_generate_with_minimum_length(self):
        passphrase = fraise.generate(minimum_length=128)
        print("Generated passphrase: {}".format(passphrase))
        assert len(passphrase) >= 128

    # Should return four dash seperated lowercase words
    def test_generate_with_seperator(self):
        passphrase = fraise.generate(separator="-")
        match = re.match(r'^([a-z]+-){3}[a-z]+$', passphrase)
        print("Generated passphrase: {}".format(passphrase))
        assert match

    # Should return a passphrase where no single word is longer than 4 characters
    def test_generate_with_max_word_length(self):
        passphrase = fraise.generate(max_word_length=4)
        print("Generated passphrase: {}".format(passphrase))
        words_in_passphrase = passphrase.split(' ')
        too_long_words = [word for word in words_in_passphrase if len(word) > 4]
        assert not too_long_words

    def test_generate_with_capitalized_true(self):
        """When capitalized is true, the first char of each word should be upper case"""
        passphrase = fraise.generate(capitalized=True)
        print("Generated passphrase: {}".format(passphrase))
        words_in_passphrase = passphrase.split(' ')
        for word in words_in_passphrase:
            assert word[0].isupper()

    def test_generate_with_capitalized_false(self):
        """When capitalized is false or ommitted, the first char of each word should be lower case"""
        uncapitalized_passphrase = fraise.generate(capitalized=False)
        print("Generated uncapitalized passphrase: {}".format(uncapitalized_passphrase))
        default_passphrase = fraise.generate()
        print("Generated default passphrase: {}".format(default_passphrase))
        for word in uncapitalized_passphrase.split(' '):
            assert word[0].islower()
        for word in default_passphrase.split(' '):
            assert word[0].islower()
