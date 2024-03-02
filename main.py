
import speech_to_text
import text_to_speech
import ChatGPTAPI


messages = []

def startJarvis():
    while(1):
        text = speech_to_text.record_text()
        print(f"text is: {text}")
        messages.append({'role': 'user', 'content': text})
        response = ChatGPTAPI.send_to_GPT(messages)
        text_to_speech.speakText(response)

if __name__ == "__main__":
    startJarvis()