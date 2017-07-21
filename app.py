#! usr/bin/python
from flask import Flask, render_template
from flask_uwsgi_websocket import GeventWebSocket

from datetime import datetime
from threading import Thread
from time import sleep

import numpy
import speech_recognition as sr
import webbrowser
import os
import sys

from colorama import init as init_colors, Fore as color

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

ws = GeventWebSocket(app)

@ws.route('/websocket')
def audio(ws):
   first_message = True
   total_msg = ""
   sample_rate = 0

   while True:
      msg = ws.receive()

      if first_message and msg is not None: # the first message should be the sample rate
         sample_rate = getSampleRate(msg)
         first_message = False
         print(color.YELLOW + 'Websocket started...')
         continue
      elif msg is not None:
         audio_as_int_array = numpy.frombuffer(msg, 'i2')
         print(color.GREEN + 'streaming audio')
         transcibe_audio(audio_as_int_array)
      else:
         break

def transcibe_audio(audio_stream):
    r = sr.Recognizer()
    with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file

    try:
        list = r.recognize(audio, True)                 # generate a list of possible transcriptions
        print("Possible transcriptions:")
        for prediction in list:
            print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
    except LookupError:                                 # speech is unintelligible
        print("Could not understand audio")

def startBrowser(url='http://127.0.0.1:5004'):
    sleep(5)
    webbrowser.open(url)

if __name__ == "__main__":
    server_options = {'debug': True, 
                      'port': os.environ.get('PORT', 5004), 
                      'host': os.environ.get('HOST', '0.0.0.0')}
    ui = Thread(target=startBrowser)
    webserver_thread = Thread(target=app.run, kwargs=server_options)
    if '-s' in sys.argv:
    	ui.start()
    webserver_thread.start()
    
