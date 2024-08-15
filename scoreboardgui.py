#Written by Oskar L. Cobb, 2023
#Inteneded only for use in Christian Fellowship School
#version 3

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os
import math
from time import sleep
import time
import threading
import keyboard
from tkinter.messagebox import showinfo, showerror, askquestion
import random
import time
from datetime import datetime
from threading import *
from flask import Flask, Response, render_template, url_for
from turbo_flask import Turbo
import sys
import os
import requests
import json
import urllib.request
from os import remove
from sys import argv

#Win build only
#os.chdir(sys._MEIPASS)

global killtime
killtime = 0
root = tk.Tk()
root.resizable(False, False)
#root.iconbitmap("cfs.ico")
app = Flask(__name__)
turbo = Turbo(app)

default = """<!--Written by Oskar L. Cobb, 2023-->
<!--Inteneded only for use in Christian Fellowship School-->

<!DOCTYPE html>
<head>
    <meta name="viewport" content="width=1720, initial-scale=1">
    <title>CFS Scoreboard</title>
    {{ turbo() }}
    <style>
    .scoreboard {
        background: #ffffff;
        float:left;
        height: 100%;
        width: 100%;
    }
    p.clear {
        clear: left;
    }
    </style>
    <link rel="icon" type="image/png" href="https://cfsknights.org/wp-content/uploads/2022/06/cfs-site-icon-150x150.png">
 </head>
 <body style="background-color: #00ff00;">
    <div class="scoreboard">
        <image style="float: left;"src="https://cfsknights.org/wp-content/uploads/2022/06/cfs-site-icon-150x150.png"/>
        <!--<p style="display: inline-block; position: relative; top: -10%; left: 15%; font-size: 80px; ">CFS</p>-->
        <div id="cfteam" style=" float: left; font-size: 42px; margin-left: 50px;"></div>
        <!--<div id="cfsbon" style="float: left; margin-left: 80px; margin-top: 80px; font-size: 24px;"></div>-->
        <div id="cfs_score" style=" float: left; border: 5px solid black; margin-left: 50px; font-size: 124px;"></div>
        <div id="awayteam" style=" float: left; margin-left: 80px; font-size: 52px; margin-top: 35px;"></div>
        <!--<div id="abon" style="float: left; margin-left: 80px; margin-top: 80px; font-size: 24px;"></div>-->
        <div id="away_score" style=" float: left; border: 5px solid black; margin-left: 40px; font-size: 124px;"></div>
        <div id="clock" style="float: right; font-size: 124px; text-align: right; vertical-align: 2px;></div>"></div>
        <div id="quarter" style="float: right; font-size: 124px; vertical-align: 2px; margin-right: 70px;"></div>
    </div>
    <script>
    var cfs_score = document.getElementById("cfs_score");
    var clock = document.getElementById("clock");
    var siteWidth = 1720;
    var scale = screen.width /siteWidth;

    document.querySelector('meta[name="viewport"]').setAttribute('content', 'width='+siteWidth+', initial-scale='+scale+'');
    setInterval(() => {
            fetch("{{ url_for('reloaded') }}")
            .then(response => {
                    response.text().then(t => {i = t})
                    console.log(i)
                    if (i === "True") {
                        window.location.replace("{{ url_for('index') }}");
                        console.log("yes")
                    }else{
                        console.log("no")
                    }
                });
            }, 1000); 
    setInterval(() => {
        fetch("{{ url_for('cfs_score') }}")
        .then(response => {
                response.text().then(t => {cfs_score.innerHTML = t})
            });
        }, 1000);  
    setInterval(() => {
        fetch("{{ url_for('clock') }}")
        .then(response => {
                response.text().then(t => {clock.innerHTML = t})
            });
        }, 1000);  
    setInterval(() => {
        fetch("{{ url_for('cfteam') }}")
        .then(response => {
                response.text().then(t => {cfteam.innerHTML = t})
            });
        }, 1000);
    setInterval(() => {
        fetch("{{ url_for('away_score') }}")
        .then(response => {
                response.text().then(t => {away_score.innerHTML = t})
            });
        }, 1000);  
    setInterval(() => {
        fetch("{{ url_for('awayteam') }}")
        .then(response => {
                response.text().then(t => {awayteam.innerHTML = t})
            });
        }, 1000);
    setInterval(() => {
        fetch("{{ url_for('quarter') }}")
        .then(response => {
                response.text().then(t => {quarter.innerHTML = t})
            });
        }, 1000);
    /*setInterval(() => {
        fetch("{{ url_for('cfsbon') }}")
        .then(response => {
                response.text().then(t => {cfsbon.innerHTML = t})
            });
        }, 1000);
    setInterval(() => {
        fetch("{{ url_for('abon') }}")
        .then(response => {
                response.text().then(t => {abon.innerHTML = t})
            });
        }, 1000);*/
    </script>
 </body>

"""

def wait(x):
    while True:
        return

