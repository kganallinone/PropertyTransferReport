import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image
import tkcalendar
from ttkthemes import ThemedStyle

ctk.set_appearance_mode("system")  # Modes: system (default), light, dark

def register_window():
    
    register = ctk.CTkToplevel()
    register.title("Property Transfer | Register")
    register.geometry("{0}x{1}+200+50".format(1000, 600))
    register.resizable(False, False)
    register.configure(fg_color = 'white')
    register.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')
    
    reg_form_bg_image = ctk.CTkImage(Image.open('python property transfer\images\_register_image.png'), size=(register.winfo_screenwidth(), register.winfo_screenheight()))
    reg_form_bg = ctk.CTkLabel(register, image=reg_form_bg_image, text=None, anchor='center')
    reg_form_bg.place(x=0, y=0, relwidth=1, relheight=1)
    
    #frame for register form
    reg_form_frame = ctk.CTkFrame(register, fg_color='transparent')
    reg_form_frame.pack(side = 'right', pady = 15, padx = 75)
    
    #register form content
    reg_form_label = ctk.CTkLabel(reg_form_frame, text='Register', font=ctk.CTkFont('Arial', size = 35, weight='bold'),text_color='#3B3B3B')
    reg_form_label.pack(pady = (15, 15), padx = 10)
    
    #user types
    user_type_options = ['Admin', 'Faculty', 'Employee']
    user_type = ctk.CTkOptionMenu(reg_form_frame, values=user_type_options, fg_color='white', text_color='black',font= ctk.CTkFont('Arial', size = 20), width=200, dropdown_fg_color='white',  dropdown_font=ctk.CTkFont('Arial', size = 20))
    user_type.pack(pady = 10, padx = 10)
    
    #user email
    user_email_entry = ctk.CTkEntry(reg_form_frame, placeholder_text='Enter email', placeholder_text_color='#525252', width=320, height=40,corner_radius= 30, border_color='#C5C5C5',fg_color='#C5C5C5', text_color='#3B3B3B')
    user_email_entry.pack(pady = 10, padx = 10)
    
    #id entry
    user_id_entry = ctk.CTkEntry(reg_form_frame, placeholder_text='Enter ID',placeholder_text_color='#525252', width=320, height=40,corner_radius= 30,border_color='#C5C5C5',fg_color='#C5C5C5', text_color='#3B3B3B')
    user_id_entry.pack(pady = 10, padx = 10)
    
    #password entry and confirmation
    user_password_entry = ctk.CTkEntry(reg_form_frame, placeholder_text='Enter Password', placeholder_text_color='#525252', width=320, height=40,corner_radius= 30, border_color='#C5C5C5',fg_color='#C5C5C5', text_color='#3B3B3B', show = '•')
    user_password_entry.pack(pady = 10, padx = 10)
    
    user_confirm_pass_entry = ctk.CTkEntry(reg_form_frame, placeholder_text='Confirm Password', placeholder_text_color='#525252', width=320, height=40,corner_radius= 30, border_color='#C5C5C5',fg_color='#C5C5C5', text_color='#3B3B3B', show = '•')
    user_confirm_pass_entry.pack(pady = 10, padx = 10)
    
    #register button
    reg_button = ctk.CTkButton(reg_form_frame, width=150, height=40, compound="left", corner_radius= 30,  fg_color='maroon', text_color='white', hover_color='#AFAFAF', font = ctk.CTkFont ('Arial', weight="bold"), text="REGISTER")
    reg_button.pack(pady = 25, padx = 10)
    
    #for login
    goto_login_frame = ctk.CTkFrame(reg_form_frame, fg_color='transparent')
    goto_login_frame.pack(pady = (15,0))
    
    goto_login = ctk.CTkLabel(goto_login_frame,text="Already have an account?", text_color='#525252', font = ctk.CTkFont ('Arial', weight="bold",size= 12))
    goto_login.pack(side = 'left')
    
    login_link = ctk.CTkLabel(goto_login_frame, text = 'Log In', text_color='#0000FF',font = ctk.CTkFont('Arial', weight="bold",size= 12))
    login_link.pack(side = 'left', padx = 3)
    
    register.mainloop()
    
register_window()