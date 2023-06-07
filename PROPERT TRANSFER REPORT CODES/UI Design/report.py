import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from tkcalendar import *

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

def report_window():
    report = ctk.CTk()
    report.title("Property Transfer | Report")
    report.geometry("{0}x{1}+200+25".format(1000,650))
    report.resizable(False, False)
    report.configure(fg_color = 'white')
    report.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')
    
    
    #header frame
    header_frame = ctk.CTkFrame(report, fg_color='#313131', height=50, width=report.winfo_width(), corner_radius=0)
    header_frame.pack(fill = 'both', side='top')

    #app logo
    app_logo = ctk.CTkImage(Image.open('python property transfer\images\icons8-data-transfer-483-white.png'), size=(25, 25))
    app_logo_label = ctk.CTkLabel(header_frame, image= app_logo, text=None)
    app_logo_label.pack(side = 'left', pady = 10, padx = 10)

    #app name
    app_name1 = ctk.CTkLabel(header_frame, text='PROPERTY', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='white')
    app_name1.pack(side = 'left', pady = 10, padx = 10)
    app_name2 = ctk.CTkLabel(header_frame, text='TRANSFER', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='#ee4444')
    app_name2.pack(side = 'left', pady = 10)

    label = ctk.CTkLabel(header_frame, text = 'Reports', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
    label.pack(side = 'right',  pady = 10, padx = 10)
    
    frame = ctk.CTkFrame(report, corner_radius=10)
    frame.pack(fill = 'x', pady = 10, padx = 10)
    
    new_report_button = ctk.CTkButton(frame, text='New Report', font= ctk.CTkFont('Arial', size = 15, weight = "bold"), fg_color='#0077B8', text_color='white', corner_radius = 30)
    new_report_button.pack(side = 'right', pady = 10, padx = 10)
    
    # Rectangle 1
    # Create and pack the content frame for Approved section
    rectangle_frame = ctk.CTkButton(report, fg_color='white', height=95, width=1834, border_width=2, border_color='gray', corner_radius=0, hover_color='white', text=None)
    rectangle_frame.pack(pady=5, padx=20)
    rectangle_frame.configure(cursor = "hand2")

    # Content inside the rectangle frame
    prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
    prof_label.place(x=20, y=20)

    items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black', fg_color='transparent')
    items_label.place(x=20, y=60)

    items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
    items_label.place(x=70, y=60)

    transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
    transfer_type_label.place(x=500, y=20)

    transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
    transfer_type_label.place(x=610, y=20)

    date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
    date_label.place(x=500, y=60)

    date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
    date_label.place(x=550, y=60)
    
    
    report.mainloop()

report_window()