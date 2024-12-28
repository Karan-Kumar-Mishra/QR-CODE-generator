#make the QR code of any text or file and image
import tkinter as tk
import os
from tkinter import *
import pyqrcode
from PIL import Image
from tkinter import filedialog
import qrcode
import PyPDF2
from tkinter import ttk
import webbrowser
import requests
import time
from plyer import notification



karan=tk.Tk()
karan.geometry("1600x800")
karan.title("QR code generator")
karan['bg']='#73a5ff'

text1=tk.Text(karan,wrap=tk.WORD,width=50,height=30,fg="white",bg="black")
text1.place(x=10,y=10)

def error_msg(msg):
    notification_title = "QR code generator Notification"
    notification_message = msg
    show_notification(notification_title, notification_message)
    return 1
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Duration of the notification in seconds
    )


def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def create_qr_code2(text, filename):
    try:
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
    except Exception as e:
        notification_title = "QR code generator Notification"
        notification_message = "The text of pdf is too large ?"
        show_notification(notification_title, notification_message)
        return 0
    return 1
       
def create_qr_code():
    text_value = text1.get("1.0", tk.END) 
    qr_code = pyqrcode.create(text_value)
    qr_code.png("QRcode.png",scale=10)
    image=Image.open("QRcode.png")
    image.show()
    
def open_text_file():
     file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
     if file_path:
            with open(file_path, 'r') as file:
             txt = file.read()
             text1.delete('1.0', END)
             text1.insert('1.0', txt)
     else:
         show_notification("QR code generator Notification","Please select the .txt file .")

image_url='https://www.google.com'
text_url=tk.Entry(width=45)

def get_value2():
    global image_url
    image_url=text_url.get()
    notification_title = "QR code generator Notification"
    notification_message = "After click on get QR code button close the application for get your URL QR code"
    show_notification(notification_title, notification_message)
    
def open_image_file():
     try:
         GUI=tk.Tk()
         GUI.title("Enter the url ")
         GUI.geometry("600x200")
         GUI['bg']='#73a5ff'
         lbl1=tk.Label(GUI,text="Enter the url for QR code :")
         lbl1.place(x=20,y=2)
         lbl1['bg']='#73a5ff'
         global text_url
         text_url=tk.Entry(GUI,width=45)
         text_url.place(x=20,y=50)
         btn=tk.Button(GUI,width=10,command=get_value2,text="Get QR code")
         btn.place(x=230,y=100)
         GUI.mainloop()
         response = requests.get(image_url)
         image_data = response.content
         qr = qrcode.QRCode(
         version=1,  # Control the size of the QR code
         error_correction=qrcode.constants.ERROR_CORRECT_L,
         box_size=10,  # Size of each box in pixels
         border=4,     # Border size in boxes
        )
         qr.add_data(image_url)
         qr.make(fit=True)
         qr_img = qr.make_image(fill_color="black", back_color="white")
         qr_img.save('QRcode.png')
         open_the_QR_code()
     except Exception as ex:
         pass
        
                 
def Open_a_pdf_file():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("pdf files", "*.pdf")])
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_text = ""
        for page_num in range(len(pdf_reader.pages)):
           page = pdf_reader.pages[page_num]
           pdf_text += page.extract_text()
           pdf_file.close()
           output_filename = 'QRcode.png'
           if(create_qr_code2(pdf_text, output_filename)):
             image=Image.open("QRcode.png")
             image.show()
    except FileNotFoundError as ex:
        show_notification("QR code generator Notification","Please select the pdf file .")

cb1 =ttk.Combobox(width=10)
cb2 =ttk.Combobox(width=10)
cb3 =ttk.Combobox(width=10)

def set_value():
    try:
        karan.config(bg=cb1.get())
        text1.config(bg=cb2.get())
        text1.config(fg=cb3.get())
    except Exception as ex:
        pass
    
def Setting():
    setting=tk.Tk()
    setting.geometry("800x500")
    setting.title("setting")
    setting['bg']='#73a5ff'
    label1 = tk.Label(setting, text="Background color ")
    label1.config(fg="black",bg="#73a5ff")
    label1.place(x=90,y=5)
    var=tk.StringVar()
    global cb1
    cb1=ttk.Combobox(setting,width=10)    
    cb1['values']=('Red',
                  'Green',
                  'Black',
                  'Blue')
    bg_color=cb1.get()
    cb1.place(x=90,y=60)
    label2=tk.Label(setting, text="Text box background color")
    label2.config(fg="black",bg="#73a5ff")
    label2.place(x=450,y=5)
    global cb2
    cb2=ttk.Combobox(setting,width=10)
    cb2['values']=('Red',
                  'Green',
                  'Black',
                  'Blue')
    text_color=cb2.get()
    cb2.place(x=450,y=60)
    label3=tk.Label(setting, text="Font color of text box")
    label3.config(fg="black",bg="#73a5ff")
    label3.place(x=80,y=190)
    global cb3
    cb3=ttk.Combobox(setting,width=10)
    cb3['values']=('Red',
                  'Green',
                  'Black',
                  'Blue',
                  'white')
    cb3.place(x=90,y=250)
    set_btn=tk.Button(setting,text="Set",width=20,height=2,bd=10,command=set_value)
    set_btn['bg']='#4169E1'
    set_btn['font']=20
    set_btn['fg']='white'
    set_btn.place(x=500,y=330)
    setting.mainloop()  
    
      

def more_option():
   webbrowser.open("https://www.qrcode-tiger.com/")

def open_the_QR_code():
    image=Image.open("QRcode.png")
    image.show()

    
btn1=Button(text="Create QR code",width=20,height=4,bd=10,bg="#4169E1",fg="white",font=20,command=create_qr_code)
btn1.place(x=890,y=100)

open_btn=Button(text="Open recente QR code",width=20,height=4,bd=10,bg="#4169E1",fg="white",font=20,command=open_the_QR_code)
open_btn.place(x=1230,y=100)

btn2=Button(text="Open a text file",width=15,height=2,bd=10,bg="#4169E1",fg="white",font=20,command=open_text_file)
btn2.place(x=830,y=280)

btn3=Button(text="Open a URL ",width=15,height=2,bd=10,bg="#4169E1",fg="white",font=20,command=open_image_file)
btn3.place(x=1080,y=280)



btn4=Button(text="Open a pdf file",width=15,height=2,bd=10,bg="#4169E1",fg="white",font=20,command=Open_a_pdf_file)
btn4.place(x=1330,y=280)

btn5=Button(text="Other QR code",width=15,height=2,bd=10,bg="#4169E1",fg="white",font=20,command=more_option)
btn5.place(x=1080,y=400)

btn6=Button(text="Setting",width=15,height=2,bd=10,bg="#4169E1",fg="white",font=20,command=Setting)
btn6.place(x=830,y=400)

btn7=Button(text="Exit",width=15,height=2,bd=10,bg="#4169E1",fg="white",font=20,command=karan.destroy)
btn7.place(x=1330,y=400)

karan.mainloop()