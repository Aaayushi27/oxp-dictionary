#pip install pyttsx3

import pyttsx3

text=pyttsx3.init()
answer=input("Enter a text you want to convert into speech :")
text.say(answer)
text.runAndWait()