def clock():
    if killtime == 0:
        return
    if killtime == 1:
        cont = 1
    while killtime == 1:
        if cont == 0:
            break

        ts = open("times.txt",'r+')
        tm = open("timem.txt",'r+')
        #sm = open("timesm.txt",'r+')
        i = sm.get()
        print(i)
        if str(i) == "start minute" or str(i) == "":
            i = "0"
        print(i)
        if int(i) <= 9:
            if int(str(i)[0]) != 0:
                i = "0" + str(i)
        print(i)
        #ss= open("timess.txt",'r+')
        x = ss.get()
        print(x)
        if str(x) == "start second" or str(x) == "":
            x = "0"
        print(x)
        if int(x) <= 9:
            if int(str(i)[0]) != 0:
                x = "0" + str(x)
        print(x)
        #em = open("timeem.txt",'r+')
        y = em.get()
        print(y)
        if str(y) == "end minute" or str(y) == "":
            y = "0"
        print(y)
        if int(y) <= 9:
            if int(str(i)[0]) != 0:
                y = "0" + str(y)
        print(y)
        #es = open("timees.txt",'r+')
        z = es.get()
        print(z)
        if str(z) == "end second" or str(z) == "":
            z = "0"
        print(z)
        if int(z) <= 9:
            if int(str(i)[0]) != 0:
                z = "0" + str(z)
        print(z)

        if int(i) > int(y):
            countup = False
            s = False
        elif int(i) < int(y):
            countup = True
            s = False
        elif int(i) == int(y):
            if int(x) > int(z):
                countup = False
                s = True
            elif int(x) < int(z):
                countup = True
                s = True
            else:
                return

        print(countup)
        print(s)
                
        if int(i) <= 0 and int(x) <= 0:
            timeleft = False
        else:
            timeleft = True
            
        if countup == False and s == False:
            z = float(z) + 0.1
            g = time.time()
            t = int(i)*60 + int(x)
            nowt = t
            valint = int(val)
            print("valint: " + str(valint))
            if val != 0 and valint == nowt:
                t = val
                print(str(val) + "\t" + str(nowt))
            print(t)
            print("t: " + str(t))
            while int(i) > int(y):
                i = time.time()
                e = i - g
                rem = float(t) - e
                i = int(rem/60)
                math1 = rem/60 - int(rem/60)
                math2 = math1 * 60
                x = float(math2)
                if killtime == 0:
                    cont = 0
                    return
                if int(x) <= 9:
                    x = "0" + str(x)
                i = str(i)
                x = str(x)
                tm.seek(0)
                tm.write(str(i))
                tm.truncate()
                ts.seek(0)
                ts.write(str(x))
                ts.truncate()
                print(str(i) + ":" + str(x))
                if float(i) <= 0 and float(x) <= 0:
                    #i = math.trunc(i)
                    #x = math.trunc(x)
                    i = str(i)
                    x = str(x)
                    tm.seek(0)
                    tm.write(i)
                    tm.truncate()
                    ts.seek(0)
                    ts.write(x)
                    ts.truncate()
                    print(str(i) + ":" + str(x))
                    return
            while float(x) > float(z):
                i = time.time()
                e = i - g
                rem = t - (e)
                i = int(rem/60)
                math1 = rem/60 - int(rem/60)
                math2 = math1 * 60
                x = float(math2)
                if killtime == 0:
                    cont = 0
                    return
                if float(x) <= 0.1:
                    x = 0
                    return
                #-------------
                i = str(i)
                x = str(x)
                tm.seek(0)
                tm.write(str(i))
                tm.truncate()
                ts.seek(0)
                ts.write(str(x))
                ts.truncate()
                print(str(i) + ":" + str(x))
                if float(i) == 0 and float(x) == 0:
                    print(str(i) + ":" + str(x))
                    return
        elif countup == False and s == True:
            z = float(z) + 0.1
            g = time.time()
            t = int(i)*60 + int(x)
            nowt = t
            valint = int(val)
            while float(x) > float(z):
                i = time.time()
                e = i - g
                rem = t - (e)
                i = int(rem/60)
                math1 = rem/60 - int(rem/60)
                math2 = math1 * 60
                x = float(math2)
                if killtime == 0:
                    cont = 0
                    return
                if float(x) <= 0.1:
                    x = 0
                    return
                #-------------
                i = str(i)
                x = str(x)
                tm.seek(0)
                tm.write(str(i))
                tm.truncate()
                ts.seek(0)
                ts.write(str(x))
                ts.truncate()
                print(str(i) + ":" + str(x))
                if float(i) == 0 and float(x) == 0:
                    print(str(i) + ":" + str(x))
                    return
        elif countup == True and s == True:
            z = float(z) + 0.1
            while float(x) > float(z):
                i = time.time()
                e = i - g
                rem = t + (e)
                i = int(rem/60)
                math1 = rem/60 - int(rem/60)
                math2 = math1 * 60
                x = float(math2)
                if killtime == 0:
                    cont = 0
                    return
                if float(x) <= 0.1:
                    x = 0
                    return
                #-------------
                i = str(i)
                x = str(x)
                tm.seek(0)
                tm.write(str(i))
                tm.truncate()
                ts.seek(0)
                ts.write(str(x))
                ts.truncate()
                print(str(i) + ":" + str(x))
                if float(i) == 0 and float(x) == 0:
                    print(str(i) + ":" + str(x))
                    return
        elif countup == True and s == False: 
            z = float(z) + 0.1
            g = time.time()
            t = int(i)*60 + int(x)
            nowt = t
            valint = int(val)
            print("valint: " + str(valint))
            if val != 0 and valint == nowt:
                t = val
                print(str(val) + "\t" + str(nowt))
            print(t)
            print("t: " + str(t))
            while int(i) > int(y):
                i = time.time()
                e = i - g
                rem = float(t) + e
                i = int(rem/60)
                math1 = rem/60 - int(rem/60)
                math2 = math1 * 60
                x = float(math2)
                if killtime == 0:
                    cont = 0
                    return
                if int(x) <= 9:
                    x = "0" + str(x)
                i = str(i)
                x = str(x)
                tm.seek(0)
                tm.write(str(i))
                tm.truncate()
                ts.seek(0)
                ts.write(str(x))
                ts.truncate()
                print(str(i) + ":" + str(x))
                if float(i) <= 0 and float(x) <= 0:
                    #i = math.trunc(i)
                    #x = math.trunc(x)
                    i = str(i)
                    x = str(x)
                    tm.seek(0)
                    tm.write(i)
                    tm.truncate()
                    ts.seek(0)
                    ts.write(x)
                    ts.truncate()
                    print(str(i) + ":" + str(x))
                    return
            while float(x) > float(z):
                i = time.time()
                e = i - g
                rem = t + (e)
                i = int(rem/60)
                math1 = rem/60 - int(rem/60)
                math2 = math1 * 60
                x = float(math2)
                if killtime == 0:
                    cont = 0
                    return
                if float(x) <= 0.1:
                    x = 0
                    return
                #-------------
                i = str(i)
                x = str(x)
                tm.seek(0)
                tm.write(str(i))
                tm.truncate()
                ts.seek(0)
                ts.write(str(x))
                ts.truncate()
                print(str(i) + ":" + str(x))
                if float(i) == 0 and float(x) == 0:
                    print(str(i) + ":" + str(x))
                    return
        break

