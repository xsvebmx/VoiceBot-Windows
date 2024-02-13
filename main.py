import os
import speech_recognition
import webbrowser
import subprocess
from datetime import datetime


name= "kari"

# Открытие браузера 
def open_chrom():
    os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

# Открытие Telegram
def open_telegram():
    webbrowser.open("https://web.telegram.org/a/#1251410089")

# Открытие YouTube 
def open_youtube():
    webbrowser.open("https://www.youtube.com")

# Открытие Spotify
def open_spotify():
    webbrowser.open("https://www.spotify.com/")

# Открытие GitHub
def open_github():
    webbrowser.open("https://github.com/")



# Главная функция 
def main():
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5
    query = ""
    
    while query != "заверши распознавание речи":
        with speech_recognition.Microphone() as mic:
            try:
                sr.adjust_for_ambient_noise(source=mic, duration=0.25)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio, language="ru-RU" ).lower()
            
            except speech_recognition.exceptions.UnknownValueError:
                print("UnknownValueError")
                query = ""

        # Открытие браузера    
        if query == f"{name} открой браузер":
            open_chrom()
        
        # Открытие Telegram
        if query == f"{name} открой telegram":
            open_telegram()
        
        # Открытие YouTube
        if query == f"{name} открой youtube":
            open_youtube()
        
        # Открытие Spotify
        if query == f"{name} включи музыку":
            open_spotify()
        
        # Открытие GitHub
        if query == f"{name} открой github":
            open_github()
        
        # Открытие калькулятора
        if query == f"{name} открой калькулятор":
            subprocess.Popen(["calc.exe"])
        if query == f"{name} время":
            current_time = datetime.now().strftime("%H:%M")
            print("Текущее время: " + current_time)

        print(query)
        

if __name__ == "__main__":
    main()