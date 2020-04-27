'''
Created on 27.04.2020

@author: Felix Steinbach
'''

import tkinter as tk
import Functions as fun
from tkinter.messagebox import showinfo
import yaml

def addParameterToList(master,lb,ent1,ent2,ent3,ent4,txt1,ent8):
    parName=ent1.get()
    refNumStr=ent2.get()
    UnitsStr=ent3.get()
    parStr=ent4.get()
    comment=ent8.get()
    valuesStr=txt1.get('1.0',tk.END)
    
    print(valuesStr)

    try:
        refNum=int(refNumStr)
    except:
        showinfo("Warning", "Reference is not a number!!!!!")
        return 0
    lb.insert(tk.END, parName)    
    units=fun.stringToList(UnitsStr)
    par=fun.stringToList(parStr)
    values=fun.stringTo2DIntList(valuesStr)
    print(values)
    
    dictTmp={"Parameter name":parName,"Comment":comment,"Reference number":refNum,"Units":units,"Value names":par,"Values":values}
    master.elementList.append(dictTmp)
    
    
def clean(master,ent1,ent2,ent3,ent4,txt1,ent8):
    ent1.delete(0,tk.END)
    ent2.delete(0,tk.END)
    ent3.delete(0,tk.END)
    ent4.delete(0,tk.END)
    ent8.delete(0,tk.END)
    txt1.delete('1.0',tk.END)
    master.selectedItem=-1
    
def editParameterInList(master,lb,ent1,ent2,ent3,ent4,txt1,ent8):
    index=master.selectedItem
    if(index< 0):
        return
    else:
        parName=ent1.get()
        refNumStr=ent2.get()
        comment=ent8.get()
        try:
            refNum=int(refNumStr)
        except:
            showinfo("Warning", "Reference is not a number!!!!!")
            return 0  
        UnitsStr=ent3.get()
        parStr=ent4.get()
        valuesStr=txt1.get('1.0',tk.END)
        units=fun.stringToList(UnitsStr)
        par=fun.stringToList(parStr)
        values=fun.stringTo2DIntList(valuesStr)  
        dictTmp={"Parameter name":parName,"Comment":comment,"Reference number":refNum,"Units":units,"Value names":par,"Values":values}
        lb.delete(index, index)
        lb.insert(index, parName)
        master.elementList[index]=dictTmp 
         
    

def addParameterToWidget(dict1,ent1,ent2,ent3,ent4,txt1):
    parName=dict1["Parameter name"]
    print(parName)
    ent1.delete(0,tk.END)
    ent1.insert(0, "parName")
    
def insertText(ent1,text):
    ent1.delete(0,tk.END)
    ent1.insert(0,text)
    
def delete(master,l,ent1,ent2,ent3,ent4,txt1,ent8):
    master.selectedItem=-1
    selection = l.curselection()  
    value = l.get(selection[0])
    
    result = tk.messagebox.askquestion("Delete Parameter", "Are You Sure to delete parameter: "+value+"?", icon='warning')
    if result == 'yes':
    #global things
    # Delete from Listbox

        l.delete(selection[0])
        del master.elementList[selection[0]]
        
    clean(master,ent1,ent2,ent3,ent4,txt1,ent8)
    # Delete from list that provided it
    #
    #ind = things.index(value)
    #del(things[ind])   
    
def saveFile(master,e1,text1,e2):
    materialNameStr=e1.get()
    referencesStr=text1.get('1.0',tk.END)
    references=fun.stringToList2(referencesStr)
    comment=e2.get()
    dictTmp1={"Material name":materialNameStr,"References":references,"Comment":comment}
    dictTmp2={"Data":master.elementList}
    
    ftypes = [('YAML files', '*.yml'), ('All files', '*')]
    f = tk.filedialog.asksaveasfile(mode='w', defaultextension=".yml",filetypes = ftypes)
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    
    yamlFile=yaml.safe_dump(dictTmp1, sort_keys=False, default_flow_style=False,allow_unicode=True)
    yamlFile2=yaml.safe_dump(dictTmp2, sort_keys=False, default_flow_style=None,allow_unicode=True)
    
    text2save = yamlFile+yamlFile2
    f.write(text2save)
    f.close()
    
    
    
    
    
    
    
def loadFile(master,lb,sc,ent1,ent2):
    
    ftypes = [('YAML files', '*.yml'), ('All files', '*')]
    dlg = tk.filedialog.Open(filetypes = ftypes)
    fl = dlg.show()
    master.selectedItem=-1
    if fl != '':
        f = open(fl, "r")
        text = f.read()
        dict1=yaml.load(text, Loader=yaml.FullLoader)
        #print(dict1)
        
        
        ent1.delete(0,tk.END)
        try:
            matName=dict1["Material name"]
            ent1.insert(0, matName)             
        except:
            print("Warning", "No material name in opened file!!!!!")
        sc.delete('1.0',tk.END)
        try:
            refList=dict1["References"]
            refStr=fun.listToString(refList,"\n")
            sc.insert('1.0', refStr)       
        except:
            print("Warning", "No references in opened file!!!!!")
        ent2.delete(0,tk.END)        
        try:
            commentStr=dict1["Comment"]
            ent2.insert(0, commentStr)  
        except:
            print("Warning", "No comment in opened file!!!!!")
            
        lb.delete(0,tk.END)        
        try:
            dataList=dict1["Data"]

            nameList=[i["Parameter name"] for i in dataList]    
            master.elementList=dataList            
            for item in nameList:
                lb.insert(tk.END, item)        
        except:
            print("Warning", "No data in opened file!!!!!")
        #print(dataList)
        
   

        


        

        
        #print(el)
    
    
    

def onselectListbox(master,evt,ent1,ent2,ent3,ent4,txt1,ent8):#,ent1):
    w = evt.widget
    index = int(w.curselection()[0])
    master.selectedItem=index
    dict1=master.elementList[int(index)]
    
    ent1.delete(0,tk.END)
    try:
        parName=dict1["Parameter name"]
        ent1.insert(0, parName) 
    except:
        print("Warning", "No parameter name in data!!!!!")        
    ent2.delete(0,tk.END)    
    try:
        refNum=dict1["Reference number"]
        ent2.insert(0, refNum)         
    except:
        print("Warning", "No reference number in data!!!!!")    
    ent8.delete(0,tk.END)    
    try:
        comment=dict1["Comment"]
        ent8.insert(0, comment)         
    except:
        print("Warning", "No comment in data!!!!!")
    ent3.delete(0,tk.END)    
    try:
        units=dict1["Units"]
        unitsStr=fun.listToString(units,";")
        ent3.insert(0, unitsStr)         
    except:
        print("Warning", "No units in data!!!!!")
    ent4.delete(0,tk.END)    
    try:
        par=dict1["Value names"]
        parStr=fun.listToString(par,";")  
        ent4.insert(0, parStr)        
    except:
        print("Warning", "No value names in data!!!!!")
    txt1.delete('1.0',tk.END)    
    try:
        values=dict1["Values"]
        valuesStr=fun.intList2DToString(values,";")  
        txt1.insert('1.0', valuesStr)         
    except:
        print("Warning", "No values in data!!!!!")

    
    
def newFile(master,lb1,scroll,e1,e2,e3,e7,e4,e5,e6,e8):
    lb1.delete(0,tk.END)
    scroll.delete(('1.0'),tk.END)
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    e5.delete(0,tk.END)
    e6.delete('1.0',tk.END)
    e7.delete(0,tk.END)
    e8.delete(0,tk.END)
    master.elementList=[]
    
def test(dict1):
    print(dict1)    


