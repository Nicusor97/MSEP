import os
import re
import sys
import tensorflow as tf

from settings import PROJECT_ROOT
from chatbot.botpredictor import BotPredictor
from text_to_speech.text_to_speech import text_to_speech_recognizer
from speech_to_text.speech_to_text import recognize_voice

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def bot_ui():
    corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
    knbs_dir = os.path.join(PROJECT_ROOT, 'Data', 'KnowledgeBase')
    res_dir = os.path.join(PROJECT_ROOT, 'Data', 'Result')
    with tf.Session() as sess:
        predictor = BotPredictor(sess, corpus_dir=corp_dir, knbase_dir=knbs_dir,
                                 result_dir=res_dir, result_file='basic')
        # This command UI has a single chat session only
        session_id = predictor.session_data.add_session()

        print("Type exit and press enter to end the conversation.")
        # Waiting from standard input.
        sys.stdout.write("Say something to be recognized by the google cloud API voices\n")
        sys.stdout.write("> ")
        sys.stdout.flush()
        # question = recognize_voice()
        question = sys.stdin.readline()
        while question:
            if question.strip() == 'exit':
                break
            # import pdb
            # pdb.set_trace()
            result = re.sub(r'_nl_|_np_', '\n', predictor.predict(session_id, question)).strip()
            print(result)
            text_to_speech_recognizer(result)
            # print(re.sub(r'_nl_|_np_', '\n', predictor.predict(session_id, question)).strip())
            print("> ", end="")
            sys.stdout.flush()
            question = sys.stdin.readline()
            # question = recognize_voice()


if __name__ == "__main__":
    bot_ui()
