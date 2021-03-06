import random
import speech_recognition as sr
from gtts import gTTS
from gtts.lang import tts_langs
from deep_translator import (GoogleTranslator)
import playsound
import os
r = sr.Recognizer()


def mike(audio_string, language=False):

    # if user specifies a language, use it
    if language:
        tts = gTTS(text=audio_string, lang=language)
    else:
        tts = gTTS(text=audio_string, lang='en')

    # create audio file
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    # play it back
    playsound.playsound(audio_file)
    print(audio_string)
    # delete it
    os.remove(audio_file)


def record_audio(ask=False, lang=False):
    with sr.Microphone() as source:
        # if sentence/question included speak it
        if ask:
            mike(ask, lang)
        audio = r.listen(source)
        voice_data = ""
        try:
            # if language specified use it
            if lang:
                voice_data = r.recognize_google(audio, language=lang)
            else:
                voice_data = r.recognize_google(audio, language='en')

        except sr.UnknownValueError:
            mike("Sorry, didn't get that")
        except sr.RequestError:
            mike("Sorry, my speech service is down")
        return voice_data.lower()
