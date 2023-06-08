from logging import RootLogger
import tkinter as tk
from tkinter import ttk
from typing import Self
import customtkinter as ctk
from PIL import Image
from tkcalendar import *
import tkinter.font as tkFont
from ttkthemes import ThemedStyle
from PIL import Image
from PIL import ImageTk


ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

class user_profile_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | Profile")
        self.geometry("{0}x{1}+200+50".format(1000, 600))
        self.resizable(False, False)
        self.configure(fg_color='white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')
        
        self.account_frame = None  # Account Setting frame

        # Header frame
        header_frame = ctk.CTkFrame(self, fg_color='#313131', height=50, width=self.winfo_width(), corner_radius=0)
        header_frame.pack(fill='both', side='top')

        # App logo
        app_logo = ctk.CTkImage(Image.open('python property transfer\images\icons8-data-transfer-483-white.png'),size=(25, 25))
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
            self,
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
            Image.open('python property transfer\images\iuser.png'),
            size=(80, 80)
        )
        user_logo_label = ctk.CTkLabel(rectangle_frame1, image=user_logo, text=None)
        user_logo_label.place(y=40, x=84)

        label = ctk.CTkLabel(rectangle_frame1, text='Prof. Martin Louies C \n Ancaja',font=ctk.CTkFont('Arial', size=18, weight="bold"), text_color='black')
        label.place(y=140, x=30)

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
            Image.open('python property transfer\images\home.png'),
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
            command=self.show_account_settings
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
            Image.open('python property transfer\images\key.png'),
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
            command=self.show_password_settings
        )
        Password_button.pack(fill='x')
        Password_button.place(y=9, x=50)

        rectangle_frame1_3 = ctk.CTkFrame(
            self,
            fg_color='maroon',
            height=500,
            width=2,
            border_width=10,
            border_color='maroon',
            corner_radius=0
        )
        rectangle_frame1_3.pack(fill='y', )
        rectangle_frame1_3.pack(side='left', padx=300)
    
        self.show_account_settings()
    
    #Function for account setting
    def show_account_settings(self):
        if self.account_frame:
            self.account_frame.destroy()
    
        self.account_frame = ctk.CTkFrame(
            self,
            fg_color='transparent',
            height=490,
            width=650,
            border_width=5,
            border_color='light gray',
            corner_radius=20
        )
        self.account_frame.pack(fill='x')
        self.account_frame.pack(side='top')
        self.account_frame.place(y=80, x=320)

        AS_label = ctk.CTkLabel(self.account_frame, text='Account Setting',font=ctk.CTkFont('Arial', size=20, weight="bold"), text_color='black')
        AS_label.place(y=40, x=40)

        #User Fullname
        FN_label = ctk.CTkLabel(self.account_frame, text='First Name', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        FN_label.place(y=100, x=40)
        
        fn_label = ctk.CTkLabel(self.account_frame, text='Martin Louies', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        fn_label.place(y=122, x=72)
        
        MN_label = ctk.CTkLabel(self.account_frame, text='Middle Name', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        MN_label.place(y=100, x=250)
        
        mn_label = ctk.CTkLabel(self.account_frame, text='Castillo', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        mn_label.place(y=122, x=295)
        
        LN_label = ctk.CTkLabel(self.account_frame, text='Last Name', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        LN_label.place(y=100, x=450)
        
        ln_label = ctk.CTkLabel(self.account_frame, text='Ancaja', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        ln_label.place(y=122, x=482)
        
        #User type
        UT_label = ctk.CTkLabel(self.account_frame, text='User type', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UT_label.place(y=180, x=40)
        
        ut_label = ctk.CTkLabel(self.account_frame, text='Faculty', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        ut_label.place(y=202, x=72)
        
        #User Email Address
        EL_label = ctk.CTkLabel(self.account_frame, text='Email Address', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        EL_label.place(y=180, x=250)
        
        el_label = ctk.CTkLabel(self.account_frame, text='martinlouiesancaja@gmail.com', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        el_label.place(y=202, x=295)
        
        #User ID
        UID_label = ctk.CTkLabel(self.account_frame, text='User ID', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UID_label.place(y=260, x=40)
        
        uid_label = ctk.CTkLabel(self.account_frame, text='01234', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        uid_label.place(y=282, x=72)
        
        #User Mobile Number
        UMN_label = ctk.CTkLabel(self.account_frame, text='Mobile Number', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UMN_label.place(y=260, x=250)
        
        umn_tbox = ctk.CTkEntry(self.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=120)
        umn_tbox.place(y=284, x=295)
        
        #User Birthday
        UB_label = ctk.CTkLabel(self.account_frame, text='Birthday', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UB_label.place(y=340, x=40)
        
        ub_tbox = ctk.CTkEntry(self.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=150)
        ub_tbox.place(y=364, x=72)
        
        #User Address
        UA_label = ctk.CTkLabel(self.account_frame, text='Address', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UA_label.place(y=340, x=250)
        
        ua_tbox = ctk.CTkEntry(self.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=300)
        ua_tbox.place(y=364, x=295)
        
        #Update Button
        update_button = ctk.CTkButton(
        self.account_frame,
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
        self.account_frame,
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
    def show_password_settings(self):
        if self.account_frame:
            self.account_frame.destroy()
            
        self.account_frame = ctk.CTkFrame(
            self,
            fg_color='transparent',
            height=490,
            width=650,
            border_width=5,
            border_color='light gray',
            corner_radius=20
        )
        self.account_frame.pack(fill='x')
        self.account_frame.pack(side='top')
        self.account_frame.place(y=80, x=320)

        AS_label = ctk.CTkLabel(self.account_frame, text='Password Setting',font=ctk.CTkFont('Arial', size=20, weight="bold"), text_color='black')
        AS_label.place(y=40, x=40)

        #Current Password
        CP_label = ctk.CTkLabel(self.account_frame, text='Current Password', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        CP_label.place(y=100, x=40)

        cp_tbox = ctk.CTkEntry(self.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=300)
        cp_tbox.place(y=126, x=72)
        
        #New Password
        NP_label = ctk.CTkLabel(self.account_frame, text='New Password', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        NP_label.place(y=180, x=40)

        np_tbox = ctk.CTkEntry(self.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=300)
        np_tbox.place(y=206, x=72)
        
        #Confirm Password
        CNP_label = ctk.CTkLabel(self.account_frame, text='Confirm Password', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        CNP_label.place(y=260, x=40)

        cnp_tbox = ctk.CTkEntry(self.account_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=300)
        cnp_tbox.place(y=286, x=72)
        
        #Save Button
        save_button = ctk.CTkButton(
        self.account_frame,
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
        self.account_frame,
        text="Cancel",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='gray',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=32,
        width=20,
        hover_color='dark gray'  # Change the background color on hover to dark red
        )
        cancel_button.place(y=440, x=120)
        
              
      
if __name__ == '__main__':
    root = tk.Tk()
    user_profile_window(root)
    root.mainloop()

