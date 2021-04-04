import speech_recognition as sr
print("\n"*20)
af = "sampleaudio.wav"
r=sr.Recognizer()
with sr.AudioFile(af) as source:
    audio = r.record(source)

print(r.recognize_google(audio))