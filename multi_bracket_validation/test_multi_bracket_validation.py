from multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation():
    sentence = '(something){}[else]'

    assert multi_bracket_validation(sentence) == True

def test_multi_bracket_validation_fail():
    sentence = '}'

    assert multi_bracket_validation(sentence) == False   

def test_multi_bracket_validation_fail_again():
    sentence = '(}[something]'

    assert multi_bracket_validation(sentence) == False 