"""Library with OpenAI API solutions as functions

References:

For building code:  https://beta.openai.com/docs/guides/code/introduction

"""

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def submit_question(text):
    """This submits a question to the OpenAI API"""

    prompt = text

    result = client.completions.create(prompt=prompt,
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    model="gpt-3.5-turbo-instruct").choices[0].text.strip(" \n")
    return result


# build a function that converts a comment into code in any language
def create_code(text, language):
    """This submits a comment to the OpenAI API to create code in any languag

    Example:
        language = '# Python3'
        text = f"Calculate the mean distance between an array of points"
        create_code(text, language)

    """
    prompt = f"## {language}\n\n{text}"

    result = client.completions.create(prompt=prompt,
    temperature=0,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    model="gpt-3.5-turbo-instruct")["choices"][0].text.strip(" \n")
    return result