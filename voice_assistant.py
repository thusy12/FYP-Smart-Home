import speech_recognition as sr
import socket
import pyttsx3
import datetime
import time


print('Your AI personal assistant')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<16:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    elif hour>=16 and hour<18:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
    else:
        speak("Hello,Good Night")
        print("Hello,Good Night")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

def recog():
    word=""
    statement=takeCommand()
      
    if 'washroom' in statement:
        word = "washroom"
        # message = word.encode()
        # sock.sendall(message)
        print("Sent message: " + word)
        speak('Ok i guide you to Washroom')
        print("Ok i guide you to Washroom")
        # return word

    elif 'kitchen' in statement:
        word = "kitchen"
        # message = word.encode()
        # sock.sendall(message)
        print("Sent message: " + word)
        speak('Ok i guide you to kitchen')
        print("Ok i guide you to kitchen")

    elif 'bed' in statement:
        word = "bed"
        # message = word.encode()
        # sock.sendall(message)
        print("Sent message: " + word)
        speak('Ok i guide you to bed room')
        print("Ok i guide you to bed room")

    elif 'chair' in statement:
        word = "chair"
        # message = word.encode()
        # sock.sendall(message)
        print("Sent message: " + word)
        speak('Ok i guide you to chair')
        print("Ok i guide you to chair")

    elif 'table' in statement:
        word = "table"
        # message = word.encode()
        # sock.sendall(message)
        print("Sent message: " + word)
        speak('Ok i guide you to table')
        print("Ok i guide you to table")

    elif 'dining' in statement:
        word = "dining"
        # message = word.encode()
        # sock.sendall(message)
        print("Sent message: " + word)
        speak('Ok i guide you to dining area')
        print("Ok i guide you to dining area")

    elif 'ball' in statement or "bowl" in statement or "bol" in statement:
        word = "ball"
        # message = word.encode()
        # sock.sendall(message)
        print("Sent message: " + word)
        speak('Ok i guide you to ball')
        print("Ok i guide you to ball")

    elif 'bat' in statement:
        word = "bat"
        # message = word.encode()
        # sock.sendall(message)
        print("Sent message: " + word)
        speak('Ok i guide you to bat')
        print("Ok i guide you to bat")

    elif 'water' in statement or "bottle" in statement:
        word = "water"
        # message = word.encode()
        # sock.sendall(message)
        print("Sent message: " + word)
        speak('Ok i guide you to water bottle')
        print("Ok i guide you to water bottle")
    else:
        word = "cell phone"
        # message = word.encode()
        # sock.sendall(message)
        print("Sent message: " + word)
        speak('cell phone')
        print("Ok i guide you to cell phone")

    return word
    

speak("Your AI personal assistant")
wishMe()
# recog()




if __name__=='__main__':

    speak("Tell me how can I help you now?")
    statement = takeCommand().lower()
    
    if "good bye" in statement or "ok bye" in statement or "stop" in statement:
        speak('Your AI personal assistant is shutting down,Good bye')
        print('Your AI personal assistant is shutting down,Good bye')
        


    elif 'time' in statement:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
        
        #if statement==0:
            #continue
        
            
            # else:
            #     print(f"user said unknown statement :{statement}\n")


time.sleep(3)