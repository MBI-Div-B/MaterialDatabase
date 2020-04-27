'''
Created on 27.04.2020

@author: Felix Steinbach
'''
#!/usr/bin/env



import tkinter as tk
from Application import Application

def main():
    root = tk.Tk() #creates window
    app=Application(master=root)

    app.mainloop()
    print("Test")    

if __name__ == '__main__':
    main()
    