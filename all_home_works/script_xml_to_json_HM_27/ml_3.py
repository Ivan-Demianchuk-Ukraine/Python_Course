import speech_recognition as sr
from gtts import gTTS
import os


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)
        text = ""

        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
        except Exception as e:
            print(e)

    return text


def speak(text):
    language = 'en'
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")


def generate_response(text):
    # TODO: implement your response generation logic here
    return "This is a response based on the extracted information."


while True:
    user_input = get_audio()
    response = generate_response(user_input)
    print(response)
    speak(response)

