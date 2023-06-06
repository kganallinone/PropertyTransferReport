import tkinter as tk
from tkinter import ttk
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

        # main frame
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill='both', expand=True)
        
        rectangle_frame1 = ctk.CTkFrame(
            main_frame, 
            fg_color='#DEDEDE', 
            height=300, 
            width=250, 
            border_width=10, 
            border_color='light gray',  
            corner_radius=20
            )
        rectangle_frame1.pack(fill='x')
        rectangle_frame1.pack(side='top')
        rectangle_frame1.place(y=30, x=30)
        
        #user logo
        user_logo = ctk.CTkImage(
            Image.open('python property transfer\images\iuser.png'),
            size=(50, 50)
            )
        user_logo_label = ctk.CTkLabel(rectangle_frame1, image=user_logo, text=None)
        user_logo_label.place(y=40, x=95)
        
        label = ctk.CTkLabel(rectangle_frame1, text='Prof. Martin Louies C \n Ancaja', font=ctk.CTkFont('Arial', size=18, weight="bold"), text_color='black')
        label.place(y=110, x=24)
        
        #Home frame
        rectangle_frame1_0 = ctk.CTkFrame(
            rectangle_frame1, 
            fg_color='#DEDEDE', 
            height=50, 
            width=220, 
            border_width=0, 
            border_color='light gray',  
            corner_radius=0
            )
        rectangle_frame1_0.pack(fill='x')
        rectangle_frame1_0.place(y=180, x=15)
        
        #home logo
        home_logo = ctk.CTkImage(
            Image.open('python property transfer\images\home.png'),
            size=(30, 30)
            )
        home_logo_label = ctk.CTkLabel(rectangle_frame1_0, image=home_logo, text=None)
        home_logo_label.pack(side='left')
        home_logo_label.place(y=10, x=20)
        
        #Home Button
        Home_button = ctk.CTkButton(
        rectangle_frame1_0,
        text="Home",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='light gray',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=32,
        width=160,
        hover_color='gray',  # Change the background color on hover to dark red
        text_color='black'
        )
        Home_button.pack(fill='x')
        Home_button.place(y=9, x=60)
        
        #Password frame
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
        rectangle_frame1_0.place(y=228, x=15)
        
        #password logo
        password_logo = ctk.CTkImage(
            Image.open('python property transfer\images\key.png'),
            size=(30, 30)
            )
        password_logo_label = ctk.CTkLabel(rectangle_frame1_0, image=password_logo, text=None)
        password_logo_label.pack(side='left')
        password_logo_label.place(y=10, x=20)
        
        #Password Button
        Password_button = ctk.CTkButton(
        rectangle_frame1_0,
        text="Password",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='light gray',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=32,
        width=160,
        hover_color='gray',  # Change the background color on hover to dark red
        text_color='black'
        )
        Password_button.pack(fill='x')
        Password_button.place(y=9, x=60)
        
        #Account Frame
        rectangle_frame2 = ctk.CTkFrame(
            main_frame, 
            fg_color='#DEDEDE', 
            height=520, 
            width=650, 
            border_width=10, 
            border_color='light gray', 
            corner_radius=20
            )
        rectangle_frame2.pack(fill='x')
        rectangle_frame2.pack(side='top')
        rectangle_frame2.place(y=30, x=320)
        
        #Account Setting
        AS_label = ctk.CTkLabel(rectangle_frame2, text='Account Setting', font=ctk.CTkFont('Arial', size=20, weight="bold"), text_color='black')
        AS_label.place(y=40, x=40)
        
        #User Fullname
        FN_label = ctk.CTkLabel(rectangle_frame2, text='First Name', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        FN_label.place(y=100, x=40)
        
        fn_label = ctk.CTkLabel(rectangle_frame2, text='Martin Louies', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        fn_label.place(y=122, x=72)
        
        MN_label = ctk.CTkLabel(rectangle_frame2, text='Middle Name', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        MN_label.place(y=100, x=250)
        
        mn_label = ctk.CTkLabel(rectangle_frame2, text='Castillo', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        mn_label.place(y=122, x=295)
        
        LN_label = ctk.CTkLabel(rectangle_frame2, text='Last Name', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        LN_label.place(y=100, x=450)
        
        ln_label = ctk.CTkLabel(rectangle_frame2, text='Ancaja', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        ln_label.place(y=122, x=482)
        
        #User type
        UT_label = ctk.CTkLabel(rectangle_frame2, text='User type', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UT_label.place(y=180, x=40)
        
        ut_label = ctk.CTkLabel(rectangle_frame2, text='Faculty', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        ut_label.place(y=202, x=72)
        
        #User Email Address
        EL_label = ctk.CTkLabel(rectangle_frame2, text='Email Address', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        EL_label.place(y=180, x=250)
        
        el_label = ctk.CTkLabel(rectangle_frame2, text='martinlouiesancaja@gmail.com', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        el_label.place(y=202, x=295)
        
        #User ID
        UID_label = ctk.CTkLabel(rectangle_frame2, text='User ID', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UID_label.place(y=260, x=40)
        
        uid_label = ctk.CTkLabel(rectangle_frame2, text='01234', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        uid_label.place(y=282, x=72)
        
        #User Mobile Number
        UMN_label = ctk.CTkLabel(rectangle_frame2, text='Mobile Number', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UMN_label.place(y=260, x=250)
        
        umn_tbox = ctk.CTkEntry(rectangle_frame2, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=120)
        umn_tbox.place(y=282, x=295)
        
        #User Birthday
        UB_label = ctk.CTkLabel(rectangle_frame2, text='Birthday', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UB_label.place(y=340, x=40)
        
        ub_tbox = ctk.CTkEntry(rectangle_frame2, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=150)
        ub_tbox.place(y=362, x=72)
        
        #User Address
        UA_label = ctk.CTkLabel(rectangle_frame2, text='Address', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        UA_label.place(y=340, x=250)
        
        ua_tbox = ctk.CTkEntry(rectangle_frame2, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=300)
        ua_tbox.place(y=362, x=295)
        
        #Update Button
        update_button = ctk.CTkButton(
        rectangle_frame2,
        text="Update",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='blue',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=32,
        width=20,
        hover_color='dark blue'  # Change the background color on hover to dark red
        )
        update_button.place(y=460, x=40)
        
        #Cancel Button
        cancel_button = ctk.CTkButton(
        rectangle_frame2,
        text="Cancel",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='gray',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=32,
        width=20,
        hover_color='dark gray'  # Change the background color on hover to dark red
        )
        cancel_button.place(y=460, x=120)
        
        
        
        
        
        
if __name__ == '__main__':
    root = tk.Tk()
    user_profile_window(root)
    root.mainloop()