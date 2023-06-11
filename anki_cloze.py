import openai
from dotenv import load_dotenv
import os
load_dotenv()



openai.api_key = os.getenv('OPENAI_API_KEY')

def create_cloze(text):
    prompt=f"Transform the following text into a cloze deletion \
            with each deletion clozing \
            approximately one word or concept.\
            Please allow for multiple deletions in one card (i.e. c1 appears multiple times in the note) \
            Please maintain exact punctuation in the result. \
            An example of a valid cloze deletion is \
            'In {{{{c1::the beginning}}}} \
            was {{{{c2::the word}}}}, and {{{{c2::the Word}}}} was with God, and {{{{c2::the Word}}}} was God.'\n\nText: {text}\n\nCloze:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=200
    )
    
    return response.choices[0].text.strip()
