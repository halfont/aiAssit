import speech_recognition as sr


#init the recognizer
r = sr.Recognizer()
fileName = "output.txt"

def record_text():
    #record text using mic
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                myText = r.recognize_google(audio2)
                return myText
        except sr.RequestError as e:
            print(f"Could not request results, {0}")
        except sr.UnknownValueError:
            print(f"unknown error")
    return

def output_text(text):
    #output text to file
    f = open(fileName, "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

def infiniteRecordToFile():
    while(1):
        text = record_text()
        output_text(text)

        print(f"wrote text to {fileName}")