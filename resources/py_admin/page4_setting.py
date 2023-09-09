import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pyrebase
from PIL import Image

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark


def settings_window():
    from resources.py_admin.page1_dashboard import dashboard_window
    
    
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

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    settings = tk.Toplevel()
    settings.title('Property Transfer | Settings')
    settings.geometry("{0}x{1}+200+50".format(1000,600))
    settings.resizable(False, False)
    
    
    #setting frame
    setting_frame = ctk.CTkFrame(settings, fg_color = 'white')
    setting_frame.pack(fill='both', expand=True)
    
    
    #Settings
    #header frame
    header_frame = ctk.CTkFrame(setting_frame, fg_color='#313131', height=50, width=settings.winfo_width(), corner_radius=0)
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
    back_button = ctk.CTkButton(header_frame, command=lambda: dashboard_open(), image= back_icon, text=None, fg_color='transparent', width= 30)
    back_button.pack(side = 'right', pady = 10, padx = 5)
    
    label = ctk.CTkLabel(header_frame, text = 'Settings', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
    label.pack(side = 'right',  pady = 15, padx = 15)
    
    frame1 = ctk.CTkFrame(setting_frame, fg_color='transparent')
    frame1.pack(fill = 'x')
    
    cat_label = ctk.CTkLabel(frame1, text='Items', font=ctk.CTkFont('Arial', size=22, weight='bold'))
    cat_label.pack(side = 'left', pady = 10, padx = 20)
    
    frame2 = ctk.CTkFrame(setting_frame, fg_color='transparent')
    frame2.pack(fill = 'x')
    
    edit_icon = ctk.CTkImage(Image.open('resources\images\SETTING\edit-black.png'), size=(90, 90))
    edit_item = ctk.CTkButton(frame2, command= lambda: open_edit_item(), image=edit_icon ,text='Edit Item', fg_color='#F6F6F6', font=ctk.CTkFont('Arial', size=20), text_color='black', hover_color='#e0e0e0', width=200)
    edit_item.pack(side = 'left', pady = 15 ,padx = 20)
    
    delete_icon = ctk.CTkImage(Image.open('resources\images\SETTING\delete-black.png'), size = (90, 90))
    delete_item = ctk.CTkButton(frame2, command=lambda: open_delete_item(), image=delete_icon ,text='Delete Item', fg_color='#F6F6F6', font=ctk.CTkFont('Arial', size=20), text_color='black', hover_color='#e0e0e0', width=200)
    delete_item.pack(side = 'left', pady = 15 ,padx = 20)
    
    def open_edit_item():
        edit_item = tk.Toplevel()
        edit_item.title('Property Transfer | Edit Items')
        edit_item.geometry("{0}x{1}+350+50".format(700,525))
        edit_item.resizable(False, False)
        
        qty_var= StringVar(edit_item)
        qty_var.set("1")
        
        #edit frame
        main_frame = ctk.CTkFrame(edit_item, fg_color='white')
        main_frame.pack(fill='both', expand=True)
        
        #header frame
        header_frame = ctk.CTkFrame(main_frame, fg_color='#313131', height=50, width=edit_item.winfo_width(), corner_radius=0)
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
        
        label = ctk.CTkLabel(header_frame, text = 'Edit Items', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
        label.pack(side = 'right',  pady = 15, padx = 15)
        
        frame1 = ctk.CTkFrame(main_frame, fg_color='transparent')
        frame1.pack(fill = 'x')
        
        search_icon = ctk.CTkImage(Image.open('resources\images\SETTING\search_icon.png'), size = (20, 20))
        search_button = ctk.CTkButton(frame1, command= lambda: search_item(), text=None,  image=search_icon, fg_color='transparent', width=20, hover_color='#e0e0e0')
        search_button.pack(side = 'right', pady = 10, padx = (0,20))
        
        search_box = ctk.CTkEntry(frame1, placeholder_text='Search item', width=200, fg_color='white')
        search_box.pack(side = 'right', pady = 10, padx = 5)
        
        #for input
        frame2 = ctk.CTkFrame(main_frame, fg_color='transparent')
        frame2.pack(fill = 'x', pady = 20)
        
        number_label = ctk.CTkLabel(frame2, text='Property Number:', font=ctk.CTkFont('Arial', size=18))
        number_label.pack(side = 'left', pady = 10, padx = 50)
        
        loc_label = ctk.CTkLabel(frame2, text='Current Location:', font=ctk.CTkFont('Arial', size=18))
        loc_label.pack(side = 'right', pady = 10, padx = 160)
        
        #input
        frame3 = ctk.CTkFrame(main_frame, fg_color='transparent')
        frame3.pack(fill = 'x')
        
        property_no = ctk.CTkEntry(frame3, width=200, fg_color='white' )
        property_no.pack(side = 'left', padx = 50)
        
        loc_options_buildings = ["Computer Laboratory 1", "Computer Laboratory 2", "Computer Laboratory 3", "Other"]
        item_loc_buildings = ctk.CTkOptionMenu(frame3, width=250, values=loc_options_buildings, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 15), dropdown_font=ctk.CTkFont('Arial', size = 15))
        item_loc_buildings.pack(side = 'right', pady = (0, 10), padx = 50)
        
        #input
        frame4 = ctk.CTkFrame(main_frame, fg_color='transparent')
        frame4.pack(fill = 'x')
        
        item_loc_room = ctk.CTkEntry(frame4, width=250, fg_color= 'white', font= ctk.CTkFont('Arial', size = 15), placeholder_text='Please Specify')
        item_loc_room.pack(side = 'right', pady = (0, 10), padx = 50)
        
        frame5 = ctk.CTkFrame(main_frame, fg_color='transparent')
        frame5.pack(fill = 'x')
        
        name_label = ctk.CTkLabel(frame5, text='Name', font=ctk.CTkFont('Arial', size=18))
        name_label.pack(side = 'left', pady = 10, padx = 50)
        
        quantity_label = ctk.CTkLabel(frame5, text='Quantity', font=ctk.CTkFont('Arial', size=18) )
        quantity_label.pack(side = 'right', pady = 10, padx = 235)
        
        #input
        frame5 = ctk.CTkFrame(main_frame, fg_color='transparent')
        frame5.pack(fill = 'x')
        
        property_name = ctk.CTkEntry(frame5, width=200, fg_color='white')
        property_name.pack(side = 'left', padx =50)
        
        item_quantity = tk.Spinbox(frame5, from_= 0, to= 1000, borderwidth=2, font= ctk.CTkFont('Arial', size = 16), bg='white', textvariable=qty_var)
        item_quantity.pack(side = 'right', pady = 10, padx = (100, 150))
        
        frame6 = ctk.CTkFrame(main_frame, fg_color='transparent')
        frame6.pack(fill = 'x')
        
        desc_label = ctk.CTkLabel(frame6, text='Description', font=ctk.CTkFont('Arial', size=18))
        desc_label.pack(side = 'left', pady = 10, padx = 50)
        
        #input
        frame7 = ctk.CTkFrame(main_frame, fg_color='transparent')
        frame7.pack(fill = 'x')
        
        description = ctk.CTkEntry(frame7, width=200, fg_color='white')
        description.pack(side = 'left', pady = 10, padx = 50)
        
        save = ctk.CTkButton(main_frame, command= lambda: save_item(), text='Save', font=ctk.CTkFont('Arial', size = 18, weight='bold'), fg_color='#0077b8')
        save.pack(side = 'right', padx = 20)
        
        
        
        def search_item():
            itemno = search_box.get()
            
            if len(itemno)== 0:
                answer=messagebox.askokcancel("Question","Enter Property No. first.")
                print(answer)
            else:    
                
                item_db = db.child("items_info").order_by_child("NO").equal_to(itemno).get()
                dltno = property_no.get()
                dttname = property_name.get()
                dtldesc = description.get()
                
                for dt in item_db.each():
                    var1 = dt.val()['NO']
                    var2 = dt.val()['NAME']
                    var3 = dt.val()['DES']
                    var4 = dt.val()['LOC']
                    var5 = dt.val()['QTY']
                    property_no.delete(0,len(dltno))
                    property_no.insert(0,var1)
                    property_name.delete(0,len(dttname))
                    property_name.insert(0,var2)
                    description.delete(0,len(dtldesc))
                    description.insert(0,var3)
                    item_loc_buildings.set(var4)
                    qty_var.set(var5)
                
        def save_item():
            itemno = property_no.get()
            itemname = property_name.get()
            itemdescrip = description.get()
            itemqty = item_quantity.get()
            itemloc = item_loc_buildings.get()
            specifyloc = item_loc_room.get()
            
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
                            
                            
                            property_no.delete(0,len(itemno))
                            property_name.delete(0,len(itemname))
                            description.delete(0,len(itemdescrip))
                            item_loc_room.delete(0,len(specifyloc))
                        except:
                            property_no.delete(0,len(itemno))
                            property_name.delete(0,len(itemname))
                            description.delete(0,len(itemdescrip))
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
                    
                    
                    property_no.delete(0,len(itemno))
                    property_name.delete(0,len(itemname))
                    description.delete(0,len(itemdescrip))
                    item_loc_room.delete(0,len(specifyloc))
                
        edit_item.mainloop()
        
        
        
    
    def open_delete_item():
        delete_item = tk.Toplevel()
        delete_item.title('Property Transfer | Edit Items')
        delete_item.geometry("{0}x{1}+350+50".format(700,525))
        delete_item.resizable(False, False)
        

        #header frame
        header_frame = ctk.CTkFrame(delete_item, fg_color='#313131', height=50, width=delete_item.winfo_width(), corner_radius=0)
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
        
        

        label = ctk.CTkLabel(header_frame, text = 'Delete Items', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
        label.pack(side = 'right',  pady = 15, padx = 15)

        frame1 = ctk.CTkFrame(delete_item, fg_color='transparent')
        frame1.pack(fill = 'x')

        search_icon = ctk.CTkImage(Image.open('resources\images\SETTING\search_icon.png'), size = (20, 20))
        search_button = ctk.CTkButton(frame1, text=None, image=search_icon, fg_color='transparent', width=20, hover_color='#e0e0e0')
        search_button.pack(side = 'right', pady = 10, padx = (0,20))

        search_box = ctk.CTkEntry(frame1, placeholder_text='Search item', width=200, fg_color='white')
        search_box.pack(side = 'right', pady = 10, padx = 5)

        #for input
        frame2 = ctk.CTkFrame(delete_item, fg_color='transparent')
        frame2.pack(fill = 'x', pady = 20)

        number_label = ctk.CTkLabel(frame2, text='Property Number:', font=ctk.CTkFont('Arial', size=18))
        number_label.pack(side = 'left', pady = 10, padx = 50)

        loc_label = ctk.CTkLabel(frame2, text='Current Location:', font=ctk.CTkFont('Arial', size=18))
        loc_label.pack(side = 'right', pady = 10, padx = 160)

        #input
        frame3 = ctk.CTkFrame(delete_item, fg_color='transparent')
        frame3.pack(fill = 'x')

        property_no = ctk.CTkEntry(frame3, width=200, fg_color='white')
        property_no.pack(side = 'left', padx = 50)

        loc_options_buildings = ["Computer Laboratory 1", "Computer Laboratory 2", "Computer Laboratory 3", "Other"]
        item_loc_buildings = ctk.CTkOptionMenu(frame3, width=250, values=loc_options_buildings, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 15), dropdown_font=ctk.CTkFont('Arial', size = 15))
        item_loc_buildings.pack(side = 'right', pady = (0, 10), padx = 50)

        #input
        frame4 = ctk.CTkFrame(delete_item, fg_color='transparent')
        frame4.pack(fill = 'x')

        item_loc_room = ctk.CTkEntry(frame4, width=250, fg_color= 'white', font= ctk.CTkFont('Arial', size = 15), placeholder_text='Please Specify')
        item_loc_room.pack(side = 'right', pady = (0, 10), padx = 50)

        frame5 = ctk.CTkFrame(delete_item, fg_color='transparent')
        frame5.pack(fill = 'x')

        name_label = ctk.CTkLabel(frame5, text='Name', font=ctk.CTkFont('Arial', size=18) )
        name_label.pack(side = 'left', pady = 10, padx = 50)

        quantity_label = ctk.CTkLabel(frame5, text='Quantity', font=ctk.CTkFont('Arial', size=18) )
        quantity_label.pack(side = 'right', pady = 10, padx = 235)

        #input
        frame5 = ctk.CTkFrame(delete_item, fg_color='transparent')
        frame5.pack(fill = 'x')

        property_name = ctk.CTkEntry(frame5, width=200, fg_color='white')
        property_name.pack(side = 'left', padx =50)

        item_quantity = tk.Spinbox(frame5, from_= 0, to= 1000, borderwidth=2, font= ctk.CTkFont('Arial', size = 16), bg='white')
        item_quantity.pack(side = 'right', pady = 10, padx = (100, 150))

        frame6 = ctk.CTkFrame(delete_item, fg_color='transparent')
        frame6.pack(fill = 'x')

        desc_label = ctk.CTkLabel(frame6, text='Description', font=ctk.CTkFont('Arial', size=18))
        desc_label.pack(side = 'left', pady = 10, padx = 50)

        #input
        frame7 = ctk.CTkFrame(delete_item, fg_color='transparent')
        frame7.pack(fill = 'x')

        description = ctk.CTkEntry(frame7, width=200, fg_color='white')
        description.pack(side = 'left', pady = 10, padx = 50)

        delete = ctk.CTkButton(delete_item, text='Delete', font=ctk.CTkFont('Arial', size = 18, weight='bold'), fg_color='#EE2A2A', hover_color='#B51818')
        delete.pack(side = 'right', padx = 20)

        delete_all = ctk.CTkButton(delete_item, text='Delete All', font=ctk.CTkFont('Arial', size = 18, weight='bold'), text_color='black',fg_color='#f6f6f6', hover_color='#B51818')
        delete_all.pack(side = 'right', padx = 20)
        
        

    
    def dashboard_open():
        settings.withdraw()
        dashboard_window()

    settings.mainloop()

#settings_window()