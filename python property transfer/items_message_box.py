import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image
import tkcalendar
from ttkthemes import ThemedStyle

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

def items_msg_box():
    
    msg_box = ctk.CTkToplevel()
    msg_box.title("Notification")
    msg_box.geometry("{0}x{1}+550+200".format(275,170))
    msg_box.resizable(False, False)
    msg_box.configure(fg_color = 'white')
    
    msg_box.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

    #header
    header_frame = ctk.CTkFrame(msg_box,fg_color='#313131', width=msg_box.winfo_width(), height= 30, corner_radius=0)
    header_frame.pack(fill = 'both', side = 'top')

    label_1 = ctk.CTkLabel(header_frame, text='PROPERTY', font= ctk.CTkFont('Arial', size = 12, weight = "bold"), text_color='white')
    label_1.pack(side = 'left', pady = 2, padx = 10)
    label_2 = ctk.CTkLabel(header_frame, text='TRANSFER', font= ctk.CTkFont('Arial', size = 12, weight = "bold"), text_color='#ee4444')
    label_2.pack(side = 'left', pady = 2)
    
    message_frame = ctk.CTkFrame(msg_box, fg_color='transparent')
    message_frame.pack(fill = 'x')
    
    check_icon = ctk.CTkImage(Image.open('python property transfer\images\white-heavy-check-mark.512x512.png'), size=(25,25))
    check_icon_label = ctk.CTkLabel(message_frame, text=None, image=check_icon)
    check_icon_label.pack(side = 'left', padx = (35,10))
    
    message = ctk.CTkLabel(message_frame, text='Item Added!', font=ctk.CTkFont('Arial', size=30, weight='bold'))
    message.pack(side = 'left', pady = 25)
    
    ok_button = ctk.CTkButton(msg_box, text='Okay', text_color='black', width=100, corner_radius=20)
    ok_button.pack(side = 'right', padx = 15)

    msg_box.mainloop()

items_msg_box()
