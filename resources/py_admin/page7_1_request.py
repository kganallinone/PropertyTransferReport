from tkinter import *
import tkinter as tk
import customtkinter as ctk
import pyrebase
from PIL import ImageTk,Image
from datetime import datetime

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


main = tk.Tk()
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

# Display item IDs with a limit of four rows per column
mainframe = ctk.CTkFrame(main,  width=main.winfo_width(), height=main.winfo_height(), fg_color='white')
mainframe.pack(fill='both')

row = 0
column = 0
count = 0
generated_db = db.child("generated_files").order_by_child("PTR").get()
for dt in generated_db.each():
    db_ptr = dt.val()['PTR']
    db_email = dt.val()['EMAIL']
    db_type = dt.val()['TRANSFER']
    db_created = dt.val()['CREATED']
    db_riname = dt.val()['RINAME'].title()
    # Convert string to datetime object
    datetime_obj = datetime.strptime(db_created, "%Y-%m-%d (%H:%M:%S)")

    # Convert datetime object to new format
    new_format = datetime_obj.strftime("%m/%d/%Y %H:%M:%S %p")
    if db_type == "Donation":
        user_db = db.child("user_accounts").order_by_child("EMAIL").equal_to(db_email).get()
        for dt in user_db.each():
            db_id = dt.val()['ID']
            db_fn = dt.val()['FN'].title()
            db_ln = dt.val()['LN'].title()
        mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
        mainuserframe.pack()
        userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=main.winfo_width(), height=80, corner_radius=10 )
        userframe.pack(padx=(20,20) , pady=(5,0))
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
        inner_frame = ctk.CTkFrame(userframe, fg_color='#ececec', width=main.winfo_width(), height=100, corner_radius=10)
        inner_frame.pack()
        inner_frame.pack_propagate(0)
        #User frame
        userinfoframe = ctk.CTkFrame(inner_frame, fg_color='#ececec', width=main.winfo_width(), height=15)
        userinfoframe.pack(fill='both',padx=(3, 0), pady=(5,0),ipadx=0, ipady=0)
        label_name = ctk.CTkLabel(userinfoframe, text=db_ln+", "+db_fn+" ● ID: "+db_id, text_color='black', font=('Arial', 13))
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
    elif db_type == "Relocate":
        mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
        mainuserframe.pack()
        userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=main.winfo_width(), height=80, corner_radius=10 )
        userframe.pack(padx=(20,20) , pady=(5,0))
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
        sideframe = ctk.CTkFrame(userframe, fg_color='#34a853', width=10, corner_radius=10)
        sideframe.pack(fill='y',side='right',padx=1 , pady=1)
        sideframe.pack_propagate(0)
        inner_frame = ctk.CTkFrame(userframe, fg_color='#ececec', width=main.winfo_width(), height=100, corner_radius=10)
        inner_frame.pack()
        inner_frame.pack_propagate(0)
        label_type = ctk.CTkLabel(inner_frame, text=db_type, text_color='black', font=('Arial', 16, 'bold'))
        label_type.pack(side='left',padx=(3, 0), pady=(10,0),ipadx=0, ipady=0, anchor='w')
        label_key = ctk.CTkLabel(inner_frame, text=" | "+db_ptr , text_color='black')
        label_key.pack(side='left', padx=(3,0), pady=(10,0),ipadx=0, ipady=0, anchor='w')
    elif db_type == "Reassignment ":
        mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
        mainuserframe.pack()
        userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=main.winfo_width(), height=80, corner_radius=10 )
        userframe.pack(padx=(20,20) , pady=(5,0))
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
        sideframe = ctk.CTkFrame(userframe, fg_color='#fbbc05', width=10, corner_radius=10)
        sideframe.pack(fill='y',side='right',padx=1 , pady=1)
        sideframe.pack_propagate(0)
        inner_frame = ctk.CTkFrame(userframe, fg_color='#ececec', width=main.winfo_width(), height=100, corner_radius=10)
        inner_frame.pack()
        inner_frame.pack_propagate(0)
        label_type = ctk.CTkLabel(inner_frame, text=db_type, text_color='black', font=('Arial', 16, 'bold'))
        label_type.pack(side='left',padx=(3, 0), pady=(10,0),ipadx=0, ipady=0, anchor='w')
        label_key = ctk.CTkLabel(inner_frame, text=" | "+db_ptr , text_color='black')
        label_key.pack(side='left', padx=(3,0), pady=(10,0),ipadx=0, ipady=0, anchor='w')
    else:
        mainuserframe = ctk.CTkFrame(mainframe, fg_color='white')
        mainuserframe.pack()
        userframe = ctk.CTkFrame(mainuserframe, fg_color='#ececec', width=main.winfo_width(), height=80, corner_radius=10 )
        userframe.pack(padx=(20,20) , pady=(5,0))
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
        sideframe = ctk.CTkFrame(userframe, fg_color='#ea4335', width=10, corner_radius=10)
        sideframe.pack(fill='y',side='right',padx=1 , pady=1)
        sideframe.pack_propagate(0)
        inner_frame = ctk.CTkFrame(userframe, fg_color='#ececec', width=main.winfo_width(), height=100, corner_radius=10)
        inner_frame.pack()
        inner_frame.pack_propagate(0)
        label_type = ctk.CTkLabel(inner_frame, text=db_type, text_color='black', font=('Arial', 16, 'bold'))
        label_type.pack(side='left',padx=(3, 0), pady=(10,0),ipadx=0, ipady=0, anchor='w')
        label_key = ctk.CTkLabel(inner_frame, text=" | "+db_ptr , text_color='black')
        label_key.pack(side='left', padx=(3,0), pady=(10,0),ipadx=0, ipady=0, anchor='w')
    count += 1
    row += 1

main.mainloop()