def killti():
    sms = open("timem.txt", "r+")
    sms = sms.read()
    sss = open("times.txt", "r+")
    sss = sss.read()
    global killtime 
    killtime = 0
    tim()

def tim():
    global killtime
    if killtime == 1:
        killtime = 0
        timr = threading.Thread(target=clock)
        timr.join()
        tim()
    elif killtime == 0:
        #global killtime
        killtime = 1
        print(killtime)
        timr = threading.Thread(target=clock)
        timr.start()

def clearsm(e):
    f = str(sm.get())
    if f == 'start minute':
        sm.delete(0,"end")
    else:
        return

def clearss(e):
    f = str(ss.get())
    if f == 'start second':
        ss.delete(0,"end")
    else:
        return

def clearem(e):
    f = str(em.get())
    if f == 'end minute':
        em.delete(0,"end")
    else:
        return

def cleares(e):
    f = str(es.get())
    if f == 'end second':
        es.delete(0,"end")
    else:
        return

def tsm(e):
    f = str(sm.get())
    if f == '':
       sm.insert(0, "start minute") 
    else:
        return

def tss(e):
    f = str(ss.get())
    if f == '':
        ss.insert(0, "start second")
    else:
        return

def tem(e):
    f = str(em.get())
    if f == '':
        em.insert(0, "end minute")
    else:
        return

def tes(e):
    f = str(es.get())
    if f == '':
        es.insert(0, "end second")
    else:
        return

def cfsscore(e):
    i = cfscore.get()
    if i == '':
        i = 0
    with open("cfs_score.txt",'r+') as pv:
        data = float(pv.read())
        print(data)
        c = int(i)
        print(c)
        if c <= 9: 
            z = math.trunc(c)
            z = str("0") + str(z)
            print(z)
            pv.seek(0)
            pv.write(z)
            pv.truncate()
        else:
            c = math.trunc(c)
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()

def awayscore1(e):
    i = awayscore.get()
    if i == '':
        i = 0
    with open("away_score.txt",'r+') as pv:
        data = float(pv.read())
        print(data)
        c = int(i)
        print(c)
        if c <= 9: 
            z = math.trunc(c)
            z = str("0") + str(z)
            print(z)
            pv.seek(0)
            pv.write(z)
            pv.truncate()
        else:
            c = math.trunc(c)
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()

def plus1cfs():
    with open("cfs_score.txt",'r+') as pv:
        data = float(pv.read())
        print(data)
        c = data + 1
        print(c)
        if c <= 9: 
            z = math.trunc(c)
            z = str("0") + str(z)
            print(z)
            pv.seek(0)
            pv.write(z)
            pv.truncate()
            cfscore.delete(0,"end")
            cfscore.insert(0, z)
        else:
            c = math.trunc(c)
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            cfscore.delete(0,"end")
            cfscore.insert(0, c)

def plus2cfs():
    with open("cfs_score.txt",'r+') as pv:
        data = float(pv.read())
        print(data)
        c = data + 2
        print(c)
        if c <= 9: 
            z = math.trunc(c)
            z = str("0") + str(z)
            print(z)
            pv.seek(0)
            pv.write(z)
            pv.truncate()
            cfscore.delete(0,"end")
            cfscore.insert(0, z)
        else:
            c = math.trunc(c)
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            cfscore.delete(0,"end")
            cfscore.insert(0, c)

