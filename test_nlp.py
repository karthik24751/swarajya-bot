from nlp.lang_intent import detect_language, extract_keywords

def test_detect_language():
    assert detect_language('मुझे राशन कार्ड चाहिए') == 'hi'
    assert detect_language('నేను రేషన్ కార్డు కావాలి') == 'te'

def test_extract_keywords():
    assert 'ration' in extract_keywords('मुझे राशन कार्ड चाहिए')
    assert 'pension' in extract_keywords('పెన్షన్ కోసం అప్లై చేయాలి') 