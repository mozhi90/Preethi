import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('-ZtuQlno3meSW4yYU1r0ay3A29S-Ed6NaqmsfNnMC1xq')
language_translator = LanguageTranslatorV3(
    version='2022-03-07',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/a6450222-f6f2-47ae-9cc6-7e8f90f34712')

def english_to_french(english_text):
    translation = language_translator.translate(text=english_text, model_id = 'en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation = language_translator.translate(text=french_text, model_id = 'fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
