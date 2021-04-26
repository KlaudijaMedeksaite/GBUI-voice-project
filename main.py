import speech_recognition as sr
import time
from time import ctime
import playsound
import os
import random
from gtts import gTTS
from gtts.lang import tts_langs
from deep_translator import (GoogleTranslator,
                             single_detection,
                             batch_detection)
import pickle
import json
import random_test
import mike
import lang_tests
import level_one
import level_two
import level_three
import extras


parts = {"l1_colours": "0", "l1_numbers": "0", "l1_animals": "0", "l2_greetings": "0", "l2_transport": "0",
         "l2_sports": "0", "l3_food": "0", "l3_clothes": "0", "l3_buildings": "0"}
progress = {"name": "", "language": "",
            "level": "0", "lvlpts": "0", "partsDone": parts, "points": "0", "saveTime": "0"}


def set_l1(p1=False, p2=False, p3=False, all=False):
    if all:
        parts['l1_colours'] = '1'
        parts['l1_animals'] = '1'
        parts['l1_numbers'] = '1'
    else:
        if p1:
            parts['l1_colours'] = p1
        if p2:
            parts['l1_animals'] = p2
        if p3:
            parts['l1_numbers'] = p3


def set_l2(p1=False, p2=False, p3=False, all=False):
    if all:
        parts['l2_greetings'] = '1'
        parts['l2_transport'] = '1'
        parts['l2_sports'] = '1'
    else:
        if p1:
            parts['l2_greetings'] = p1
        if p2:
            parts['l2_transport'] = p2
        if p3:
            parts['l2_sports'] = p3


def set_l3(p1=False, p2=False, p3=False, all=False):
    if all:
        parts['l3_food'] = '1'
        parts['l3_clothes'] = '1'
        parts['l3_buildings'] = '1'
    else:
        if p1:
            parts['l3_food'] = p1
        if p2:
            parts['l3_clothes'] = p2
        if p3:
            parts['l3_buildings'] = p3


# LANG METHODS


def get_name():
    confirmed = False
    mike.mike('Welcome to uno lingo. What is your name?')
    name = mike.record_audio()
    print(name)
    while confirmed == False:
        voice_confirm = mike.record_audio(
            "Your name is " + name + ". Is that correct? Say yes to confirm")
        if "yes" in voice_confirm:
            confirmed = True
        else:
            name = mike.record_audio('What is your name?')
            print(name)

    mike.mike('Nice to meet you, ' + name+'.')
    mike.mike("My name is Mike.")
    return name


def choose_language():
    valid = False
    chosen = False
    langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)
    print("Languages available: ")
    for key in langs_dict:
        if langs_dict[key] in tts_langs():
            print(key)

    while valid == False:
        while chosen == False:
            choice = mike.record_audio("Please select a new language to learn")
            try:
                languageToLearn = extras.get_language_short(choice)
                if languageToLearn in tts_langs():
                    valid = True
                if valid == True:
                    response = mike.record_audio(
                        "You have chosen " + choice+", say yes to start learning this language.")
                    if 'yes' in response:
                        chosen = True
                        return languageToLearn
            except:
                return 0


# SETUP - LEVELS
def get_level():
    response = ''
    name = progress['name']
    mike.mike(
        name + ", would you like to take a test to find out what language level you are on?")
    while len(response) < 1:
        response = mike.record_audio()
        if 'yes' in response:
            level = test_Level()
        elif 'no' in response:
            mike.mike('What level are you on?')
            level = mike.record_audio()
            level = int(level)
            while level > 3 or level < 1:
                level = mike.record_audio(
                    "I'm sorry, please choose a level between one and four.")
    set_parts(level)
    progress['partsDone'] = parts
    return str(level)


def test_Level():
    percent = 0
    percent = lang_tests.test_l1(progress['language'])
    if percent >= 70:
        percent = lang_tests.test_l2(progress['language'])
        if percent >= 70:
            level = 3
        else:
            level = 2
    elif percent >= 40:
        level = 2
    else:
        level = 1

    mike.mike("The tests have determined you are at level " + str(level))
    return level


