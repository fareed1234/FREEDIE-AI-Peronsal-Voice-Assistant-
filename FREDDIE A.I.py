# PROJECT NAME: FREDDIE A.I
# MADE BY: MUHAMMAD FAREED

import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import openai
from pytube import Search
import requests
base_url = 'http://localhost:8080'
# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')


# Set your OpenAI API Key
openai.api_key = "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"  # Replace with your OpenAI key

# Function to speak
def freddie_speak(text):
    engine.say(text)
    engine.runAndWait()

def get_server_health():
    response = requests.get(f'{base_url}/health')
    return response.json()

# Function to listen for commands
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("I didn't catch that. Please say it again.")
            freddie_speak("I didn't catch that. Please say it again.")
            return listen_command()  # Recursively call listen_command until we get input
        except sr.RequestError:
            print("I'm unable to reach the speech service.")
            freddie_speak("I'm unable to reach the speech service.")
            return None

# Open Google
def open_google():
    print("With Pleasure Sir")
    freddie_speak("With Pleasure Sir")
    webbrowser.open("https://www.google.com")

# Open YouTube
def open_youtube():
    print("With Pleasure Sir")
    freddie_speak("With Pleasure Sir")
    webbrowser.open("https://www.youtube.com")

def open_instagram():
    print("With Pleasure Sir")
    freddie_speak("With Pleasure Sir")
    webbrowser.open("https://www.instagram.com/")

def open_facebook():
    print("With Pleasure Sir")
    freddie_speak("With Pleasure Sir")
    webbrowser.open("https://www.facebook.com/")

