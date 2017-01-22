#######
# Python 3.5
#
# Author: Renee Woznick
#
# -*- coding: utf-8 -*-
#######
#Python Drill: PyDrill_shutil_module_34_idle_daily_file_transfer_gui
#
 
import shutil
import os
import glob
import time
import datetime
 
from tkinter import filedialog
from tkinter import *
import tkinter as tk
 
def file_move(src, dest, age):
 
    for name in glob.glob(os.path.join(src, '*.txt')):
 
        file_mtime = round(os.stat(name).st_mtime)
        time_in_seconds_since_epoch = round(time.mktime(datetime.datetime.today().timetuple()))
 
        if ((time_in_seconds_since_epoch - age) <= file_mtime) :
            print ('SOURCE : ', src)
            print ('BACKUP : ', dest)
            print (name, "--> ", dest)
            shutil.move (name , dest)
 
def selectDirectory():
    directoryname = filedialog.askdirectory(parent=root,initialdir="/")
    return directoryname
 
def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo
 
 
# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
 
def onSelectSourceDir(self):
    sourceDir = selectDirectory()
    if sourceDir and sourceDir.strip():
        #messagebox.askokcancel("Source Directory", (str.join ('', (sourceDir, ' Selected'))))
        self.txt_sourceDir.delete (0,END)
        self.txt_sourceDir.insert (END, sourceDir)
 
def onSelectTargetDir(self):
    targetDir = selectDirectory()
    if targetDir and targetDir.strip():
        #messagebox.askokcancel("Target Directory", (str.join ('', (targetDir, ' Selected'))))
        self.txt_targetDir.delete (0,END)
        self.txt_targetDir.insert (END, targetDir)
 
def onCopy(self):
    targetDir = self.txt_targetDir.get()
    sourceDir = self.txt_sourceDir.get()
 
    if sourceDir and sourceDir.strip() and targetDir and targetDir.strip() and (sourceDir != targetDir):
        file_age = 86400
        file_move(sourceDir, targetDir, file_age)
        messagebox.askokcancel("File Move", "File move complete")
 
def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets, but is a little confusing at
        first, but that is what this demo is here for...
    """
    self.lbl_sourceDir = tk.Label(self.master,text='Source Directory:',bg="#F0F0F0")
    self.lbl_sourceDir.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
 
    self.lbl_targetDir = tk.Label(self.master,text='Target Directory:',bg="#F0F0F0")
    self.lbl_targetDir.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
 
    self.txt_sourceDir = tk.Entry(self.master,text='')
    self.txt_sourceDir.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,0),pady=(0,0),sticky=N+E+W)
 
    self.txt_targetDir = tk.Entry(self.master,text='')
    self.txt_targetDir.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,0),pady=(0,0),sticky=N+E+W)
 
    self.btn_add = tk.Button(self.master,width=30,height=2,text='Select Source Directory',command=lambda: onSelectSourceDir(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
 
    self.btn_update = tk.Button(self.master,width=30,height=2,text='Select Target Directory',command=lambda: onSelectTargetDir(self))
    self.btn_update.grid(row=9,column=0,padx=(25,0),pady=(45,10),sticky=W)
 
    self.btn_close = tk.Button(self.master,width=30,height=2,text='Copy',command=lambda: onCopy(self))
    self.btn_close.grid(row=10,column=0,padx=(25,0),pady=(45,10),sticky=E)
 
    self.btn_close = tk.Button(self.master,width=30,height=2,text='Close',command=lambda: ask_quit(self))
    self.btn_close.grid(row=11,column=0,padx=(25,0),pady=(45,10),sticky=E)
 
 
# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
 
        # define our master frame configuration
        self.master = master
        self.master.minsize(500,500) #(Height, Width)
        self.master.maxsize(500,500)
        # This CenterWindow method will center our app on the user's screen
        center_window(self,500,300)
        self.master.title("File Move Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master
 
        # load in the GUI widgets from a separate module,
        # keeping your code comparmentalized and clutter free
        load_gui(self)
       
        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
 
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional
            functionalityor appearances such as a borderwidth.
        """
        self.master.config(menu=menubar, borderwidth='1')
 
       
"""
    It is from these few lines of code that Python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following and in this order:
 
    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
