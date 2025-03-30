# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"

    print("Input Text:", input_text)  # Debugging input text
    print("Output File Path:", output_filepath)  # Debugging output file path

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    print(f"Audio saved to {output_filepath}")

# Example usage
input_text = "Hi, let's code with me!"
output_filepath = "gtts_testing.mp3"  # Replace with a full path if needed
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath=output_filepath)

import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    # Create the audio object
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    print(f"Audio saved to {output_filepath}")

    # Play the audio file using pydub
    try:
        audio = AudioSegment.from_file(output_filepath, format="mp3")
        play(audio)
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Define input text and output file path
input_text = "Hi, let's code with me, autoplay testing!"
output_filepath = "gtts_testing_autoplay.mp3"

# Call the function
text_to_speech_with_gtts(input_text=input_text, output_filepath=output_filepath)