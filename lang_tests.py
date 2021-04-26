import mike
import main
import extras
import random_test
from gtts import gTTS
from gtts.lang import tts_langs
from deep_translator import (GoogleTranslator,
                             single_detection,
                             batch_detection)


def test_l1(lan):
    language = extras.get_language_long(lan)
    count = 0
    tPoints = 0
    # Five questions to test the most basic words
    while count < 3:
        if count % 2 == 0:
            phrase = random_test.easy_noun()
        else:
            phrase = random_test.easy_adj()

        userAnswer = mike.record_audio(
            "What is " + phrase + " in " + language + "?", lan)
        translated = GoogleTranslator(
            source='auto', target=lan).translate(text=phrase)
        print("You said: " + userAnswer +
              "\n The correct answer was: " + translated)
        count = count + 1
        if len(userAnswer) > 0:
            if userAnswer in translated:
                print("+1")
                tPoints = tPoints + 1

    if tPoints > 2:
        tPoints = 2
    percent = (tPoints/2)*100
    return percent


def test_l2(lan):
    language = extras.get_language_long(lan)
    count = 0
    tPoints = 0
    # Five questions to test the most basic words
    while count < 4:
        phrase = random_test.simple_sentence()

        translated = GoogleTranslator(
            source='auto', target=lan).translate(text=phrase)
        if lan in tts_langs():
            mike.mike("Translate this phrase to English: ")
            mike.mike(translated, lan)
            answer = phrase
            userAnswer = mike.record_audio()
            print("You said: " + userAnswer +
                  "\n The correct answer was: " + phrase)
        else:
            # language not supported, alternative test, harder test
            answer = translated
            userAnswer = mike.record_audio(
                "What is " + phrase + " in " + language + "?", lan)
            print("You said: " + userAnswer +
                  "\n The correct answer was: " + translated)
            # extra 0.1 points per alternative question
            tPoints = tPoints + 0.1

        count = count + 1
        if len(userAnswer) > 0:
            if userAnswer in answer:
                print("+1")
                tPoints = tPoints + 1

    if tPoints > 3:
        tPoints = 3
    percent = (tPoints/3)*100
    print(percent)
    return percent
