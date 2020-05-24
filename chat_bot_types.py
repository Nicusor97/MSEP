"""This is the main script which will be executed when we want to talk with a chat bot """

from __future__ import absolute_import

import os
import sys
import six
import subprocess
import logging

_logger = logging.getLogger(__name__)
_THIS_SCRIPT_LOC = os.path.dirname(os.path.realpath(__file__))


def query_yes_no(question):
    valid = {"reddit-chatbot": "reddit-chatbot", "reddit": "reddit",
             "cornell-chatbot": "cornell-chatbot", "cornell": "cornell",
             "default-chatbot": "default-chatbot", "default": "default"}

    while True:
        sys.stdout.write(question + " [reddit-chatbot/cornell-chatbot/default-chatbot]")
        choice = six.moves.input().lower()
        if choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'reddit-chatbot', 'cornell-chatbot' or 'default-chatbot' "
                  "(or 'reddit' or 'cornell' or 'default')")


def main():
    _logger.info("Choose the chatbot type and run talk with a pretrained model for this type of chatbot")
    user_input = query_yes_no("What kind of chat bot would you like to talk to?")
    cwd = os.getcwd()
    if user_input == "reddit-chatbot" or user_input == "reddit":
        start_reddit_bot_path = os.path.join(cwd, 'start_reddit_chatbot.bat')
        deactivate_reddit_venv = os.path.join(cwd, 'deactivate_reddit_env.bat')
        try:
            _logger.info("*********** Start to talk with a pre-trained reddit chat bot")
            p = subprocess.Popen(start_reddit_bot_path)
            p.communicate()
        except subprocess.CalledProcessError:
            _logger.error("Here was a problem with the reddit chat bot initialization. If the error persists please"
                          "check the hparams for the reddit model")
        finally:
            subprocess.call(deactivate_reddit_venv)
            os.chdir(cwd)
    else:
        if user_input == "cornell-chatbot" or user_input == "cornell":
            _logger.debug("*********** Start the cornell chatbot ***********")
            start_cornell_bot_path = os.path.join(cwd, 'start_cornell_chatbot.bat')
            try:
                _logger.debug("*********** Start the cornell chatbot ***********")
                p = subprocess.Popen(start_cornell_bot_path)
                p.communicate()
            except subprocess.CalledProcessError:
                _logger.error("Here was a problem with the reddit chat bot initialization. If the error persists please"
                              "check the hparams for the reddit model")

        else:
            if user_input == "default-chatbot" or user_input == "default":
                start_default_chatbot = os.path.join(cwd, 'start_default_chatbot.bat')
                try:
                    _logger.info("*********** Start to talk with a pre-trained reddit chat bot")
                    p = subprocess.Popen(start_default_chatbot)
                    p.communicate()
                except subprocess.CalledProcessError:
                    _logger.error(
                        "Here was a problem with the reddit chat bot initialization. If the error persists please"
                        "check the hparams for the reddit model")
                finally:
                    os.chdir(cwd)
            else:
                raise Exception("The option introduced is not a valid one. Please try again ...")


if __name__ == "__main__":
    main()
