import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import *
import pyrebase
from PIL import Image
ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

def user_list_window():

    config = {
        "apiKey": "AIzaSyCyCtXg05ff-tocdUaxjBFfa550TLfKZQ4",
        "authDomain": "puplopez-ptp.firebaseapp.com",
        "databaseURL": "https://puplopez-ptp-default-rtdb.firebaseio.com",
        "projectId": "puplopez-ptp",
        "storageBucket": "puplopez-ptp.appspot.com",
        "messagingSenderId": "638312293451",
        "appId": "1:638312293451:web:79e9405d11db0496f599ce",
        "measurementId": "G-9Z3SPKFR9V"
    }
    
    firebase = pyrebase.initialize_app(config)
    
    db = firebase.database()
    
    
    user_list = ctk.CTk()
    user_list.title("Property Transfer | Users")
    user_list.geometry("{0}x{1}+250+50".format(950,500))
    user_list.resizable(False, False)
    user_list.configure(fg_color = 'white')
    user_list.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

    #header frame
    header_frame = ctk.CTkFrame(user_list, fg_color='#313131', height=50, width=user_list.winfo_width(), corner_radius=0)
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
    
    label = ctk.CTkLabel(header_frame, text = 'Users', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
    label.pack(side = 'right',  pady = 10, padx = 10)
    
    
    #Users
    frame1 = ctk.CTkFrame(user_list, fg_color='transparent')
    frame1.pack(side = 'left', fill = 'both', pady = 10, padx = 15)
    
    columns = ('id_number', 'lastname', 'firstname', 'email' ,'usertype')
    
    user_table = ttk.Treeview(frame1, columns=columns, show='headings', height=20)
    user_table.pack(fill=tk.BOTH)
    
    user_table.column('id_number', width=150)
    user_table.column('lastname', width=150)
    user_table.column('firstname', width=150)
    user_table.column('email', width=150)
    user_table.column('usertype', width=150)
    
    user_table.heading('id_number', text='ID Number')
    user_table.heading('lastname', text='Last Name')
    user_table.heading('firstname', text='First Name')
    user_table.heading('email', text='Email')
    user_table.heading('usertype', text='User Type')
    
    user_db = db.child("user_accounts").order_by_child("ID").get()
    for dt in user_db.each():
        user_table.insert("",'end',values=(dt.val()['ID'],dt.val()['LN'],dt.val()['FN'],dt.val()['EMAIL'],dt.val()['TYPE']))
    
    #Delete User
    frame2 = ctk.CTkFrame(user_list, fg_color='transparent')
    frame2.pack(side = 'right', fill = 'both' ,pady = 15, padx = (0,15))
    
    delete_frame = ctk.CTkFrame(frame2, fg_color='#E9E9E9')
    delete_frame.pack()
    
    del_label = ctk.CTkLabel(delete_frame, text='Delete User')
    del_label.pack(pady = 10, padx = 15)
    
    del_entry = ctk.CTkEntry(delete_frame, placeholder_text='Enter User ID', width=150)
    del_entry.pack(pady = 10, padx = 15)
    
    del_button = ctk.CTkButton(delete_frame, text='Delete', width= 100,fg_color='#0077B8', text_color='white')
    del_button.pack(pady = 10)
    
    user_list.mainloop()


user_list_window()