def plus3cfs():
    with open("cfs_score.txt",'r+') as pv:
        data = float(pv.read())
        print(data)
        c = data + 3
        print(c)
        if c <= 9: 
            z = math.trunc(c)
            z = str("0") + str(z)
            print(z)
            pv.seek(0)
            pv.write(z)
            pv.truncate()
            cfscore.delete(0,"end")
            cfscore.insert(0, z)
        else:
            c = math.trunc(c)
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            cfscore.delete(0,"end")
            cfscore.insert(0, c)

def plus1aw():
    with open("away_score.txt",'r+') as pv:
        data = float(pv.read())
        print(data)
        c = data + 1
        print(c)
        if c <= 9: 
            z = math.trunc(c)
            z = str("0") + str(z)
            print(z)
            pv.seek(0)
            pv.write(z)
            pv.truncate()
            awayscore.delete(0,"end")
            awayscore.insert(0, z)
        else:
            c = math.trunc(c)
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            awayscore.delete(0,"end")
            awayscore.insert(0, c)

def plus2aw():
    with open("away_score.txt",'r+') as pv:
        data = float(pv.read())
        print(data)
        c = data + 2
        print(c)
        if c <= 9: 
            z = math.trunc(c)
            z = str("0") + str(z)
            print(z)
            pv.seek(0)
            pv.write(z)
            pv.truncate()
            awayscore.delete(0,"end")
            awayscore.insert(0, z)
        else:
            c = math.trunc(c)
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            awayscore.delete(0,"end")
            awayscore.insert(0, c)

def plus3aw():
    with open("away_score.txt",'r+') as pv:
        data = float(pv.read())
        print(data)
        c = data + 3
        print(c)
        if c <= 9: 
            z = math.trunc(c)
            z = str("0") + str(z)
            print(z)
            pv.seek(0)
            pv.write(z)
            pv.truncate()
            awayscore.delete(0,"end")
            awayscore.insert(0, z)
        else:
            c = math.trunc(c)
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            awayscore.delete(0,"end")
            awayscore.insert(0, c)

def min1cfs():
    try:
        with open("cfs_score.txt",'r+') as pv:
            data = float(pv.read())
            print(data)
            c = data - 1
            print(c)
            if c <= 9: 
                z = math.trunc(c)
                z = str("0") + str(z)
                print(z)
                pv.seek(0)
                pv.write(z)
                pv.truncate()
                cfscore.delete(0,"end")
                cfscore.insert(0, z)
            else:
                c = math.trunc(c)
                c = str(c)
                pv.seek(0)
                pv.write(c)
                pv.truncate()
                cfscore.delete(0,"end")
                cfscore.insert(0, c)
            print(c)
            if int(c) < 0 :
                with open("cfs_score.txt",'r+') as pv:
                    c = 0
                    c = str(c) + "0"
                    pv.seek(0)
                    pv.write(c)
                    pv.truncate()
                    cfscore.delete(0,"end")
                    cfscore.insert(0, c) 
    except ValueError:
        with open("cfs_score.txt",'r+') as pv:
            c = 0
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            cfscore.delete(0,"end")
            cfscore.insert(0, c)

def min2cfs():
    try:
        with open("cfs_score.txt",'r+') as pv:
            data = float(pv.read())
            print(data)
            c = data - 2
            print(c)
            if c <= 9: 
                z = math.trunc(c)
                z = str("0") + str(z)
                print(z)
                pv.seek(0)
                pv.write(z)
                pv.truncate()
                cfscore.delete(0,"end")
                cfscore.insert(0, z)
            else:
                c = math.trunc(c)
                c = str(c)
                pv.seek(0)
                pv.write(c)
                pv.truncate()
                cfscore.delete(0,"end")
                cfscore.insert(0, c)
            print(c)
            if int(c) < 0 :
                with open("cfs_score.txt",'r+') as pv:
                    c = 0
                    c = str(c) + "0"
                    pv.seek(0)
                    pv.write(c)
                    pv.truncate()
                    cfscore.delete(0,"end")
                    cfscore.insert(0, c) 
    except ValueError:
        with open("cfs_score.txt",'r+') as pv:
            c = 0
            c = str(c) + "0"
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            cfscore.delete(0,"end")
            cfscore.insert(0, c)

def min3cfs():
    try:
        with open("cfs_score.txt",'r+') as pv:
            data = float(pv.read())
            print(data)
            c = data - 3
            print(c)
            if c <= 9: 
                z = math.trunc(c)
                z = str("0") + str(z)
                print(z)
                pv.seek(0)
                pv.write(z)
                pv.truncate()
                cfscore.delete(0,"end")
                cfscore.insert(0, z)
            else:
                c = math.trunc(c)
                c = str(c)
                pv.seek(0)
                pv.write(c)
                pv.truncate()
                cfscore.delete(0,"end")
                cfscore.insert(0, c)
            print(c)
            if int(c) < 0 :
                with open("cfs_score.txt",'r+') as pv:
                    c = 0
                    c = str(c) + "0"
                    pv.seek(0)
                    pv.write(c)
                    pv.truncate()
                    cfscore.delete(0,"end")
                    cfscore.insert(0, c) 
    except ValueError:
        with open("cfs_score.txt",'r+') as pv:
            c = 0
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            cfscore.delete(0,"end")
            cfscore.insert(0, c)

