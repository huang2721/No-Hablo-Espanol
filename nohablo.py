import requests
import sys
import json
from requests.auth import HTTPBasicAuth


def main():
    text_to_speech_api_key = 'rlYYbQbqwdrzFpndaGRbb8V7q7afmfFxKZ9IBeLQ5r7J'
    text_to_speech_url = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/0102f85d-c4cd-4cc3-928e-3c7482e01e0f'
    speech_to_text_api_key = 'QO6Rj8oWPbPJtN8cCETL4RsA5WHlDNAVEoWgAT_L33mH'
    speech_to_text_url = 'https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/88abb65f-7ae0-44fc-bb7f-a88e6d5031ac' 
    language_translator_api_key = 'uHSQ5qFc8bepT-FACslFzxsuD4btr-lnL27RgZwYcMY1'
    language_translator_url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/e25a4ca7-9b06-435d-a187-dea3e5d0030b'

    #speech-to-text
    url = speech_to_text_url + "/v1/recognize"
    headers = {'Content-Type': 'audio/flac'}
    auth = ("apikey", speech_to_text_api_key)
    data = open('./audio-file.flac', 'rb').read()

    r = requests.post(url, data =  data , auth = auth , headers = headers)
    text = r.json()['results'][0]['alternatives'][0]['transcript']
    
    #translator


    
if __name__ == "__main__":
    main()

    