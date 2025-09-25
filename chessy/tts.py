import pyttsx3

def tts(engine = None):
    if engine == None:
        engine = pyttsx3.init()
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 0.9)

    voices = engine.getProperty('voices')
    for voice in voices:
        if "french" in voice.languages or "FR" in voice.id:
            engine.setProperty('voice', voice.id)
            break

    engine.say("E")
    engine.runAndWait()
