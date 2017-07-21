#! /usr/bin/python
import os
import unittest
import speech_recognition as sr

class TestSpeechRecognition(unittest.TestCase):
    def testPlayVideo(self):
        wav = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data', 'play_video.wav')

        r = sr.Recognizer()
        with sr.WavFile(wav) as source:
            audio = r.record(source)                        # extract audio data from the file

        try:
            list = r.recognize(audio, True)                 # generate a list of possible transcriptions
            print("Possible transcriptions:")
            for prediction in list:
                print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
        except LookupError:                                 # speech is unintelligible
            print("Could not understand audio")


if __name__ == '__main__':
    unittest.main()