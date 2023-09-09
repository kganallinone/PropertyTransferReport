import tkinter as tk
import customtkinter as ctk
from PIL import Image
from tkcalendar import *
from PIL import Image
from tkinter import messagebox 
from openpyxl import load_workbook
import pyrebase


ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

def user_profile_window():
    
    #from resources.py_home.user import how_account_settings
    
    user_profile = tk.Toplevel()
    user_profile.title("Property Transfer | Profile")
    user_profile.geometry("{0}x{1}+200+50".format(1000, 600))
    user_profile.resizable(False, False)
    user_profile.configure(background='white')

    
    user_profile.account_frame = None  # Account Setting frame
    
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

    
    wb = load_workbook("./resources/user/data/UserLog.xlsx", data_only=True)
    sh = wb["User email"]
    email = sh["A1"].value
    print(email)
    
    
    users_db = db.child("user_accounts").order_by_child("EMAIL").equal_to(email).get()
    for dt in users_db.each():
        userstype = dt.val()['TYPE']
        usersfn = dt.val()['FN']
        usermi = dt.val()['MI']
        userln = dt.val()['LN']
        usersemail = dt.val()['EMAIL']
        usersid = dt.val()['ID']
        userpw = dt.val()['PW']
        userdep = dt.val()['DEPARTMENT']

    
    #Function for account setting
    def show_account_settings():
        
        user_profile.account_frame = ctk.CTkFrame(
            user_profile,
            fg_color='transparent',
            height=490,
            width=650,
            border_width=5,
            border_color='light gray',
            corner_radius=20
        )
        user_profile.account_frame.pack(fill='x')
        user_profile.account_frame.pack(side='top')
        user_profile.account_frame.place(y=80, x=320)

        AS_label = ctk.CTkLabel(user_profile.account_frame, text='Account Setting',font=ctk.CTkFont('Arial', size=20, weight="bold"), text_color='black')
        AS_label.place(y=40, x=40)

        #User Fullname
        FN_label = ctk.CTkLabel(user_profile.account_frame, text='First Name', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        FN_label.place(y=100, x=40)
        
        fn_label = ctk.CTkLabel(user_profile.account_frame, text= usersfn, font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        fn_label.place(y=122, x=72)
        
        MN_label = ctk.CTkLabel(user_profile.account_frame, text='Middle Name', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        MN_label.place(y=100, x=250)
        
        mn_label = ctk.CTkLabel(user_profile.account_frame, text=usermi, font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        mn_label.place(y=122, x=295)
        
        LN_label = ctk.CTkLabel(user_profile.account_frame, text='Last Name', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        LN_label.place(y=100, x=450)
        
        ln_label = ctk.CTkLabel(user_profile.account_frame, text=userln, font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        ln_label.place(y=122, x=482)
        
        #User type
        UT_label = ctk.CTkLabel(user_profile.account_frame, text='User type', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UT_label.place(y=180, x=40)
        
        ut_label = ctk.CTkLabel(user_profile.account_frame, text=userstype, font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        ut_label.place(y=202, x=72)
        
        #User Email Address
        EL_label = ctk.CTkLabel(user_profile.account_frame, text='Email Address', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        EL_label.place(y=180, x=250)
        
        el_label = ctk.CTkLabel(user_profile.account_frame, text=usersemail, font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        el_label.place(y=202, x=295)
        
        #User ID
        UID_label = ctk.CTkLabel(user_profile.account_frame, text='User ID', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UID_label.place(y=260, x=40)
        
        uid_label = ctk.CTkLabel(user_profile.account_frame, text=usersid, font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        uid_label.place(y=282, x=72)
        
        #User Mobile Number
        UMN_label = ctk.CTkLabel(user_profile.account_frame, text='Mobile Number', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UMN_label.place(y=260, x=250)
        
        umn_tbox = ctk.CTkEntry(user_profile.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=120)
        umn_tbox.place(y=284, x=295)
        
        #User Birthday
        UB_label = ctk.CTkLabel(user_profile.account_frame, text='Birthday', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UB_label.place(y=340, x=40)
        
        ub_tbox = ctk.CTkEntry(user_profile.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=150)
        ub_tbox.place(y=364, x=72)
        
        #User Address
        UA_label = ctk.CTkLabel(user_profile.account_frame, text='Address', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UA_label.place(y=340, x=250)
        
        ua_tbox = ctk.CTkEntry(user_profile.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=300)
        ua_tbox.place(y=364, x=295)
        
        #Update Button
        update_button = ctk.CTkButton(
        user_profile.account_frame,
        text="Update",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='blue',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=32,
        width=20,
        hover_color='dark blue'  # Change the background color on hover to dark red
        )
        update_button.place(y=440, x=40)
        
        #Cancel Button
        cancel_button = ctk.CTkButton(
        user_profile.account_frame,
        text="Cancel",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='gray',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=32,
        width=20,
        hover_color='dark gray'  # Change the background color on hover to dark red
        )
        cancel_button.place(y=440, x=120)
    
      

    #Function for password account
    def show_password_settings():
        
        def changePW():
            users_db = db.child("user_accounts").order_by_child("EMAIL").equal_to(email).get()
            for dt in users_db.each():
                userstype = dt.val()['TYPE']
                usersfn = dt.val()['FN']
                usermi = dt.val()['MI']
                userln = dt.val()['LN']
                usersemail = dt.val()['EMAIL']
                usersid = dt.val()['ID']
                userpw = dt.val()['PW']
                userdep = dt.val()['DEPARTMENT']
                
            currentpw = cp_tbox.get()
            newpw = np_tbox.get()
            cnewpw = cnp_tbox.get()
            
            
            if len(currentpw) == 0 or len(newpw) == 0 or len(cnewpw) == 0:
                answer = messagebox.askyesno("Question","Please Complete you!")
                print(answer)
            else:
                
                if userpw == currentpw:
                    if newpw == cnewpw:
                        r_data = {
                                "EMAIL": usersemail, 
                                "ID": usersid,
                                "PW": cnewpw, 
                                "TYPE": userstype,
                                "DEPARTMENT": userdep,
                                "FN": usersfn,
                                "MI": usermi,
                                "LN": userln
                                }
                        db.child("user_accounts").child(usersid).set(r_data)
                        answer = messagebox.askyesno("Question","Success.")
                        print(answer)
                    else:
                        answer = messagebox.askyesno("Question","Please confirm your pasword again.")
                        print(answer)
                else:
                    answer = messagebox.askyesno("Question","Invalid password. Please try again!")
                    print(answer)
        
        if user_profile.account_frame:
            user_profile.account_frame.destroy()
            
        user_profile.account_frame = ctk.CTkFrame(
            user_profile,
            fg_color='transparent',
            height=490,
            width=650,
            border_width=5,
            border_color='light gray',
            corner_radius=20
        )
        user_profile.account_frame.pack(fill='x')
        user_profile.account_frame.pack(side='top')
        user_profile.account_frame.place(y=80, x=320)

        AS_label = ctk.CTkLabel(user_profile.account_frame, text='Password Setting',font=ctk.CTkFont('Arial', size=20, weight="bold"), text_color='black')
        AS_label.place(y=40, x=40)

        #Current Password
        CP_label = ctk.CTkLabel(user_profile.account_frame, text='Current Password', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        CP_label.place(y=100, x=40)

        cp_tbox = ctk.CTkEntry(user_profile.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=300)
        cp_tbox.place(y=126, x=72)
        
        #New Password
        NP_label = ctk.CTkLabel(user_profile.account_frame, text='New Password', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        NP_label.place(y=180, x=40)

        np_tbox = ctk.CTkEntry(user_profile.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=300)
        np_tbox.place(y=206, x=72)
        
        #Confirm Password
        CNP_label = ctk.CTkLabel(user_profile.account_frame, text='Confirm Password', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        CNP_label.place(y=260, x=40)

        cnp_tbox = ctk.CTkEntry(user_profile.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=300)
        cnp_tbox.place(y=286, x=72)
        
        #Save Button
        save_button = ctk.CTkButton(
        user_profile.account_frame,
        command= changePW,
        text="Save",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='blue',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=32,
        width=70,
        hover_color='dark blue'  # Change the background color on hover to dark red
        )
        save_button.place(y=440, x=40)
        
        #Cancel Button
        cancel_button = ctk.CTkButton(
        user_profile.account_frame,
        text="Cancel",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='gray',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=32,
        width=20,
        hover_color='dark gray'  # Change the background color on hover to dark red
        )
        cancel_button.place(y=440, x=120)
    # Header frame
    header_frame = ctk.CTkFrame(user_profile, fg_color='#313131', height=50, width=user_profile.winfo_width(), corner_radius=0)
    header_frame.pack(fill='both', side='top')

    # App logo
    app_logo = ctk.CTkImage(Image.open('resources\images\DEFAULT\PTRLogo_White.ico'),size=(25, 25))
    app_logo_label = ctk.CTkLabel(header_frame, image=app_logo, text=None)
    app_logo_label.pack(side='left', pady=10, padx=10)

    # App name
    app_name1 = ctk.CTkLabel(header_frame, text='PROPERTY', font=ctk.CTkFont('Arial', size=22, weight="bold"),text_color='white')
    app_name1.pack(side='left', pady=10, padx=10)
    app_name2 = ctk.CTkLabel(header_frame, text='TRANSFER', font=ctk.CTkFont('Arial', size=22, weight="bold"),text_color='#ee4444')
    app_name2.pack(side='left', pady=10)

    # Label
    label = ctk.CTkLabel(header_frame, text='Profile', font=ctk.CTkFont('Arial', size=25, weight="bold"),text_color='white')
    label.pack(side='right', pady=15, padx=15)

    rectangle_frame1 = ctk.CTkFrame(
        user_profile,
        fg_color='white',
        height=300,
        width=250,
        border_width=5,
        border_color='light gray',
        corner_radius=20
    )
    rectangle_frame1.pack(fill='x')
    rectangle_frame1.pack(side='top')
    rectangle_frame1.place(y=80, x=30)

    # User logo
    user_logo = ctk.CTkImage(
        Image.open('resources\images\DEFAULT\iuser.png'),
        size=(80, 80)
    )
    user_logo_label = ctk.CTkLabel(rectangle_frame1, image=user_logo, text=None)
    user_logo_label.place(y=40, x=84)

    label = ctk.CTkLabel(rectangle_frame1, text= usersfn+" "+usermi+'\n '+userln ,font=ctk.CTkFont('Arial', size=18, weight="bold"), text_color='black')
    label.place(y=140, x=70)

    # Home frame
    rectangle_frame1_0 = ctk.CTkFrame(
        rectangle_frame1,
        fg_color='transparent',
        height=50,
        width=220,
        border_width=0,
        border_color='light gray',
        corner_radius=0
    )
    rectangle_frame1_0.pack(fill='x')
    rectangle_frame1_0.place(y=190, x=15)

    # Home logo
    home_logo = ctk.CTkImage(
        Image.open('resources\images\DEFAULT\home.png'),
        size=(30, 30)
    )
    home_logo_label = ctk.CTkLabel(rectangle_frame1_0, image=home_logo, text=None)
    home_logo_label.pack(side='left')
    home_logo_label.place(y=10, x=10)

    # Home Button
    Home_button = ctk.CTkButton(
        rectangle_frame1_0,
        text="Home",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='light gray',
        corner_radius=10,
        height=32,
        width=160,
        hover_color='gray',
        text_color='black',
        command=show_account_settings
    )
    Home_button.pack(fill='x')
    Home_button.place(y=9, x=50)

    # Password frame
    rectangle_frame1_0 = ctk.CTkFrame(
        rectangle_frame1,
        fg_color='transparent',
        height=50,
        width=220,
        border_width=0,
        border_color='light gray',
        corner_radius=0
    )
    rectangle_frame1_0.pack(fill='x')
    rectangle_frame1_0.place(y=238, x=15)

    # Password logo
    password_logo = ctk.CTkImage(
        Image.open('resources\images\DEFAULT\key.png'),
        size=(30, 30)
    )
    password_logo_label = ctk.CTkLabel(rectangle_frame1_0, image=password_logo, text=None)
    password_logo_label.pack(side='left')
    password_logo_label.place(y=10, x=10)

    # Password Button
    Password_button = ctk.CTkButton(
        rectangle_frame1_0,
        text="Password",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='light gray',
        corner_radius=10,
        height=32,
        width=160,
        hover_color='gray',
        text_color='black',
        command = show_password_settings
    )
    Password_button.pack(fill='x')
    Password_button.place(y=9, x=50)

    rectangle_frame1_3 = ctk.CTkFrame(
        user_profile,
        fg_color='maroon',
        height=500,
        width=2,
        border_width=10,
        border_color='maroon',
        corner_radius=0
    )
    rectangle_frame1_3.pack(fill='y', )
    rectangle_frame1_3.pack(side='left', padx=300)

    
    show_account_settings()
    
    
  
    
    def callback():
        from resources.py_client.client_dashboard import dashboard_window_client
        try:
            user_profile.withdraw()
            dashboard_window_client()
        
        except Exception as e:
            if messagebox.askok("ERROR", e ):
                print(e)

    user_profile.protocol("WM_DELETE_WINDOW", callback)
    
    user_profile.mainloop()
    
#user_profile_window()
              
      

