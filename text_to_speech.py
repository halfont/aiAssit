import pyttsx3



def speakText(textToSpeak):
    engine = pyttsx3.init()
    engine.say(textToSpeak)
    engine.runAndWait()