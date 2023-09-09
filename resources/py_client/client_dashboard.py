import customtkinter as ctk
from openpyxl import load_workbook
from PIL import Image
        
ctk.set_appearance_mode("light")  # Modes: system (default), light, dark       
        
def dashboard_window_client():   
    
    from resources.py_home.login import login_window
    from resources.py_client.client_items import items_window
    from resources.py_client.client_requestlist import requestlist_window
    from resources.py_client.client_profile import user_profile_window
    from resources.py_client.client_translist import requestlist_window2
    
    #<----------------FIREBASE END--------------------------------->#
    dashboard_client = ctk.CTkToplevel()
    dashboard_client.title('Property Transfer | Client Dashboard')
    dashboard_client.geometry("{0}x{1}+300+70".format(700,450))
    dashboard_client.resizable(False, False)
    dashboard_client.configure(fg_color = 'white')
    
    def request_open():
        dashboard_client.withdraw()
        requestlist_window()

    def items_open():
        dashboard_client.withdraw()
        items_window()
        
    def login_open():
        dashboard_client.withdraw()
        login_window()

    def user_open():
        dashboard_client.withdraw()
        user_profile_window()

    def trans_open():
        dashboard_client.withdraw()
        requestlist_window2()

 
    wb = load_workbook("./resources/user/data/UserLog.xlsx", data_only=True)
    sh = wb["User email"]
    email = sh["A1"].value
    print(email)
    
    
    
    topframe1 = ctk.CTkFrame(dashboard_client, fg_color='black', corner_radius=0, width=240)
    topframe1.pack(side = 'left', fill = 'both')
    topframe1.pack_propagate(0)
    
    #app logo
    app_logo = ctk.CTkImage(Image.open('resources\images\DEFAULT\PTRLogo_White.ico'), size=(45, 45))
    app_logo_label = ctk.CTkLabel(topframe1, image= app_logo, text=None)
    app_logo_label.pack(pady = (50,0), padx = 10)
    
    #app name
    subframe1 = ctk.CTkFrame(topframe1, fg_color='transparent', corner_radius=0)
    subframe1.pack(fill = 'x')
    
    app_name1 = ctk.CTkLabel(subframe1, text='PROPERTY', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='white')
    app_name1.pack(pady = 10, padx = 10)
    app_name2 = ctk.CTkLabel(subframe1, text='TRANSFER', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='#ee4444')
    app_name2.pack(pady = 10)
    
    uni = ctk.CTkLabel(subframe1, text = 'PUP - Lopez Branch', font=ctk.CTkFont('Arial', size = 18), text_color='white')
    uni.pack(pady = 50)
    
    
    botframe = ctk.CTkFrame(topframe1, corner_radius=0, height=100)
    botframe.pack(side = 'bottom', fill = 'both')
    botframe.pack_propagate(0)
    
    active_user = ctk.CTkLabel(botframe, text=email)
    active_user.pack(pady = (15,0), padx = 10)
    
    #logout button
    logout_button = ctk.CTkButton(botframe, command= lambda: login_open(), text='Logout', font=ctk.CTkFont('Arial', size = 16), corner_radius=20,fg_color='#AC0D0D',hover_color='#880808')
    logout_button.pack(pady = 10, padx = 10, side = 'bottom')
    
    #item
    topframe2 = ctk.CTkFrame(dashboard_client, fg_color='maroon', corner_radius=0, width=230, height=225)
    topframe2.pack(side = 'left', fill = 'y')
    topframe2.pack_propagate(0)
    
    items_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-item-90.png'), size=(90, 90))
    items_button = ctk.CTkButton(topframe2, command= lambda: items_open(), fg_color='transparent', image= items_icon, text='Items', width= 30, font=ctk.CTkFont('Arial', size = 18), text_color='white', compound="top", hover_color='#808080')
    items_button.pack(pady = 50)
    
    
    #transactions
    botframe2 = ctk.CTkFrame(topframe2, fg_color='white', corner_radius=0, height=225)
    botframe2.pack(side = 'bottom', fill = 'both')
    botframe2.pack_propagate(0)
    
    transaction_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-file-128.png'), size=(90, 90))
    transaction_button = ctk.CTkButton(botframe2, command= lambda: trans_open(), fg_color='transparent',image= transaction_icon, text='Transactions', width= 30,font=ctk.CTkFont('Arial', size = 18),text_color='black',compound="top", hover_color='#e0e0e0')
    transaction_button.pack(pady = 50)
    
    #send requests
    topframe3 = ctk.CTkFrame(dashboard_client, fg_color='white', corner_radius=0, width=230, height=225)
    topframe3.pack(side = 'left', fill = 'y')
    topframe3.pack_propagate(0)
    
    request_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-table-100.png'), size=(90, 90))
    request_button = ctk.CTkButton(topframe3, command= lambda: request_open(), fg_color='transparent', image= request_icon, text='Send Requests', width= 30,font=ctk.CTkFont('Arial', size = 18), text_color='black', compound="top", hover_color='#e0e0e0')
    request_button.pack(pady = 50)
    
    #profile/user
    botframe3 = ctk.CTkFrame(topframe3,fg_color='maroon', corner_radius=0, height=225)
    botframe3.pack(side = 'bottom', fill = 'both')
    botframe3.pack_propagate(0)
    
    users_icon = ctk.CTkImage(Image.open('resources\images\DASHBOARD\icons8-user-90 (2).png'), size=(90, 90))
    users_button = ctk.CTkButton(botframe3, command= lambda: user_open(),  fg_color='transparent', image= users_icon, text='Profile', width= 30,font=ctk.CTkFont('Arial', size = 18), text_color='white', compound="top", hover_color='#808080')
    users_button.pack(pady = 50)

    def callback():
        try:
            from tkinter import messagebox 
            import subprocess
            progs = str(subprocess.check_output('tasklist'))
            process_name = "PropertyTransfer.exe"
            if process_name in progs:
                if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
                    subprocess.call("TASKKILL /F /IM PropertyTransfer.exe", shell=True)
                    dashboard_client.destroy()
            else:
                if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
                    dashboard_client.destroy()
            
        except Exception as e:
            if messagebox.askok("ERROR", e ):
                print(e)

    dashboard_client.protocol("WM_DELETE_WINDOW", callback)
    dashboard_client.mainloop()
    
#dashboard_window_client()