# PLAY - LEVELS


def begin_level():
    # "switch" for levels here
    if progress['level'] == '1':
        load_lvl_1()
    elif progress['level'] == '2':
        load_lvl_2()
    elif progress['level'] == '3':
        load_lvl_3()

    return 0


def set_parts(lvl, p1=False, p2=False, p3=False):

    if lvl == "1":
        set_l1(p1, p2, p3)
    elif lvl == "2":
        set_l1(all="1")
        set_l2(p1, p2, p3)
    elif lvl == "3":
        set_l1(all="1")
        set_l2(all="1")
        set_l3(p1, p2, p3)


def part_choice(lvl):

    user_input = "   "
    top = []
    topicStr = ""
    validChoice = False
    if lvl == '1':
        top.append(progress['partsDone']['l1_colours'])
        top.append(progress['partsDone']['l1_animals'])
        top.append(progress['partsDone']['l1_numbers'])

        topics = ["colours", "animals", "numbers"]
    elif lvl == '2':
        top.append(progress['partsDone']['l2_greetings'])
        top.append(progress['partsDone']['l2_transport'])
        top.append(progress['partsDone']['l2_sports'])

        topics = ["greetings", "transport", "sports"]
    elif lvl == '3':
        print("level: ", lvl)
        top.append(progress['partsDone']['l3_food'])
        top.append(progress['partsDone']['l3_clothes'])
        top.append(progress['partsDone']['l3_buildings'])

        topics = ["food", "clothes", "buildings"]

    else:
        Exception
    topic = []
    j = 0
    while j < 3:
        if top[j] == "0":
            topic.append(str(topics[j]))
            topicStr = topicStr + str(topics[j]) + ", "
        j = j+1

    topicStr = topicStr[:-2]

    if topicStr == "":
        return 10
    else:
        user_input = mike.record_audio(
            "Please select a topic. Your options include " + topicStr)

        while validChoice == False:
            print("You said: " + user_input)

            if user_input == "":
                user_input = "    "
            if user_input in topicStr:
                validChoice = True
                # return user_input
            else:
                if user_input == "    ":
                    user_input = mike.record_audio(
                        "That is not a valid option. Please select one of the following: " + topicStr)
                else:
                    user_input = mike.record_audio(
                        user_input + " is not a valid option. Please select one of the following: " + topicStr)
        x = 0
        while x < len(topics):
            if user_input in str(topics[x]):
                part_no = x
                return part_no
            x = x+1
        return part_no


# Easiest level, teach colours, numbers and animals

def load_lvl_1():
    save_progress()

    mike.mike("\n\nLevel One")
    print("---------------------------------------------------------")
    load_this = part_choice('1')
    if load_this == 0:
        l1_colours()
        load_lvl_1()
    if load_this == 1:
        l1_animals()
        load_lvl_1()
    if load_this == 2:
        l1_numbers()
        load_lvl_1()
    if load_this == 10:
        mike.mike("\n\nCongratulations, you have finished level one!")
        print("Total points this level: ", progress['points'])

        load_lvl_2()


def l1_numbers():
    points = progress['points']
    lan = progress['language']
    newP = level_one.numbers(lan)
    print("---------------------------------------------------------")
    print("Points this level: ", newP,
          "\nPossible points this level: 11")
    points = int(points)+newP
    print("Total points: ", points)
    points = str(points)
    # set this part to done so it won't be available again
    progress['partsDone']['l1_numbers'] = "1"
    progress['points'] = points


def l1_animals():
    points = progress['points']

    lan = progress['language']

    newP = level_one.animals(lan)
    print("---------------------------------------------------------")
    print("Points this level: ", newP,
          "\nPossible points this level: 11")
    points = int(points)+newP

    print("Total points: ", points)
    points = str(points)

    # set this part to done so it won't be available again
    progress['partsDone']['l1_animals'] = "1"
    progress['points'] = points


