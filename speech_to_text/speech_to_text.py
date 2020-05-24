"""
This script will be used to recognize the voice from the microphone and convert it into text
"""

import speech_recognition as sr
import logging


_logger = logging.getLogger(__name__)
_recognizer = sr.Recognizer()


def audio_speak():
    with sr.Microphone() as source:
        _logger.debug("Speak Anything and wait until the google cloud will recognize the voice")
        audio = _recognizer.listen(source)

    return audio


def recognize_voice():
    """
    This method will be used to recognize the voice from the input user.

    :return: Will return a String which will be the recognized voice.
    """

    text = None
    audio = audio_speak()
    if audio:
        try:
            text = _recognizer.recognize_google(audio)
            _logger.debug('You said: {}'.format(text))
        except Exception as exc:
            _logger.error("Google Cloud could not recognize your voice. The error is : {}".format(exc))
            raise
    else:
        _logger.error("The voice is not recognized, maybe you could try again. If this error persists please check "
                      "if you the google_cloud_voice_api is set correctly")

    return text







