#pip install --upgrade "ibm-watson>=5.1.0"
import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
import threading
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('vVWMZcTRxRDvaaXyGGWH0pIHHcHqFa8X_NHona-UvxDM')
service = SpeechToTextV1(authenticator=authenticator)
service.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/8f450cc1-8340-40a1-a018-49a07ed81e9b')

models = service.list_models().get_result()
#print(json.dumps(models, indent=2))

model = service.get_model('en-US_BroadbandModel').get_result()
#print(json.dumps(model, indent=2))
def get_prediction_ibm(path):
    with open(join(dirname(__file__), path),
            'rb') as audio_file:
        results = service.recognize(
                audio=audio_file,
                content_type='audio/wav',
                timestamps=True,
                word_confidence=True).get_result()
            

    return results['results'][0]['alternatives'][0]['transcript']
