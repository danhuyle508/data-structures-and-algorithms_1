from repeated_word import repeated_word
def test_repeated_word_pass():
    stuff = 'cat and a cat'
    assert repeated_word(stuff) == 'cat'
def test_repeated_word_pass_again():
    stuff = 'the cat in the hat'
    assert repeated_word(stuff) == 'the'
def test_repeated_word_fail():
    stuff = 'there are no repeating words'
    assert repeated_word(stuff) == 'No matching words.'    