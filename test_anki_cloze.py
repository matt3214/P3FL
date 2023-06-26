from anki_cloze import *
import pytest




verse_text_cases = ["Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν περὶ τοῦ λόγου τῆς ζωῆς.",
                    "καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν",
                    "If we say we have not sinned, we make him a liar, and his word is not in us."]


@pytest.mark.parametrize("inputs", [verse_text_cases])
def test_anki_cloze(inputs):
    for t in inputs:
        prepped = t.lower()
        assert is_anki_cloze_accurate(prepped)
