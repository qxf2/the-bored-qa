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
def get_quotes():
    with open('quotes.csv','r') as csv_file: #Opens the file in read mode
        csv_reader = csv.reader(csv_file,delimiter='#')
        data = random.choice (list(csv_reader))
        selected_quote=''.join(data)
    
    # Pass the selected quote to the template.
    return render_template('quotes.html',quote=selected_quote)
    
@app.route("/read",methods=['POST'])
def read_json():
    f = open('situational_questions.json')
    data = json.load(f)
    for i in data:
        print (i)
        return render_template('quotes.html',quote=i)
#'app' is the instance for the Flask application.Run the application in a particular port!!
if __name__=='__main__' :
    app.run(host='0.0.0.0', port=5000, debug= True)