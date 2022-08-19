from typing import Text
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as kit
import psutil
import pyautogui
#import pydirectinput
import operator
from googletrans import Translator
import bangla
import cv2
import os
import numpy as np
import pyautogui as p


engin= pyttsx3.init ('sapi5')
voices= engin.getProperty('voices')
#print(voices[0].id)
engin.setProperty('voice',voices[1].id)


def speak(audio):
    engin.say(audio)
    engin.runAndWait()



    

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("good morning")

        elif hour>=12 and hour<18:
                speak("good afternoon")

        else:
            speak("good evening")
        speak("i am your assistant sir. please tell me how can i help you")


def takeCommand():
    


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  


    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None" 
    return query

def sys():
    sys.exit


def takeBangla():
    


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='bn-in') 
        print(f"User said: {query}\n")  


    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None" 
    return query


def Tran():
    speak("tell me the line")
    line=takeBangla()
    traslate = Translator()
    result=traslate.translate(line)
    Text=result.text
    speak(f"the translation for the line is "+Text)
    print(f"the translation for the line is "+Text)



    

    



def TaskExecution():
    def TaskExecution():
     p.press('esc')
    speak("verification successful")
    speak("welcome back sir")
    
    #TaskExecution()
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower() 

        
        if 'wikipedia' in query:  
            speak('ok sir, Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'about shamim sir' in query:
            speak("Shamim Ahmed sir,  Assistant Professor Department of Computer Science & Engineering in Bangladesh University of Business and Technology , EDUCATION B.Sc. Engineering in Computer Science and Engineering, Dhaka University of Engineering & Technology, 2011 MSc in Computer Science and Engineering, Dhaka University of Engineering & Technology, 2014 B.Sc. ,,PUBLICATIONS ,Face Detection and Recognition System Based on Principal Component Analysis (PCA) with Back Propagation Neural Networks")
        elif 'how are you' in query:
            speak("i am fine sir, and you")
        elif 'i am fine' in query:
            speak("ok sir")

        elif 'translator' in query:
            Tran()

        #elif 'open google' in query:
            #speak("ok sir, opening google")
            #webbrowser.open("google.com")

        elif 'open google' in query:
            speak("ok sir, what should i search on  google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'close google' in query:
            speak("ok sir, closing google")
            os.system("taskkill /f /im iexplore.exe")

        elif 'close youtube' in query:
            speak("ok sir, closing youtube")
            os.system("taskkill /f /im chrome.exe")


        elif 'open notepad' in query:
            speak("ok sir, opening notepad")
            note = 'C:\\WINDOWS\\system32\\notepad.exe'
            os.startfile(note)

        elif 'close notepad' in query:
            speak("ok sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")


        elif 'open code blocks' in query:
            speak("ok sir, opening codeblocks")
            note = 'C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe'
            os.startfile(note)

        elif 'close code blocks' in query:
            speak("ok sir, closing codeblocks")
            os.system("taskkill /f /im codeblocks.exe")


        elif 'open pycharm' in query:
            speak("ok sir, opening pycharm")
            note = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe'
            os.startfile(note)

        elif 'close pycharm' in query:
            speak("ok sir, closing pycharm")
            os.system("taskkill /f /im pycharm64.exe")   
            
        elif 'i love you robot' in query:
            speak("sorry sir, i have a boyfriend his mane is google")
            
        elif 'what' in query:
            speak("yes sir, alrady i have a boyfriend ") 

        elif 'ok play sad song' in query:
            speak("ok sir, playing sad song")
            music_dir = 'G:\\random\\New folder (2)'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            

        elif 'i need relax' in query:
            speak("ok sir, what can i do")

        elif 'play popular song' in query:
            speak("ok sir, playing popular song")
            music_dir = 'G:\\random\\New folder (3)'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        #elif 'open youtube' in query:
           # speak("ok sir,, opening youtube")
           # webbrowser.open("youtube.com")

        elif 'open facebook' in query:
           speak("ok sir,, opening facebook")
           webbrowser.open("www.facebook.com")

        elif 'close facebook' in query:
            speak("ok sir, closing facebook")
            os.system("taskkill /f /im chrome.exe")

        elif 'open youtube' in query:
            speak("ok sir, what should i search on  youtube")
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")

        elif 'again play music' in query:
            speak("ok sir, what should i search on drive")
            music_dir = 'G:\\random'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        

    
        elif 'how much power we have' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")

        elif 'good bye' in query:
            speak("ok sir ,,have a nice day")
            sys()


        #elif 'the time' in query:
            #strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            #speak(f"Sir, the time is {strTime}")


            

        #elif 'send message' in query:
            #speak("tell me the phone number")
            #phone = int(takeCommand())
           # ph= phone
            #speak("tell me the message")
           # msg=takeCommand()
            #speak("tell me the time")
            #speak("time in hour")
           # hour=int(takeCommand())
           # speak("time in minute")
            #min=int(takeCommand())
            #kit.sendwhatmsg(ph,msg,hour,min,20)
            #speak("sending successfull")



        
        #if percentage>=75:
           #speak("we have enough power to continue work")
        
        #elif percentage>=40 and percentage<=75:
            #speak("we need to charge our battery")

        #elif percentage>=15:
             #speak("low battery")
             

        
        
        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'volume mute' in query:
          pyautogui.press("volumemute")
        
        #mathematical operation
        elif 'i need to calculate'in query:
 
            r = sr.Recognizer()
    
            with sr.Microphone() as source:
                speak("ok sir")
                print("Listening...")
                r.adjust_for_ambient_noise(source) 
                audio = r.listen(source)
            
                my_string=r.recognize_google(audio)
                print(my_string)
            try:
                def get_operator_fn(op):
                    return{
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        '/' : operator.__truediv__,
                        'mod' : operator.mod,
                        }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                   
                speak(eval_binary_expr(*(my_string.split())))
                print(eval_binary_expr(*(my_string.split())))
            except Exception as e:
                print("Listening...")

recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


id = 2 #number of persons you want to Recognize


names = ['','bappi']  #names, leave first empty bcz counter starts from 0


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
cam.set(3, 640) # set video FrameWidht
cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# flag = True

while True:

    ret, img =cam.read() #read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
        if (accuracy < 100):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            
            TaskExecution()
            

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
            
            speak("verification is failed")
            break
            

        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
    TaskExecution()




                    
                    



    


   