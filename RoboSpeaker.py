import win32com.client as wincom
import time

speak = wincom.Dispatch("SAPI.SpVoice")
text = "Python text to speech test.using win32com.client is activate"
speak.Speak(text)
time.sleep(3)
# text = "This text is read after 3 seconds"
# speak.Speak(text)
if __name__ == '__main__':
    speak.Speak("welcome to RoboSpeaker 1.1 Created by Rahul")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "exit>>":
            break
        command = speak.Speak (x)
        
