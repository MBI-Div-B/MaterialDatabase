'''
Created on 27.04.2020

@author: Felix Steinbach
'''

import tkinter as tk
import tkinter.filedialog
from rowNumberTextWidget import ScrollText
import widgetFunctions as wf

class Application(tk.Frame):
    '''
    classdocs
    '''


    def __init__(self, master=None):
        '''
        Constructor
        '''
        super().__init__(master)
        master.geometry('800x600')
        master.title("MBI Material Database Editor")
        master.selectedItem=-1
        master.elementList=[]        
        self.loadWidgets(master)
        
    def loadWidgets(self,master=None):
        w1 = tk.Label(master, text="Material name")
        w1.place(x=5,y=5)
        
        e1 = tk.Entry(master)
        e1.place(x=90,y=7.5, height=20, width=150)
        
        w2 = tk.Label(master, text="References")
        w2.place(x=5,y=40)
        
        scroll = ScrollText(master)
        scroll.insert(tk.END, '')
        scroll.place(x=90,y=40, height=20*4, width=500)
        scroll.text.focus()
        master.after(200, scroll.redraw())
        
        
        w3 = tk.Label(master, text="Comment")
        w3.place(x=5,y=130)
        e2 = tk.Entry(master)
        e2.place(x=90,y=132.5, height=20, width=150)
        
        w4 = tk.Label(master, text="Data")
        w4.place(x=5,y=170)
        
        
        lb1=tk.Listbox(master)
        lb1.place(x=90,y=170, height=300, width=150)
        lb1.bind('<<ListboxSelect>>', lambda event : wf.onselectListbox(master,event,ent1=e3,ent2=e7,ent3=e4,ent4=e5,txt1=e6,ent8=e8) )
        
        #,el=elementList,ent1=e3
        
        btn2 = tk.Button(master, text = "Delete", command = lambda: wf.delete(master,lb1,e3,e7,e4,e5,e6,e8))
        btn2.place(x=170,y=480, height=20, width=70)
        
        
        #Parameterframe
        w4 = tk.Label(master, text="Parameter:")
        w4.place(x=300,y=150)
        
        fr1 = tk.Frame(master, highlightbackground="black", highlightthickness=1)
        fr1.place(x=300,y=170, height=410, width=350)
        
        w5 = tk.Label(fr1, text="Parameter name")
        w5.place(x=5,y=5)
        e3 = tk.Entry(fr1)
        e3.place(x=120,y=7.5, height=20, width=200)
        e3.bind("<KeyRelease>", lambda event : wf.editParameterInList(master,lb1,e3,e7,e4,e5,e6,e8))
        
        
        w9 = tk.Label(fr1, text="Comment")
        w9.place(x=5,y=37.5)
        e8 = tk.Entry(fr1)
        e8.place(x=120,y=37.5, height=20, width=200)
        e8.bind("<KeyRelease>", lambda event : wf.editParameterInList(master,lb1,e3,e7,e4,e5,e6,e8))
        
        w9 = tk.Label(fr1, text="Reference number")
        w9.place(x=5,y=67.5)
        e7 = tk.Entry(fr1)
        e7.place(x=120,y=67.5, height=20, width=30)
        e7.bind("<KeyRelease>", lambda event : wf.editParameterInList(master,lb1,e3,e7,e4,e5,e6,e8))
        
        w6 = tk.Label(fr1, text="Units")
        w6.place(x=5,y=107.5)
        e4 = tk.Entry(fr1)
        e4.place(x=120,y=107.5, height=20, width=200)
        sc1 = tk.Scrollbar(fr1, orient=tk.HORIZONTAL, command=e4.xview)
        e4.configure(xscrollcommand=sc1.set)
        sc1.place(x=120,y=127.5, height=20, width=200)
        e4.bind("<KeyRelease>", lambda event : wf.editParameterInList(master,lb1,e3,e7,e4,e5,e6,e8))
        
        w7 = tk.Label(fr1, text="Value names")
        w7.place(x=5,y=147.5)
        e5 = tk.Entry(fr1)
        e5.place(x=120,y=147.5, height=20, width=200)
        sc2 = tk.Scrollbar(fr1, orient=tk.HORIZONTAL, command=e5.xview)
        e5.configure(xscrollcommand=sc2.set)
        sc2.place(x=120,y=167.5, height=20, width=200)
        e5.bind("<KeyRelease>", lambda event : wf.editParameterInList(master,lb1,e3,e7,e4,e5,e6,e8))
        
        w8 = tk.Label(fr1, text="Values")
        w8.place(x=5,y=177.5)
        e6 = tk.Text(fr1,wrap='none')
        e6.place(x=120,y=187.5, height=140, width=200)
        sc3 = tk.Scrollbar(fr1, orient=tk.HORIZONTAL, command=e6.xview)
        e6.configure(xscrollcommand=sc3.set)
        sc3.place(x=120,y=327.5, height=20, width=200)
        sc4 = tk.Scrollbar(fr1, orient=tk.VERTICAL, command=e6.yview)
        e6.configure(yscrollcommand=sc4.set)
        sc4.place(x=320,y=187.5, height=130, width=20)
        e6.bind("<KeyRelease>", lambda event : wf.editParameterInList(master,lb1,e3,e7,e4,e5,e6,e8))
        
        btn1 = tk.Button(fr1,text="Add",command=lambda: wf.addParameterToList(master,lb1,e3,e7,e4,e5,e6,e8))
        btn1.place(x=270,y=360, height=20, width=50)
        
        
        #btn3 = tk.Button(fr1,text="Edit",command=lambda : editParameterInList(lb1,e3,e7,e4,e5,e6,e8))
        #btn3.place(x=200,y=360, height=20, width=50)
        
        
        
        btn4 = tk.Button(fr1,text="Clean",command=lambda: wf.clean(master,e3,e7,e4,e5,e6,e8))
        btn4.place(x=200,y=360, height=20, width=50)    
        
        #btn2 = tk.Button(fr1,text="print",command=lambda: insertText(e3,"Test"))
        #btn2.place(x=170,y=310, height=20, width=50)
        
        
        btn5 = tk.Button(master,text="Save",command=lambda: wf.saveFile(master,e1,scroll,e2))
        btn5.place(x=400,y=5, height=20, width=50)
        
        
        btn6 = tk.Button(master,text="Load",command=lambda: wf.loadFile(master,lb=lb1,sc=scroll,ent1=e1,ent2=e2))
        btn6.place(x=470,y=5, height=20, width=50)
        
        btn7 = tk.Button(master,text="New",command=lambda: wf.newFile(master,lb1,scroll,e1,e2,e3,e7,e4,e5,e6,e8))
        btn7.place(x=330,y=5, height=20, width=50)

        
        