import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image
import tkcalendar

ctk.set_appearance_mode("system")  # Modes: system (default), light, dark

#history window
class history_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | History")
        self.geometry("{0}x{1}+200+50".format(950, 550))
        self.resizable(False, False)
        self.configure(fg_color = 'white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')
    

        #header frame
        header_frame = ctk.CTkFrame(self, fg_color='#313131', height=50, width=self.winfo_width(), corner_radius=0)
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

        #user
        user_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-user-30.png'), size=(30, 30))
        user_button = ctk.CTkButton(header_frame, image= user_icon, text=None, fg_color='transparent', width= 30)
        user_button.pack(side = 'right', pady = 10, padx = 20)
        
        #settings
        settings_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-settings-50.png'), size=(30, 30))
        settings_button = ctk.CTkButton(header_frame, image= settings_icon, text=None, fg_color='transparent', width= 30)
        settings_button.pack(side = 'right', pady = 10, padx = 20)
        
        #notification bell
        notif_bell_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-bell-48.png'), size=(30, 30))
        notif_bell_button = ctk.CTkButton(header_frame, image= notif_bell_icon, text=None, fg_color='transparent', width= 30)
        notif_bell_button.pack(side = 'right', pady = 10, padx = 20)
        
        history_label = ctk.CTkLabel(self, text = 'History')
        history_label.pack()
        
        
#users window
class users_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | Users")
        self.geometry("{0}x{1}+200+50".format(1000, 600))
        self.resizable(False, False)
        self.configure(fg_color = 'white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')
    

        #header frame
        header_frame = ctk.CTkFrame(self, fg_color='#313131', height=50, width=self.winfo_width(), corner_radius=0)
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

        #user
        user_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-user-30.png'), size=(30, 30))
        user_button = ctk.CTkButton(header_frame, image= user_icon, text=None, fg_color='transparent', width= 30)
        user_button.pack(side = 'right', pady = 10, padx = 20)
        
        #settings
        settings_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-settings-50.png'), size=(30, 30))
        settings_button = ctk.CTkButton(header_frame, image= settings_icon, text=None, fg_color='transparent', width= 30)
        settings_button.pack(side = 'right', pady = 10, padx = 20)
        
        #notification bell
        notif_bell_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-bell-48.png'), size=(30, 30))
        notif_bell_button = ctk.CTkButton(header_frame, image= notif_bell_icon, text=None, fg_color='transparent', width= 30)
        notif_bell_button.pack(side = 'right', pady = 10, padx = 20)
        
        users_label = ctk.CTkLabel(self, text = 'Users')
        users_label.pack()
        
        
class report_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | Report")
        self.geometry("{0}x{1}+200+50".format(1000, 600))
        self.resizable(False, False)
        self.configure(fg_color = 'white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')
    

        #header frame
        header_frame = ctk.CTkFrame(self, fg_color='#313131', height=50, width=self.winfo_width(), corner_radius=0)
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

        #user
        user_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-user-30.png'), size=(30, 30))
        user_button = ctk.CTkButton(header_frame, image= user_icon, text=None, fg_color='transparent', width= 30)
        user_button.pack(side = 'right', pady = 10, padx = 20)
        
        #settings
        settings_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-settings-50.png'), size=(30, 30))
        settings_button = ctk.CTkButton(header_frame, image= settings_icon, text=None, fg_color='transparent', width= 30)
        settings_button.pack(side = 'right', pady = 10, padx = 20)
        
        #notification bell
        notif_bell_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-bell-48.png'), size=(30, 30))
        notif_bell_button = ctk.CTkButton(header_frame, image= notif_bell_icon, text=None, fg_color='transparent', width= 30)
        notif_bell_button.pack(side = 'right', pady = 10, padx = 20)
        
        report_label = ctk.CTkLabel(self, text = 'Report')
        report_label.pack()
       
        
#request window
class request_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | Requests")
        self.geometry("{0}x{1}+200+50".format(1000, 600))
        self.resizable(False, False)
        self.configure(fg_color = 'white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')
    

        #header frame
        header_frame = ctk.CTkFrame(self, fg_color='#313131', height=50, width=self.winfo_width(), corner_radius=0)
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

        #user
        user_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-user-30.png'), size=(30, 30))
        user_button = ctk.CTkButton(header_frame, image= user_icon, text=None, fg_color='transparent', width= 30)
        user_button.pack(side = 'right', pady = 10, padx = 20)
        
        #settings
        settings_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-settings-50.png'), size=(30, 30))
        settings_button = ctk.CTkButton(header_frame, image= settings_icon, text=None, fg_color='transparent', width= 30)
        settings_button.pack(side = 'right', pady = 10, padx = 20)
        
        #notification bell
        notif_bell_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-bell-48.png'), size=(30, 30))
        notif_bell_button = ctk.CTkButton(header_frame, image= notif_bell_icon, text=None, fg_color='transparent', width= 30)
        notif_bell_button.pack(side = 'right', pady = 10, padx = 20)
        
        request_label = ctk.CTkLabel(self, text = 'Requests')
        request_label.pack()
        
        
