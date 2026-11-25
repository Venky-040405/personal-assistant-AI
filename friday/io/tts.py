import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')[1].id  # Select the female voice
engine.setProperty('voice', voice)  # Set the voice (0 for male, 1 for female)
engine.setProperty('rate', 200)  # Set the speech rate (words per minute)
engine.setProperty('volume', 1.0)  # Set the volume (0.0 to 1.0)

def speak(text):    
    engine.say(text)
    engine.runAndWait()