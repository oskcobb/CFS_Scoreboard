#Written by Oskar L. Cobb, 2022
#Inteneded only for use in Christian Fellowship School

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import os
import math
from time import sleep as wait
import threading

global killtime
killtime = 0
root = tk.Tk()
root.iconbitmap("cfs.ico")

def time():
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
        i = int(sm.get())
        print(i)
        if int(i) <= 9:
            i = "0" + str(i)
        print(i)
        #ss= open("timess.txt",'r+')
        x = int(ss.get())
        print(x)
        if int(x) <= 9:
            x = "0" + str(x)
        print(x)
        #em = open("timeem.txt",'r+')
        y = int(em.get())
        print(y)
        if int(y) <= 9:
            y = "0" + str(y)
        print(y)
        #es = open("timees.txt",'r+')
        z = int(es.get())
        print(z)
        if int(z) <= 9:
            z = "0" + str(z)
        print(z)

        if i > y:
            countup = False
            s = False
        elif i < y:
            countup = True
            s = False
        elif i == y:
            if x > z:
                countup = False
                s = True
            elif x < z:
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
            while int(i) > int(y):
                if killtime == 0:
                    cont = 0
                    return
                # formating
                if int(x) == 0:
                    i = int(i) - 1
                    x = 59
                    if int(i) <= 9:
                        i = "0" + str(i)
                #-------------
                x = int(x) - int(1)
                if int(x) <= 9:
                    x = "0" + str(x)
                #-------------
                #sm.write(str(i))
                #ss.write(str(x))
                i = str(i)
                x = str(x)
                tm.seek(0)
                tm.write(str(i))
                tm.truncate()
                ts.seek(0)
                ts.write(str(x))
                ts.truncate()
                print(str(i) + ":" + str(x))
                if int(i) <= 0 and int(x) <= 0:
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
                if int(x) == 0:
                    i = int(i) - 1
                    x = 59
                    if int(i) <= 9:
                        i = "0" + str(i)
                wait(1)
            while int(x) > int(z):
                if killtime == 0:
                    cont = 0
                    return
                # formating
                if int(x) == 0:
                    i = int(i) - 1
                    x = 59
                    if int(i) <= 9:
                        i = "0" + str(i)
                #-------------
                x = int(x) - int(1)
                if int(x) <= 9:
                    x = "0" + str(x)
                #-------------
                i = str(i)
                x = str(x)
                tm.seek(0)
                tm.write(str(i))
                tm.truncate()
                ts.seek(0)
                ts.write(str(x))
                ts.truncate()
                if int(x) <= 9:
                    x = "0" + str(x)
                    print(x)
                print(str(i) + ":" + str(x))
                if int(i) <= 0 and int(x) <= 0:
                    print(str(i) + ":" + str(x))
                    return
                wait(1)
        elif countup == False and s == True:
            while int(x) > int(z):
                if killtime == 0:
                    cont = 0
                    return
                if int(x) == 0:
                    i = int(i) - 1
                    x = 59
                    if int(i) <= 9:
                        i = "0" + str(i)
                x = int(x) - int(1)
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
                if int(x) <= 9:
                    x = "0" + str(x)
                    print(x)
                print(str(i) + ":" + str(x))
                if int(i) <= 0 and int(x) <= 0:
                    print(str(i) + ":" + str(x))
                    return
                wait(1)
        elif countup == True and s == True:
            while int(x) < int(z):
                if killtime == 0:
                    cont = 0
                    break
                x = int(x) + 1
                if int(x) == 60:
                    i = int(i) + 1
                    x = 0
                    if int(i) <= 9:
                        i = "0" + str(i)
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
                #if int(x) <= 9:
                    #x = "0" + str(x)
                print(str(i) + ":" + str(x))
                if int(i) <= 0 and int(x) <= 0:
                    print(str(i) + ":" + str(x))
                    return
                wait(1)
        elif countup == True and s == False: 
            while int(i) < int(y):
                if killtime == 0:
                    cont = 0
                    return
                # formating
                x = int(x) + 1
                if int(x) == 60:
                    i = int(i) + 1
                    x = 00
                    if int(i) <= 9:
                        i = "0" + str(i)
                #-------------
                if int(x) <= 9:
                    x = "0" + str(x)
                #-------------
                print(str(i) + ":" + str(x))
                i = str(i)
                x = str(x)
                tm.seek(0)
                tm.write(str(i))
                tm.truncate()
                ts.seek(0)
                ts.write(str(x))
                ts.truncate()
                if int(i) <= 0 and int(x) <= 0:
                    print(str(i) + ":" + str(x))
                    return
                wait(1)
            while int(x) < int(z):
                if killtime == 0:
                    cont = 0
                    return
                # formating
                x = int(x) + 1
                if int(x) == 60:
                    i = int(i) + 1
                    x = 00
                    if int(i) <= 9:
                        i = "0" + str(i)
                #-------------
                if int(x) <= 9:
                    x = "0" + str(x)
                #-------------
                i = str(i)
                x = str(x)
                tm.seek(0)
                tm.write(str(i))
                tm.truncate()
                ts.seek(0)
                ts.write(str(x))
                ts.truncate()
                if int(x) <= 9:
                    x = "0" + str(x)
                    print(x)
                if int(x) <= 9:
                    x = "0" + str(x)
                print(str(i) + ":" + str(x))
                if int(i) <= 0 and int(x) <= 0:
                    print(str(i) + ":" + str(x))
                    return
                wait(1)
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
        timr = threading.Thread(target=time)
        timr.join()
        tim()
    elif killtime == 0:
        #global killtime
        killtime = 1
        print(killtime)
        timr = threading.Thread(target=time)
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
    except ValueError:
        with open("cfs_score.txt",'r+') as pv:
            c = 0
            c = str(c)
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
    sms = sms.read()
    sss = open("times.txt", "r+")
    sss = sss.read()
    sm.delete(0, tk.END)
    ss.delete(0, tk.END)
    global killtime 
    killtime = 0
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
p3 = tk.Radiobutton(root, text='3rd', variable=var3, value='3', command=psel)
p4 = tk.Radiobutton(root, text='4th', variable=var3, value='4', command=psel)

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
os.startfile("scoreboardweb.exe")
root.geometry("451x350")
root.title("CFS Scoreboard")
root.mainloop()
