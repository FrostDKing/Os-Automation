import pyttsx3 as p3
import os
import speech_recognition as sr
import pygetwindow as gw
import webbrowser
import pyautogui
import random
import time

#initialization of engines
engine = p3.init()
recognizer = sr.Recognizer()

#opening files
'''with open(r"location") as f:
    greeting = f.readlines()
greeting = [line.strip() for line in greeting]

with open(r"locatiuon") as f2:
    bye=f2.readlines()
bye = [line.strip() for line in bye]

with open(r"locatioin") as f3:
    sorry=f3.readlines()
sorry= [line.strip() for line in sorry]'''

def speak(text):
    engine.setProperty('rate',210)
    engine.setProperty('volume', 0.9)
    voices = engine.getProperty('voices')
    voices = engine.setProperty('voice', voices[5].id)
    engine.say(text) , print(text)
    engine.runAndWait()

def listen():
    """Capture audio and convert it to text."""
    with sr.Microphone() as source:
        '''phrase=random.choice(greeting)'''
        "speak(phrase)"
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            '''sy=random.choice(sorry)'''
            "speak(sy)"
            return None
        except sr.RequestError:
            speak("Could not request results; check your network connection.")
            return None

# Main loop
while True:
    time.sleep(0.5)
    command = listen()
    if command:
        if "open" in command.lower():

            if "youtube" in command.lower():
                speak("Opening youtube")
                webbrowser.open("https://www.youtube.com")

            elif "anime" in command.lower():
                speak("Time to watch some anime")
                webbrowser.open("https://aniwave.to/home")

            elif "google" in command.lower():
                speak("Opening Google")
                webbrowser.open("https://www.google.com")

            elif "chat gpt" in command.lower():
                speak("Opening Gpt")
                webbrowser.open("https://chatgpt.com/?model=auto")

            elif "gmail" in command.lower():
                speak("Opening Gmail")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            
            elif "task manager" in command.lower():
                speak("Opening Task Manager")
                pyautogui.hotkey('ctrl','shift','esc')

            elif "file explorer" in command.lower():
                speak("Opening File Explorer")
                pyautogui.hotkey('win','e')
            
            else:
                application_open=command.lower().partition("open")
                pyautogui.press('win')
                
                pyautogui.write(application_open[-1])
                time.sleep(1)
                pyautogui.press("enter")
            

        elif "close" in command.lower():
            try:
                splited_command= command.lower().split()
                index_no=splited_command.index("close")
                index_no=index_no+1
                app=splited_command[index_no]
                speak(f"Closing {app}")
                window=gw.getWindowsWithTitle(splited_command[index_no])[0]
                window.activate()
                pyautogui.hotkey('alt','f4')
                
            except Exception as e:
                speak("An Error Occurred")


        elif "exit" in command.lower():
            "bi=random.choice(bye)"
            "speak(bi)"
            break
        else:
            speak(f"You said: {command}")