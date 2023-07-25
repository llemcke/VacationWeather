import js2py
from formData import *
from flask import Flask, render_template, request
from api_calls import apiCalls
from db_script import dbAccess
from weather import Weather


locations=[]
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
   return render_template('index.html')

@app.route("/calculate",)
def calculate():
   
   
   print("works")
   return render_template('index.html')



if __name__ == '__main__':

   app.run(debug=True)






