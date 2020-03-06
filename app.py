"""
The Bored QA
"""

#Importing flask module
from flask import Flask
import random
import csv

#Importing render_template to include html files and css.
from flask import render_template

#Give a name to the application, here its 'app'.
app = Flask(__name__)

#Route the application to go to a specific path.
@app.route("/",methods=['POST'])
def get_quotes():
    with open('quotes.csv','r') as csv_file: #Opens the file in read mode
        csv_reader = csv.reader(csv_file,delimiter='#')
        data = random.choice (list(csv_reader))
        selected_quote=''.join(data)
    
    # Pass the selected quote to the template.
    return render_template('quotes.html',quote=selected_quote)
    


#'app' is the instance for the Flask application.Run the application in a particular port!!
if __name__=='__main__' :
    app.run(host='0.0.0.0', port=5000, debug= True)