def min1aw():
    try:
        with open("away_score.txt",'r+') as pv:
            data = float(pv.read())
            print(data)
            c = data - 1
            print(c)
            if c <= 9: 
                z = math.trunc(c)
                z = str("0") + str(z)
                print(z)
                pv.seek(0)
                pv.write(z)
                pv.truncate()
                awayscore.delete(0,"end")
                awayscore.insert(0, z)
            else:
                c = math.trunc(c)
                c = str(c)
                pv.seek(0)
                pv.write(c)
                pv.truncate()
                awayscore.delete(0,"end")
                awayscore.insert(0, c)
            print(c)
            if int(c) < 0 :
                with open("away_score.txt",'r+') as pv:
                    c = 0
                    c = str(c) + "0"
                    pv.seek(0)
                    pv.write(c)
                    pv.truncate()
                    awayscore.delete(0,"end")
                    awayscore.insert(0, c) 
    except ValueError:
        with open("away_score.txt",'r+') as pv:
            c = 0
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            awayscore.delete(0,"end")
            awayscore.insert(0, c)

def min2aw():
    try:
        with open("away_score.txt",'r+') as pv:
            data = float(pv.read())
            print(data)
            c = data - 2
            print(c)
            if c <= 9: 
                z = math.trunc(c)
                z = str("0") + str(z)
                print(z)
                pv.seek(0)
                pv.write(z)
                pv.truncate()
                awayscore.delete(0,"end")
                awayscore.insert(0, z)
            else:
                c = math.trunc(c)
                c = str(c)
                pv.seek(0)
                pv.write(c)
                pv.truncate()
                awayscore.delete(0,"end")
                awayscore.insert(0, c)
            print(c)
            if int(c) < 0 :
                with open("away_score.txt",'r+') as pv:
                    c = 0
                    c = str(c) + "0"
                    pv.seek(0)
                    pv.write(c)
                    pv.truncate()
                    awayscore.delete(0,"end")
                    awayscore.insert(0, c) 
    except ValueError:
        with open("away_score.txt",'r+') as pv:
            c = 0
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            awayscore.delete(0,"end")
            awayscore.insert(0, c)

def min3aw():
    try:
        with open("away_score.txt",'r+') as pv:
            data = float(pv.read())
            print(data)
            c = data - 3
            print(c)
            if c <= 9: 
                z = math.trunc(c)
                z = str("0") + str(z)
                print(z)
                pv.seek(0)
                pv.write(z)
                pv.truncate()
                awayscore.delete(0,"end")
                awayscore.insert(0, z)
            else:
                c = math.trunc(c)
                c = str(c)
                pv.seek(0)
                pv.write(c)
                pv.truncate()
                awayscore.delete(0,"end")
                awayscore.insert(0, c)
            print(c)
            if int(c) < 0 :
                with open("away_score.txt",'r+') as pv:
                    c = 0
                    c = str(c) + "0"
                    pv.seek(0)
                    pv.write(c)
                    pv.truncate()
                    awayscore.delete(0,"end")
                    awayscore.insert(0, c)   
    except ValueError:
        with open("away_score.txt",'r+') as pv:
            c = 0
            c = str(c)
            pv.seek(0)
            pv.write(c)
            pv.truncate()
            awayscore.delete(0,"end")
            awayscore.insert(0, c)

def cfsbon():
    i = var1.get()
    if i == "off":
        #write off
        with open("cfsbon.txt",'r+') as pv:
            i = ""
            pv.seek(0)
            pv.write(i)
            pv.truncate()
    elif i == "bonus":
        #write bonus
        with open("cfsbon.txt",'r+') as pv:
            i = "Bonus"
            pv.seek(0)
            pv.write(i)
            pv.truncate()
    elif i == "dbl bonus":
        #write double bonus
        with open("cfsbon.txt",'r+') as pv:
            i = "Bonus+"
            pv.seek(0)
            pv.write(i)
            pv.truncate()

def abon():
    i = var.get()
    if i == "off":
        #write off
        with open("abon.txt",'r+') as pv:
            i = ""
            pv.seek(0)
            pv.write(i)
            pv.truncate()
    elif i == "bonus":
        #write bonus
        with open("abon.txt",'r+') as pv:
            i = "Bonus"
            pv.seek(0)
            pv.write(i)
            pv.truncate()
    elif i == "dbl bonus":
        #write double bonus
        with open("abon.txt",'r+') as pv:
            i = "Bonus+"
            pv.seek(0)
            pv.write(i)
            pv.truncate()

def psel():
    i = var3.get()
    if i == "1":
        #write 1
        with open("sel.txt",'r+') as pv:
            i = "1st"
            pv.seek(0)
            pv.write(i)
            pv.truncate()
    elif i == "2":
        #write 2
        with open("sel.txt",'r+') as pv:
            i = "2nd"
            pv.seek(0)
            pv.write(i)
            pv.truncate()
    elif i == "3":
        #write 3
        with open("sel.txt",'r+') as pv:
            i = "3rd"
            pv.seek(0)
            pv.write(i)
            pv.truncate()
    elif i == "4":
        #write 4
        with open("sel.txt",'r+') as pv:
            i = "4th"
            pv.seek(0)
            pv.write(i)
            pv.truncate()

