import spacy
from spacy.lang.en import English
from fuzzywuzzy import fuzz

nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    text = text.lower().strip() # convert text to lowercase and remove whitespace
    doc = nlp(text)
    tokens = [token for token in doc if not token.is_stop and not token.is_punct] # remove stop words and punctuation
    return tokens


def extract_information(text):
    doc = nlp(text)
    # use POS tagging and NER to extract information from the text
    return doc


def generate_response(text):
    doc = extract_information(text)
    # use a dialogue management system to generate a response based on the extracted information
    response = "I'm sorry, I don't understand. Could you please rephrase your question?"
    max_score = 0
    for turn in dialogue:
        score = fuzz.partial_ratio(text, turn[0].split(": ")[1])
        if score > max_score:
            max_score = score
            response = turn[1].split(": ")[1]
    return response

dialogue = [
    ("User: Hi, can you teach me some English?", "Bot: Sure, what would you like to learn?"),
    ("User: Can you give me some examples of present continuous tense?", "Bot: Of course! The present continuous tense is used to describe actions that are happening now. For example, 'I am typing on my computer' or 'He is walking to the store.'"),
    ("User: Can you explain the difference between 'its' and 'it's'?", "Bot: 'Its' is a possessive pronoun, which means it is used to show that something belongs to something else. For example, 'The cat licked its paw.' 'It's', on the other hand, is a contraction of 'it is' or 'it has'. For example, 'It's raining outside' or 'It's been a long day.'"),
    ("User: That makes sense. Thanks for your help!", "Bot: You're welcome! Let me know if you have any other questions.")
]

user_input = "Hi, can you teach me some English?"
response = generate_response(user_input)
print(response)

user_input = "Can you give me some examples of present continuous tense?"
response = generate_response(user_input)
print(response)

user_input = "Can you explain the difference between 'its' and 'it's'?"
response = generate_response(user_input)
print(response)

user_input = "Thank you for your help"
response = generate_response(user_input)
print(response)
