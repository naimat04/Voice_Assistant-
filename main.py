import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time
pyttsx3 speech_recognition, webbrowser, datetime, pyjokes, time
def sp_to_text():
    recognizer =  sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Undertand")

def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate",150)
    engine.say(x)
    engine.runAndWait()

#text_to_speech("Hello welcome")

if __name__ == "__main__":
    if sp_to_text().lower() == "hello":
        while True:
            data_1 = sp_to_text().lower()

            if "your name" in data_1:
                name= "my name is nem"
                text_to_speech(name)
            elif "old are you" in data_1:
                age= "I'm two years old"
                text_to_speech(age)
            elif "time" in data_1:
                time = datetime.datetime.now().strftime("%I%M%p")
                text_to_speech(time)
            elif "youtube" in data_1:
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data_1:
                joke_new = pyjokes.get_joke(language="en", category="neutral")
                text_to_speech(joke_new)
            elif "exit" in data_1:
                text_to_speech("Thank you")
                break
            time.sleep(5)

    else:
        print("Thanks")


