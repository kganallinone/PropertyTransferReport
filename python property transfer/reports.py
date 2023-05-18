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
        self.geometry("{0}x{1}+200+5".format(1050, 690))
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
        frame.pack(fill = 'both', pady = 5, padx = 15)
        
        sub_frame = ctk.CTkFrame(frame, fg_color='transparent')
        sub_frame.pack(fill = 'x')
        
        entity_label = ctk.CTkLabel(sub_frame, text='Entity Name: ')
        entity_label.pack(side = 'left', pady = 5, padx = 10)
        
        entities = ["Polytechnic University of the Philippines - Lopez Branch"]
        entity_name = ctk.CTkOptionMenu(sub_frame, width=300, values=entities, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 12), dropdown_font=ctk.CTkFont('Arial', size = 12))
        entity_name.pack(side = 'left', pady = 5, padx = 10)
        
        fund_cluster_label = ctk.CTkLabel(sub_frame, text='Fund Cluster: ')
        fund_cluster_label.pack(side = 'left', pady = 5, padx = 10)
        fund_cluster= ctk.CTkEntry(sub_frame)
        fund_cluster.pack(side = 'left', pady = 5, padx = 10)
        
        sub_frame2 = ctk.CTkFrame(frame, fg_color='transparent')
        sub_frame2.pack(fill = 'x')
        
        from_label = ctk.CTkLabel(sub_frame2, text='From Accountable Officer/Agency Cluster Fund: ')
        from_label.pack(side = 'left', pady = 5, padx = 10)
        from_ao_afc = ctk.CTkEntry(sub_frame2, width = 300)
        from_ao_afc.pack(side = 'left', pady = 5, padx = 10)
        
        ptr_label = ctk.CTkLabel(sub_frame2, text='PTR No.: ')
        ptr_label.pack(side = 'left', pady = 5, padx = 10)
        ptr_no = ctk.CTkEntry(sub_frame2)
        ptr_no.pack(side = 'left', pady = 5, padx = 10)
        
        sub_frame3 = ctk.CTkFrame(frame, fg_color='transparent')
        sub_frame3.pack(fill = 'x')
        
        to_label = ctk.CTkLabel(sub_frame3, text='To Accountable Officer/Agency Cluster Fund: ')
        to_label.pack(side = 'left', pady = 5, padx = 10)
        to_ao_afc = ctk.CTkEntry(sub_frame3, width = 300)
        to_ao_afc.pack(side = 'left', pady = 5, padx = 10)
        
        date_label = ctk.CTkLabel(sub_frame3, text='Date: ')
        date_label.pack(side = 'left', pady = 5, padx = 10)
        date = DateEntry(sub_frame3, font= ctk.CTkFont('Arial', size = 15) )
        date.pack(side = 'left', pady = 5, padx = 10, ipady =2, ipadx = 2)
        
        frame2 = ctk.CTkFrame(self, corner_radius=20)
        frame2.pack(fill = 'both', pady = 5, padx = 15)
        
        sub_frame4 = ctk.CTkFrame(frame2, fg_color='transparent')
        sub_frame4.pack(fill = 'x')
        
        transfer_type_label = ctk.CTkLabel(sub_frame4, text='Transfer Type (Select Only One): ')
        transfer_type_label.pack(side = 'left', pady = 10, padx = 10)
        transfer_1 = ctk.CTkCheckBox(sub_frame4, text='Donation')
        transfer_1.pack(side = 'left', pady = 5, padx = 10)
        
        transfer_2 = ctk.CTkCheckBox(sub_frame4, text='Relocate')
        transfer_2.pack(side = 'left', pady = 5, padx = 10)
        
        transfer_3 = ctk.CTkCheckBox(sub_frame4, text='Reassign')
        transfer_3.pack(side = 'left', pady = 5, padx = 10)
        
        transfer_4 = ctk.CTkCheckBox(sub_frame4, text='Others (Specify): ')
        transfer_4_2 = ctk.CTkEntry(sub_frame4)
        transfer_4.pack(side = 'left', pady = 5, padx = 10)
        transfer_4_2.pack(side = 'left', pady = 5, padx = 10)
        
        frame3 = ctk.CTkScrollableFrame(self)
        frame3.pack(fill = 'both', pady = 5, padx = 15)
        
        frame4 = ctk.CTkFrame(self)
        frame4.pack(fill = 'both', pady = 5, padx = (15, 0), side = 'left')
        
        sub_frame5 = ctk.CTkFrame(frame4, fg_color='transparent')
        sub_frame5.pack(fill = 'x')
        reason_label = ctk.CTkLabel(sub_frame5, text = 'Reasons for Transfer: ')
        reason_label.pack(side = 'left', pady = 5, padx = 10)
        
        reasons = ctk.CTkTextbox(frame4, width= 200)
        reasons.pack(fill = 'both', pady = 2, padx = 5)
        
        frame5 = ctk.CTkFrame(self)
        frame5.pack(fill = 'both', pady = 5, padx = 15, side = 'left')
        
        #approved by
        sub_frame6 = ctk.CTkFrame(frame5, fg_color='transparent')
        sub_frame6.pack(fill = 'x')
        
        approved_by_label = ctk.CTkLabel(sub_frame6, text = 'Approved by: ')
        approved_by_label.pack(side = 'left', pady = 3, padx = 10)
        
        name_label = ctk.CTkLabel(sub_frame6, text = 'Printed Name: ')
        name_label.pack(side = 'left', pady = 3, padx = 10)
        approve_name = ctk.CTkEntry(sub_frame6)
        approve_name.pack(side = 'left', pady = 3, padx = 10)
        
        designation_label = ctk.CTkLabel(sub_frame6, text = 'Designation: ')
        designation_label.pack(side = 'left', pady = 3, padx = 10)
        approve_designation = ctk.CTkEntry(sub_frame6)
        approve_designation.pack(side = 'left', pady = 3, padx = 10)
        
        sub_frame6_2 = ctk.CTkFrame(frame5, fg_color='transparent')
        sub_frame6_2.pack(fill = 'x')
        
        approve_date_label = ctk.CTkLabel(sub_frame6_2, text = 'Date: ')
        approve_date_label.pack(side = 'left', pady = 3, padx = (105, 0))
        approve_date = DateEntry(sub_frame6_2, font= ctk.CTkFont('Arial', size = 12) )
        approve_date.pack(side = 'left', pady = 3, padx = 10)
        
        
        #Released/issued by
        sub_frame7 = ctk.CTkFrame(frame5, fg_color='transparent')
        sub_frame7.pack(fill = 'x')
        
        released_by_label = ctk.CTkLabel(sub_frame7, text = 'Released/Issued by: ')
        released_by_label.pack(side = 'left', pady = 3, padx = 10)
        
        name_label = ctk.CTkLabel(sub_frame7, text = 'Printed Name: ')
        name_label.pack(side = 'left', pady = 3, padx = 10)
        release_name = ctk.CTkEntry(sub_frame7)
        release_name.pack(side = 'left', pady = 3, padx = 10)
        
        designation_label = ctk.CTkLabel(sub_frame7, text = 'Designation: ')
        designation_label.pack(side = 'left', pady = 3, padx = 10)
        release_designation = ctk.CTkEntry(sub_frame7)
        release_designation.pack(side = 'left', pady = 3, padx = 10)
        
        sub_frame7_2 = ctk.CTkFrame(frame5, fg_color='transparent')
        sub_frame7_2.pack(fill = 'x')
        
        release_date_label = ctk.CTkLabel(sub_frame7_2, text = 'Date: ')
        release_date_label.pack(side = 'left', pady = 3, padx = (150, 0))
        release_date = DateEntry(sub_frame7_2, font= ctk.CTkFont('Arial', size = 12) )
        release_date.pack(side = 'left', pady = 3, padx = 10)
        
        #receive by
        sub_frame8 = ctk.CTkFrame(frame5, fg_color='transparent')
        sub_frame8.pack(fill = 'x')
        
        received_by_label = ctk.CTkLabel(sub_frame8, text = 'Received by: ')
        received_by_label.pack(side = 'left', pady = 5, padx = 10)
        
        name_label = ctk.CTkLabel(sub_frame8, text = 'Printed Name: ')
        name_label.pack(side = 'left', pady = 2, padx = 10)
        receive_name = ctk.CTkEntry(sub_frame8)
        receive_name.pack(side = 'left', pady = 2, padx = 10)
        
        designation_label = ctk.CTkLabel(sub_frame8, text = 'Designation: ')
        designation_label.pack(side = 'left', pady = 2, padx = 10)
        receive_designation = ctk.CTkEntry(sub_frame8)
        receive_designation.pack(side = 'left', pady = 2, padx = 10)
        
        sub_frame8_2 = ctk.CTkFrame(frame5, fg_color='transparent')
        sub_frame8_2.pack(fill = 'x')
        
        receive_date_label = ctk.CTkLabel(sub_frame8_2, text = 'Date: ')
        receive_date_label.pack(side = 'left', pady = 5, padx = (150, 0))
        receive_date = DateEntry(sub_frame8_2, font= ctk.CTkFont('Arial', size = 12) )
        receive_date.pack(side = 'left', pady = 2, padx = 10)
        
        gen_report = ctk.CTkButton(self, text = 'Generate Report', font= ctk.CTkFont('Arial', size = 12, weight = "bold"), text_color='white', corner_radius = 30)
        gen_report.pack(side = 'right', pady = 0, padx = (0, 15), ipady = 5)
        