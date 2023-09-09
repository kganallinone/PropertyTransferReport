from tkinter import *
import tkinter as tk
import customtkinter as ctk
import pyrebase
from PIL import Image
from datetime import datetime
from openpyxl import load_workbook

def requestlist_window():
    
    # Configure your Firebase project
    firebase_config = {
        "apiKey": "AIzaSyCyCtXg05ff-tocdUaxjBFfa550TLfKZQ4",
        "authDomain": "puplopez-ptp.firebaseapp.com",
        "projectId": "puplopez-ptp",
        "databaseURL": "https://puplopez-ptp-default-rtdb.firebaseio.com/",
        "storageBucket": "puplopez-ptp.appspot.com",
        "messagingSenderId": "638312293451",
        "appId": "1:638312293451:web:79e9405d11db0496f599ce",
        "measurementId": "G-9Z3SPKFR9V"
    }

    # Initialize Pyrebase
    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()

    wb = load_workbook("./resources/user/data/UserLog.xlsx", data_only=True)
    sh = wb["User email"]
    email = sh["A1"].value
    print(email)
    
    def on_frame_click(value):
        from resources.py_admin.admin_openrequest import showptr_window
        main.withdraw()
        showptr_window(value)
        print(0)

    def on_canvas_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def create_report():
        from resources.py_admin.admin_request import request_window
        main.withdraw()
        request_window()
        print(0)
    
       
    main = tk.Toplevel()
    main.title("Property Transfer | Request")
    main.geometry("{0}x{1}+200+50".format(1000, 600))
    main.configure(background='white')
    main.resizable(False, False)
    open_img = PhotoImage(file = 'resources\images\DEFAULT\PTR.png')   
    main.iconphoto(False, open_img)  



    #header frame
    header_frame = ctk.CTkFrame(main, fg_color='#313131', height=50, width=main.winfo_width(), corner_radius=0)
    header_frame.pack(fill = 'both', side='top')
    
    #app logo
    app_logo = ctk.CTkImage(Image.open('resources\images\DEFAULT\PTRLogo_White.ico'), size=(25, 25))
    app_logo_label = ctk.CTkLabel(header_frame, image= app_logo, text=None)
    app_logo_label.pack(side = 'left', pady = 10, padx = 10)

    #app name
    app_name1 = ctk.CTkLabel(header_frame, text='PROPERTY', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='white')
    app_name1.pack(side = 'left', pady = 10, padx = 10)
    app_name2 = ctk.CTkLabel(header_frame, text='TRANSFER', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='#ee4444')
    app_name2.pack(side = 'left', pady = 10)

    #info frame
    info_frame = ctk.CTkFrame(main, fg_color='#ececec', height=40, width=main.winfo_width(), corner_radius=0)
    info_frame.pack(fill = 'both', side='top', padx=(20,20) , pady=(10,0))
    t = ctk.CTkLabel(info_frame, text='Request List |', font= ctk.CTkFont('Arial', size = 16, weight='bold'), text_color='black')
    t.pack(side = 'left', padx=(10,0), pady = 10)
    description = ctk.CTkLabel(info_frame, text=' Wait for approval of your request.', font= ctk.CTkFont('Arial', size = 16), text_color='black')
    description.pack(side = 'left' ,padx=(3,0), pady = 10)
    #create report

    c_report = ctk.CTkButton(info_frame, command=create_report, text = 'Add New Report', font= ctk.CTkFont('Arial', size = 15, weight = "bold"),fg_color='#0077B8', text_color='white', corner_radius = 30)
    c_report.pack(side = 'right', pady = 5, padx = (0, 20))
    
    # Create a canvas widget
    canvas = tk.Canvas(main, bg='white')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a scrollbar widget
    scrollbar = tk.Scrollbar(main, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", on_canvas_configure)

    # Bind the mousewheel event to the canvas
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    # Display item IDs with a limit of four rows per column
    mainframe = ctk.CTkFrame(canvas,  width=main.winfo_width(), height=main.winfo_height(), fg_color='white')
    mainframe.pack(fill='both')

    row = 0
    column = 0
    count = 0
    generated_db = db.child("generated_files").order_by_child("CREATED").get()
    for dt in generated_db.each():
        db_ptr = dt.val()['PTR']
        db_email = dt.val()['EMAIL']
        db_type = dt.val()['TRANSFER']
        db_created = dt.val()['CREATED']
        db_remarks = dt.val()['REMARKS']
        db_riname = dt.val()['RINAME'].title()
        # Convert string to datetime object
        datetime_obj = datetime.strptime(db_created, "%Y-%m-%d (%H:%M:%S)")

        # Convert datetime object to new format
        new_format = datetime_obj.strftime("%m/%d/%Y %H:%M:%S %p")
        if db_remarks == 'PENDING':
            if db_type == "Donation":
                user_db = db.child("user_accounts").order_by_child("EMAIL").equal_to(db_email).get()
                for dt in user_db.each():
                    db_id = dt.val()['ID']
                    db_fn = dt.val()['FN'].title()
                    db_ln = dt.val()['LN'].title()
                mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
                mainuserframe.pack()
                userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=main.winfo_width()-45, height=80, corner_radius=10 )
                userframe.pack(padx=(25,20) , pady=(5,0))
                userframe.pack_propagate(0)
                photoframe = ctk.CTkFrame(userframe, fg_color='#ececec', width=50,height=70, corner_radius=20)
                photoframe.pack(fill='y',side='left',padx=5 , pady=5)
                photoframe.pack_propagate(0)
                # Assuming you have an image file named "image.png"
                image_path = r"resources\images\DEFAULT\userprofile.png"

                # Create a CTkImage instance with the image file
                image = ctk.CTkImage(Image.open(image_path), size=(40, 40))
                image_label = ctk.CTkLabel(photoframe, image=image, text='')
                image_label.pack(padx=(3, 0), pady=(10,0))  
                sideframe = ctk.CTkFrame(userframe, fg_color='#4285F4', width=10, corner_radius=10)
                sideframe.pack(fill='y',side='right',padx=1 , pady=1)
                sideframe.pack_propagate(0)
                inner_frame = ctk.CTkButton(userframe, command=lambda val=db_ptr: on_frame_click(val), fg_color='#ececec',hover_color='#ececec', width=main.winfo_width(), height=100, corner_radius=10)
                inner_frame.pack()
                inner_frame.pack_propagate(0)
                #User frame
                userinfoframe = ctk.CTkFrame(inner_frame, fg_color='#ececec', width=main.winfo_width(), height=15)
                userinfoframe.pack(fill='both',padx=(3, 0), pady=(5,0),ipadx=0, ipady=0)
                label_name = ctk.CTkLabel(userinfoframe, text=db_ln+", "+db_fn+" ● ID: "+db_id+" ● "+db_remarks, text_color='black', font=('Arial', 13))
                label_name.pack(side='left',padx=(0, 0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                dtframe = ctk.CTkFrame(userinfoframe, fg_color='#ececec')
                dtframe.pack(padx=(0, 0), pady=(0,0),ipadx=0, ipady=0, anchor='e')
                label_created = ctk.CTkLabel(dtframe, text=new_format, text_color='black', font=('Arial', 13))
                label_created.pack(padx=(0, 10), pady=(0,0),ipadx=0, ipady=0)
                #Item Info
                label_type = ctk.CTkLabel(inner_frame, text=db_type, text_color='black', font=('Arial', 22, 'bold'))
                label_type.pack(side='left',padx=(3, 0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                label_key = ctk.CTkLabel(inner_frame, text=" | PTR No: "+db_ptr+" | Received by: "+db_riname, text_color='black', font=('Arial', 22))
                label_key.pack(side='left', padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                label_key.bind("<Button-1>", lambda event, val=db_ptr: on_frame_click(val))
                
            elif db_type == "Relocate": 
                user_db = db.child("user_accounts").order_by_child("EMAIL").equal_to(db_email).get()
                for dt in user_db.each():
                    db_id = dt.val()['ID']
                    db_fn = dt.val()['FN'].title()
                    db_ln = dt.val()['LN'].title()
                mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
                mainuserframe.pack()
                userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=main.winfo_width()-45, height=80, corner_radius=10 )
                userframe.pack(padx=(25,20) , pady=(5,0))
                userframe.pack_propagate(0)
                photoframe = ctk.CTkFrame(userframe, fg_color='#ececec', width=50,height=70, corner_radius=20)
                photoframe.pack(fill='y',side='left',padx=5 , pady=5)
                photoframe.pack_propagate(0)
                # Assuming you have an image file named "image.png"
                image_path = r"resources\images\DEFAULT\userprofile.png"

                # Create a CTkImage instance with the image file
                image = ctk.CTkImage(Image.open(image_path), size=(40, 40))
                image_label = ctk.CTkLabel(photoframe, image=image, text='')
                image_label.pack(padx=(3, 0), pady=(10,0))  
                sideframe = ctk.CTkFrame(userframe, fg_color='#34a853', width=10, corner_radius=10)
                sideframe.pack(fill='y',side='right',padx=1 , pady=1)
                sideframe.pack_propagate(0)
                inner_frame = ctk.CTkButton(userframe,command=lambda val=db_ptr: on_frame_click(val), fg_color='#ececec',hover_color='#ececec', width=main.winfo_width(), height=100, corner_radius=10)
                inner_frame.pack()
                inner_frame.pack_propagate(0)
                #User frame
                userinfoframe = ctk.CTkFrame(inner_frame, fg_color='#ececec', width=main.winfo_width(), height=15)
                userinfoframe.pack(fill='both',padx=(3, 0), pady=(5,0),ipadx=0, ipady=0)
                label_name = ctk.CTkLabel(userinfoframe, text=db_ln+", "+db_fn+" ● ID: "+db_id+" ● "+db_remarks, text_color='black', font=('Arial', 13))
                label_name.pack(side='left',padx=(0, 0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                dtframe = ctk.CTkFrame(userinfoframe, fg_color='#ececec')
                dtframe.pack(padx=(0, 0), pady=(0,0),ipadx=0, ipady=0, anchor='e')
                label_created = ctk.CTkLabel(dtframe, text=new_format, text_color='black', font=('Arial', 13))
                label_created.pack(padx=(0, 10), pady=(0,0),ipadx=0, ipady=0)
                #Item Info
                label_type = ctk.CTkLabel(inner_frame, text=db_type, text_color='black', font=('Arial', 22, 'bold'))
                label_type.pack(side='left',padx=(3, 0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                label_key = ctk.CTkLabel(inner_frame, text=" | PTR No: "+db_ptr+" | Received by: "+db_riname, text_color='black', font=('Arial', 22))
                label_key.pack(side='left', padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                label_key.bind("<Button-1>", lambda event, val=db_ptr: on_frame_click(val))
            elif db_type == "Reassignment":
                user_db = db.child("user_accounts").order_by_child("EMAIL").equal_to(db_email).get()
                for dt in user_db.each():
                    db_id = dt.val()['ID']
                    db_fn = dt.val()['FN'].title()
                    db_ln = dt.val()['LN'].title()
                mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
                mainuserframe.pack()
                userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=main.winfo_width()-45, height=80, corner_radius=10 )
                userframe.pack(padx=(25,20) , pady=(5,0))
                userframe.pack_propagate(0)
                photoframe = ctk.CTkFrame(userframe, fg_color='#ececec', width=50,height=70, corner_radius=20)
                photoframe.pack(fill='y',side='left',padx=5 , pady=5)
                photoframe.pack_propagate(0)
                # Assuming you have an image file named "image.png"
                image_path = r"resources\images\DEFAULT\userprofile.png"

                # Create a CTkImage instance with the image file
                image = ctk.CTkImage(Image.open(image_path), size=(40, 40))
                image_label = ctk.CTkLabel(photoframe, image=image, text='')
                image_label.pack(padx=(3, 0), pady=(10,0))  
                sideframe = ctk.CTkFrame(userframe, fg_color='#fbbc05', width=10, corner_radius=10)
                sideframe.pack(fill='y',side='right',padx=1 , pady=1)
                sideframe.pack_propagate(0)
                inner_frame = ctk.CTkButton(userframe, command=lambda val=db_ptr: on_frame_click(val), fg_color='#ececec',hover_color='#ececec', width=main.winfo_width(), height=100, corner_radius=10)
                inner_frame.pack()
                inner_frame.pack_propagate(0)
                #User frame
                userinfoframe = ctk.CTkFrame(inner_frame, fg_color='#ececec', width=main.winfo_width(), height=15)
                userinfoframe.pack(fill='both',padx=(3, 0), pady=(5,0),ipadx=0, ipady=0)
                label_name = ctk.CTkLabel(userinfoframe, text=db_ln+", "+db_fn+" ● ID: "+db_id+" ● "+db_remarks, text_color='black', font=('Arial', 13))
                label_name.pack(side='left',padx=(0, 0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                dtframe = ctk.CTkFrame(userinfoframe, fg_color='#ececec')
                dtframe.pack(padx=(0, 0), pady=(0,0),ipadx=0, ipady=0, anchor='e')
                label_created = ctk.CTkLabel(dtframe, text=new_format, text_color='black', font=('Arial', 13))
                label_created.pack(padx=(0, 10), pady=(0,0),ipadx=0, ipady=0)
                #Item Info
                label_type = ctk.CTkLabel(inner_frame, text=db_type, text_color='black', font=('Arial', 22, 'bold'))
                label_type.pack(side='left',padx=(3, 0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                label_key = ctk.CTkLabel(inner_frame, text=" | PTR No: "+db_ptr+" | Received by: "+db_riname, text_color='black', font=('Arial', 22))
                label_key.pack(side='left', padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                label_key.bind("<Button-1>", lambda event, val=db_ptr: on_frame_click(val))
            else:
                user_db = db.child("user_accounts").order_by_child("EMAIL").equal_to(db_email).get()
                for dt in user_db.each():
                    db_id = dt.val()['ID']
                    db_fn = dt.val()['FN'].title()
                    db_ln = dt.val()['LN'].title()
                mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
                mainuserframe.pack()
                userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=main.winfo_width()-45, height=80, corner_radius=10 )
                userframe.pack(padx=(25,20) , pady=(5,0))
                userframe.pack_propagate(0)
                photoframe = ctk.CTkFrame(userframe, fg_color='#ececec', width=50,height=70, corner_radius=20)
                photoframe.pack(fill='y',side='left',padx=5 , pady=5)
                photoframe.pack_propagate(0)
                # Assuming you have an image file named "image.png"
                image_path = r"resources\images\DEFAULT\userprofile.png"

                # Create a CTkImage instance with the image file
                image = ctk.CTkImage(Image.open(image_path), size=(40, 40))
                image_label = ctk.CTkLabel(photoframe, image=image, text='')
                image_label.pack(padx=(3, 0), pady=(10,0))  
                sideframe = ctk.CTkFrame(userframe, fg_color='#ea4335', width=10, corner_radius=10)
                sideframe.pack(fill='y',side='right',padx=1 , pady=1)
                sideframe.pack_propagate(0)
                inner_frame = ctk.CTkButton(userframe,command=lambda val=db_ptr: on_frame_click(val), fg_color='#ececec',hover_color='#ececec', width=main.winfo_width(), height=100, corner_radius=10)
                inner_frame.pack()
                inner_frame.pack_propagate(0)
                #User frame
                userinfoframe = ctk.CTkFrame(inner_frame, fg_color='#ececec', width=main.winfo_width(), height=15)
                userinfoframe.pack(fill='both',padx=(3, 0), pady=(5,0),ipadx=0, ipady=0)
                label_name = ctk.CTkLabel(userinfoframe, text=db_ln+", "+db_fn+" ● ID: "+db_id+" ● "+db_remarks, text_color='black', font=('Arial', 13))
                label_name.pack(side='left',padx=(0, 0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                dtframe = ctk.CTkFrame(userinfoframe, fg_color='#ececec')
                dtframe.pack(padx=(0, 0), pady=(0,0),ipadx=0, ipady=0, anchor='e')
                label_created = ctk.CTkLabel(dtframe, text=new_format, text_color='black', font=('Arial', 13))
                label_created.pack(padx=(0, 10), pady=(0,0),ipadx=0, ipady=0)
                #Item Info
                label_type = ctk.CTkLabel(inner_frame, text=db_type, text_color='black', font=('Arial', 22, 'bold'))
                label_type.pack(side='left',padx=(3, 0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                label_key = ctk.CTkLabel(inner_frame, text=" | PTR No: "+db_ptr+" | Received by: "+db_riname, text_color='black', font=('Arial', 22))
                label_key.pack(side='left', padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
                label_key.bind("<Button-1>", lambda event, val=db_ptr: on_frame_click(val))
        count += 1
        row += 1

    # Add the scrollable frame to the canvas
    canvas.create_window((0, 0), window=mainframe, anchor="nw")
    
    def callback():
        from tkinter import messagebox
        from resources.py_admin.page1_dashboard import dashboard_window
        try:
            main.withdraw()
            dashboard_window()
                
        except Exception as e:
            if messagebox.askok("ERROR", e ):
                print(e)
                

    main.protocol("WM_DELETE_WINDOW", callback)
    main.mainloop()

#requestlist_window()