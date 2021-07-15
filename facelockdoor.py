import cv2
import numpy as np
from os import listdir
from os.path import isfile,join
import serial
import time
import pyttsx3
import speech_recognition as sr #pip install speechRecognition
q=1
x=0
c=0
m=0
d=0
ard = serial.Serial('com10' ,9600)
ard1 = serial.Serial('com5' ,9600)
count=0
while q<=2:
    data_path = 'C:/Users/user/Desktop/python/image/'
    onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]
    Training_data, Lebels = [],[]
    for i , files in enumerate(onlyfiles):
        image_path = data_path + onlyfiles[i]
        images = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        Training_data.append(np.asarray(images, dtype = np.uint8)) 
        Lebels.append(i)

    Lebels = np.asarray(Lebels, dtype = np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(Training_data),np.asarray(Lebels))
    print("training complete")
    q+=1
face_classifier = cv2.CascadeClassifier('C:/Users/user/AppData/Local/Programs/Python/Python38\Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",140)
engine.setProperty("volume",1000)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing... wait a minute")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please... icannot recognizing")  
        query = "none"
    if not "none" in query:
        speak("ok")
    return query



def input1(count):
    if count<3:
        count+=1
        incoming = ard1.read()
        speak("ok")
        print(incoming.decode())
        if incoming.decode() == 'f':
            speak("Finger print is  missing ,,please try agai later")
            exit()
            
        elif incoming.decode() =='p':
            speak("password is  missing ,,please try agai later")
            exit()

        elif incoming.decode()=='o':
           var='s'
           ard.write(var.encode())
           speak("Door is opening.")
           time.sleep(5)
           speak(" Door is closing in  5 seconds....5 ....4 ....3....2....1")
           inc= ard.read()
           if inc.decode() =='y':
                automation()
                return 0
        else:
            speak("data not found")
            exit()
           
    elif count>=3:
        speak("Sorry door cannot be opened")
        exit()
    incoming=""

def automation():
    speak('Automation has been started please tell me command')
    while True:
        query=takeCommand().lower()
        if "turn on light" in query: 
            var = 'e'
            t=var.encode()
            speak("ok sir... Turning on light")
            ard.write(t)
            time.sleep(1)
        elif "turn off light" in query or "turn of light"in query:
            var='d'
            speak("ok sir... Turning off light")
            t=var.encode()
            ard.write(t)
            time.sleep(1)
        elif "turn on fan" in query:
            var='g'
            speak("ok sir... Turning on fan")
            t=var.encode()
            ard.write(t)
            time.sleep(1)
        elif "turn off fan" in query or "turn of fan" in query:
            var='f'
            speak("ok sr... Turning off fan")
            t=var.encode()
            ard.write(t)
            time.sleep(1)
        elif "stop automation" in query:
            return 0
    

def face_detector(img, size= 0.5):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return img,[]
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi,(200,200))
    
    return img,roi

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        result= model.predict(face)
        if result[1]<500:
            
            confidence = int((1-(result[1])/300)*100)
            display_string = str(confidence)
            cv2.putText(image, display_string,(100,120),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,255,0))

        if confidence>=76:
            cv2.putText(image,"unlocked",(250,450),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,255,255))
            cv2.imshow('face',image)
            x+=1
        else:
            cv2.putText(image,"locked",(250,450),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,255,255))
            cv2.imshow('face',image)
            c+=1
    except:
        cv2.putText(image,"Face not found",(250,450),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,255,255))
        cv2.imshow('face',image)
        d+=1
        pass
    
    if cv2.waitKey(1)==13 or x==10 or c==30 or d==20:
        cap.release()
        cv2.destroyAllWindows()
        if x>=5:
            m=1
            time.sleep(2)
            var = 'm'
            t=var.encode()
            speak("Face recognition completed...it is matching with database!!...welcome..sir..please eter password and fingerprint")
            ard1.write(t)
            x=0
            c=0
            d=0
            input1(0)
            continue
        elif c==30:
            speak("face is not matching..please try again")
            na=input("enter y to try again or n to stop:-")
            if na== 'y':
                x=0
                c=0
                d=0
                cap= cv2.VideoCapture(0)
                continue
            elif na=='n':
                break 
        elif d==20:
            speak("face is not found please try again ")
            na=input("enter y to try again or n to stop:-")
            if na== 'y':
                x=0
                c=0
                d=0
                cap= cv2.VideoCapture(0)
                continue
            elif na=='n':
                break   
     