# Using gTTS

import os
from dotenv import load_dotenv
load_dotenv()
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = 'en'
    
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text="Hello, how are you?"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# using ElevenLabs

import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Callum",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

# Setup Model

import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language = 'en'
    
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin": # macOS
            subprocess.run(["afplay", output_filepath])
        elif os_name == "Windows": # Windows
            subprocess.run(["ffplay", "-nodisp", "-autoexit", output_filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os_name == "Linux": # Linux
            subprocess.run(["aplay", output_filepath])
        else:
            raise OSError("Unsupported OS")
    except OSError as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text="Hello, this is Harsh, testing new function Autoplay"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Callum",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin": # macOS
            subprocess.run(["afplay", output_filepath])
        elif os_name == "Windows": # Windows
            subprocess.run(["ffplay", "-nodisp", "-autoexit", output_filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os_name == "Linux": # Linux
            subprocess.run(["aplay", output_filepath])
        else:
            raise OSError("Unsupported OS")
    except OSError as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")