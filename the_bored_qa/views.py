"""
The Bored QA
"""
import json
import os
import random
from flask import render_template, request
from the_bored_qa import app
#import open_questions
#import explain_me
#import architecture_diagrams

#Where are the data files stored?
CURR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURR_PATH, 'static', 'data')

def get_challenges_metadata():
    "Return the contents of the file holding challenges metadata"
    challenges_metadata = []
    challenges_metadata_src = os.path.join(DATA_PATH, 'challenge_metadata.json')
    with open(challenges_metadata_src) as file_handle:
        data = json.load(file_handle)
        challenges_metadata = data["challenges_meta"]

    return challenges_metadata


def get_template(challenge_type):
    "Return the template to use based on challenge type"
    template_name = 'error.html'
    challenges_metadata = get_challenges_metadata()
    for challenge_meta in challenges_metadata:
        if challenge_meta.get('type', '') == challenge_type.lower():
            template_name = challenge_meta.get('template', 'error.html')
            break

    return template_name

def get_datafile(challenge_type):
    "Return the template to use based on challenge type"
    datafile = None
    challenges_metadata = get_challenges_metadata()
    for challenge_meta in challenges_metadata:
        if challenge_meta.get('type', '') == challenge_type.lower():
            datafile = challenge_meta.get('data', None)
            break

    return datafile

def read_questions(datafile):
    "Return all the situtational questions"
    questions = []
    questions_src = os.path.join(DATA_PATH, datafile)
    with open(questions_src) as file_handle:
        data = json.load(file_handle)
        questions = data["challenges"]

    return questions

def get_challenges(challenge_type=None):
    "Get a list of all available challenges"
    challenges = []
    if challenge_type is None:
        #Collect challenges of all types
        challenges_metadata = get_challenges_metadata()
        for challenge_meta in challenges_metadata:
            challenges += read_questions(challenge_meta['data'])
    else:
        datafile = get_datafile(challenge_type)
        if datafile is not None:
            challenges += read_questions(datafile)

    return challenges

def get_next_question(challenge_type=None):
    "Pick a question"
    challenges = get_challenges(challenge_type)
    challenge = random.choice(challenges)
    challenge_template = get_template(challenge.get('type', ''))

    return render_template(challenge_template, challenge=challenge, endpoint=challenge_type)

@app.route("/", methods=['GET', 'POST'])
def read_json():
    "Read json or other questions files"
    if request.method == 'POST':
        return get_next_question()

    return render_template("index.html")

@app.route("/error")
def error_screen():
    "Display the error screen when something goes wrong"
    return render_template("error.html")

@app.route("/what")
def what():
    "What is this site?"

    return render_template("what.html")

@app.route("/why")
def why():
    "Why did we make this site"

    return render_template("why.html")

@app.route("/how")
def how():
    "How to use this site"

    return render_template("how.html")

@app.route("/faq")
def faq():
    "FAQs"

    return render_template("faq.html")

#----START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
