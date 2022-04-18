# sudo_passer
Sudo Password GUI to CLI

This Tkinter Program passes the Sudo Password to a program of choice in the Command Line.

As we all know, you never have to enter the "Sudo Pwassword" on the Raspberry Pi. Should this change (they have already removed the user Pi) I wrote this pass Throu GUI for my Python programs. Under Ubuntu, the legitimation always calles "pkexec". This opens a graphical password request.

I found it from the beginning stupid that there is no such thing for PI_OS. That's why I did it myself.
     
This is an early version that is intended to test
    
![GUI](https://github.com/actionschnitzel/sudo_passer/blob/main/pw.png)    
     
### By modifying the pass_pw, each program can be controlled.
     
     
```
    def pass_pw(self):
        pw = self.entry.get()
        pw = str(pw)
        popen(f"xterm -e 'bash -c \"echo '{pw}' | sudo -S apt update && exit; exec bash\"'") # replace sudo apt update with "what evaa"
        app.quit()
```
