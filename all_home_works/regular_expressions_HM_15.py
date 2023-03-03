import re


import re

import re

import re

import re

import re

def generate_sentence(text: str) -> str:
    # Split the text into sentences
    sentences = re.findall(r'[A-Z][^.?!]*[.?!]', text)

    # Extract the first word from each sentence
    words = [re.findall(r'\b\w+\b', sentence)[0] for sentence in sentences]

    # Join the words together and capitalize the first letter
    sentence = " ".join(words).capitalize()

    return sentence










text = "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."
result = generate_sentence(text)
print(result) # Hello and who or yes claro.

text = "Hola..."
result = generate_sentence(text)
print(result) # Hola.


