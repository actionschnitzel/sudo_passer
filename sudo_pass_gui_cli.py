import tkinter as tk
from tkinter import *
import os
from os import popen

#Note: The program that should be executed with sudo can be changed at "def pass_pw"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        app_width = 300
        app_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.wait_visibility(self)
        self.wm_attributes("-alpha", 0.90)
        self["background"] = "#333333"
        self.resizable(0, 0)        
        #self.overrideredirect(True)

        global user
        user = os.environ.get('LOGNAME')
        print(f"Hi,{user} waz uuuuup?!")

        self.labl = tk.Label(self, text=f"Hi, {user}!\n\nSudo Legitimation",background="#333333",foreground="white",font=("Helvetica", 16),)
        self.labl.pack(pady=20,padx=20)

        self.entry = tk.Entry(show='*')
        self.entry.pack()

        self.btn = tk.Button(self, text="Ok",command=self.pass_pw,highlightthickness=2,borderwidth=0,background="#333333",foreground="white",font=("Helvetica", 12, "bold"))
        self.btn.pack(pady=20)

        self.btn = tk.Button(self, text="Cancel",command=self.quit,highlightthickness=2,borderwidth=0,background="#333333",foreground="white",font=("Helvetica", 12, "bold"))
        self.btn.pack(pady=20)

        

    def pass_pw(self):
        pw = self.entry.get()
        pw = str(pw)
        popen(f"xterm -e 'bash -c \"echo '{pw}' | sudo -S apt update && exit; exec bash\"'") # replace sudo apt update with "what evaa"
        app.quit()

if __name__ == "__main__":
    app = App()
    app.title("")
    app.mainloop()