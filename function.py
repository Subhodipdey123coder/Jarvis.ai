
import requests
from jarvis import *
from hugchat import hugchat
import os
import pygame
import smtplib
import datetime
import pyttsx3
import speech_recognition as sr
import time
import webbrowser
import speedtest



engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
newrate=rate-15                 # Here the rate defines the speed of the speach
engine.setProperty('voice',voices[0].id)  # Here voices[0] defines the male version speach ... for female version use voices[1]
engine.setProperty('rate', newrate)

password="hellojarvis" 



def get_gender(name):
    try:
        response = requests.get(f"https://api.genderize.io/?name={name}")
        data = response.json()
        if data['gender']:
            return data['gender']
        else:
            return "Unknown"
    except Exception as e:
        print("Error retrieving gender:", e)
        return "Unknown"

def select_gender(name):
    gender = get_gender(name)
    if gender == "male":
        return "Sir"
    elif gender == "female":
        return "Mam"
    else:
        return "User"
def select_tone(name):
    gender = get_gender(name)
    if gender == "male":
        return "Mr."
    elif gender == "female":
        return "Miss."
    else:
        return "User"

#Fuction of enter the password to activate the jarvis
def start_program():
    # Function to start the program
    while True:
        speak(f"{name} please enter the password to activate me,")
        user_input = takecommand().lower().replace(" ","")
        if user_input.strip() == password.lower().strip():
            speak("------JARVIS-ACTIVATED------")
            break
        else:
            speak("Incorrect password.")
     
            
  
# Function to speak the text
def speak(audio):
    engine.say(audio)
    print("Jarvis : "+audio)
    engine.runAndWait()


#take the name input for print the user name in the query

speak("Please Tell Me Your Name?")
name=input(">> ")



# Function to recognize audio from microphone
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source,timeout=5,phrase_time_limit=7)
        
        
        
        try:
                speak(f"Definately {select_gender(name)}")
                query=r.recognize_google(audio,language='en-in')
                print(f"{name} : {query}")
                return query
                
 
        except Exception as e:
                speak(f"Do you repeat it {select_gender(name)} ....I can't Recognize it")
                return "none"
        return query




#Wish Function
def wish():
    hour=int(datetime.datetime.now().hour)
    tt= datetime.datetime.now().strftime("%H:%M %p")

    if hour>=0 and hour<12:
        speak(f"Good Morning {select_gender(name)}, it's {tt}")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon {select_gender(name)} , it's {tt}")
    else:
        speak(f"Good Evening {select_gender(name)}, it's {tt}")

    # Mandatory Speach   
    speak(f"Welcome {select_tone(name)} {name}. Your personal assistant JARVIS reporting for duty. How may I be of service?")

# Fuction of the script about the JARVIS
def respond_to_about_me_query():
    about_me_response = """
    My name is "JARVIS" .I am your personal AI assistant, created and devoleped By "Mr. Subhodip Dey" on 11th April, 2024. I am here to assist you with various tasks and provide useful information. 
    My purpose is to make your life easier by helping you with tasks such as managing your schedule, providing weather updates, playing music, and much more.
    Feel free to ask me anything, and I'll do my best to assist you.
    """
    speak(about_me_response)


#Sending Email Function
def sendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        # Replace with your actual Gmail credentials
        sender_email = 'subhodipdey643@gmail.com'
        sender_password = 'fzui hyul ddez gtcu' # This is the app password of google Which have to generate 


        # Log in to the Gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to, content)

        # Close the connection
        server.close()


#Take the weather api to fetch the data of the user given city waether

def weather():
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    API = "e3e2ec4fe3ad8c1eeadcf7e97fbd9a05"
    speak("tell me the city name")
    city = takecommand().lower()

    url = f"{base_url}?q={city}&appid={API}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Weather Data:")
        print("-------------")
        speak("City:", data["name"])
        speak("Weather:", data["weather"][0]["description"])
        speak("Temperature:", data["main"]["temp"], "Kelvin")
        speak("Humidity:", data["main"]["humidity"], "%")
        speak("Wind Speed:", data["wind"]["speed"], "m/s")
    else:
        print("Failed to fetch weather data. Status code:", response.status_code)


# function to find the song from your directory by entering the name of the specific song

def search_song(directory, song_name):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp3") and song_name.lower() in file.lower():
                return os.path.join(root, file)
    return None

def play_song(song_path):
    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

def music():
    directory = r"E:\Songs"
    speak("Sir which song you want to play ? ")
    song_name = takecommand().lower()
    song_path = search_song(directory, song_name)
    if song_path:
        os.startfile(os.path.join(song_path))
    else:
        speak("Song not found.")


#Function to open and chat with the openai - Chatgpt

def chatbox():

    user=takecommand().lower()
    chatbot=hugchat.ChatBot(cookie_path="cookies.json")
    id=chatbot.new_conversation()
    chatbot.change_conversation(id)
    response=chatbot.chat(user)
    speak(response)
    print(response)
    return response 


"""
#function to read the news and fetch by api

def news():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'in',
        'apiKey': '401c57a20beb40c5a541714115fed1e1'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for bad status codes
        news = response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching news:", e)
        engine.say("Can't access the link. Please check your internet connection.")
        engine.runAndWait()
        exit()

    for article in news['articles']:
        print("##############################################################\n")
        print(article['title'], "\n\n")
        engine.say(article['title'])
        print('______________________________________________________\n')

        engine.runAndWait()

        print(article['description'], "\n\n")
        engine.say(article['description'])
        engine.runAndWait()
        print("..............................................................")
        time.sleep(2)"""

# function to fetch the news data
def news():
    webbrowser.open_new("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")

    

# Function to fetch the internet speed and print it in the console
def check_internet_speed():
    # Create speedtest object
    st = speedtest.Speedtest()

    # Perform download speed test
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps

    # Perform upload speed test
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

    return download_speed, upload_speed

def speed():
    download_speed, upload_speed = check_internet_speed()
    speak("Download Speed: {:.2f} Mbps".format(download_speed))
    speak("Upload Speed: {:.2f} Mbps".format(upload_speed))