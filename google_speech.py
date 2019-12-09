import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
'/home/wei/google/credentials/56952e1412ca.json')

# Instantiates a client
client = speech.SpeechClient(credentials=credentials)


### define write txt

def write_txt(name,txt):
    with open('txt/{}.txt'.format(name),'w') as tt:
        tt.write(txt)


### test video

ViPath = 'videos'
AuPath = 'audio'
ViList = []
AuList = []

# for videos in os.listdir(ViPath):
#     if videos.endswith('.mp4'):
#         ViList.append(videos)
#
#
# for vi in ViList:
#     # os.path.join(ViPath,vi)
#     au = vi.split('.')[0]+'.wav'
#     vipath = os.path.join(ViPath,vi)
#     aupath = os.path.join(AuPath,au)
#     AuList.append(au)
#     os.system('ffmpeg -i %s -ar 16000 %s'%(vipath,aupath))


# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
     'audio',
     'English.wav')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    audio_channel_count=2,
    language_code='en-US'          # en-GB en-US nl-NL

)

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:

    trans = result.alternatives[0].transcript
    write_txt('English',trans)
    print('Transcript: {}'.format(trans))





