"""
The Bored QA
"""

#Importing flask module
from flask import Flask
import random
import csv
import json
from flask import request
import open_questions
import explain_me

#Importing render_template to include html files and css.
from flask import render_template

#Give a name to the application, here its 'app'.
app = Flask(__name__)

#Route the application to go to a specific path.
@app.route("/")
def index():
    return render_template("quotes.html")

    
@app.route("/",methods=['POST'])
def read_json():
    "Read json or other questions files"
    files = []
    with open ('situational_questions.json') as f:
        data = json.load(f)    
        situational_questions = data["situational_questions"]
        files.append(situational_questions)
    
    # Include open questions
    files.append(open_questions.questions)

    # Include explain me questions
    files.append(explain_me.common_commands_list)

    chosen_file = random.choice(files)
    questions = random.choice(chosen_file) 
    question = questions['question'] 

    # Get the question type or set None if no type found
    question_type = questions.get('type',None)

    return render_template('quotes.html',question=question,question_type=question_type)



#'app' is the instance for the Flask application.Run the application in a particular port!!
if __name__=='__main__' :
    app.run(host='0.0.0.0', port=5000, debug= True)