def l1_colours():
    points = progress['points']

    lan = progress['language']
    newP = level_one.colours(lan)
    print("---------------------------------------------------------")
    print("Points this level: ", newP,
          "\nPossible points this level: 11")
    points = int(points)+newP
    print("Total points: ", points)
    points = str(points)

    # set this part to done so it won't be available again
    progress['partsDone']['l1_colours'] = "1"
    progress['points'] = points


# Slightly more difficult level, teach more complex words and some adjectives


def load_lvl_2():
    save_progress()
    mike.mike("\n\nLevel Two")
    print("---------------------------------------------------------")
    load_this = part_choice('2')
    if load_this == 0:
        l2_greetings()
        load_lvl_2()
    if load_this == 1:
        l2_transport()
        load_lvl_2()
    if load_this == 2:
        l2_sports()
        load_lvl_2()
    if load_this == 10:
        mike.mike("\n\nCongratulations, you have finished level two!")
        print("Total points this level: ", progress['points'])
        load_lvl_3()

# Medium level, teach basic sentences


def l2_transport():
    points = progress['points']

    lan = progress['language']
    newP = level_two.transport(lan)
    print("---------------------------------------------------------")
    print("Points this level: ", newP,
          "\nPossible points this level: 11")
    points = int(points)+newP

    print("Total points: ", points)
    points = str(points)

    # set this part to done so it won't be available again
    progress['partsDone']['l2_transport'] = "1"
    progress['points'] = points


def l2_sports():
    points = progress['points']

    lan = progress['language']
    newP = level_two.sports(lan)
    print("---------------------------------------------------------")
    print("Points this level: ", newP,
          "\nPossible points this level: 11")
    points = int(points)+newP

    print("Total points: ", points)
    points = str(points)

    # set this part to done so it won't be available again
    progress['partsDone']['l2_sports'] = "1"
    progress['points'] = points


def l2_greetings():
    points = progress['points']

    lan = progress['language']
    newP = level_two.greetings(lan)
    print("---------------------------------------------------------")
    print("Points this level: ", newP,
          "\nPossible points this level: 11")
    points = int(points)+newP

    print("Total points: ", points)
    points = str(points)

    # set this part to done so it won't be available again
    progress['partsDone']['l2_greetings'] = "1"
    progress['points'] = points


def load_lvl_3():

    save_progress()

    mike.mike("\n\nLevel Three")
    print("---------------------------------------------------------")
    load_this = part_choice('3')
    if load_this == 0:
        l3_food()
        load_lvl_3()
    if load_this == 1:
        l3_clothes()
        load_lvl_3()
    if load_this == 2:
        l3_buildings()
        load_lvl_3()
    if load_this == 10:
        mike.mike("\n\nCongratulations, you have finished level three!")
        print("Total points this level: ", progress['points'])


def l3_food():
    points = progress['points']

    lan = progress['language']
    newP = level_three.food(lan)
    print("---------------------------------------------------------")
    print("Points this level: ", newP,
          "\nPossible points this level: 11")
    points = int(points)+newP

    print("Total points: ", points)
    points = str(points)

    # set this part to done so it won't be available again
    progress['partsDone']['l3_food'] = "1"
    progress['points'] = points


def l3_clothes():
    points = progress['points']

    lan = progress['language']
    newP = level_three.clothes(lan)
    print("---------------------------------------------------------")
    print("Points this level: ", newP,
          "\nPossible points this level: 11")
    points = int(points)+newP

    print("Total points: ", points)
    points = str(points)

    # set this part to done so it won't be available again
    progress['partsDone']['l3_clothes'] = "1"
    progress['points'] = points


def l3_buildings():
    points = progress['points']

    lan = progress['language']
    newP = level_three.buildings(lan)
    print("---------------------------------------------------------")
    print("Points this level: ", newP,
          "\nPossible points this level: 11")
    points = int(points)+newP

    print("Total points: ", points)
    points = str(points)

    # set this part to done so it won't be available again
    progress['partsDone']['l3_buildings'] = "1"
    progress['points'] = points


