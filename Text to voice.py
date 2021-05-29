#import the Gtts module for text
#to speech conversion
import os
from gtts import gTTS
mytext='hello Rishab'
language='en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("output.mp3")
os.system("start output.mp3")
