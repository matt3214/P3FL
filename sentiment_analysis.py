import openai
from dotenv import load_dotenv
import os
import re
import string

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def sentiment_analysis(text,prompt_append=None):
    prompt=f"Please perform a sentiment analysis of the following text. Rate it on a scale from -5 to 5 with 5 being the most positive.\n\nText: {text}"
    if prompt_append is not None:
        prompt=prompt+prompt_append
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=200
    )
    result=response.choices[0].text.strip()
    return result


def sentiment_analysis(text,prompt_append=None):
    prompt=f"Please perform a sentiment analysis of the following text. Rate it on a scale from -5 to 5 with 5 being the most positive.\n\nText: {text}"
    if prompt_append is not None:
        prompt=prompt+prompt_append
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=200
    )
    result=response.choices[0].text.strip()
    return result