def killt():
    sms = open("timem.txt", "r+")
    sms = float(sms.read())
    sss = open("times.txt", "r+")
    sss = float(sss.read())
    sm.delete(0, tk.END)
    ss.delete(0, tk.END)
    global killtime 
    killtime = 0
    global mval
    global sval
    global val
    mval = sms
    sval = sss
    val = float(mval)*60.0 + float(sval)
    sms = int(sms)
    sss = int(sss)
    sm.insert(0, sms)
    ss.insert(0, sss)

def cfteam(e):
    with open("cfteam.txt",'r+') as pv:
            i = cfsteam.get()
            pv.seek(0)
            pv.write(i)
            pv.truncate()

def awayteamfunc(e):
    with open("awayteam.txt",'r+') as pv:
            i = awayteam.get()
            pv.seek(0)
            pv.write(i)
            pv.truncate()

def installobsthing():
    if sys.platform.startswith('win32') == False:
        showerror("Error: this feature is only functional on windows currently.")

def OBS():
    ohbees = Toplevel(root)
    ohbees.resizable(False, False)
    ohbees.title("OBS Setup Info")
    ohbees.geometry("300x312")
    t1 = tk.Label(ohbees, text="""
            Capture type: Browser
            Width: 2000
            Height: 150
            Base (Canvas) Resolution: 1920x1080

""")
#    button = tk.Button(ohbees,
#                                 text="Install OBS Element",
#                                 command= lambda: installobsthing())
#    t1.pack()
#    button.pack()
    

def keys():
    showinfo("Hotkeys", """ 
             Alt + N   ->  Start clock
             Alt + M   ->  Pause clock
             Ctrl + 1  ->  Plus one to home score
             Ctrl + 2  ->  Plus two to home score
             Ctrl + 3  ->  Plus three to home score
             Alt + 1   ->  Minus one to home score
             Alt + 2   ->  Minus two to home score 
             Alt + 3   ->  Minus three to home score
             Ctrl + 4  ->  Plus one to away score
             Ctrl + 5  ->  Plus two to away score
             Ctrl + 6  ->  Plus three to away score 
             Alt + 4   ->  Minus one to away score
             Alt + 5   ->  Minus two to away score
             Alt + 6   ->  Minus three to away score
             Alt + 8   ->  Clear time
             Alt + 9   ->  Clear score
             Alt + 0   ->  Clear all
             """)

def about():
    showinfo("Window", "CFS Digital Scoreboard\nVersion: 3\ninteneded only for use in Christian Fellowship School\n\n\nWritten by Oskar Cobb, 2022-2024")

def saveEmergency():
    with open("index.html",'w') as index:
        index.write(str(code.get("1.0", tk.END)))
        index.close()
    with open("htmlfile.txt",'w') as pv:
        pv.write("index.html")
        pv.close()
    with open("reload.txt",'w') as pv:
        pv.write("True")
        pv.close()
    txtedit.destroy()

def rst(code):
    code.delete("1.0",END)
    code.insert("1.0", default)
    with open("reload.txt",'w') as pv:
        pv.write("True")
        pv.close()

def textedit():
    global code
    global txtedit
    txtedit = Toplevel(root)
    txtedit.resizable(False, False)
    txtedit.title("Emergency theme edit")
    txtedit.geometry("600x512")
    scrollbar = Scrollbar(txtedit) 
    scrollbar.pack(side=RIGHT, 
               fill=BOTH) 
    code = Text(txtedit, 
                 yscrollcommand=scrollbar.set) 
    code.pack(fill=BOTH)
    scrollbar.config(command=code.yview) 
    cancelbtn = Button(txtedit, text="Cancel", command=txtedit.destroy)
    savebtn = Button(txtedit, text="Save", command=saveEmergency)
    rstbtn = Button(txtedit, text="Reset to default", command= lambda: rst(code))
    cancelbtn.pack(side=RIGHT)
    savebtn.pack(side=RIGHT)
    rstbtn.pack(side=RIGHT)
    code.insert("1.0", default)

def dl_theme(name):
    r = requests.get('https://raw.githubusercontent.com/oskcobb/CFS_Scoreboard-Themes/main/themes.json')
    themes = json.loads(r.text)
    for theme in themes["themes"]:
        print(theme)
        print(name)
        print()
        if theme["name"] == name:
            temp = theme["name"]
            url = theme["url"]
            print(url)
            try:
                print(url)
                dl = str(requests.get(url).text)
            except:
                showerror("Error", "URL Error")
                pass
            with open("index.html",'w') as index:
                index.write(dl)
                index.close()
            with open("reload.txt",'w') as pv:
                pv.write("True")
                pv.close()

def choosetheme():
    chooseth = Toplevel(root)
    chooseth.resizable(False, False)
    chooseth.title("Choose Theme")
    #chooseth.geometry("300x312")
    r = requests.get('https://raw.githubusercontent.com/oskcobb/CFS_Scoreboard-Themes/main/themes.json')
    themes = json.loads(r.text)
    for theme in themes["themes"]:
        name = theme["name"]
        print(name)
        button = tk.Button(chooseth,
                                 text=name,
                                 command= lambda j=name: dl_theme(j))
        button.pack()

