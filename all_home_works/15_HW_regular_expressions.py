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
