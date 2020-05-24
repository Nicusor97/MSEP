#!/usr/bin/env python

"""Google Cloud Text-To-Speech API sample application .

Example usage:
    python quickstart.py
"""

import os
from playsound import playsound
from google.cloud import texttospeech

_THIS_SCRIPT_LOC = os.path.dirname(os.path.realpath(__file__))


def text_to_speech_recognizer(text, voice_gender=None):
    """Synthesizes speech from the input string of text or ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    audio_files_path = os.path.join(_THIS_SCRIPT_LOC, 'audio_files')
    import random
    audio_file_generated_path = os.path.join(audio_files_path, 'output_{}.mp3'.format(
        random.randint(1, 10000000000)
    ))
    # The response's audio_content is binary.
    with open(audio_file_generated_path, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "{}"'.format(audio_file_generated_path))

    playsound('{}'.format(os.path.join(audio_file_generated_path)))

#
# if __name__ == '__main__':
#     text_to_speech_recognizer("Hello World !")
