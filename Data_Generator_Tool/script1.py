from flask import Flask, render_template, request, flash, session, jsonify, redirect
from werkzeug.exceptions import HTTPException
from flask_session import Session
import os, sys
import random
import random, threading, webbrowser
import os
import sys
import faker
import app4

module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)
from  FileOperations import SaveFile
from  Generator import AddressDetails
from  Generator import CreditCardDetails
from  Generator import PersonalData
from  Generator import ProfessionalDetails
from  Generator import RandomDetails
from  Generator import BankCustomer
from  configparser import ConfigParser
import time


sess = Session()
SESSION_TYPE = 'memcache'
PEOPLE_FOLDER = os.path.join('static', 'css')

app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image1.jpg')
    return render_template("home.html", user_image = full_filename)

@app.route('/redirect/')
def test_redirect():
    return redirect("/")

@app.errorhandler(500)
def error_500(exception):
    return render_template("500.html")


@app.errorhandler(404)
def error_404(exception):
    return render_template("404.html")

@app.route('/', methods=["GET", "POST"])
def maindata_loop():
    count = request.form['Number_records']
    filename = request.form['File_Name']
    columns_no = request.form['Column_Number']
    print(count,filename,columns_no)
    if (count == "") or (filename == "") or (columns_no == ""):
        flash("Mandatory fields can't be empty, please try again..!","warning")
        clear_data()     
    else:
        app4.main_function()
    return clear_data()


def clear_data():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image1.jpg')
    return render_template("home.html", user_image = full_filename)
# *********************Take number of records****************************#
@app.route("/", methods=["GET", "POST"])
def take_number_of_records():
    count = request.form['Number_records']
    filename = request.form['File_Name']
    columns_no = request.form['Column_Number']
    try:
        count = int(count)
    except Exception as e:
        error_500(e)
    return count

def savefilename():
    filename = request.form['File_Name']
    return filename


def take_column_details():
    dataname = request.form['Column_Number']
    allColumns = dataname.split(",")
    for z in range (0, len(allColumns)):
        allColumns[z] = allColumns[z].strip()
    return allColumns
    

@app.route('/about/')
def about():
    return render_template("about.html")




if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)

    threading.Timer(1.25, lambda: webbrowser.open(url) ).start()

    app.run(port=port, debug=False)