#items window
class items_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | Items")
        self.geometry("{0}x{1}+200+50".format(1000, 600))
        self.resizable(False, False)
        self.configure(fg_color = 'white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')
    

        #header frame
        header_frame = ctk.CTkFrame(self, fg_color='#313131', height=50, width=self.winfo_width(), corner_radius=0)
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

        #user
        user_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-user-30.png'), size=(30, 30))
        user_button = ctk.CTkButton(header_frame, image= user_icon, text=None, fg_color='transparent', width= 30)
        user_button.pack(side = 'right', pady = 10, padx = 20)
        
        #settings
        settings_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-settings-50.png'), size=(30, 30))
        settings_button = ctk.CTkButton(header_frame, image= settings_icon, text=None, fg_color='transparent', width= 30)
        settings_button.pack(side = 'right', pady = 10, padx = 20)
        
        #notification bell
        notif_bell_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-bell-48.png'), size=(30, 30))
        notif_bell_button = ctk.CTkButton(header_frame, image= notif_bell_icon, text=None, fg_color='transparent', width= 30)
        notif_bell_button.pack(side = 'right', pady = 10, padx = 20)
        
        frame = ctk.CTkFrame(self, fg_color='transparent')
        frame.pack(fill = 'both')
        label = ctk.CTkLabel(frame, text = 'Items', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color="black")
        label.pack(side = 'left',  pady = 15, padx = 15)
        
                