# Perform a Google Search
def perform_google_search(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    freddie_speak(f"Searching Google for {query}")

# Get OpenAI GPT response
def get_ai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-4o-mini",
            prompt=prompt,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return answer
    except Exception as e:
        print(f"Error with OpenAI: {e}")
        return "Sorry, I encountered an error with OpenAI."
    
def post_completion(context, user_input):
    prompt = f"{context}\nUser: {user_input}\nAssistant:"
    data = {
        'prompt': prompt,
        'temperature': 0.8,
        'top_k': 35,
        'top_p': 0.95,
        'n_predict': 400,
        'stop': ["</s>", "Assistant:", "User:"]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'{base_url}/completion', json=data, headers=headers)
    if response.status_code == 200:
        return response.json()['content'].strip()
    else:
        return "Error processing your request. Please try again."
    
def update_context(context, user_input, assistant_response):
    return f"{context}\nUser: {user_input}\nAssistant: {assistant_response}"

def search_movie_online(movie_title, platform='youtube'):
    search_query = movie_title.replace(" ", "+")  # Format the search query for the URL
    if platform == 'youtube':
        url = f"https://www.youtube.com/results?search_query={search_query}+full+movie"
    elif platform == 'netflix':
        url = f"https://www.netflix.com/search?q={search_query}"
    else:
        # Default to Google search for the movie
        url = f"https://www.google.com/search?q={search_query}+full+movie"
    print(f"Searching for {movie_title} on {platform.capitalize()}.")
    freddie_speak(f"Searching for {movie_title} on {platform.capitalize()}.")
    webbrowser.open(url)
    print("Is there anyting else i can assist you with sir? ")
    freddie_speak("Is there anyting else i can assist you with sir? ")


def play_song_on_youtube(song_name):
    print(f"Searching for {song_name} on YouTube.")
    freddie_speak(f"Searching for {song_name} on YouTube.")
    search = Search(song_name)
    results = search.results
    if results:
        video_url = results[0].watch_url
        print(f"Playing {song_name} on YouTube.")
        freddie_speak(f"Playing {song_name} on YouTube.")
        webbrowser.open(video_url)
    else:
        print("Sorry, I couldn't find the song on YouTube.")
        freddie_speak("Sorry, I couldn't find the song on YouTube.")
# AI Assistant Introduction
def freddie_ai():
    print("SYSTEMS ONLINE!")
    print("Welcome Sir. How can I assist you today?")
    freddie_speak("Welcome Sir. How can I assist you today?")

# Main function
if __name__ == '__main__':
    freddie_ai()

    while True:
        command = listen_command()

        if command is None:
            continue

        if 'hello' in command or 'how are you' in command:
            print('I am fine, sir. How may I help you?')
            freddie_speak('I am fine, sir. How may I help you?')

        elif 'open youtube' in command:
            open_youtube()
            print("Is there anyting else i can assist you with sir? ")
            freddie_speak("Is there anyting else i can assist you with sir? ")

        elif 'open google' in command:
            open_google()
            print("Is there anyting else i can assist you with sir? ")
            freddie_speak("Is there anyting else i can assist you with sir? ")

        elif 'open instagram' in command:
            open_instagram()
            print("Is there anyting else i can assist you with sir? ")
            freddie_speak("Is there anyting else i can assist you with sir? ")

        elif 'open facebook' in command:
            open_facebook()
            print("Is there anyting else i can assist you with sir? ")
            freddie_speak("Is there anyting else i can assist you with sir? ")


        elif 'search' in command:
            search_query = command.replace('search', '').strip()
            perform_google_search(search_query)
            print("Is there anyting else i can assist you with sir? ")
            freddie_speak("Is there anyting else i can assist you with sir? ")

        elif 'play' in command:
            song_name = command.replace('play', '').strip()
            if song_name:
                print('With pleaure sir.')
                play_song_on_youtube(song_name)
                print("Is there anyting else i can assist you with sir? ")
                freddie_speak("Is there anyting else i can assist you with sir? ")
            else:
                print('Please specify a song name.')
                freddie_speak('Please specify a song name.')
                print("Is there anyting else i can assist you with sir? ")
                freddie_speak("Is there anyting else i can assist you with sir? ")
        elif 'ask' in command or 'tell' in command:
            prompt = command.replace('ask', '').replace('can', '').strip()
            print(f"Fetching response for: {prompt}")
            freddie_speak("Let me think...")
            response = get_ai_response(prompt)
            print(f"AI Response: {response}")
            freddie_speak(response)
            print("Is there anyting else i can assist you with sir? ")
            freddie_speak("Is there anyting else i can assist you with sir? ")

        elif 'time' in command:
            print('With Pleasure Sir.')
            freddie_speak('With Pleasure Sir.')
            current_time = time.strftime("%I:%M %p")
            print(f'The time is {current_time}')
            freddie_speak(f'The time is {current_time}')
            print("Is there anyting else i can assist you with sir? ")
            freddie_speak("Is there anyting else i can assist you with sir? ")

        elif 'movie' in command:

            print('With Pleasure .Tell me the name of the movie, sir.')
            freddie_speak('With Pleasure . Tell me the name of the movie, sir.')
            movie_title = listen_command()
            
            if movie_title:
                print("Which platform would you like to search on? YouTube, Netflix, or Google?")
                freddie_speak("Which platform would you like to search on? YouTube, Netflix, or Google?")
                platform = listen_command()

            elif platform not in ['youtube', 'netflix','Netflix','google']:
                    print("I am sorry, I couldn't recognize the platform. Defaulting to YouTube.")
                    freddie_speak("I am sorry, I couldn't recognize the platform. Defaulting to YouTube.")
                    platform = 'youtube'
                    
            search_movie_online(movie_title, platform)



        elif any(word in command for word in ['name','who','introduce']):
            print('I am FREDDIE, your personal AI assistant.')
            freddie_speak('I am FREDDIE, your personal AI assistant.')
            
        elif any(word in command for word in ['nice to meet you','nice']):
            print('Nice to meet you too sir. ')
            freddie_speak('Nice to meet you too sir. ')

        elif any(word in command for word in ['what can you do','what tasks do you perform','what','what can you do for me','what else can you do for me']):
            print('I can assist you to many kinds of things like i can tell the time, open social media platforms for you, Play any kind of movie you want to watch, play songs to help you lighten your mood, and search for any topic or event related to your command you give to me. What would you like to focus on today?')
            freddie_speak('I can assit you to many kinds of things like i can tell the time, open social media platforms for you, Play any kind of movie you want to watch, play songs to help you lighten your mood, and search for any topic or event related to your command you give to me. What would you like to focus on today? ')

        elif any(word in command for word in ['shut', 'close', 'leave', 'thank', 'goodbye', 'nothing','iam good']):
            print('Ok sir. Have a nice day.')
            freddie_speak('Ok sir. Have a nice day.')
            break

        else:
            print("I am sorry, I do not understand that command.")
            freddie_speak("I am sorry, I do not understand that command.")
