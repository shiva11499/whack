import speech_recognition as sr
audio_file  = "test.wav"
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
    print ("You said: "+ r.recognize_google(audio))
    