import extras
import mike
from deep_translator import (GoogleTranslator)
import main


def food(lan):
    language = extras.get_language_long(lan)
    print("\n\nFood in " + language)
    print("---------------------------------------------------------")

    numEn = ["bread", "chicken", "beef", "meat", "fruit",
             "vegetable", "apple", "banana", "tomato", "carrot", "pizza"]

    numL = []
    for n in numEn:
        numOth = GoogleTranslator(
            source='en', target=lan).translate(text=n)
        numOth = numOth.lower()
        numL.append(numOth)

    newP = 0
    i = 8
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


def clothes(lan):

    language = extras.get_language_long(lan)
    print("\n\nClothes in " + language)
    print("---------------------------------------------------------")

    numEn = ["blouse", "t-shirt", "hoodie", "pants", "jeans",
             "socks", "shoes", "belt", "hat", "scarf", "jacket"]

    numL = []
    for n in numEn:
        numOth = GoogleTranslator(
            source='en', target=lan).translate(text=n)
        numOth = numOth.lower()
        numL.append(numOth)

    newP = 0
    i = 9
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


def buildings(lan):
    language = extras.get_language_long(lan)
    print("\n\nBuildings in " + language)
    print("---------------------------------------------------------")

    numEn = ["shop", "church", "gym", "library", "townhall",
             "house", "apartment", "school", "university", "factory", "police station"]

    numL = []
    for n in numEn:
        numOth = GoogleTranslator(
            source='en', target=lan).translate(text=n)
        numOth = numOth.lower()
        numL.append(numOth)

    newP = 0
    i = 9
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
