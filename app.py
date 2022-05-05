import tkinter as tk  # -->> make easy GUI
from tkinter import Canvas, Frame, filedialog, Text   #--> provides interface in GUI
import os

from django.apps import apps  #-->> OS use run the aap


root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        Apps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    
    for widget in Frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="select file", 
                                        filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for aap in apps:
        label = tk.Label(Frame, text=apps, bg="gray")
        label.pack()

def runapps():
    for app in apps:
        os.startfile(app)



Canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
Canvas.pack()

Frame = tk.Frame(root, bg="white")
Frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)   

openfile = tk.Button(root, text="open file", padx=10,
                     pady=5, fg="white", bg="#263D42", command=addApp)
openfile.pack()


runapps = tk.Button(root, text="run apps", padx=10,
                     pady=5, fg="white", bg="#263D42", command=runapps)
runapps.pack()



for app in apps:
    label = tk.Label(Frame, text=app)
    label.pack()


root.mainloop()   # at the code is basic of the make the gUI

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')
