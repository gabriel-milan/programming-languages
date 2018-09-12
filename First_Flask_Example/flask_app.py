# Imports
from flask import Flask
from file_parser import generateDict

# Instancing flask
app = Flask(__name__)

@app.route('/nota/<dre>')
def show_student_grade (dre):
    gradesDict = generateDict('grades.txt')
    print (gradesDict[dre])
    return "A nota de {} foi {}".format(gradesDict[dre][0], gradesDict[dre][1])