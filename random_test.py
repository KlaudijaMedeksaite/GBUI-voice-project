import random
from wonderwords import RandomSentence


def easy_adj():
    adj_file = open("test_words/english-adjectives.txt", "r")
    lines = adj_file.read().split('\n')
    return random.choice(lines)


def easy_noun():
    noun_file = open("test_words/english-nouns.txt", "r")
    lines = noun_file.read().split('\n')
    return random.choice(lines)


def simple_sentence():
    ssent_file = open("test_words/SimpleSentence.txt", "r")
    lines = ssent_file.read().split('\n')
    return random.choice(lines)


def difficult_sentence():
    dsent_file = open("test_words/MedSentence.txt", "r")
    lines = dsent_file.read().split('\n')
    return random.choice(lines)


if __name__ == "__main__":
    difficult_sentence()
