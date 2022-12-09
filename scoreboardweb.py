#Written by Oskar L. Cobb, 2022
#Inteneded only for use in Christian Fellowship School

import random
import time
from datetime import datetime
from time import sleep as wait
from threading import *
from flask import Flask, Response, render_template, url_for
from turbo_flask import Turbo
import sys
import os

app = Flask(__name__)
turbo = Turbo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cfs_score')
def cfs_score():
    def generate():
        with open("cfs_score.txt", "r+") as cs:
            name = cs.read()
            print(name)
            yield str(name)
    return Response(generate(), mimetype='text') 

@app.route('/away_score')
def away_score():
    def generate():
        with open("away_score.txt", "r+") as cs:
            name = cs.read()
            print(name)
            yield str(name)
    return Response(generate(), mimetype='text') 

@app.route('/clock')
def clock():
    def countdown():
        s = open("times.txt", "r+")
        m = open("timem.txt", "r+")
        sec = s.read()
        min = m.read()
        n = str(min) + ":" + str(sec)
        yield str(n)
    return Response(countdown(), mimetype='text') 

@app.route('/cfteam')
def cfteam():
    def team():
        i = open("cfsbon.txt", "r+")
        i = i.read()
        i = str(i)
        n = open("cfteam.txt", "r+")
        n = n.read()
        n = "CFS <br>" + str(n) + '<br> <p style="font-size: 30px; margin-top: 5px; margin-right: 2px; margin-bottom: 0px; margin-left: 10px;">' + i + '</p>'
        yield str(n)
    return Response(team(), mimetype='text') 

@app.route('/awayteam')
def awayteam():
    def team():
        i = open("abon.txt", "r+")
        i = i.read()
        i = str(i)
        n = open("awayteam.txt", "r+")
        n = n.read()
        n = str(n) + '<br> <p style="font-size: 30px; margin-top: 5px; margin-right: 2px; margin-bottom: 0px; margin-left: 5px;">    ' + i + '</p>'
        yield str(n)
    return Response(team(), mimetype='text')

@app.route('/quarter')
def quarter():
    def quarter():
        n = open("sel.txt", "r+")
        n = n.read()
        n = str(n)
        yield str(n)
    return Response(quarter(), mimetype='text')

@app.route('/cfsbon')
def cfsbon():
    def cfsbon():
        n = open("cfsbon.txt", "r+")
        n = n.read()
        n = str(n)
        yield str(n)
    return Response(cfsbon(), mimetype='text')

@app.route('/abon')
def abon():
    def abon():
        n = open("abon.txt", "r+")
        n = n.read()
        n = str(n)
        yield str(n)
    return Response(abon(), mimetype='text')

if __name__ == '__main__':
    #os.system("python scoreboardqt.py &")
    app.run(debug=True, threaded=True)