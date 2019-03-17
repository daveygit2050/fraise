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
