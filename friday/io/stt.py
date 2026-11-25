import speech_recognition as sr

recognize = sr.Recognizer()
def calibrate_microphone():
    with sr.Microphone() as source:
        recognize.adjust_for_ambient_noise(source, duration=0.5)

def Recognize():
    try:
        with sr.Microphone() as source:
            audio = recognize.listen(source)
        text = recognize.recognize_google(audio).lower()
        return text
    except (sr.WaitTimeoutError, sr.UnknownValueError):
        return ""                                    # silence or unclear audio, stay quiet
    except sr.RequestError as e:
        print(f"Speech service error: {e}")
        return ""    
    except Exception as e:
        print(f"Unexpected error: {e}")                    # anything else
        return ""       