from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def convertion(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans= Translator()
    trans1= trans.translate(text,src=src1,dest=dest1).text
    return trans1

def data():
    s= combo_source.get()
    d= combo_destination.get()
    msg= source_txt.get(1.0,END)
    textget= convertion(text = msg, src=s , dest=d)
    destination_text.delete(1.0,END)
    destination_text.insert(END,textget)


root = Tk()
root.title("translater")
root.geometry("500x750")
root.config(bg='grey')



lab_txt=Label(root,text="Google Translater",font=("Time New Roman",25,"bold"),fg="black",bg="grey")
lab_txt.place(x=110,y=20,)

frame =Frame(root)
frame.pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="black",bg="grey")
lab_txt.place(x=160,y=150)

source_txt=Text(root,font=("Time New Roman",20,"bold"),fg="black",wrap=WORD)
source_txt.place(x=10,y=250,height=150,width=480)


list_txt =list(LANGUAGES.values())
combo_source= ttk.Combobox(root,value=list_txt)
combo_source.place(x=10,y=430,height=25,width=100)
combo_source.set("English")

button_change = Button(root,text="Translate",relief=RAISED,command=data)
button_change.place(x=150,y=430,height=25,width=200)

combo_destination= ttk.Combobox(root,value=list_txt)
combo_destination.place(x=390,y=430,height=25,width=100)
combo_source.set("English")

lab_txt=Label(root,text="Destination text",font=("Time New Roman",20,"bold"),fg="black",bg="grey")
lab_txt.place(x=150,y=480)

destination_text=Text(root,font=("Time New Roman",20,"bold"),fg="black",wrap=WORD)
destination_text.place(x=10,y=540,height=150,width=480)

lab_txt=Label(root,text="MADE BYE SUMIT",font=("Time New Roman",10,"bold"),fg="black",bg="grey")
lab_txt.place(x=10,y=5,)

root.mainloop()
