```python
import speech_recognition as sr
import edge_tts
import asyncio
import pygame
import webbrowser
import datetime
import pyautogui
import time

VOICE = "hi-IN-SwaraNeural"
AUDIO_FILE = r"C:\Jarvis\jarvis_voice.mp3"

recognizer = sr.Recognizer()


async def make_voice(text):
    voice = edge_tts.Communicate(
        text,
        VOICE,
        rate="-10%"
    )
    await voice.save(AUDIO_FILE)


def speak(text):
    print("JARVIS:", text)

    asyncio.run(make_voice(text))

    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO_FILE)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()


def listen():
    with sr.Microphone() as source:
        print("🎤 Jarvis sun raha hai...")

        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            command = recognizer.recognize_google(
                audio,
                language="hi-IN"
            )

            print("YOU:", command)

            command = command.lower()
            command = command.replace("जार्विस", "")
            command = command.replace("jarvis", "")
            return command.strip()

        except:
            return ""


def jarvis():
    speak("नमस्ते सौरव जी, जार्विस तैयार है।")

    while True:
        command = listen()

        if not command:
            continue

        if "गूगल खोलो" in command:
            speak("गूगल खोल रहा हूँ।")
            webbrowser.open("https://www.google.com")

        elif "यूट्यूब खोलो" in command:
            speak("यूट्यूब खोल रहा हूँ।")
            webbrowser.open("https://www.youtube.com")

        elif "नोटपैड खोलो" in command:
            speak("नोटपैड खोल रहा हूँ।")
            pyautogui.hotkey("win", "r")
            time.sleep(1)
            pyautogui.write("notepad")
            pyautogui.press("enter")

        elif "समय बताओ" in command or "टाइम बताओ" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"अभी {current_time} बज रहे हैं।")

        elif "बंद हो जाओ" in command or "jarvis band" in command:
            speak("ठीक है सौरव जी।")
            break

        else:
            speak("कमांड समझ नहीं आई।")


if __name__ == "__main__":
    jarvis()
```
