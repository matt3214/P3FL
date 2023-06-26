import openai
from dotenv import load_dotenv
import os
import re
import string

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

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


x="""Psalm 1:1 LXX
1 {{c1::μακάριος ἀνήρ::μἀ}} ὃς {{c2::οὐκ ἐπορεύθη ἐν βουλῇ ἀσεβῶν::οἐἐβἀ}} καὶ {{c3::ἐν ὁδῷ ἁμαρτωλῶν οὐκ ἔστη::ἐὁἁοἔ}} καὶ {{c4::ἐπὶ καθέδραν λοιμῶν οὐκ ἐκάθισεν::ἐκλοἐ}}"""

def create_cloze(text,prompt_append=None,add_hint=False):
    prompt=f"Transform the following text into a cloze deletion \
            with each deletion clozing \
            approximately one word or concept.\
            Please allow for multiple deletions in one card (i.e. c1 appears multiple times in the note) \
            Please maintain exact punctuation in the result."
    example="\nAn example of a valid cloze deletion is \
            'In {{{{c1::the beginning}}}} \
            was {{{{c2::the word}}}}, and {{{{c2::the Word}}}} was with God, and {{{{c2::the Word}}}} was God.'"
    example_with_hint="\nPlease also add a hint composed of the first letter of each word clozed.\
            'An example of a valid cloze deletion is \
            'In {{{{c1::the beginning::tb}}}} \
            was {{{{c2::the word::tw}}}}, and {{{{c2::the Word::tW}}}} was with God, and {{{{c2::the Word::tW}}}} was God.'"
    append="\n\nText: {text}\n\nCloze:"
    
    
    final_prompt=""
    if prompt_append is not None:
        prompt=prompt+prompt_append
    if add_hint:
        final_prompt=prompt+example_with_hint+append
    else:
        final_prompt=prompt+example+append
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=final_prompt,
        temperature=0.3,
        max_tokens=200
    )
    clozed=response.choices[0].text.strip()
    return clozed
    # if same_words(resolve_clozes(clozed),text):
    #     return clozed
    # else:
    #     return None