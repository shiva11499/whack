import speech_recognition as sr
from firebase import firebase
firebase = firebase.FirebaseApplication("https://helperglove.firebaseio.com",None)
#data = {"Name":"Abhay"}
firebase.post('/',{'Abhay':'Abhay'})
##import pyrebase
##config = { "apiKey": "AlzaSyZfM5PDT8Fe3uPsyrfdzn6Cx6O7Kwg-3rs",
##           "databaseURL": "helperglove.firebaseio.com",
##           
##    }
##firebase = pyrebase.initialize_app(config)
##auth = firebase.auth()
##db = firebase.database()
##data = {"name":"Abhay"}
##results = db.child("users").push(data, user['idToken'])
##db.child("users").push(data)
mic_name = "USB PnP Sound Device"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()

for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
#print (device_id)        
with sr.Microphone(device_index = 002, sample_rate = sample_rate, chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print ("say something")
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        
        print ("you said:" + text)
        if text=="Abhay":
            print("Alert")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results ,{0}".format(e))
