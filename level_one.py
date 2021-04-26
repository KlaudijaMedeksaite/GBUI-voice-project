import extras
import mike
from deep_translator import (GoogleTranslator)
import main


def colours(lan):

    language = extras.get_language_long(lan)

    print("\n\nColours in " + language)
    print("---------------------------------------------------------")
    clrEn = ["white", "grey", "black", "brown", "red",
             "green", "blue", "yellow", "pink", "purple", "orange"]
    clrL = []
    for n in clrEn:
        clrOth = GoogleTranslator(
            source='en', target=lan).translate(text=n)
        clrOth = clrOth.lower()
        clrL.append(clrOth)

    i = 9
    newP = 0

    while i < 11:
        correct = False
        mike.mike(clrEn[i] + " in " + language + " is ")
        mike.mike(clrL[i], lan)

        mike.mike("Say " + clrEn[i] + " in " + language)
        user_input = mike.record_audio(lang=lan)
        user_input = user_input.lower()
        attempt = 0
        while correct == False:
            print("You said: " + user_input)
            if clrL[i] in user_input:
                print("Correct!")
                newP = newP + 1

                correct = True
            elif "quit" in user_input:
                main.save_progress()
                exit()
            else:
                if attempt < 3:
                    mike.mike("Let's try again, say ")
                    user_input = mike.record_audio(clrL[i], lan)
                else:
                    print("Let's move on")
                    correct = True
                attempt = attempt + 1

        i = i + 1

    return newP


def animals(lan):
    language = extras.get_language_long(lan)
    print("\n\nAnimals in " + language)
    print("---------------------------------------------------------")
    anmEn = ["dog", "cat", "cow", "horse",
             "lion", "monkey", "snake", "turtle", "bear", "tiger", "sheep"]
    anmL = []
    for n in anmEn:
        anmOth = GoogleTranslator(
            source='en', target=lan).translate(text=n)
        anmOth = anmOth.lower()
        anmL.append(anmOth)

    i = 9
    newP = 0
    while i < 11:
        correct = False
        mike.mike(anmEn[i] + " in " + language + " is ")
        mike.mike(anmL[i], lan)

        mike.mike("Say " + anmEn[i] + " in " + language)
        user_input = mike.record_audio(lang=lan)
        user_input = user_input.lower()
        attempt = 0
        while correct == False:
            print("You said: " + user_input)
            if anmL[i] in user_input:
                print("Correct!")
                newP = newP + 1
                correct = True
            elif "quit" in user_input:
                main.save_progress()
                exit()
            else:
                if attempt < 3:
                    mike.mike("Let's try again, say ")
                    user_input = mike.record_audio(anmL[i], lan)
                else:
                    print("Let's move on")
                    correct = True
                attempt = attempt + 1

        i = i + 1
    return newP


def numbers(lan):

    language = extras.get_language_long(lan)
    print("\n\nNumbers in " + language)
    print("---------------------------------------------------------")

    numEn = ["zero", "one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine", "ten"]

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
            elif str(i) in user_input:
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
