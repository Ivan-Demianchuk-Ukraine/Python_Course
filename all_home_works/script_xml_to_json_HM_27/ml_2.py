import speech_recognition as sr
import pyttsx3
import spacy
from sklearn.metrics.pairwise import cosine_similarity
def get_response_nearest_neighbor(input_text, data):
    input_embedding = embedding_model.encode(input_text)
    similarities = cosine_similarity([input_embedding], [embedding_model.encode(input) for input, response in data])
    closest_index = similarities.argmax()
    return data[closest_index][1]

nlp = spacy.load("en_core_web_sm")
engine = pyttsx3.init()
engine.setProperty('rate', 110)
r = sr.Recognizer()


def preprocess_text(text):
    text = text.lower().strip()
    doc = nlp(text)
    tokens = [token for token in doc if not token.is_stop and not token.is_punct]
    return tokens


def extract_information(text):
    doc = nlp(text)
    return doc


def generate_response(text):
    doc = extract_information(text)
    response = "This is a response based on the extracted information."
    return response

dialogue = [("Can you teach me some English", "Sure, what would you like to learn?"),
            ("Give me some examples of present continuous tense", "The present continuous tense is used to describe actions that are happening now. For example, 'I am typing on my computer' or 'He is walking to the store.'"),
            ("Explain the difference between its and it's", "'Its' is a possessive pronoun, which means it is used to show that something belongs to something else. For example, 'The cat licked its paw.' 'It's', on the other hand, is a contraction of 'it is' or 'it has'. For example, 'It's raining outside' or 'It's been a long day.'"),
            ("Thanks for your help", "You're welcome!"),
            ("What is your name?", "My name is Chatbot."),
            ("Hello", "Hi dear"),
            ("hello", "Hi dear"),
            ("How old are you?", "I don't have an age, I'm just a computer program."),
            ("What's the meaning of life?",
             "The meaning of life is a philosophical question that has been debated for centuries."),
            ("What's the weather like today?", "I'm sorry, I don't have access to real-time weather data."),
            ("Can you tell me a joke?", "Why did the tomato turn red? Because it saw the salad dressing!"),
            ("What's your favorite color?",
             "As a computer program, I don't have a favorite color, but I think blue is nice."),
            ("Can you recommend a good book to read?",
             "One of my favorite books is 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams."),
("what is your name", "My name is ChatGPT."),
            ("where are you from", "I was created by OpenAI."),
            ("what is the capital of France", "The capital of France is Paris."),
            ("how tall is the Eiffel Tower", "The Eiffel Tower is 324 meters tall."),
            ("who is the current US president", "The current US president is Joe Biden."),
            ("what is the meaning of life", "That's a deep question. Philosophers have been trying to answer that for centuries."),
            ("can you recommend a good book to read", "Sure! What genre do you enjoy?"),
            ("what is the difference between a crocodile and an alligator",
             "Crocodiles have V-shaped snouts, while alligators have U-shaped snouts."),
            ("how do I make a good cup of coffee",
             "There are many ways to make coffee, but I recommend starting with freshly roasted beans and a good quality grinder.")
            ]





sports_dialogue = [("Who won the Super Bowl last year?", "The Tampa Bay Buccaneers won the Super Bowl last year."),
                   ("What is the record for the most home runs in a single season?", "The record for the most home runs in a single season is 73, set by Barry Bonds in 2001."),
                   ("What is the oldest tennis tournament in the world?", "The oldest tennis tournament in the world is Wimbledon, which was first held in 1877.")]

# Merge the two dialogue lists
dialogue += sports_dialogue



def get_audio_input():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."


def output_audio(text):
    engine.say(text)
    engine.runAndWait()


while True:
    user_input = get_audio_input()
    print(f"You said: {user_input}")
    user_input_tokens = preprocess_text(user_input)
    for question, response in dialogue:
        if all(token.text in question for token in user_input_tokens):
            output_audio(response)
            print(f"Bot: {response}")
            break
    else:
        get_response_nearest_neighbor(user_input, dialogue)
        response = generate_response(user_input)
        output_audio(response)
        print(f"Bot: {response}")
