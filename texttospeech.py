import pyttsx3
tts = pyttsx3.init()   


print("Text to Speech")


user_text = input("Type: ")

print("Speaking.")
tts.say(user_text)
tts.runAndWait()

print("Done.")
