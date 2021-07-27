import datetime
from gtts import gTTS			# Google's text to speech
import os
import playsound				# To play saved mp3 file
import requests
import selenium					# To control browser operation
import speech_recognition as sr	# Converts speech to text
import time
import webbrowser
import wikipedia

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def talk():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data=""
        try : 
            data=input.recognize_google(audio)
            print("Your question is, " + data)

        except sr.UnknownValueError:
            print("Sorry, I did not hear your question. Please repeat again.")
    return data

def listen():
	WAKE = 'hey'
	text = ''

	respond("Mandu listens")
	
	while True:
		text=talk().lower()

		if text.count(WAKE) > 0:
			take_query()

		else:
			continue

def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file  =str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)

def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number
	# that will help us in telling the day
	Day_dict = {1: 'Monday',	2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday',	6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		respond("The day is " + day_of_the_week)


def tellTime():
	
	# This method will give the time
	time = str(datetime.datetime.now())
	
	# the time will be displayed like
	# this "2020-06-05 17:50:14.582630"
	# and then after slicing we can get time
	print(time)
	hour = time[11:13]
	min = time[14:16]
	respond("The time is " + hour + "Hours and" + min + "Minutes")	

def hello():
	
	respond("Hi, I am Mandu your personal desktop assistant")


def take_query():

	respond("How can I help you?")
	print("Listening")

	text=talk().lower()

	if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
		respond("OK, bye and take care")
	
	if 'wikipedia' in text:
		respond('Searching Wikipedia')
		text = text.replace("wikipedia", "")
		results = wikipedia.summary(text, sentences=3)
		respond("According to Wikipedia")
		print(results)
		respond(results)

	elif 'time' in text:
		strTime=datetime.datetime.now().strtime("%H:%M:%S")
		respond(f"the time is {strTime}")
		
	elif "which day is it" in text:
		tellDay()

	elif 'search' in text:
		text = text.replace("search", "")
		webbrowswer.open_new_tab(text)
		time.sleep(5)

	elif "open google drive" in text:
		webbrowser.open_new_tab("https://drive.google.com/drive/u/0/shared-with-me")
		respond("Google drive is open")
		time.sleep(5)
		
	elif "open gmail" in text:
		webbrowser.open_new_tab("https://mail.google.com/mail/u/0/?ogbl#inbox")
		respond("Gmail is open")
		time.sleep(5)

	elif "open google" in text:
		webbrowser.open_new_tab("https://www.google.com")
		respond("Google is open")
		time.sleep(5)

	elif 'youtube' in text:
		driver = webdriver.Chrome(r"Mention your webdriver location")
		driver.implicitly_wait(1)
		driver.maximize_window()
		respond("Opening in youtube")
		indx = text.split().index('youtube')
		query = text.split()[indx + 1:]
		driver.get("https://www.youtube.com/result?search_query =" + '+'.join(query))

	elif "open word doc" in text:
		respond("Opening Microsoft Word")
		os.startfile("C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE")

	else:
		respond("Application not available")

if __name__=='__main__':

	hello()

    listen()

# Create .exe file
# pyinstaller Virtual_Assistant.py 
