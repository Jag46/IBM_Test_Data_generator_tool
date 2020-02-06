from flask import Flask, render_template, request, flash, session
from flask_session import Session
import os, sys
import random
import random, threading, webbrowser
import os
import sys
import faker
import script1


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

config = ConfigParser()
config.read("Configuration.cfg")
configmethod = ConfigParser()
configmethod.read("MethodMapping.cfg")

def main_function():
# *********************Take number of records****************************#
    count= script1.take_number_of_records()

#  Take File Name from User
    filename= script1.savefilename()

#  Connect with File
    SaveFile.connect_with_file(filename)


    start = time.perf_counter()

    allColumns = script1.take_column_details()
    columnCount=len(allColumns)
    counter=0
    global methodName
    for j in allColumns:
        counter=counter+1
        try:
            methodName = config.get('DataDetails',str(j))
            methodName = str(methodName).replace("get_","").replace("()","")
        except Exception as e:
            script1.error_500(e)
        methodName = methodName.capitalize()
        SaveFile.writeDatatoFile(methodName)
        if(counter!=columnCount):
            SaveFile.addLineSeperator()
    SaveFile.switchline()
    SaveFile.saveFile()

    for i in range(1,count+1):
        counter = 0
        for j in allColumns:
            counter = counter + 1
            try:
                methodName = config.get('DataDetails',str(j))
                methodName=configmethod.get('DataDetails',methodName)
            except Exception as e:
                script1.error_500(e)
            result=eval(methodName)
            SaveFile.writeDatatoFile(result)
            if (counter != columnCount):
                SaveFile.addLineSeperator()
        SaveFile.switchline()
    SaveFile.saveFile()
    SaveFile.closeFile()
    value = (time.perf_counter() - start)
    value1 = ("%.2f" % round(value,2))
    print(value1)
    value1 = str(value1)
    print("Time Taken by Script(in seconds) : "+(value1))
    flash("Data generated successfully in :"+value1+" seconds","success")
    SaveFile.open_Savedfolder()