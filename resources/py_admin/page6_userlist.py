from tkinter import *
import tkinter as tk
import customtkinter as ctk
import pyrebase
from PIL import ImageTk,Image

def user_windowlist():
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


    main = tk.Toplevel()
    main.title("Property Transfer | User Accounts")
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

    # Display item IDs with a limit of four rows per column
    mainframe = ctk.CTkFrame(main,  width=main.winfo_width(), height=main.winfo_height(), fg_color='white')
    mainframe.pack(fill='both')

    row = 0
    column = 0
    count = 0
    user_db = db.child("user_accounts").order_by_child("ID").get()
    for dt in user_db.each():
        db_id = dt.val()['ID']
        db_email = dt.val()['EMAIL']
        db_type = dt.val()['TYPE']
        db_fn = dt.val()['FN'].upper()
        db_ln = dt.val()['LN'].upper()
        if count >= 3:
            count = 0
            column = 0
            row += 1
        if db_type == "Admin":
            mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
            mainuserframe.grid(row=row, column=column)
            userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=300, height=100, corner_radius=10 )
            userframe.pack(padx=(20,10) , pady=(20,0))
            userframe.pack_propagate(0)
            photoframe = ctk.CTkFrame(userframe, fg_color='#ececec', width=50,height=80, corner_radius=20)
            photoframe.pack(fill='y',side='left',padx=5 , pady=5)
            photoframe.pack_propagate(0)
            # Assuming you have an image file named "image.png"
            image_path = r"resources\images\DEFAULT\userprofile.png"

            # Create a CTkImage instance with the image file
            image = ctk.CTkImage(Image.open(image_path), size=(40, 40))
            image_label = ctk.CTkLabel(photoframe, image=image, text='')
            image_label.pack(padx=(3, 0), pady=(10,0))  
            sideframe = ctk.CTkFrame(userframe, fg_color='maroon', width=10, corner_radius=10)
            sideframe.pack(fill='y',side='right',padx=1 , pady=1)
            sideframe.pack_propagate(0)
            inner_frame = ctk.CTkFrame(userframe, fg_color='#ececec', width=300, height=100, corner_radius=10)
            inner_frame.pack()
            inner_frame.pack_propagate(0)
            label_name = ctk.CTkLabel(inner_frame, text=db_ln+", "+db_fn, text_color='black', font=('Arial', 16, 'bold'))
            label_name.pack(padx=(3, 0), pady=(10,0),ipadx=0, ipady=0, anchor='w')
            label_type = ctk.CTkLabel(inner_frame, text=db_type , text_color='black')
            label_type.pack(padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
            label_key = ctk.CTkLabel(inner_frame, text="ID:"+db_id , text_color='black')
            label_key.pack(padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
        elif db_type == "Employee":
            mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
            mainuserframe.grid(row=row, column=column)
            userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=300, height=100, corner_radius=10 )
            userframe.pack(padx=(20,10) , pady=(20,0))
            userframe.pack_propagate(0)
            photoframe = ctk.CTkFrame(userframe, fg_color='#ececec', width=50,height=80, corner_radius=20)
            photoframe.pack(fill='y',side='left',padx=5 , pady=5)
            photoframe.pack_propagate(0)
            # Assuming you have an image file named "image.png"
            image_path = r"resources\images\DEFAULT\userprofile.png"

            # Create a CTkImage instance with the image file
            image = ctk.CTkImage(Image.open(image_path), size=(40, 40))
            image_label = ctk.CTkLabel(photoframe, image=image, text='')
            image_label.pack(padx=(3, 0), pady=(10,0)) 
            sideframe = ctk.CTkFrame(userframe, fg_color='#26ad00', width=10, corner_radius=10)
            sideframe.pack(fill='y',side='right',padx=1 , pady=1)
            sideframe.pack_propagate(0)
            inner_frame = ctk.CTkFrame(userframe, fg_color='#ececec', width=300, height=100, corner_radius=10)
            inner_frame.pack()
            inner_frame.pack_propagate(0)
            label_name = ctk.CTkLabel(inner_frame, text=db_ln+", "+db_fn, text_color='black', font=('Arial', 16, 'bold'))
            label_name.pack(padx=(3, 0), pady=(10,0),ipadx=0, ipady=0, anchor='w')
            label_type = ctk.CTkLabel(inner_frame, text=db_type , text_color='black')
            label_type.pack(padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
            label_key = ctk.CTkLabel(inner_frame, text="ID:"+db_id , text_color='black')
            label_key.pack(padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
        elif db_type == "Faculty":
            mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
            mainuserframe.grid(row=row, column=column)
            userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=300, height=100, corner_radius=10 )
            userframe.pack(padx=(20,10) , pady=(20,0))
            userframe.pack_propagate(0)
            photoframe = ctk.CTkFrame(userframe, fg_color='#ececec', width=50,height=80, corner_radius=20)
            photoframe.pack(fill='y',side='left',padx=5 , pady=5)
            photoframe.pack_propagate(0)
            # Assuming you have an image file named "image.png"
            image_path = r"resources\images\DEFAULT\userprofile.png"

            # Create a CTkImage instance with the image file
            image = ctk.CTkImage(Image.open(image_path), size=(40, 40))
            image_label = ctk.CTkLabel(photoframe, image=image, text='')
            image_label.pack(padx=(3, 0), pady=(10,0)) 
            sideframe = ctk.CTkFrame(userframe, fg_color='#0045ad', width=10, corner_radius=10)
            sideframe.pack(fill='y',side='right',padx=1 , pady=1)
            sideframe.pack_propagate(0)
            inner_frame = ctk.CTkFrame(userframe, fg_color='#ececec', width=300, height=100, corner_radius=10)
            inner_frame.pack()
            inner_frame.pack_propagate(0)
            label_name = ctk.CTkLabel(inner_frame, text=db_ln+", "+db_fn, text_color='black', font=('Arial', 16, 'bold'))
            label_name.pack(padx=(3, 0), pady=(10,0),ipadx=0, ipady=0, anchor='w')
            label_type = ctk.CTkLabel(inner_frame, text=db_type , text_color='black')
            label_type.pack(padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
            label_key = ctk.CTkLabel(inner_frame, text="ID:"+db_id , text_color='black')
            label_key.pack(padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
        

        count += 1
        column += 1

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