def update_check():
    latest_ver = requests.get("https://api.github.com/repos/oskcobb/CFS_Scoreboard/releases/latest").json()["tag_name"]
    print(latest_ver)
    if latest_ver != version_num:
        update = askquestion("Update Available", "A new update is available: \n \nVersion " + str(latest_ver) + "\n \nWould you like to update now?")
        if update == "yes":
            showinfo("Directory","Please select a directory to download the new version.")
            save = filedialog.askdirectory()
            dl_url = requests.get("https://api.github.com/repos/oskcobb/CFS_Scoreboard/releases/latest").json()["assets"][0]['browser_download_url']
            file_path = str(save) + f"/CFS_Scoreboard {latest_ver}.exe"
            urllib.request.urlretrieve(dl_url, file_path)
            delquestion = askquestion("Complete", "Done downloading.\n\nWould you like to remove the current version?")
            if delquestion == "yes":
                showinfo("Complete", "Please open the new file after this closes to finish install.")
                remove(argv[0])
                #os.startfile(file_path)
                exit()

button1timetest = tk.Button(
    text="⏵",
    width=2,
    height=1,
    relief=FLAT,
    command=tim
)
button1timestop = tk.Button(
    text="⏸",
    width=2,
    height=1,
    relief=FLAT,
    command=killt
)
button1cf = tk.Button(
    text="+1",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=plus1cfs
)
button2cf = tk.Button(
    text="+2",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=plus2cfs
)
button3cf = tk.Button(
    text="+3",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=plus3cfs
)
buttonm1cf = tk.Button(
    text="-1",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=min1cfs
)
buttonm2cf = tk.Button(
    text="-2",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=min2cfs
)
buttonm3cf = tk.Button(
    text="-3",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=min3cfs
)
button1aw = tk.Button(
    text="+1",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=plus1aw
)
button2aw = tk.Button(
    text="+2",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=plus2aw
)
button3aw = tk.Button(
    text="+3",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=plus3aw
)
buttonm1aw = tk.Button(
    text="-1",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=min1aw
)
buttonm2aw = tk.Button(
    text="-2",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=min2aw
)
buttonm3aw = tk.Button(
    text="-3",
    width=1,
    height=1,
    fg="black",
    relief=FLAT,
    command=min3aw
)
root.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24), weight=1)
#root.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38), weight=1)
t = tk.Label(text="CFS Scoreboard \n Control panel")
cfs = tk.Label(text="CFS")
away = tk.Label(text="Away")
team1 = tk.Label(text="Team")
team2 = tk.Label(text="Team")
score1 = tk.Label(text="Score")
score2 = tk.Label(text="Score")
spacer = tk.Label(text=" ")
spacer2 = tk.Label(text=" ")
c1 = tk.Label(text=":")
c2 = tk.Label(text=":")
period = tk.Label(text="Period")
cfsteam = tk.Entry(fg="black", bg="white", width=11)
awayteam = tk.Entry(fg="black", bg="white", width=11)
cfscore = tk.Entry(fg="black", bg="white", width=11)
awayscore = tk.Entry(fg="black", bg="white", width=11)
var1 = StringVar(root, "Off")
cfsbo = tk.Radiobutton(root, text='Off', variable=var1, value='off', command=cfsbon)
cfsb = tk.Radiobutton(root, text='Bonus', variable=var1, value='bonus', command=cfsbon)
cfsdb = tk.Radiobutton(root, text='Dbl bonus', variable=var1, value='dbl bonus', command=cfsbon)
var = StringVar(root, "Off")
abo = tk.Radiobutton(root, text='Off', variable=var, value='off', command=abon)
ab = tk.Radiobutton(root, text='Bonus', variable=var, value='bonus', command=abon)
adb = tk.Radiobutton(root, text='Dbl bonus', variable=var, value='dbl bonus', command=abon)
sm = tk.Entry(fg="black", bg="white", width=11)
sm = tk.Entry(fg="black", bg="white", width=11)
ss = tk.Entry(fg="black", bg="white", width=11)
em = tk.Entry(fg="black", bg="white", width=11)
es = tk.Entry(fg="black", bg="white", width=11)
var3 = StringVar(root, "1st")
p1 = tk.Radiobutton(root, text='1st', variable=var3, value='1', command=psel)
p2 = tk.Radiobutton(root, text='2nd', variable=var3, value='2', command=psel)
half = tk.Radiobutton(root, text='Half', variable=var3, value='half', command=psel)
p3 = tk.Radiobutton(root, text='3rd', variable=var3, value='3', command=psel)
p4 = tk.Radiobutton(root, text='4th', variable=var3, value='4', command=psel)
keyboard.add_hotkey('Ctrl + 1', plus1cfs)
keyboard.add_hotkey('Ctrl + 2', plus2cfs)
keyboard.add_hotkey('Ctrl + 3', plus3cfs)
keyboard.add_hotkey('Alt + 1', min1cfs)
keyboard.add_hotkey('Alt + 2', min2cfs)
keyboard.add_hotkey('Alt + 3', min3cfs)
keyboard.add_hotkey('Ctrl + 4', plus1aw)
keyboard.add_hotkey('Ctrl + 5', plus2aw)
keyboard.add_hotkey('Ctrl + 6', plus3aw)
keyboard.add_hotkey('Alt + 4', min1aw)
keyboard.add_hotkey('Alt + 5', min2aw)
keyboard.add_hotkey('Alt + 6', min3aw)
keyboard.add_hotkey('Alt + n', tim)
keyboard.add_hotkey('Alt + m', killt)
menubar = Menu(root)
help_ = Menu(menubar, tearoff = 0)
theme_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Themes', menu = theme_)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Hotkeys', command = keys)
help_.add_command(label ='OBS Setup', command = OBS)
help_.add_command(label ='About', command = about)
theme_.add_command(label ='Choose new theme', command = choosetheme)
theme_.add_command(label ='Emergency theme editor', command = textedit)
#button1timetest.config(image=play)
#button1timetest.image = play
rl1 = 8
rl2 = 9
re3 = 10
rn1 = 5

