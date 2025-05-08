import pyttsx3

def speak(text):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[19].id)
  engine.setProperty('rate', 174)
  engine.say(text)
  engine.runAndWait()

speak("hello Jarvis yes sir how may i help you ?")

    # text = str(text)
    # engine = pyttsx3.init('sapi5')
    # voices = engine.getProperty('voices') 
    # engine.setProperty('voice', voices[0].id)
    # engine.setProperty('rate', 174)
    # eel.DisplayMessage(text)
    # engine.say(text)
    # eel.receiverText(text)
    # engine.runAndWait()
