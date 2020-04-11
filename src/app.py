# import pyttsx
# engine = pyttsx.init()
# engine.say('Good morning.')
# engine.runAndWait()
from gtts import gTTS
import subprocess
import playsound
import os
f=open('/Users/Deathdater/PycharmProjects/PDFReader/data/data.txt', 'r+')
data=f.read()
f.close()
tts = gTTS(text=data, lang='en')
tts.save('/Users/Deathdater/PycharmProjects/PDFReader/data/play.mp3')
subprocess.call(["afplay",'/Users/Deathdater/PycharmProjects/PDFReader/data/play.mp3'])
review=input("how is my voice? ")
print('Thanks for your feedback!!')

#playsound.playsound('/Users/Deathdater/PycharmProjects/PDFReader/data/play.mp3')

