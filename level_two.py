import extras
import mike
from deep_translator import (GoogleTranslator)
import main

# The three parts of the second level


def greetings(lan):
    language = extras.get_language_long(lan)
    print("\n\nGreetings in " + language)
    print("---------------------------------------------------------")

    numEn = ["hi", "greetings", "good morning", "good afternoon", "good evening", "goodbye",
             "nice to meet you", "see you later", "see you soon", "how are you", "what's up"]

    numL = []
    for n in numEn:
        numOth = GoogleTranslator(
            source='en', target=lan).translate(text=n)
        numOth = numOth.lower()
        numL.append(numOth)

    newP = 0
    i = 0
    while i < 11:
        correct = False
        mike.mike(numEn[i] + " in " + language + " is ")
        mike.mike(numL[i], lan)

        mike.mike("Say " + numEn[i] + " in " + language)
        user_input = mike.record_audio(lang=lan)
        attempt = 0
        while correct == False:
            print("You said: " + user_input)
            if numL[i] in user_input:
                print("Correct!")
                newP = newP + 1
                correct = True
            elif "quit" in user_input:
                main.save_progress()
                exit()
            else:
                if attempt < 3:
                    mike.mike("Let's try again, say ")
                    user_input = mike.record_audio(numL[i], lan)
                else:
                    print("Let's move on")
                    correct = True
                attempt = attempt + 1
        i = i + 1
    return newP


def transport(lan):

    language = extras.get_language_long(lan)
    print("\n\nTransport in " + language)
    print("---------------------------------------------------------")

    numEn = ["cycling", "running", "walking", "driving", "flying",
             "sailing", "train", "boat", "airplane", "car", "bus"]

    numL = []
    for n in numEn:
        numOth = GoogleTranslator(
            source='en', target=lan).translate(text=n)
        numOth = numOth.lower()
        numL.append(numOth)

    newP = 0
    i = 0
    while i < 11:
        correct = False
        mike.mike(numEn[i] + " in " + language + " is ")
        mike.mike(numL[i], lan)

        mike.mike("Say " + numEn[i] + " in " + language)
        user_input = mike.record_audio(lang=lan)
        attempt = 0
        while correct == False:
            print("You said: " + user_input)
            if numL[i] in user_input:
                print("Correct!")
                newP = newP + 1
                correct = True
            elif "quit" in user_input:
                main.save_progress()
                exit()
            else:
                if attempt < 3:
                    mike.mike("Let's try again, say ")
                    user_input = mike.record_audio(numL[i], lan)
                else:
                    print("Let's move on")
                    correct = True
                attempt = attempt + 1
        i = i + 1

    return newP


def sports(lan):
    language = extras.get_language_long(lan)
    print("\n\nSports in " + language)
    print("---------------------------------------------------------")

    numEn = ["basketball", "football", "running", "volleyball", "tennis", "golf",
             "rugby", "hockey", "badminton", "baseball", "archery"]

    numL = []
    for n in numEn:
        numOth = GoogleTranslator(
            source='en', target=lan).translate(text=n)
        numOth = numOth.lower()
        numL.append(numOth)

    newP = 0
    i = 0
    while i < 11:
        correct = False
        mike.mike(numEn[i] + " in " + language + " is ")
        mike.mike(numL[i], lan)

        mike.mike("Say " + numEn[i] + " in " + language)
        user_input = mike.record_audio(lang=lan)
        attempt = 0
        while correct == False:
            print("You said: " + user_input)
            if numL[i] in user_input:
                print("Correct!")
                newP = newP + 1
                correct = True
            elif "quit" in user_input:
                main.save_progress()
                exit()
            else:
                if attempt < 3:
                    mike.mike("Let's try again, say ")
                    user_input = mike.record_audio(numL[i], lan)
                else:
                    print("Let's move on")
                    correct = True
                attempt = attempt + 1
        i = i + 1
    return newP
