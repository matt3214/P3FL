from sentiment_analysis import *
import pytest




sentence_test_cases = [{"text":"I am having a great day","sentiment":"4"},{"text":"I am having a good day","sentiment":"3"},{"text":"I am having a bad day","sentiment":"-1"}]


@pytest.mark.parametrize("inputs", [verse_text_cases])
def test_anki_cloze(inputs):
    for t in inputs:
        prepped = t.lower()
        assert is_anki_cloze_accurate(prepped)
