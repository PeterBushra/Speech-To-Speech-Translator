import speech_recognition as sr


r = sr.Recognizer()

def Transcribe(audioPath):
    
    loaded = sr.AudioFile(audioPath)
    with loaded as source:
        audio = r.record(source)
    recognized = r.recognize_google(audio)
    return recognized

