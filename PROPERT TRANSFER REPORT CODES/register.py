import customtkinter as ctk
from tkinter import messagebox
import pyrebase
from PIL import Image

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

def register_window():
    from login import login_window
    
    #<----------------FIREBASE CONFIGURATION--------------------------------->#
    config = {
        "apiKey": "AIzaSyCyCtXg05ff-tocdUaxjBFfa550TLfKZQ4",
        "authDomain": "puplopez-ptp.firebaseapp.com",
        "projectId": "puplopez-ptp",
        "databaseURL": "https://puplopez-ptp-default-rtdb.firebaseio.com/",
        "storageBucket": "puplopez-ptp.appspot.com",
        "messagingSenderId": "638312293451",
        "appId": "1:638312293451:web:79e9405d11db0496f599ce",
        "measurementId": "G-9Z3SPKFR9V"
    }
    #<----------------FIREBASE CONNECT--------------------------------->#
    firebase = pyrebase.initialize_app(config)

    db = firebase.database()
    # Get a reference to the auth service
    auth = firebase.auth()

    #<----------------FIREBASE END--------------------------------->#
    
    
    register = ctk.CTkToplevel()
    register.title("Property Transfer | Register")
    register.geometry("{0}x{1}+200+50".format(1000, 600))
    register.resizable(False, False)
    register.configure(fg_color = 'white')
    register.iconbitmap('PTR.ico')
    
    def signup_function():
            r_uid = user_id_entry.get()
            r_email =  user_email_entry.get()
            r_pw = user_password_entry.get()
            r_cpw = user_confirm_pass_entry.get()
            r_type = user_type.get()
            
            
            if len(r_uid) == 0 or len(r_email) == 0 or len(r_pw) == 0 or len(r_cpw) == 0:
                answer=messagebox.askokcancel("Question","Complete your data")
                print(answer)
            
            else:
               
                if r_pw == r_cpw:
                    try:
                        auth.create_user_with_email_and_password(r_email, r_cpw)
                        r_data = {
                                    "EMAIL": r_email, 
                                    "ID": r_uid,
                                    "PW": r_cpw, 
                                    "TYPE": r_type,
                                    "DEPARTMENT": "NONE",
                                    "FN": "NONE",
                                    "MI": "NONE",
                                    "LN": "NONE"
                                 }
                        db.child("user_accounts").child(r_uid).set(r_data)
                        register.withdraw()
                        login_window()
                        user_id_entry.delete(0,len(r_uid))
                        user_email_entry.delete(0,len(r_email))
                        user_password_entry.delete(0,len(r_pw))
                        user_confirm_pass_entry.delete(0,len(r_cpw))
                    except:
                        user_id_entry.delete(0,len(r_uid))
                        user_email_entry.delete(0,len(r_email))
                        user_password_entry.delete(0,len(r_pw))
                        user_confirm_pass_entry.delete(0,len(r_cpw))
                        answer=messagebox.askokcancel("Question","Invalid Registration, please try again")
                        print(answer)
                else:
                    
                    answer=messagebox.askokcancel("Question","Please enter the correct password")
                    print(answer)
    
    #<----------------VARIABLES OF ENTRY--------------------------------->#    
        
    #<------------------------------END--------------------------------->#               
    
    reg_form_bg_image = ctk.CTkImage(Image.open('resources\images\_register_image.png'), size=(register.winfo_screenwidth(), register.winfo_screenheight()))
    reg_form_bg = ctk.CTkLabel(register, image=reg_form_bg_image, text=None, anchor='center')
    reg_form_bg.place(x=0, y=0, relwidth=1, relheight=1)
    
    #frame for register form
    reg_form_frame = ctk.CTkFrame(register, fg_color='transparent')
    reg_form_frame.pack(side = 'right', pady = 15, padx = 75)
    
    #register form content
    reg_form_label = ctk.CTkLabel(reg_form_frame, text='Register', font=ctk.CTkFont('Arial', size = 35, weight='bold'),text_color='#3B3B3B')
    reg_form_label.pack(pady = (15, 15), padx = 10)
    
    #user types
    user_type_options = ['Employee','Faculty']
    user_type = ctk.CTkOptionMenu(reg_form_frame, values=user_type_options, fg_color='white', text_color='black',font= ctk.CTkFont('Arial', size = 20), width=200, dropdown_fg_color='white',  dropdown_font=ctk.CTkFont('Arial', size = 20))
    user_type.pack(pady = 10, padx = 10)
    
    #user email
    user_email_entry = ctk.CTkEntry(reg_form_frame,  placeholder_text='Enter email', placeholder_text_color='#525252', width=320, height=40,corner_radius= 30, border_color='#C5C5C5',fg_color='#C5C5C5', text_color='#3B3B3B')
    user_email_entry.pack(pady = 10, padx = 10)
    
    #id entry
    user_id_entry = ctk.CTkEntry(reg_form_frame,placeholder_text='Enter ID',placeholder_text_color='#525252', width=320, height=40,corner_radius= 30,border_color='#C5C5C5',fg_color='#C5C5C5', text_color='#3B3B3B')
    user_id_entry.pack(pady = 10, padx = 10)
    
    #password entry and confirmation
    user_password_entry = ctk.CTkEntry(reg_form_frame,  placeholder_text='Enter Password', placeholder_text_color='#525252', width=320, height=40,corner_radius= 30, border_color='#C5C5C5',fg_color='#C5C5C5', text_color='#3B3B3B', show = '•')
    user_password_entry.pack(pady = 10, padx = 10)
    
    user_confirm_pass_entry = ctk.CTkEntry(reg_form_frame,  placeholder_text='Confirm Password', placeholder_text_color='#525252', width=320, height=40,corner_radius= 30, border_color='#C5C5C5',fg_color='#C5C5C5', text_color='#3B3B3B', show = '•')
    user_confirm_pass_entry.pack(pady = 10, padx = 10)
    
    #register button
    reg_button = ctk.CTkButton(reg_form_frame,command=signup_function, width=150, height=40, compound="left", corner_radius= 30,  fg_color='maroon', text_color='white', hover_color='#4F0000', font = ctk.CTkFont ('Arial', weight="bold"), text="REGISTER")
    reg_button.pack(pady = 25, padx = 10)
    
    #for login
    goto_login_frame = ctk.CTkFrame(reg_form_frame, fg_color='transparent')
    goto_login_frame.pack(pady = (15,0))
    
    goto_login = ctk.CTkLabel(goto_login_frame,text="Already have an account?", text_color='#525252', font = ctk.CTkFont ('Arial', weight="bold",size= 12))
    goto_login.pack(side = 'left')
    
    def login_open():
        register.withdraw()
        login_window()
        
    login_link = ctk.CTkLabel(goto_login_frame, text = 'Log In', text_color='#0000FF',font = ctk.CTkFont('Arial', weight="bold",size= 12))
    login_link.pack(side = 'left', padx = 3)
    
    login_link.bind(
        "<Button-1>", 
        lambda e:
        login_open()
        )
    
    register.mainloop()
    
#register_window()