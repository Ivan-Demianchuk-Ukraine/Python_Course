# There is a text fragment consisting of sentences.
# A sentence is a string that begins with a capital letter and ends with a period, question mark, or exclamation
# mark (or more than one).
# Words consist only of Latin letters, separated by spaces or commas with spaces.
# A sentence can be one word long.
# Make a sentence from the first words of the fragment's sentences.
# Only the first word of the final sentence must be capitalized, the rest must be small.
# The sentence must end with a dot.

import re


def generate_sentence(text: str) -> str:
    sentences = re.findall(r'[A-Z][^.?!]*[.?!]', text)

    words = [re.findall(r'\b\w+\b', sentence)[0] for sentence in sentences]

    sentence = " ".join(words).capitalize()

    sentence = sentence + '.'

    return sentence


input_text = "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro..?"
result = generate_sentence(input_text)
print(result)

input_text = "Hola..."
result = generate_sentence(input_text)
print(result)
