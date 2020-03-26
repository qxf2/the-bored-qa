"""
The Bored QA
"""

#Importing flask module
from flask import Flask
import random
import csv
import json
from flask import request

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
    with open ('situational_questions.json') as f:
        data = json.load(f)    
        questions=data["situational_questions"]
        random_index=random.choice(questions)
        question=random_index["question"] 
        
    return render_template('quotes.html',question=question)



#'app' is the instance for the Flask application.Run the application in a particular port!!
if __name__=='__main__' :
    app.run(host='0.0.0.0', port=5000, debug= True)