import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image
from tkcalendar import *

ctk.set_appearance_mode("system")  # Modes: system (default), light, dark

class report_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | Report")
        self.geometry("{0}x{1}+200+30".format(1000, 650))
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

        label = ctk.CTkLabel(header_frame, text = 'Reports', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
        label.pack(side = 'right',  pady = 15, padx = 15)

        frame = ctk.CTkFrame(self, height=400, corner_radius=20)
        frame.pack(fill = 'both', pady = 15, padx = 15)
        
        sub_frame = ctk.CTkFrame(frame)
        sub_frame.pack(fill = 'x')
        
        entity_label = ctk.CTkLabel(sub_frame, text='Entity Name: ')
        entity_label.pack(side = 'left', pady = 10, padx = 10)
        entity_name = ctk.CTkEntry(sub_frame, width=300)
        entity_name.pack(side = 'left', pady = 10, padx = 10)
        
        fund_cluster_label = ctk.CTkLabel(sub_frame, text='Fund Cluster: ')
        fund_cluster_label.pack(side = 'left', pady = 10, padx = 10)
        fund_cluster= ctk.CTkEntry(sub_frame)
        fund_cluster.pack(side = 'left', pady = 10, padx = 10)
        
        sub_frame2 = ctk.CTkFrame(frame)
        sub_frame2.pack(fill = 'x')
        
        from_label = ctk.CTkLabel(sub_frame2, text='From Accountable Officer/Agency Cluster Fund: ')
        from_label.pack(side = 'left', pady = 10, padx = 10)
        from_ao_afc = ctk.CTkEntry(sub_frame2, width = 300)
        from_ao_afc.pack(side = 'left', pady = 10, padx = 10)
        
        ptr_label = ctk.CTkLabel(sub_frame2, text='PTR No.: ')
        ptr_label.pack(side = 'left', pady = 10, padx = 10)
        ptr_no = ctk.CTkEntry(sub_frame2)
        ptr_no.pack(side = 'left', pady = 10, padx = 10)
        
        sub_frame3 = ctk.CTkFrame(frame)
        sub_frame3.pack(fill = 'x')
        
        to_label = ctk.CTkLabel(sub_frame3, text='To Accountable Officer/Agency Cluster Fund: ')
        to_label.pack(side = 'left', pady = 10, padx = 10)
        to_ao_afc = ctk.CTkEntry(sub_frame3, width = 300)
        to_ao_afc.pack(side = 'left', pady = 10, padx = 10)
        
        date_label = ctk.CTkLabel(sub_frame3, text='Date: ')
        date_label.pack(side = 'left', pady = 10, padx = 10)
        date = DateEntry(sub_frame3, font= ctk.CTkFont('Arial', size = 15) )
        date.pack(side = 'left', pady = 10, padx = 10, ipady =2, ipadx = 2)
        
        frame2 = ctk.CTkFrame(self, corner_radius=20)
        frame2.pack(fill = 'both', pady = 15, padx = 15)
        
        sub_frame4 = ctk.CTkFrame(frame2)
        sub_frame4.pack(fill = 'x')
        
        transfer_type_label = ctk.CTkLabel(sub_frame4, text='Transfer Type (Select Only One): ')
        transfer_type_label.pack(side = 'left', pady = 10, padx = 10)
        transfer_1 = ctk.CTkCheckBox(sub_frame4, text='Donation')
        transfer_1.pack(side = 'left', pady = 10, padx = 10)
        
        transfer_2 = ctk.CTkCheckBox(sub_frame4, text='Relocate')
        transfer_2.pack(side = 'left', pady = 10, padx = 10)
        
        transfer_3 = ctk.CTkCheckBox(sub_frame4, text='Reassign')
        transfer_3.pack(side = 'left', pady = 10, padx = 10)
        
        transfer_4 = ctk.CTkCheckBox(sub_frame4, text='Others (Specify): ')
        transfer_4_2 = ctk.CTkEntry(sub_frame4)
        transfer_4.pack(side = 'left', pady = 10, padx = 10)
        transfer_4_2.pack(side = 'left', pady = 10, padx = 10)
        
        frame3 = ctk.CTkScrollableFrame(self)
        frame3.pack(fill = 'both', pady = 15, padx = 15)
        
        gen_report = ctk.CTkButton(self, text = 'Generate Report', font= ctk.CTkFont('Arial', size = 15, weight = "bold"), text_color='white', corner_radius = 30)
        gen_report.pack(side = 'right', pady = 10, padx = 15, ipady = 5)