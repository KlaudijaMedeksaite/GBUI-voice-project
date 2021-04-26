from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeepL,
                             QCRI,
                             single_detection,
                             batch_detection)

# get supported languages and code
langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)
# print(langs_dict)
text = "Hi my name is Claudia and I speak english, babe"
translated = GoogleTranslator(
    source='auto', target='german').translate(text=text)

print(translated)

lang = single_detection(
    'labas, kaip sekasi?', api_key='71fe8105d0c5235edc5b77e8263b0ab2')
print(lang)

# https://github.com/nidhaloff/deep-translator