#dashboard window
class dashboard_window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Property Transfer | Dashboard")
        self.geometry("{0}x{1}+200+50".format(1000,550))
        self.resizable(False, False)
        self.configure(fg_color = 'white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')
    
        #header frame
        header_frame = ctk.CTkFrame(self, fg_color='#313131', height=50, width=self.winfo_width(), corner_radius=0)
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

        #user
        user_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-user-30.png'), size=(30, 30))
        user_button = ctk.CTkButton(header_frame, image= user_icon, text=None, fg_color='transparent', width= 30)
        user_button.pack(side = 'right', pady = 10, padx = 20)
        
        #settings
        settings_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-settings-50.png'), size=(30, 30))
        settings_button = ctk.CTkButton(header_frame, image= settings_icon, text=None, fg_color='transparent', width= 30)
        settings_button.pack(side = 'right', pady = 10, padx = 20)
        
        #notification bell
        notif_bell_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-bell-48.png'), size=(30, 30))
        notif_bell_button = ctk.CTkButton(header_frame, image= notif_bell_icon, text=None, fg_color='transparent', width= 30)
        notif_bell_button.pack(side = 'right', pady = 10, padx = 20)
        
        #footer
        footer_frame = ctk.CTkFrame(self, fg_color='maroon', height=26, corner_radius=0)
        footer_frame.pack(fill = 'both', side='bottom')
        
        #mini dashboard frame
        mini_dashboard_frame = ctk.CTkFrame(self, fg_color='transparent')
        mini_dashboard_frame.pack(fill='both')
        
        #mini dashboard
        mini_dashboard_title = ctk.CTkLabel(mini_dashboard_frame, text="Mini Dashboard",font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color="black")
        mini_dashboard_title.pack(side = 'left', pady = 15, padx = 15)
        
        mini_dashboard_container = ctk.CTkFrame(self, fg_color='transparent')
        mini_dashboard_container.pack(fill = 'both')
        
        date_filter_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-date-100.png'), size=(40, 40))
        date_filter = ctk.CTkButton(mini_dashboard_frame, text =None, image=date_filter_icon,fg_color='transparent', width= 30 )
        date_filter.pack(side = 'right', pady = 15, padx = 15)
        
        #mini dashboard contents
        mini_dashboard_content_frame = ctk.CTkFrame(mini_dashboard_container, fg_color = 'transparent')
        mini_dashboard_content_frame.pack(side = 'left', padx =24, fill = 'y')
        
        content1 = ctk.CTkFrame(mini_dashboard_content_frame, height=100, width=285, corner_radius=20)
        content1.pack()
        content1.pack_propagate(0)
        content1_label = ctk.CTkLabel(content1, text="No. of Items", height=80, width=260, anchor="nw", font= ctk.CTkFont('Arial', size = 22, weight = "bold"))
        content1_label.pack(pady = (10,0), padx = (10,0))
        
        mini_dashboard_content_frame2 = ctk.CTkFrame(mini_dashboard_container, fg_color = 'transparent')
        mini_dashboard_content_frame2.pack(side = 'left', padx =24, fill = 'y')
        
        content2 = ctk.CTkFrame(mini_dashboard_content_frame2, height=100, width=285, corner_radius=20 )
        content2.pack()
        content2.pack_propagate(0)
        content2_label = ctk.CTkLabel(content2, text="No. of Transfers", height=80, width=260, anchor="nw", font= ctk.CTkFont('Arial', size = 22, weight = "bold"))
        content2_label.pack(pady = (10,0), padx = (10,0))
        
        mini_dashboard_content_frame3 = ctk.CTkFrame(mini_dashboard_container, fg_color = 'transparent')
        mini_dashboard_content_frame3.pack(side = 'left', padx =24,fill = 'y')
        
        content3 = ctk.CTkFrame(mini_dashboard_content_frame3, height=100, width=285, corner_radius=20)
        content3.pack()
        content3.pack_propagate(0)
        content3_label = ctk.CTkLabel(content3, text="No. of Users", height=80, width=260, anchor="nw", font= ctk.CTkFont('Arial', size = 22, weight = "bold"))
        content3_label.pack(pady = (10,0), padx = (10,0))
        
        #nav
        nav_frame = ctk.CTkFrame(mini_dashboard_content_frame, fg_color='transparent')
        nav_frame.pack(fill = 'both')
        
        nav_text = ctk.CTkLabel(nav_frame, text="Navigation",font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color="black")
        nav_text.pack(side = 'left', pady = 15)
        
        nav_container = ctk.CTkFrame(self, fg_color='transparent', width=self.winfo_width(), border_width=2, border_color='maroon', corner_radius=10)
        nav_container.pack(fill = 'both', side = 'left', padx =15, pady = (0,20))

        #nav buttons
        items_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-item-90.png'), size=(90, 90))
        items_button = ctk.CTkButton(nav_container, command = self.open_items_toplevel, fg_color='transparent', image= items_icon, text='Items', width= 30, text_color='black', compound="top")
        items_button.pack(side = 'left', pady = 10, padx = 45)
        
        self.items_toplevel_window = None
        
        request_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-table-100.png'), size=(90, 90))
        request_button = ctk.CTkButton(nav_container, command = self.open_request_toplevel, fg_color='transparent', image= request_icon, text='Request', width= 30, text_color='black', compound="top")
        request_button.pack(side = 'left', pady = 10, padx = 45)
        
        self.request_toplevel_window = None
        
        report_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-file-128.png'), size=(90, 90))
        report_button = ctk.CTkButton(nav_container, command = self.open_report_toplevel, fg_color='transparent',image= report_icon, text='Reports', width= 30,text_color='black',compound="top")
        report_button.pack(side = 'left', pady = 10, padx = 45)
        
        self.report_toplevel_window = None
        
        users_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-users-90.png'), size=(90, 90))
        users_button = ctk.CTkButton(nav_container,command = self.open_users_toplevel, fg_color='transparent', image= users_icon, text='Users', width= 30,text_color='black', compound="top")
        users_button.pack(side = 'left', pady = 10, padx = 45)
        
        self.users_toplevel_window = None
        
        history_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-history-96.png'), size=(90, 90))
        history_button = ctk.CTkButton(nav_container,command = self.open_history_toplevel, fg_color='transparent', image= history_icon, text='History', width= 30, text_color='black',compound="top")
        history_button.pack(side = 'left', pady = 10, padx = 45)
        
        self.history_toplevel_window = None
    
    #open items window
    def open_items_toplevel(self):
        if self.items_toplevel_window is None or not self.items_toplevel_window.winfo_exists():
            self.items_toplevel_window = items_window(self)  # create window if its None or destroyed
        else:
            self.items_toplevel_window.focus()  # if window exists focus it
    
    #open request window
    def open_request_toplevel(self):
        if self.request_toplevel_window is None or not self.request_toplevel_window.winfo_exists():
            self.request_toplevel_window = request_window(self)  # create window if its None or destroyed
        else:
            self.request_toplevel_window.focus()  # if window exists focus it

    #open report window
    def open_report_toplevel(self):
        if self.report_toplevel_window is None or not self.report_toplevel_window.winfo_exists():
            self.report_toplevel_window = report_window(self)  # create window if its None or destroyed
        else:
            self.report_toplevel_window.focus()  # if window exists focus it
    
    #open users window
    def open_users_toplevel(self):
        if self.users_toplevel_window is None or not self.users_toplevel_window.winfo_exists():
            self.users_toplevel_window = users_window(self)  # create window if its None or destroyed
        else:
            self.users_toplevel_window.focus()  # if window exists focus it
    
    #open history window
    def open_history_toplevel(self):
        if self.history_toplevel_window is None or not self.history_toplevel_window.winfo_exists():
            self.history_toplevel_window = history_window(self)  # create window if its None or destroyed
        else:
            self.history_toplevel_window.focus()  # if window exists focus it
    
dashboard_window = dashboard_window()
dashboard_window.mainloop()

