import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image

ctk.set_appearance_mode("system")  # Modes: system (default), light, dark

class items_window(ctk.CTk):
    def __init__(self):
        super().__init__()
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
        
        #mini dashboard frame
        mini_dashboard_frame = ctk.CTkFrame(self, fg_color='transparent' )
        mini_dashboard_frame.pack(fill='both')
        
        #mini dashboard
        mini_dashboard_title = ctk.CTkLabel(mini_dashboard_frame, text="Mini Dashboard",font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color="black")
        mini_dashboard_title.pack(side = 'left', pady = 15, padx = 15)
        
        mini_dashboard_container = ctk.CTkFrame(self, fg_color='transparent')
        mini_dashboard_container.pack(fill = 'both')
        #mini dashboard contents
        mini_dashboard_content_frame = ctk.CTkFrame(mini_dashboard_container, fg_color = 'transparent')
        mini_dashboard_content_frame.pack(side = 'left', padx =20,fill = 'y')
        
        content1 = ctk.CTkFrame(mini_dashboard_content_frame, height=100, width=300, corner_radius=15 )
        content1.pack(fill = 'y')
        content1_label = ctk.CTkLabel(content1, text="No. of Items", height=100, width=300, anchor="nw", font= ctk.CTkFont('Arial', size = 22, weight = "bold"))
        content1_label.pack(pady = (10,0), padx = (10,0))
        
        mini_dashboard_content_frame2 = ctk.CTkFrame(mini_dashboard_container, fg_color = 'transparent')
        mini_dashboard_content_frame2.pack(side = 'left', padx =20, fill = 'y')
        
        content2 = ctk.CTkFrame(mini_dashboard_content_frame2, height=100, width=300, corner_radius=15 )
        content2.pack(fill = 'y')
        content2_label = ctk.CTkLabel(content2, text="No. of Transfers", height=100, width=300, anchor="nw", font= ctk.CTkFont('Arial', size = 22, weight = "bold"))
        content2_label.pack(pady = (10,0), padx = (10,0))
        
        mini_dashboard_content_frame3 = ctk.CTkFrame(mini_dashboard_container, fg_color = 'transparent')
        mini_dashboard_content_frame3.pack(side = 'left', padx =20,fill = 'y')
        
        content3 = ctk.CTkFrame(mini_dashboard_content_frame3, height=100, width=300, corner_radius=15)
        content3.pack(fill = 'y')
        content3_label = ctk.CTkLabel(content3, text="No. of Users", height=100, width=300, anchor="nw", font= ctk.CTkFont('Arial', size = 22, weight = "bold"))
        content3_label.pack(pady = (10,0), padx = (10,0))
        

items_window = items_window()
items_window.mainloop()

