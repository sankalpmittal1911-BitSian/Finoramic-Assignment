import os
import json
import pip 
from subprocess import call
from tkinter import * 
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import pkg_resources
from pip._internal.operations.freeze import freeze
from packaging import version

# For setting environment paths and installing prerequisites
def set_path():
    path = str(entry1.get())
    path2 = str(path)[:-7]
    call('setx PATH "%PATH%;"'+path2)
    call('python -m pip install --upgrade pip')
    call('setx PATH "%PATH%;"'+path)
    call('pip install packaging')

# For opening JSON file
def Load_JSON():
    global f
    f = askopenfile(mode ='r', filetypes =[('JSON files', '*.json')])
    s = str(f)[25:-29]
    path = os.path.abspath(s)
    entry2.insert(tk.END, s)

# For installing all the dependencies and listing the required result in a listbox
def install_dep():
    data = json.load(f) 
    l = []
    for i in data['Dependencies']: 
        l.append(i)
    for package in l:
        if(package[0:3]=="pip"):
            call('python -m pip install '+package)
            continue
        call("pip install " + package)
    delim = [None]*len(l)
    vers = [None]*len(l)
    names = [None]*len(l)
    for i in range(len(l)):
        if("==" in l[i]):
            delim[i] = "=="
        elif(">=" in l[i]):
            delim[i] = ">="
        else:
            delim[i] = "<="
        s = l[i].split(delim[i])
        names[i],vers[i] = s[0],s[1]
        vers[i] = vers[i].rstrip("\n")

    pkgs = {}
    for s in (list(freeze(local_only=True))):
        x = s.split("==")
        pkgs[x[0]] = x[1]
        
    unins_pkg = []
    for i in range(len(names)):
        if(names[i] not in pkgs):
            unins_pkg.append(l[i])
            continue
        if((delim[i] == "==") | (delim[i] == ">=")):
            if(version.parse(pkgs[names[i]]) < version.parse(vers[i])):
                unins_pkg.append(l[i])
        elif(delim[i] == "<="):
            if(version.parse(pkgs[names[i]]) > version.parse(vers[i])):
                unins_pkg.append(l[i])
    listbox.delete(0,END)
    if(len(unins_pkg)==0):
        listbox.insert(0,"Success!")
    else:
        unins_pkg = ["The uninstalled dependencies are:\n"]+unins_pkg
        for v in unins_pkg: 
            listbox.insert(END, v) 
      
    listbox.config(yscrollcommand = scrollbar.set) 
  
    scrollbar.config(command = listbox.yview) 
    entry2.delete(0, END)
    
        

f = ""
#Tkinter Frontend

root= tk.Tk()
root.title("Package Installer")
canvas1 = tk.Canvas(root, width = 600, height = 500)
canvas1.pack()

label1 = tk.Label(root, text='Enter path for pip:')
label1.config(font=('helvetica', 10))
canvas1.create_window(300, 20, window=label1)

entry1 = tk.Entry (root) 
canvas1.create_window(300, 40, window=entry1)

button1 = tk.Button(text='Set Path', command=set_path, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(300, 70, window=button1)

button2 = tk.Button(text='Browse JSON File', command=Load_JSON, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(300, 150, window=button2)

entry2 = tk.Entry (root,width=30) 
canvas1.create_window(300, 180, window=entry2)

button3 = tk.Button(text='Install Dependencies', command=install_dep, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(300, 250, window=button3)

listbox = tk.Listbox(root,height=12, width=50) 
canvas1.create_window(300, 380, window=listbox)

scrollbar = tk.Scrollbar(root,orient="vertical") 

root.mainloop()
