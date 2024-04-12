import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import socket
import requests
import wikipedia
import webbrowser
import subprocess
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pygame
from hugchat import hugchat
import pyautogui
import tkinter as tk
import json


from function import *
#password to activate the Jarvis

# Function to select the gender atomatically according to the juser input name   



# Main Function and queries to perform

if __name__ == "__main__":
        start_program()
        
        wish()

        while True:
            query = takecommand().lower()

            if 1:
            


                if "open spotify" in query:
                    speak(f"Here is your Spotify {select_gender(name)}")
                    npath=r"C:\Users\subho\AppData\Roaming\Spotify\Spotify.exe"
                    os.startfile(npath)

                elif "close spotify" in query:
                    speak(f"Ok {select_gender(name)}, Closing the Spotify App")
                    os.system("taskkill /F /IM Spotify.exe")

                elif "open vs code" in query:
                    speak(f"Here is your VS-Code {select_gender(name)}")
                    npath=r"C:\Users\subho\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                    os.startfile(npath)
                    

                elif "close vs code" in query:
                    speak(f"Ok {select_gender(name)}, Closing the Vs Code Editor")
                    os.system("taskkill /f /im Code.exe")

                elif "open camera" in query:
                    speak(f"Here is your Cemera {select_gender(name)}")

                    cap = cv2.VideoCapture(0)

            # Check if the camera is opened successfully
                    if not cap.isOpened():
                        print("Error: Could not open camera.")
                    
                    
                    while True:
            # Capture frame-by-frame
                        ret, frame = cap.read()

            # Check if the frame is captured successfully
                        if not ret:
                            print("Error: Could not read frame.")
                            break

                        # Display the captured frame
                        cv2.imshow('Laptop Camera', frame)

                        # Check for the 'q' key to quit the program
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                    # Release the camera and close all OpenCV windows
                    cap.release()
                    cv2.destroyAllWindows()



                elif "open command prompt" in query:
                    speak(f"Here is your Command Prompt {select_gender(name)}")
                    os.system("start cmd")

                elif "close command prompt" in query:
                    speak(f"Ok {select_gender(name)}, Closing the Command Prompt")
                    os.system("taskkill /F /IM cmd.exe")
                    

                elif "play my musics" in query:
                    music()
                    speak(f"Here is your Music {select_gender(name)}..")
                    break


                

                elif "IP address" in query:
                    try:
                        public_ip = requests.get('https://api.ipify.org').text
                        speak(f"Public IP Address: {public_ip}")
                    except requests.RequestException as e:
                        speak(f"Error retrieving public IP address: {e}")

                elif "wikipedia" in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences = 5)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)


                elif 'current time' in query:

                    now=(datetime.datetime.now())   
                    speak(f"{select_gender(name)}, the current time is {now}")

                elif "open google" in query:
                    speak(f"Here is your Google {select_gender(name)}")
                    speak(f"{select_gender(name)}, Please tell me... What should I search on Google?")
                    cm = takecommand().lower()
                    webbrowser.open_new_tab(f"https://www.google.com/search?q={cm}") #here you have to mention the google search bar's class or name... and it works 

                elif "send message" in query:
                    speak("In which number do you want to send the massage")
                    num=input(">> ")
                    speak(f"{select_gender(name)}.. Tell me the massage")
                    massage=takecommand().lower()
                    hour1=datetime.datetime.now().strftime("%H")
                    min1=datetime.datetime.now().strftime("%M")
                    kit.sendwhatmsg(num,massage,int(hour1),int(min1)+1) # here we have to mention the time when i want to send the message like (19,33 -> means 19 = 7pm , 33= minutes)

            
                elif "open youtube" in query:
                    speak(f"Here is your YouTube {select_gender(name)}..")
                    speak(f"{select_gender(name)}, please tell me... What are you searching for at YouTube?")
                    cm = takecommand().lower()
                    webbrowser.open_new_tab(f"https://www.youtube.com/search?search_query={cm}")               

                elif "tell me a joke" in query:
                    joke=pyjokes.get_joke(language="en", category="all")
                    speak(joke)
                

                sites=[["facebook","https://facebook.com"],["instagram","https://instagram.com"],["twitter","https://twitter.com"]]
                for site in sites:
                    if f"open {site[0]}".lower() in query:
                        speak(f"Here is your {site[0]} {select_gender(name)}...")
                        webbrowser.open_new_tab(site[1])  #opens website in new tab

                
                if "send email" in query:
                
                    try:
                        speak("What should i say?")
                        content=takecommand().lower()
                        to="subhodipdey642@gmail.com"
                        sendEmail(to,content)
                        speak("Email has been sent.")
                    except Exception as e:
                        print(e)
                        speak(f"Sorry,{select_gender(name)} I am unable to send the email")


                elif "shut down the system" in query:
                    os.system("shutdown /p /f 5")

                elif "restart the system" in query:
                    os.system("shutdown /r /f 5")

                elif "sleep the system" in query:
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

                elif "mute" in query:
                    speak(f"Ok {select_gender(name)}.. I have muted")
                    pyautogui.press('volumemute')


                elif "increase volume" in query:
                    speak("Enter How much do you want to increase the volume?")
                    vol = int(input(">> ") ) # Corrected this line to convert user input to integer
                    for i in range(vol):  # Corrected syntax for loop
                        pyautogui.press('volumeup')

                elif "decrease volume" in query:
                    speak("Enter How much do you want to decrease the volume?")
                    vol = int(input(">> ") ) # Corrected this line to convert user input to integer
                    for i in range(vol):  # Corrected syntax for loop
                        pyautogui.press('volumedown')

                elif "no jarvis" in query:
                    speak(f" {select_gender(name)}, it's always a pleasure to assist you, Have A Good Day ...")
                    sys.exit()


                elif "open ai" in query:
                    
                    speak(f"Now {select_gender(name)} you can ask me anything..")
                        
                    chatbox()


                elif "weather" in query:
                    weather()   
                    speak(f"Here is your weather {select_gender(name)}")

                elif "tell me about yourself" in query:
                    respond_to_about_me_query()

                elif "news" in query:
                    speak(f"Here is your news {select_gender(name)}")
                    news()
                elif "stock market" in query:
                    speak(f"Here is your current stock market data {select_gender(name)}")
                    webbrowser.open_new("https://in.tradingview.com/symbols/NSE-NIFTY/")

                elif "internet speed" in query:
                    speak("Here is your internet speed data which i observed.")
                    speed()



  

            speak(f"Do you have any other work {select_gender(name)}?")
  
        
        
                
 





     
   


        




