#!/usr/bin/env python

"""Google Cloud Text-To-Speech API sample application.

Example usage:
    python list_voices.py
"""


# [START tts_list_voices]
def list_voices():
    """Lists the available voices."""
    from google.cloud import texttospeech
    from google.cloud.texttospeech import enums
    client = texttospeech.TextToSpeechClient()

    # Performs the list voices request
    voices = client.list_voices()

    for voice in voices.voices:
        # Display the voice's name. Example: tpc-vocoded
        print('Name: {}'.format(voice.name))

        # Display the supported language codes for this voice. Example: "en-US"
        for language_code in voice.language_codes:
            print('Supported language: {}'.format(language_code))

        ssml_gender = enums.SsmlVoiceGender(voice.ssml_gender)

        # Display the SSML Voice Gender
        print('SSML Voice Gender: {}'.format(ssml_gender.name))

        # Display the natural sample rate hertz for this voice. Example: 24000
        print('Natural Sample Rate Hertz: {}\n'.format(
            voice.natural_sample_rate_hertz))
# [END tts_list_voices]


if __name__ == '__main__':
    list_voices()
