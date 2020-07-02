"""
The bored QA app starts here!
"""
from flask import Flask

app = Flask(__name__)

from the_bored_qa import views
