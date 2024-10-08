#!/usr/bin/python -i
#Written by Oskar L. Cobb, 2024
#Inteneded only for use in Christian Fellowship School
#version 3

import random
import time
from datetime import datetime
from time import sleep as wait
from threading import *
from flask import Flask, Response, render_template, url_for, redirect
from turbo_flask import Turbo
import sys
import os
#import obsws_python as obs

app = Flask(__name__)
turbo = Turbo(app)
html = 'index.html'
#cl = obs.ReqClient(host='localhost', port=4455, password='', timeout=3)
#cl.create_scene_item(1, "Browser")

@app.route('/')
def index():
    global html
    try:
        with open("index.html", "r+") as birdsarentreal:
            html = birdsarentreal.read()
        with open("templates/index.html", "w") as birdsarentreal: 
            birdsarentreal.write(html)
            birdsarentreal.close()
    except:
        print('Error: index.html not found. Returning to defaults.')
    print(html)
    return render_template("index.html")

@app.route('/reloaded')
def reloaded():
    with open("reload.txt",'r+') as rd:
        load = rd.read()
        print(load)
        yield load
        if load == "True":
            rd.write("False")
    return Response(reloaded(), mimetype='text')

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
        sec = int(float(sec))
        min = int(float(min))
        if sec <= 9:
            sec = "0" + str(sec)
        n = str(min) + ":" + str(sec)
        if int(min) == 0 and int(sec) <= 10 and int(sec) > 9 and int(sec) != 0:
            n = '<div style="float: right; font-size: 124px; text-align: right; vertical-align: 2px; color: red;">' + str(sec) + "</p>"
        elif int(min) == 0 and int(sec) <= 9 and int(sec) != 0:
            sec = sec.replace('0', '')
            n = '<div style="float: right; font-size: 124px; text-align: right; margin-right: 40px; vertical-align: 2px; color: red;">' + str(sec) + "</p>"
        else:
            n = '<div style="float: right; font-size: 124px; text-align: right; vertical-align: 2px;">' + n + "</p>"
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
        print(n)
        l = n.lower()
        if l == "jv" or l == "varsity" or l == "ms" or l == " girls jv" or l == " boys jv" or l == "girls varsity" or l == "boys varsity" or l == "girls ms" or l == "boys ms":
            n = "CFS <br>" + str(n) + '<br> <p style="font-size: 30px; margin-top: 5px; margin-right: 2px; margin-bottom: 0px; margin-left: 10px;">' + i + '</p>'
        else:
            n = '<div style=" float: left; margin-left: 10px; font-size: 52px; margin-top: 35px;">' + str(n) + '</div> <br> <p style="font-size: 30px; margin-top: 5px; margin-right: 2px; margin-bottom: 0px; margin-left: 10px;">' + i + '</p>' 
        print(n)
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
