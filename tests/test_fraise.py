import re

import fraise

# Should return four space seperated lowercase words
def test_basic_generate():
    passphrase = fraise.generate()
    match = re.match("^([a-z]+\s){3}[a-z]+$", passphrase)
    print("Generated passphrase: {}".format(passphrase))
    assert match
