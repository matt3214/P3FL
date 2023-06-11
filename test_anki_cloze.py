from anki_cloze import create_cloze
import re
import pytest
import string

def resolve_clozes(clozed_text):
    """
    Resolve cloze deletions in a text.

    :param clozed_text: Text with cloze deletions.
    :type clozed_text: str
    :return: Text with cloze deletions resolved.
    :rtype: str
    """
    return re.sub(r"{{c\d::(.*?)}}", r"\1", clozed_text)


def clean_string(s):
    return s.translate(str.maketrans('', '', string.punctuation))

def same_words(a,b):
    return clean_string(a)==clean_string(b)

def is_anki_cloze_accurate(verse_text):
    clozed=create_cloze(verse_text)
    resolved=resolve_clozes(clozed)
    print('verse_text:',verse_text)
    #print('clozed:',clozed)
    print('resolved:  ',resolved)
    return same_words(verse_text,resolved)


verse_text_cases = ["Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν περὶ τοῦ λόγου τῆς ζωῆς.",
                    "καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν",
                    "If we say we have not sinned, we make him a liar, and his word is not in us."]


@pytest.mark.parametrize("inputs", [verse_text_cases])
def test_anki_cloze(inputs):
    for t in inputs:
        prepped = t.lower()
        assert is_anki_cloze_accurate(prepped)
