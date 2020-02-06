import os
import csv
from flask import Flask, flash


def connect_with_file(filename):
    global file
    path=os.path.dirname(os.path.abspath(__file__))
    path=path.replace("FileOperations","").replace("Data_Generator_Tool","")
    print(path+filename+".csv")
    file = open(path+filename+".csv", 'w')
    

def open_Savedfolder():
    path = "C:\\Users\\JagadishBR\\Downloads\\app4-flask-website"
    path = os.path.realpath(path)
    os.startfile(path)

def writeDatatoFile(data):
    file.write(str(data))

def switchline():
    file.write("\n")

def addLineSeperator():
    file.write(',')

def saveFile():
    file.flush()


def closeFile():
    file.close()