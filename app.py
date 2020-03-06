"""
The Bored QA

"""
#Importing flask module
from flask import Flask
import random
import csv
import pandas as pd
#Importing render_template to include html files and css.
from flask import render_template

#Give a name to the application, here its 'app'.
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("quotes.html")
#Route the application to go to a specific path.
# I think '/' is the default page.
@app.route("/",methods=['POST'])

#Add a function so that application  can run it... 1 function is always required...
def get_quotes():
    with open('quotes.csv','r') as csv_file: #Opens the file in read mode
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
        for i in data:
            print(i)
    
            # Select a random quote.
            selected_quote = random.choice(i)

    # Pass the selected quote to the template.
    return render_template('quotes.html',quote=selected_quote)


#'app' is the instance for the Flask application.Run the application in a particular port!!
if __name__=='__main__' :
    app.run(host='0.0.0.0', port=5000, debug= True)