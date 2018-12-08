import datetime
import time
h=[7,2,]
m=[38]

def glow():
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)
    LED = 21
    GPIO.setup(LED,GPIO.OUT)
    GPIO.output(LED,True)
    time.sleep(5)
    GPIO.output(LED,False)
def hear():
    from gtts import gTTS 
    import os
    mytext = 'its time to take paracitamal'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    

while True:
    now =datetime.datetime.now()
    print(now.hour,":",now.minute)
    if now.hour in h:
        if now.minute in m:
            print("Its time to take Tablet")
            glow()
            hear()
            break
        else:
            print("wait")





    
