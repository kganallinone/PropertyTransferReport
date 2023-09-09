from tkinter import *
import tkinter as tk
import customtkinter as ctk
from PIL import Image
import pyrebase
from openpyxl import load_workbook

        
ctk.set_appearance_mode("light")  # Modes: system (default), light, dark       
        
def dashboard_window():      
    from resources.py_home.login import login_window
    from resources.py_admin.page2_items import items_window
    from resources.py_admin.admin_requestlist import requestlist_window
    from resources.py_admin.page4_setting import settings_window
    from resources.py_home.user import user_profile_window
    from resources.py_admin.admin_reportlist import reportlist_window
    from resources.py_admin.page6_userlist import user_windowlist
    
    
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
    
    #<----------------FIREBASE END--------------------------------->#
    #<----------------GET LOGIN EMAIL--------------------------------->#
    wb = load_workbook("./resources/user/data/UserLog.xlsx", data_only=True)
    sh = wb["User email"]
    email = sh["A1"].value
    print(email)
 
    #<-------------------------- END--------------------------------->#
    item_count = db.child("items_info").get()
    item_db = db.child("dashboard_info").child("ITEMNO").get()
    data = item_count.val()
    itemdb_name = item_db.val()['NAME']
    itemdb_max = item_db.val()['MAX']
    item_total = item_db.val()['NO']
    item_total = len(data)-1
    item_db = db.child("dashboard_info").child("ITEMNO").set({"MAX": itemdb_max,"NAME": itemdb_name,"NO":item_total})
    
    user_db = db.child("dashboard_info").child("USERNO").get()
    user_total = user_db.val()['NO']

        # Assume you have a list stored in a specific location in the database
    list_ref = db.child("generated_files").get()

    # Retrieve the list from the reference
    your_list = list_ref.val()

    # Get the length of the list
    transfer_total = len(your_list)
    
    dashboard = tk.Toplevel()
    dashboard.title("Property Transfer | Admin Dashboard")
    dashboard.geometry("{0}x{1}+200+50".format(1000,550))
    dashboard.resizable(False, False)
    dashboard.configure(background='white')
    open_img = PhotoImage(file = 'resources\images\DEFAULT\PTR.png')   
    dashboard.iconphoto(False, open_img)   
    

    def items_open():
        dashboard.withdraw()
        items_window()
        
    def request_open():
        dashboard.withdraw()
        requestlist_window()
    
    def report_open():
        dashboard.withdraw()
        reportlist_window()
        
    def login_open():
        dashboard.withdraw()
        login_window()
        
    def setting_open():
        dashboard.withdraw()
        settings_window()

    def user_open():
        dashboard.withdraw()
        user_profile_window()
    
    def userlist_open():
        dashboard.withdraw()
        user_windowlist()

    #header frame
    header_frame = ctk.CTkFrame(dashboard, fg_color='#313131', height=50, width=dashboard.winfo_width(), corner_radius=0)
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

    
    
    logout_button = ctk.CTkButton(header_frame,command=lambda: login_open(),  text='Logout', font=ctk.CTkFont('Arial', size=15), fg_color='#AC0D0D', text_color='white', hover_color='#880808', width= 30)
    logout_button.pack(side = 'right', pady = 10, padx = 20)
  
    #settings
    settings_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-settings-50.png'), size=(30, 30))
    settings_button = ctk.CTkButton(header_frame, command= lambda: setting_open(), image= settings_icon, text=None, fg_color='transparent', width= 30)
    settings_button.pack(side = 'right', pady = 10, padx = 20)
    
    #user
    user_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-user-30.png'), size=(30, 30))
    user_button = ctk.CTkButton(header_frame,command= lambda: user_open(), image= user_icon, text=None, fg_color='transparent', width= 30)
    user_button.pack(side = 'right', pady = 10, padx = 20)
    
    #footer
    footer_frame = ctk.CTkFrame(dashboard, fg_color='maroon', height=26, corner_radius=0)
    footer_frame.pack(fill = 'both', side='bottom')
    footer_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-user-30.png'), size=(15, 15))
    footer_logo = ctk.CTkLabel(footer_frame, image= footer_icon, text=None, fg_color='transparent', width= 20)
    footer_logo.pack(side = 'left', pady = 10, padx = 5)
    
    usr_eml = ctk.CTkLabel(footer_frame, text=email, font= ctk.CTkFont('Arial', size = 14, weight = "bold"), text_color='white')
    usr_eml.pack(side = 'left', padx= 0, pady = 10)
   
    
    
    #mini dashboard frame
    mini_dashboard_frame = ctk.CTkFrame(dashboard, fg_color='transparent')
    mini_dashboard_frame.pack(fill='both')
    
    #mini dashboard
    mini_dashboard_title = ctk.CTkLabel(mini_dashboard_frame, text="Mini Dashboard",font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color="black")
    mini_dashboard_title.pack(side = 'left', pady = 15, padx = 15)
    
    mini_dashboard_container = ctk.CTkFrame(dashboard, fg_color='transparent')
    mini_dashboard_container.pack(fill = 'both')
    
   
    #mini dashboard contents
    mini_dashboard_content_frame = ctk.CTkFrame(mini_dashboard_container, fg_color = 'transparent')
    mini_dashboard_content_frame.pack(side = 'left', padx =24, fill = 'y')
    
    content1 = ctk.CTkFrame(mini_dashboard_content_frame, height=100, width=285, corner_radius=20)
    content1.pack()
    content1.pack_propagate(0)
    content1_label = ctk.CTkLabel(content1, text="No. of Items",width=260, anchor="nw", font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='#3B3B3B')
    content1_label.pack(pady = (4,0), padx = (0,0))
    content1_label2 = ctk.CTkLabel(content1, text=item_total , width=260, anchor="e" ,font= ctk.CTkFont('Arial', size = 50, weight = "bold"), text_color='#525252')
    content1_label2.pack(pady = (0,0), padx = (0,0))
    
    mini_dashboard_content_frame2 = ctk.CTkFrame(mini_dashboard_container, fg_color = 'transparent')
    mini_dashboard_content_frame2.pack(side = 'left', padx =24, fill = 'y')
    
    content2 = ctk.CTkFrame(mini_dashboard_content_frame2, height=100, width=285, corner_radius=20 )
    content2.pack()
    content2.pack_propagate(0)
    content2_label = ctk.CTkLabel(content2, text="No. of Transfers",width=260, anchor="nw", font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='#3B3B3B')
    content2_label.pack(pady = (4,0), padx = (0,0))
    content2_label2 = ctk.CTkLabel(content2, text=transfer_total , width=260, anchor="e" ,font= ctk.CTkFont('Arial', size = 50, weight = "bold"), text_color='#525252')
    content2_label2.pack(pady = (0,0), padx = (0,0))
    
    mini_dashboard_content_frame3 = ctk.CTkFrame(mini_dashboard_container, fg_color = 'transparent')
    mini_dashboard_content_frame3.pack(side = 'left', padx =24,fill = 'y')
    
    content3 = ctk.CTkFrame(mini_dashboard_content_frame3, height=100, width=285, corner_radius=20)
    content3.pack()
    content3.pack_propagate(0)
    content3_label = ctk.CTkLabel(content3, text="No. of Users",width=260, anchor="nw", font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='#3B3B3B')
    content3_label.pack(pady = (4,0), padx = (0,0))
    content3_label2 = ctk.CTkLabel(content3, text=user_total , width=260, anchor="e" ,font= ctk.CTkFont('Arial', size = 50, weight = "bold"), text_color='#525252')
    content3_label2.pack(pady = (0,0), padx = (0,0))
    #nav
    nav_frame = ctk.CTkFrame(mini_dashboard_content_frame, fg_color='transparent')
    nav_frame.pack(fill = 'both')
    
    nav_text = ctk.CTkLabel(nav_frame, text="Navigation",font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color="black")
    nav_text.pack(side = 'left', pady = 15)
    
    nav_container = ctk.CTkFrame(dashboard, fg_color='transparent', width=dashboard.winfo_width(), border_width=2, border_color='maroon', corner_radius=10)
    nav_container.pack(fill = 'both', side = 'left', padx =(25,0), pady = (0,20))

    #nav buttons
    items_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-item-90.png'), size=(90, 90))
    items_button = ctk.CTkButton(nav_container, command=items_open, fg_color='transparent', image= items_icon, text='Items', width= 30, text_color='black', compound="top", hover_color='#e0e0e0')
    items_button.pack(side = 'left', pady = 10, padx = 65)
    

    
    request_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-table-100.png'), size=(90, 90))
    request_button = ctk.CTkButton(nav_container, command=request_open, fg_color='transparent', image= request_icon, text='Requests', width= 30, text_color='black', compound="top", hover_color='#e0e0e0')
    request_button.pack(side = 'left', pady = 10, padx = 65)
    

    
    report_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-file-128.png'), size=(90, 90))
    report_button = ctk.CTkButton(nav_container,command=report_open, fg_color='transparent',image= report_icon, text='Reports', width= 30,text_color='black',compound="top", hover_color='#e0e0e0')
    report_button.pack(side = 'left', pady = 10, padx = 65)
    

    
    users_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-users-90.png'), size=(90, 90))
    users_button = ctk.CTkButton(nav_container,command=userlist_open, fg_color='transparent', image= users_icon, text='Users', width= 30,text_color='black', compound="top", hover_color='#e0e0e0')
    users_button.pack(side = 'left', pady = 10, padx = 65)

    
   
    
    def callback():
        try:
            from tkinter import messagebox 
            import subprocess
            progs = str(subprocess.check_output('tasklist'))
            process_name = "PropertyTransfer.exe"
            if process_name in progs:
                if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
                    subprocess.call("TASKKILL /F /IM PropertyTransfer.exe", shell=True)
                    dashboard.destroy()
            else:
                if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
                    dashboard.destroy()
            
        except Exception as e:
            if messagebox.askok("ERROR", e ):
                print(e)

    dashboard.protocol("WM_DELETE_WINDOW", callback)
    dashboard.mainloop()    
    
#dashboard_window()