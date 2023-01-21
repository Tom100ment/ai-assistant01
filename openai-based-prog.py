
import speech_recognition as sr
import openai
import os
import speech_recognition as sr


openai.api_key = " "  ## provide api key here



def transcribe_audio(audio_data):
    r = sr.Recognizer()
    audio = sr.AudioData(audio_data, sample_rate=44100, sample_width=2)
    text = r.recognize_google(audio)
    return text


def get_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = transcribe_audio(audio.get_wav_data())
    return text

def takeCommand():
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Listening...',
    )
    query = response.choices[0].text
    return query.strip()

def execute_command(text):
    if "open" in text:
        # code to open something
        file_or_website = text.replace("open", "").strip()
        os.system(f"start {file_or_website}")
    #elif "search" in text:
        # code to search for something
    # add more commands here
    elif "search" in text:
        # code to search for something
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"search {text} in wikipedia",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "play" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"search {text} in youtube",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "time" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"what is the time",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "date" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"what is the date",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "day" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"what is the day",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "month" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"what is the month",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "year" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"what is the year",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "weather" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"what is the weather",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "temperature" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"what is the temperature",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "search" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"search {text} in wikipedia",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "how are you" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"how are you",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "what is your name" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"what is your name",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "hey" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"hey",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "hello" in text:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"hello",
            max_tokens=2048
        )
        print(response.choices[0].text)
        os.system(f"start {response.choices[0].text}")
        
    elif "exit" in text:
        exit()


if __name__ == "__main__":
    while True:
        text = get_voice_command()
        execute_command(text)
        
    
