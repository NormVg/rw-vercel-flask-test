import speech_recognition as sr

def reco(file):
    r = sr.Recognizer()
    

    
    with sr.AudioFile(file) as source:
        audio = r.record(source)
    result = r.recognize_google(audio)
    print(result)
    return result

