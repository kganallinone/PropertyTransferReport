from tkinter import *
import customtkinter as ctk
from PIL import ImageTk,Image
import pyrebase
from tkinter import messagebox


def login_window():
    from register import register_window
    from page1_dashboard import dashboard_window
    ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
    
    #<----------------FIREBASE CONFIGURATION--------------------------------->#
    config = {
        "apiKey": "xxxxxxx",
        "authDomain": "xxxxxxx",
        "projectId": "xxxxxxx",
        "databaseURL": "xxxxxxx",
        "storageBucket": "xxxxxxx",
        "messagingSenderId": "xxxxxxx",
        "appId": "xxxxxxx",
        "measurementId": "xxxxxxx"
    }
    #<----------------FIREBASE CONNECT--------------------------------->#
    firebase = pyrebase.initialize_app(config)


    # Get a reference to the auth service
    auth = firebase.auth()

    #<----------------FIREBASE END--------------------------------->#

   
    login = ctk.CTkToplevel()
    login.title("Property Transfer | login")
    login.geometry("{0}x{1}+200+50".format(1000, 600))
    login.resizable(False, False)
    login.configure(fg_color = 'white')
    login.iconbitmap('PTR.ico')

    #------------------- lOGIN FUNCTION ------------------------------------#
    
    def button_function():
        email = login_email.get()
        pw = login_pw.get()
        
        try:
            auth.sign_in_with_email_and_password(email, pw)
            login.withdraw()
            dashboard_window()
            
        except:
            login_pw.delete(0,len(pw))
            answer = messagebox.askyesno("Question","Invalid user! Register first!")
            print(answer)

    
    #------------------- DESIGN FUNCTION ------------------------------------#



    #------------------- uI DESIGN------------------------------------#

    login_openimg = Image.open(r'resources\images\signup_bg.png')
    #resize_image = openimage1.resize(( login.winfo_width(),login.winfo_height()))
    login_resize_image = login_openimg.resize((login.winfo_screenwidth(),login.winfo_screenheight()))
    login_img1=ImageTk.PhotoImage(login_resize_image)
    '''l1=ctk.CTkLabel(login,image=img1 )
    l1.pack()'''
    login_label= Label(login, image=login_img1)
    login_label.image = login_img1
    login_label.pack()
    
    
   

    
    login_label1=ctk.CTkLabel( 
        login_label, 
        text="LOG-IN",
        text_color='#3B3B3B',
        font = ctk.CTkFont (
        'Arial', 
        weight="bold",
        size= 40
        ), 
        fg_color='#FFFFFF'
        )
    login_label1.place(x=695, y=100)

    login_email=ctk.CTkEntry(
        login_label, 
        width=320, 
        height=40,
        corner_radius= 30,
        border_color='#C5C5C5',
        placeholder_text='Email',
        placeholder_text_color='#525252',
        fg_color='#C5C5C5',
        text_color='#3B3B3B'
        )

    login_email.place(x=610, y=170)


    login_pw=ctk.CTkEntry(
        login_label, 
        width=320, 
        height=40,
        corner_radius= 30,
        border_color='#C5C5C5',
        placeholder_text='Password',
        placeholder_text_color='#525252',
        fg_color='#C5C5C5',
        text_color='#3B3B3B',
        show= '●'
        )
    login_pw.place(x=610, y=240)

    login_label2=ctk.CTkLabel(
        login_label, 
        text="Forget Password?",
        text_color='#525252',
        font = ctk.CTkFont (
        'Arial', 
        weight="bold",
        size= 12
        ), 
        fg_color='#FFFFFF'
        )

    login_label2.place(x=715, y=290)

    #Create custom button
    login_bttn1 = ctk.CTkButton(
        login_label, 
        command=button_function, 
        width=150, 
        height=40, 
        compound="left", 
        corner_radius= 30, 
        fg_color='maroon', 
        text_color='white', 
        hover_color='#4F0000', 
        font = ctk.CTkFont (
            'Arial', 
            weight="bold"
            ), 
        text="LOG-IN" 
        )

    login_bttn1.place(x=690, y=340)
    
    login_label3=ctk.CTkLabel(
        login_label, 
        text="Don't have an account yet?",
        text_color='#525252',
        font = ctk.CTkFont (
        'Arial', 
        weight="bold",
        size= 12
        ), 
        fg_color='#FFFFFF'
        )

    login_label3.place(x=660, y=480) 
    
    def register_open():
        login.withdraw()
        register_window()
        
    login_label4=ctk.CTkLabel(
        login_label,
        text="Register.",
        text_color='#0000FF',
        font = ctk.CTkFont (
        'Arial', 
        weight="bold",
        size= 12
        ), 
        fg_color='#FFFFFF'
        )

    login_label4.place(x=815, y=480)
    login_label4.bind(
        "<Button-1>", 
        lambda e:
        register_open()
        )

    login.mainloop()

    
#login_window()
