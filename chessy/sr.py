import speech_recognition as sr

def sr(sr = None):
    if sr == None:
        sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    audio_text = sr.listen(source)
    print("Time over, thanks")

    try:
        print("Text: "+sr.recognize_google(audio_text,language="fr-FR"))
    except:
         print("Sorry, I did not get that")