t.grid(row=1, column=9, columnspan=3)
cfs.grid(row=2, column=4, columnspan=2)
away.grid(row=2, column=14, columnspan=3)
team1.grid(row=3, column=1, columnspan=2)
team2.grid(row=3, column=12, columnspan=2)
score1.grid(row=4, column=1, columnspan=2)
score2.grid(row=4, column=12, columnspan=2)
cfsteam.grid(row=3, column=3, columnspan=4)
cfscore.grid(row=4, column=3, columnspan=4)
button1cf.grid(row=rn1, column=1)
button2cf.grid(row=rn1, column=2)
button3cf.grid(row=rn1, column=3)
buttonm1cf.grid(row=rn1, column=4)
buttonm2cf.grid(row=rn1, column=5)
buttonm3cf.grid(row=rn1, column=6)
awayteam.grid(row=3, column=14, columnspan=4)
awayscore.grid(row=4, column=14, columnspan=4)
button1aw.grid(row=rn1, column=12)
button2aw.grid(row=rn1, column=13)
button3aw.grid(row=rn1, column=14)
buttonm1aw.grid(row=rn1, column=15)
buttonm2aw.grid(row=rn1, column=16)
buttonm3aw.grid(row=rn1, column=17)
spacer.grid(row=6, column=0)
cfsbo.grid(row=7, column=0, columnspan=3)
cfsb.grid(row=8, column=0, columnspan=4)
cfsdb.grid(row=9, column=0, columnspan=5)
abo.grid(row=7, column=15, columnspan=2)
ab.grid(row=8, column=15, columnspan=3)
adb.grid(row=9, column=15, columnspan=5)
sm.grid(row=rl1, column=9, sticky="nsew")
c1.grid(row=rl1, column=10, sticky="nsew")
ss.grid(row=rl1, column=11, sticky="nsew")
em.grid(row=rl2, column=9, sticky="nsew")
c2.grid(row=rl2, column=10, sticky="nsew")
es.grid(row=rl2, column=11, sticky="nsew")
button1timetest.grid(row=re3, column=9, sticky="nsew")
button1timestop.grid(row=re3, column=11, sticky="nsew")
spacer2.grid(row=11, column=0)
period.grid(row=12, column=9, columnspan=3, sticky="nsew")
p1.grid(row=13, column=4, columnspan=2)
p2.grid(row=13, column=8, columnspan=2)
#half.grid(row=13, column=9, columnspan=2)
p3.grid(row=13, column=11, columnspan=2)
p4.grid(row=13, column=14, columnspan=2)


cfsteam.bind("<KeyRelease>", cfteam)
awayteam.bind("<KeyRelease>", awayteamfunc)
cfscore.bind("<KeyRelease>", cfsscore)
awayscore.bind("<KeyRelease>", awayscore1)
sm.bind("<FocusIn>", clearsm)
ss.bind("<FocusIn>", clearss)
em.bind("<FocusIn>", clearem)
es.bind("<FocusIn>", cleares)
sm.bind("<FocusOut>", tsm)
ss.bind("<FocusOut>", tss)
em.bind("<FocusOut>", tem)
es.bind("<FocusOut>", tes)


sm.insert(0, "start minute")
ss.insert(0, "start second")
em.insert(0, "end minute")
es.insert(0, "end second")
cfscore.insert(0, "00")
awayscore.insert(0, "00")

with open("cfs_score.txt",'w') as pv:
    pv.write("00")
    pv.close()
with open("away_score.txt",'w') as pv:
    pv.write("00")
    pv.close()
with open("times.txt",'w') as pv:
    pv.write("00")
    pv.close()
with open("timem.txt",'w') as pv:
    pv.write("00")
    pv.close()
with open("awayteam.txt",'w') as pv:
    pv.write("")
    pv.close()
with open("cfteam.txt",'w') as pv:
    pv.write("")
    pv.close()
with open("cfsbon.txt",'w') as pv:
    pv.write("")
    pv.close()
with open("abon.txt",'w') as pv:
    pv.write("")
    pv.close()
with open("sel.txt",'w') as pv:
    pv.write("1st")
    pv.close()
with open("reload.txt",'w') as pv:
    pv.write("False")
    pv.close()
with open("index.html",'w') as pv:
    try:
        r = requests.get('https://raw.githubusercontent.com/oskcobb/CFS_Scoreboard-Themes/main/Basketball.html')
        r = r.text
        pv.write(r)
        pv.close()
    except:
        print("Error getting theme from server. Using default theme.")
        pv.write(default)
        pv.close()
global val
val = 0
version_num = "v3.0"
#os.startfile("scoreboardweb.py")
root.geometry("451x350")
root.title("CFS Scoreboard")
root.config(menu = menubar)
update_check()
root.mainloop()
