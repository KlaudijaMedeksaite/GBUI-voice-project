import time
from deep_translator import (GoogleTranslator)


def make_time():
    y = time.gmtime().tm_year
    y = str(y)
    d = time.gmtime().tm_yday
    d = str(d)
    h = time.gmtime().tm_hour
    h = str(h)
    m = time.gmtime().tm_min
    m = str(m)
    tim = y+""+d+""+h+""+m
    return tim


def get_language_long(val):
    langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)
    val = val.lower().strip()
    for key, value in langs_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


def get_language_short(key):
    langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)
    try:
        return langs_dict[key.lower().strip()]
    except:
        return "val doesn't exist"
