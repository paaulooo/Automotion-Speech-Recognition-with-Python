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
        speak("O QUE DESEJA?")
        audio = recognizer.listen(source)
        print("Escutando...")
        
    try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            print(text)


            #Commands

            if "google" in text.lower():
                os.system("start chrome.exe")

            elif "fechar navegador" in text.lower():
                os.system("taskkill /F /IM chrome.exe")

            elif "youtube" in text.lower():
                os.system("start chrome.exe https://www.youtube.com/")
                
            elif "jogar" in text.lower():
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

            elif "placa" in text.lower():
                os.startfile("C:\Program Files\AMD\CNext\CNext\RadeonSoftware.exe")
            
            elif "Persona 5" or "persona cinco" in text.lower():
                os.startfile("C:\Program Files (x86)\Steam\steamapps\common\P5R\P5R.exe")
            
            

    except sr.UnknownValueError:
            speak("Desculpe, não entendi o que você disse.")    

    return speak(text)



if __name__ == "__main__":
    listen()