def graduate():
    mike.mike("Congratulations, you have completed the course")
    print("---------------------------------------------------------")

    user_answer = mike.record_audio("Say new game to learn a new language.")
    return user_answer


# SAVES


def save_progress():
    res = load_progress(progress['name'])
    newPrint = res

    check = "'language': " + "'"+str(progress['language']+"'")
    progress['saveTime'] = extras.make_time()

    if(not(check in str(res))):
        try:
            with open('saves/'+progress['name'] + '.txt', 'ab+') as f:
                pickle.dump(progress, f)

        except:
            os.makedirs("saves")
            with open('saves/'+progress['name'] + '.txt', 'ab+') as f:
                pickle.dump(progress, f)
    else:
        with open('saves/'+progress['name'] + '.txt', 'wb') as f:
            pickle.dump("", f)

        x = 0
        while x < len(newPrint):
            if check in str(newPrint[x]):
                if str(progress['saveTime'] >= newPrint[x]['saveTime']):
                    if progress in newPrint:
                        del newPrint[x]
                    else:
                        newPrint[x] = progress

            x = x + 1
        for n in newPrint:
            with open('saves/'+progress['name'] + '.txt', 'ab+') as f:
                pickle.dump(n, f)


def load_progress(n):
    results = []
    try:
        with open('saves/'+n + '.txt', 'rb') as f:
            try:
                while True:
                    results.append(pickle.load(f))
            except EOFError:
                pass
        return results
    except:
        print("no saved file")
        return 0


def check_saves(name, language=False):
    langsSaved = []
    savedP = load_progress(name)
    if language:
        try:
            savedP = str(savedP).replace('\'', '\"')
            ps = json.loads(str(savedP))
            for p in ps:
                if p['language'] == language:
                    level = p['level']
                    progress['partsDone'] = p['partsDone']
            return level
        except:
            return 0
    else:
        try:
            savedP = str(savedP).replace("'',", "")
            savedP = str(savedP).replace('\'', '\"')
            ps = json.loads(str(savedP))
            for p in ps:
                langsSaved.append(p['language'])
            return langsSaved
        except:
            return langsSaved


def choose_save(saves):
    valid = False

    mike.mike("saved languages include ")
    for s in saves:
        mike.mike(extras.get_language_long(s))
    language = mike.record_audio(
        "Which language would you like to continue learning?")
    print("You have chosen: " + language)
    while valid == False:
        try:
            language = extras.get_language_short(language)
        except:
            return

        if language in saves:
            level = check_saves(progress['name'], language)
            progress['language'] = language
            progress['level'] = str(level)
            valid = True
        else:
            language = mike.record_audio(
                "I'm sorry, that is not a valid option. Choose a different language.")
            print("You have chosen: " + language)

# PART METHODS


def startup():
    # get users name
    name = get_name()
    progress['name'] = name

    # check if user has saved file
    saves = check_saves(name)
    if saves:
        answered = False
        answer = ""
        while answered == False:
            answer = mike.record_audio(
                "You have saved progress available. Would you like to continue progress?")
            if "yes" in answer:
                answered = True
                progBool = True
            if "no" in answer:
                answered = True
                progBool = False

    else:
        progBool = False
    if progBool == True:
        # if yes - ask which save to load
        choose_save(saves)
        return
    else:
        # ask language to learn
        progress['language'] = choose_language()
        progress['level'] = get_level()
        save_progress()
        return

# TEST METHODS


def print_prog():
    print("Name: " + progress['name'])
    print("Language: " + progress['language'])
    print("Level: " + progress['level'])
    print("Parts: ", progress['partsDone'])


def easy_set(name=False, lang=False, level=False):
    if name and lang and level:
        progress['name'] = name
        progress['language'] = lang
        progress['level'] = level
    else:
        progress['name'] = "John"
        progress['language'] = 'es'
        progress['level'] = '1'

    set_parts(progress['level'])


if __name__ == "__main__":
    answer = "new game"
    while(answer == "new game"):
        startup()
        begin_level()
        answer = graduate()
        if answer == "quit game":
            mike.mike("Goodbye, ", progress['name'])
            exit()
