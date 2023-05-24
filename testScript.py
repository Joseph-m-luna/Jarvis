import pyttsx3
from resemble import Resemble
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio


def demo1():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.say('pleased to meet you sir')
        engine.runAndWait()

def demo2():
    # download and load all models
    preload_models()

    # generate audio from text
    text_prompt = """
        Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
        But I also have other interests such as playing tic tac toe.
    """
    audio_array = generate_audio(text_prompt)

    # save audio to disk
    write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
    
    # play text in notebook
    Audio(audio_array, rate=SAMPLE_RATE)

demo2()