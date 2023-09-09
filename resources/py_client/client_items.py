import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import *
import pyrebase
from tkinter import messagebox
from ttkthemes import ThemedStyle
from PIL import Image

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

def items_window():
    
    from resources.py_client.client_dashboard import dashboard_window_client
    
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
    
    
    #print(item_db.val())

    #<----------------FIREBASE END--------------------------------->#
    items = ctk.CTkToplevel()
    items.title("Property Transfer | Items")
    items.geometry("{0}x{1}+200+50".format(1000, 600))
    items.resizable(False, False)
    items.configure(fg_color = 'white')
   

    s = ThemedStyle(items)
    s.theme_use('breeze')
    
    def dashboard_open():
        items.withdraw()
        dashboard_window_client()
        
    def add_item_firebase():
        itemno = item_no.get()
        itemname = item_name.get()
        itemdescrip = item_description.get()
        itemqty = item_quantity.get()
        itemloc = item_loc_buildings.get()
        specifyloc = item_loc_room.get()
        for dt2 in item_table.get_children():
            item_table.delete(dt2)
        if len(itemno) == 0 or len(itemname) == 0 or len(itemdescrip) == 0 or len(itemloc) == 0 or itemqty == 0:
            answer=messagebox.askokcancel("Question","Complete your data")
            print(answer)
            
        else:
            
            if itemloc == "Other":
                if len(specifyloc)==0:
                    answer=messagebox.askokcancel("Question","Complete your data")
                    print(answer)
                else:
                    try:
                        item_data = {
                                    "NO": itemno, 
                                    "NAME": itemname,
                                    "DES": itemdescrip, 
                                    "LOC": specifyloc,
                                    "QTY": itemqty,
                                    "DETECT": "TRUE"
                                 }
                        db.child("items_info").child(itemno).set(item_data)
                        item_db = db.child("dashboard_info").child("ITEMNO").get()
                        itemdb_name = item_db.val()['NAME']
                        itemdb_max = item_db.val()['MAX']
                        item_total = item_db.val()['NO']+1
                        db.child("dashboard_info").child("ITEMNO").set({"MAX": itemdb_max,"NAME": itemdb_name,"NO":item_total})
                        item_db = db.child("items_info").order_by_child("DETECT").equal_to("TRUE").get()
                        for dt in item_db.each():
                            item_table.insert("",'end',values=(dt.val()['NO'],dt.val()['NAME'],dt.val()['DES'],dt.val()['LOC'],dt.val()['QTY']))
                            
                        
                        item_no.delete(0,len(itemno))
                        item_name.delete(0,len(itemname))
                        item_description.delete(0,len(itemdescrip))
                        item_loc_room.delete(0,len(specifyloc))
                    except:
                        item_no.delete(0,len(itemno))
                        item_name.delete(0,len(itemname))
                        item_description.delete(0,len(itemdescrip))
                        item_loc_room.delete(0,len(specifyloc))
                        answer=messagebox.askokcancel("Question","Invalid item info, please try again")
                        print(answer)
            else:
                item_data = {
                            "NO": itemno, 
                            "NAME": itemname,
                            "DES": itemdescrip, 
                            "LOC": itemloc,
                            "QTY": itemqty,
                            "DETECT": "TRUE"
                            }
                db.child("items_info").child(itemno).set(item_data)
                item_db = db.child("dashboard_info").child("ITEMNO").get()
                itemdb_name = item_db.val()['NAME']
                itemdb_max = item_db.val()['MAX']
                item_total = item_db.val()['NO']+1
                db.child("dashboard_info").child("ITEMNO").set({"MAX": itemdb_max,"NAME": itemdb_name,"NO":item_total})
                
                item_db = db.child("items_info").order_by_child("DETECT").equal_to("TRUE").get()
                for dt in item_db.each():
                    item_table.insert("",'end',values=(dt.val()['NO'],dt.val()['NAME'],dt.val()['DES'],dt.val()['LOC'],dt.val()['QTY']))
                
                item_no.delete(0,len(itemno))
                item_name.delete(0,len(itemname))
                item_description.delete(0,len(itemdescrip))
                item_loc_room.delete(0,len(itemloc))
    
    #header frame
    header_frame = ctk.CTkFrame(items, fg_color='#313131', height=50, width=items.winfo_width(), corner_radius=0)
    header_frame.pack(fill = 'both', side='top')

    #app logo
    app_logo = ctk.CTkImage(Image.open('resources\images\DEFAULT\PTRLogo_White.png'), size=(25, 25))
    app_logo_label = ctk.CTkLabel(header_frame, image= app_logo, text=None)
    app_logo_label.pack(side = 'left', pady = 10, padx = 10)

    #app name
    app_name1 = ctk.CTkLabel(header_frame, text='PROPERTY', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='white')
    app_name1.pack(side = 'left', pady = 10, padx = 10)
    app_name2 = ctk.CTkLabel(header_frame, text='TRANSFER', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='#ee4444')
    app_name2.pack(side = 'left', pady = 10)
    
    #back
    back_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\_back-white.png'), size=(20, 20))
    back_button = ctk.CTkButton(header_frame, command=dashboard_open, image= back_icon, text=None, fg_color='transparent', width= 30)
    back_button.pack(side = 'right', pady = 10, padx = 5)


    label = ctk.CTkLabel(header_frame, text = 'Items', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
    label.pack(side = 'right',  pady = 15, padx = 15)
    
   
    
    #for table
    frame = ctk.CTkFrame(items, width = 700)
    frame.pack(fill = 'both', side = 'left', padx = 15, pady = 15)
    
    #<----------------TABLE FIREBASE--------------------------------->#
    
    columns = ('property_no', 'name', 'description', 'current_loc', 'quantity')
    
    item_table = ttk.Treeview(frame, columns=columns, show='headings', height=24, selectmode="browse")
    item_table.grid(row=1, column=1, padx=20, pady=20)
    item_table["columns"]=("1","2","3","4", "5")
    item_table['show']='headings'
    item_table.pack(fill=tk.BOTH)
    
    item_table.column("1", width=150, anchor='c')
    item_table.column("2", width=150, anchor='c')
    item_table.column("3", width=150, anchor='c')
    item_table.column("4", width=150, anchor='c')
    item_table.column("5", width= 100, anchor='c')
    
    
    item_table.heading("1", text='Property No.')
    item_table.heading("2", text='Name')
    item_table.heading("3", text='Description')
    item_table.heading("4", text='Current Location')
    item_table.heading("5", text='Quantity')
   
    
    
    
    items_db = db.child("items_info").order_by_child("DETECT").equal_to("TRUE").get()
    for dt in items_db.each():
        item_table.insert("",'end',values=(dt.val()['NO'],dt.val()['NAME'],dt.val()['DES'],dt.val()['LOC'],dt.val()['QTY']))
    
    
    
    #<----------------TABLE FIREBASE--------------------------------->#
    #for input
    frame2 = ctk.CTkFrame(items, width = 300, fg_color='#f5f7f7', corner_radius=20)
    frame2.pack(fill = 'both', side = 'left', padx = (0,15), pady = 15)
    
    #item no.
    item_no_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
    item_no_label_frame.pack(fill = 'x', pady = (20, 0))
    item_no_label = ctk.CTkLabel(item_no_label_frame, text = 'Property No.', font= ctk.CTkFont('Arial', size = 18))
    item_no_label.pack(side = 'left', pady = (10,0), padx = 10)
    
    item_no = ctk.CTkEntry(frame2, width=250, font= ctk.CTkFont('Arial', size = 15), fg_color='white')
    item_no.pack(pady = (0, 10), padx = 10)
    
    #item name
    item_name_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
    item_name_label_frame.pack(fill = 'x')
    item_name_label = ctk.CTkLabel(item_name_label_frame, text = 'Name', font= ctk.CTkFont('Arial', size = 18))
    item_name_label.pack(side = 'left', pady = (10,0), padx = 10)
    
    item_name = ctk.CTkEntry(frame2, width=250, font= ctk.CTkFont('Arial', size = 15), fg_color='white')
    item_name.pack(pady = (0, 10), padx = 10)
    
    #item description
    item_description_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
    item_description_label_frame.pack(fill = 'x')
    item_description_label = ctk.CTkLabel(item_description_label_frame, text = 'Description', font= ctk.CTkFont('Arial', size = 18))
    item_description_label.pack(side = 'left', pady = (10,0), padx = 10)
    
    item_description = ctk.CTkEntry(frame2, width=250, font= ctk.CTkFont('Arial', size = 15), fg_color='white')
    item_description.pack(pady = (0, 10), padx = 10)
    
    #item location
    item_loc_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
    item_loc_label_frame.pack(fill = 'x')
    item_loc_label = ctk.CTkLabel(item_loc_label_frame, text = 'Current Location', font= ctk.CTkFont('Arial', size = 18))
    item_loc_label.pack(side = 'left', pady = (10,0), padx = 10)
    
    loc_options_buildings = ["Computer Laboratory 1", "Computer Laboratory 2", "Computer Laboratory 3", "Other"]
    item_loc_buildings = ctk.CTkOptionMenu(frame2, width=250, values=loc_options_buildings, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 15), dropdown_font=ctk.CTkFont('Arial', size = 15))
    item_loc_buildings.pack(pady = (0, 10), padx = 10)
    item_loc_room = ctk.CTkEntry(frame2, width=250, fg_color= 'white', font= ctk.CTkFont('Arial', size = 15), placeholder_text='Please Specify')
    item_loc_room.pack(pady = (0, 10), padx = 10)
    
    #item quantity
    item_quantity_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
    item_quantity_label_frame.pack(fill = 'x')
    item_quantity_label = ctk.CTkLabel(item_quantity_label_frame, text = 'Quantity', font= ctk.CTkFont('Arial', size = 18))
    item_quantity_label.pack(side = 'left', pady = (10,0), padx = 10)
    
    item_quantity = tk.Spinbox(frame2, from_= 0, to= 1000, borderwidth=2, width=250, font= ctk.CTkFont('Arial', size = 16), bg='white')
    item_quantity.pack(pady = (0, 10), padx = 10)
    
    #add button
    add_button = ctk.CTkButton(frame2, command=add_item_firebase, text = 'Add', font= ctk.CTkFont('Arial', size = 18, weight = "bold"), text_color='white', fg_color='#0077B8', corner_radius = 30)
    add_button.pack(pady = 20, ipady = 5)
    
    
    def callback():
        from resources.py_client.client_dashboard import dashboard_window_client  
        try:
            items.withdraw()
            dashboard_window_client()
            
        except Exception as e:
            if messagebox.askok("ERROR", e ):
                print(e)
                

    items.protocol("WM_DELETE_WINDOW", callback)
    items.mainloop()


    
#items_window()
#2022-04-05030-208-19