import speech_recognition as sr
import pyttsx3 as tts
import datetime as date 
import pyautogui as pg
import os as os
import pygetwindow as gw


def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        speak("What do you wish?")
        audio = recognizer.listen(source)
        print("Listening...")
        
    try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            print(text)


            #Commands

            if "google" in text.lower():
                os.system("start chrome.exe")

            elif "close browser" in text.lower():
                os.system("taskkill /F /IM chrome.exe")

            elif "youtube" in text.lower():
                os.system("start chrome.exe https://www.youtube.com/")
                
            elif "play" in text.lower():
                steam_path = r"C:\Program Files (x86)\Steam\Steam.exe"
                window = None
                for win in gw.getWindowsWithTitle("Steam"):
                    if win.isMinimized:
                        window = win
                        break

                if window:
                    window.restore()
                    window.activate()
                else:
                    os.startfile(steam_path)
            
            elif "spotify" in text.lower():
                os.system("start spotify.exe")

            elif "video driver" in text.lower():
                os.startfile("C:\Program Files\AMD\CNext\CNext\RadeonSoftware.exe")

            elif "time" in text.lower():
                speak("It is now " + date.datetime.now().strftime("%H:%M:%S"))
            
            

    except sr.UnknownValueError:
            speak("Sorry, i don't understand this.")    

    return speak(text)



if __name__ == "__main__":
    listen()
