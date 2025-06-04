from email_classifier.preprocess import clean_text


def test_clean_text_basic():
    text = "Hello!!! This is a TEST email, visit http://example.com"
    cleaned = clean_text(text)
    assert 'http' not in cleaned
    assert cleaned.islower()
