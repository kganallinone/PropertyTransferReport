import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image
from tkcalendar import *
from ttkthemes import ThemedStyle

ctk.set_appearance_mode("system")  # Modes: system (default), light, dark

#history window
class history_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | History")
        self.geometry("{0}x{1}+200+50".format(1000, 550))
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

        label = ctk.CTkLabel(header_frame, text = 'History', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
        label.pack(side = 'right',  pady = 15, padx = 15)
        
        
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

        label = ctk.CTkLabel(header_frame, text = 'Users', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
        label.pack(side = 'right',  pady = 15, padx = 15)
        
        
class report_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | Report")
        self.geometry("{0}x{1}+170+5".format(1050, 690))
        self.resizable(False, False)
        self.configure(fg_color = 'white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

        
        s = ThemedStyle(self)
        s.theme_use('breeze')
        
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

        self_scroll_frame = ctk.CTkScrollableFrame(self, fg_color='white', height=560)
        self_scroll_frame.pack(fill = 'both')
        
        frame = ctk.CTkFrame(self_scroll_frame, height=400, corner_radius=20, fg_color='#F4F4F4')
        frame.pack(fill = 'both', pady = 5, padx = 15)
        
        sub_frame = ctk.CTkFrame(frame, fg_color='transparent')
        sub_frame.pack(fill = 'x')
        
        entity_label = ctk.CTkLabel(sub_frame, text='Entity Name: ')
        entity_label.pack(side = 'left', pady = 5, padx = 10)
        
        entities = ["Polytechnic University of the Philippines - Lopez Branch"]
        entity_name = ctk.CTkOptionMenu(sub_frame, width=300, values=entities, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 12), dropdown_font=ctk.CTkFont('Arial', size = 12))
        entity_name.pack(side = 'left', pady = 5, padx = 10)
        
        fund_cluster_label = ctk.CTkLabel(sub_frame, text='Fund Cluster: ')
        fund_cluster_label.pack(side = 'left', pady = 5, padx = (170,0))
        fund_cluster= ctk.CTkEntry(sub_frame, fg_color='white')
        fund_cluster.pack(side = 'left', pady = 5, padx = 10)
        
        sub_frame2 = ctk.CTkFrame(frame, fg_color='transparent')
        sub_frame2.pack(fill = 'x')
        
        from_label = ctk.CTkLabel(sub_frame2, text='From Accountable Officer/Agency Cluster Fund: ')
        from_label.pack(side = 'left', pady = 5, padx = 10)
        from_ao_afc = ctk.CTkEntry(sub_frame2, width = 300, fg_color='white')
        from_ao_afc.pack(side = 'left', pady = 5, padx = 10)
        
        ptr_label = ctk.CTkLabel(sub_frame2, text='PTR No.: ')
        ptr_label.pack(side = 'left', pady = 5, padx = 10)
        ptr_no = ctk.CTkEntry(sub_frame2, fg_color='white', width = 155)
        ptr_no.pack(side = 'left', pady = 5, padx = 10)
        
        sub_frame3 = ctk.CTkFrame(frame, fg_color='transparent')
        sub_frame3.pack(fill = 'x')
        
        to_label = ctk.CTkLabel(sub_frame3, text='To Accountable Officer/Agency Cluster Fund: ')
        to_label.pack(side = 'left', pady = 5, padx = 10)
        to_ao_afc = ctk.CTkEntry(sub_frame3, width = 300, fg_color='white')
        to_ao_afc.pack(side = 'left', pady = 5, padx = 10)
        
        date_label = ctk.CTkLabel(sub_frame3, text='Date: ')
        date_label.pack(side = 'left', pady = 5, padx = 24)
        date = DateEntry(sub_frame3, font= ctk.CTkFont('Arial', size = 15) )
        date.pack(side = 'left', pady = 5, padx = 10, ipady =2, ipadx = 2)
        
        #transfer types
        frame2 = ctk.CTkFrame(self_scroll_frame, corner_radius=20, fg_color='#F4F4F4')
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
        transfer_4_2 = ctk.CTkEntry(sub_frame4, fg_color='white')
        transfer_4.pack(side = 'left', pady = 5, padx = 10)
        transfer_4_2.pack(side = 'left', pady = 5, padx = 10)
        
        #items
        frame3 = ctk.CTkFrame(self_scroll_frame,  fg_color='#F4F4F4')
        frame3.pack(fill = 'both', pady = 5, padx = 15)
        
        sub_frame4_3 = ctk.CTkFrame(frame3, fg_color='#F4F4F4')
        sub_frame4_3.pack(fill = 'x')
        
        item_label = ctk.CTkLabel(sub_frame4_3, text='Items')
        item_label.pack(side = 'left', pady = 5, padx = 10)

        #search item by property number
        search_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-search-150.png'), size=(25, 25))
        search_button = ctk.CTkButton(sub_frame4_3, image=search_icon, text=None, width = 25, fg_color='transparent')
        search_button.pack(side = 'right', padx = (5, 10))
        property_no = ctk.CTkEntry(sub_frame4_3, placeholder_text='Property Number', width = 200, fg_color='white')
        property_no.pack(side = 'right')
        
        #result of search
        sub_frame4_4 = ctk.CTkFrame(frame3, fg_color='#F4F4F4')
        sub_frame4_4.pack(fill = 'x', pady = 20)
        
        result_label = ctk.CTkLabel(sub_frame4_4, text='Result: ')
        result_label.pack(side = 'left', pady = 5, padx = 10)
        result_property_no = ctk.CTkEntry(sub_frame4_4, placeholder_text='Property Number', width = 170, fg_color='white')
        result_property_no.pack(side = 'left', pady = 5, padx = 10)
        result_name = ctk.CTkEntry(sub_frame4_4, placeholder_text='Name', width = 170, fg_color='white')
        result_name.pack(side = 'left', pady = 5, padx = 10)
        result_desc = ctk.CTkEntry(sub_frame4_4, placeholder_text='Description', width = 170, fg_color='white')
        result_desc.pack(side = 'left', pady = 5, padx = 10)
        quantity = tk.Spinbox(sub_frame4_4, from_= 0, to= 1000, borderwidth=1, font= ctk.CTkFont('Arial', size = 16), bg='white')
        quantity.pack(side = 'left', pady = 5, padx= 10)
        add_button = ctk.CTkButton(sub_frame4_4, text='Add', width = 60, font=ctk.CTkFont('Arial', weight='bold'))
        add_button.pack(side = 'left', pady = 5, padx = 10)
        
        #item table
        
        sub_frame4_5 = ctk.CTkFrame(self_scroll_frame, fg_color='#F4F4F4')
        sub_frame4_5.pack(fill = 'x', pady = 5, padx = 15)
        
        columns = ('date_acquired', 'property_no', 'name',  'description', 'quantity', 'condition')
        
        item_table_report = ttk.Treeview(sub_frame4_5, columns=columns, show='headings', height=15)
        item_table_report.pack(fill=tk.BOTH)
        
        item_table_report.column('date_acquired', width = 100)
        item_table_report.column('property_no', width = 100)
        item_table_report.column('name', width = 100)
        item_table_report.column('description', width = 100)
        item_table_report.column('quantity', width = 100)
        item_table_report.column('condition', width = 100)
        
        item_table_report.heading('date_acquired', text='Date Acquired')
        item_table_report.heading('property_no', text='Property No.')
        item_table_report.heading('name', text='Name')
        item_table_report.heading('quantity', text='Quantity')
        item_table_report.heading('condition', text='Condition')
        
        #reasons
        frame4 = ctk.CTkFrame(self_scroll_frame)
        frame4.pack(fill = 'both', pady = 5, padx = 15)
        
        sub_frame5 = ctk.CTkFrame(frame4, fg_color='transparent')
        sub_frame5.pack(fill = 'x')
        reason_label = ctk.CTkLabel(sub_frame5, text = 'Reasons for Transfer: ')
        reason_label.pack(side = 'left', pady = 5, padx = 10)
        
        reasons = ctk.CTkTextbox(frame4, height=100, fg_color='white')
        reasons.pack(fill = 'both', pady = 10, padx = 10)
        
        #approved by
        frame5 = ctk.CTkFrame(self_scroll_frame, fg_color='#F4F4F4')
        frame5.pack(fill = 'both', pady = 5, padx = 15)
       
        sub_frame6 = ctk.CTkFrame(frame5, fg_color='transparent')
        sub_frame6.pack(fill = 'x')
        
        approved_by_label = ctk.CTkLabel(sub_frame6, text = 'Approved by: ')
        approved_by_label.pack(side = 'left', pady = 3, padx = 10)
        
        sub_frame6_2 = ctk.CTkFrame(frame5, fg_color='transparent')
        sub_frame6_2.pack(fill = 'x')
        
        name_label = ctk.CTkLabel(sub_frame6_2, text = 'Printed Name: ')
        name_label.pack(side = 'left', pady = 3, padx = 10)
        approve_name = ctk.CTkEntry(sub_frame6_2, width = 300, fg_color='white')
        approve_name.pack(side = 'left', pady = 3, padx = 10)
        
        designation_label = ctk.CTkLabel(sub_frame6_2, text = 'Designation: ')
        designation_label.pack(side = 'left', pady = 3, padx = 10)
        approve_designation = ctk.CTkEntry(sub_frame6_2, width = 200, fg_color='white')
        approve_designation.pack(side = 'left', pady = 3, padx = 10)
        
        approve_date_label = ctk.CTkLabel(sub_frame6_2, text = 'Date: ')
        approve_date_label.pack(side = 'left', pady = 3, padx = 10)
        approve_date = DateEntry(sub_frame6_2, font= ctk.CTkFont('Arial', size = 12) )
        approve_date.pack(side = 'left', pady = 3, padx = 10)
        
        #Released/issued by
        frame6 = ctk.CTkFrame(self_scroll_frame, fg_color='#F4F4F4')
        frame6.pack(fill = 'both', pady = 5, padx = 15) 
        
        sub_frame7 = ctk.CTkFrame(frame6, fg_color='transparent')
        sub_frame7.pack(fill = 'x')
        
        released_by_label = ctk.CTkLabel(sub_frame7, text = 'Released/Issued by: ')
        released_by_label.pack(side = 'left', pady = 3, padx = 10)
        
        sub_frame7_2 = ctk.CTkFrame(frame6, fg_color='transparent')
        sub_frame7_2.pack(fill = 'x')
        
        name_label = ctk.CTkLabel(sub_frame7_2, text = 'Printed Name: ')
        name_label.pack(side = 'left', pady = 3, padx = 10)
        release_name = ctk.CTkEntry(sub_frame7_2, width = 300, fg_color='white')
        release_name.pack(side = 'left', pady = 3, padx = 10)
        
        designation_label = ctk.CTkLabel(sub_frame7_2, text = 'Designation: ')
        designation_label.pack(side = 'left', pady = 3, padx = 10)
        release_designation = ctk.CTkEntry(sub_frame7_2, width = 200, fg_color='white')
        release_designation.pack(side = 'left', pady = 3, padx = 10)
        
        release_date_label = ctk.CTkLabel(sub_frame7_2, text = 'Date: ')
        release_date_label.pack(side = 'left', pady = 3, padx = 10)
        release_date = DateEntry(sub_frame7_2, font= ctk.CTkFont('Arial', size = 12) )
        release_date.pack(side = 'left', pady = 3, padx = 10)
        
        #receive by
        frame7 = ctk.CTkFrame(self_scroll_frame, fg_color='#F4F4F4')
        frame7.pack(fill = 'both', pady = 5, padx = 15) 
        
        sub_frame8 = ctk.CTkFrame(frame7, fg_color='transparent')
        sub_frame8.pack(fill = 'x')
        
        received_by_label = ctk.CTkLabel(sub_frame8, text = 'Received by: ')
        received_by_label.pack(side = 'left', pady = 5, padx = 10)
        
        sub_frame8_2 = ctk.CTkFrame(frame7, fg_color='transparent')
        sub_frame8_2.pack(fill = 'x')
        
        name_label = ctk.CTkLabel(sub_frame8_2, text = 'Printed Name: ')
        name_label.pack(side = 'left', pady = 2, padx = 10)
        receive_name = ctk.CTkEntry(sub_frame8_2, width = 300, fg_color='white')
        receive_name.pack(side = 'left', pady = 2, padx = 10)
        
        designation_label = ctk.CTkLabel(sub_frame8_2, text = 'Designation: ')
        designation_label.pack(side = 'left', pady = 2, padx = 10)
        receive_designation = ctk.CTkEntry(sub_frame8_2, width= 200, fg_color='white')
        receive_designation.pack(side = 'left', pady = 2, padx = 10)
        
        receive_date_label = ctk.CTkLabel(sub_frame8_2, text = 'Date: ')
        receive_date_label.pack(side = 'left', pady = 5, padx = 10)
        receive_date = DateEntry(sub_frame8_2, font= ctk.CTkFont('Arial', size = 12) )
        receive_date.pack(side = 'left', pady = 2, padx = 10)
        
        gen_report = ctk.CTkButton(self, text = 'Generate Report', font= ctk.CTkFont('Arial', size = 17, weight = "bold"), text_color='white', corner_radius = 30)
        gen_report.pack(side = 'right', pady = 0, padx = (0, 15), ipady = 3)
        
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
        
        label = ctk.CTkLabel(header_frame, text = 'Requests', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
        label.pack(side = 'right',  pady = 15, padx = 15)
        
        frame = ctk.CTkFrame(self)
        frame.pack(fill = 'both', side = 'left', padx = 15, pady = 15)
        
#items window
class items_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | Items")
        self.geometry("{0}x{1}+200+50".format(1000, 600))
        self.resizable(False, False)
        self.configure(fg_color = 'white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

        s = ThemedStyle(self)
        s.theme_use('breeze')
        
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

        label = ctk.CTkLabel(header_frame, text = 'Items', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
        label.pack(side = 'right',  pady = 15, padx = 15)
        
        #for table
        frame = ctk.CTkFrame(self, width = 700)
        frame.pack(fill = 'both', side = 'left', padx = 15, pady = 15)
        
        columns = ('property_no', 'name', 'description', 'current_loc')
        
        item_table = ttk.Treeview(frame, columns=columns, show='headings', height=24)
        item_table.pack(fill=tk.BOTH)
        
        item_table.column('property_no', width=175)
        item_table.column('name', width=175)
        item_table.column('description', width=175)
        item_table.column('current_loc', width=175)
        
        item_table.heading('property_no', text='Property No.')
        item_table.heading('name', text='Name')
        item_table.heading('description', text='Description')
        item_table.heading('current_loc', text='Current Location')
        
        #for input
        frame2 = ctk.CTkFrame(self, width = 300, fg_color='#f5f7f7', corner_radius=20)
        frame2.pack(fill = 'both', side = 'left', padx = (0,15), pady = 15)
        
        #item no.
        item_no_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
        item_no_label_frame.pack(fill = 'x', pady = (20, 0))
        item_no_label = ctk.CTkLabel(item_no_label_frame, text = 'Property No.', font= ctk.CTkFont('Arial', size = 18))
        item_no_label.pack(side = 'left', pady = (10,0), padx = 10)
        
        item_no = ctk.CTkEntry(frame2, width=250, font= ctk.CTkFont('Arial', size = 15), fg_color='white')
        item_no.pack(pady = (0, 10), padx = 10)
        
        #item name
        item_name_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
        item_name_label_frame.pack(fill = 'x')
        item_name_label = ctk.CTkLabel(item_name_label_frame, text = 'Name', font= ctk.CTkFont('Arial', size = 18))
        item_name_label.pack(side = 'left', pady = (10,0), padx = 10)
        
        item_name = ctk.CTkEntry(frame2, width=250, font= ctk.CTkFont('Arial', size = 15), fg_color='white')
        item_name.pack(pady = (0, 10), padx = 10)
        
        #item description
        item_description_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
        item_description_label_frame.pack(fill = 'x')
        item_description_label = ctk.CTkLabel(item_description_label_frame, text = 'Description', font= ctk.CTkFont('Arial', size = 18))
        item_description_label.pack(side = 'left', pady = (10,0), padx = 10)
        
        item_description = ctk.CTkEntry(frame2, width=250, font= ctk.CTkFont('Arial', size = 15), fg_color='white')
        item_description.pack(pady = (0, 10), padx = 10)
        
        #item location
        item_loc_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
        item_loc_label_frame.pack(fill = 'x')
        item_loc_label = ctk.CTkLabel(item_loc_label_frame, text = 'Current Location', font= ctk.CTkFont('Arial', size = 18))
        item_loc_label.pack(side = 'left', pady = (10,0), padx = 10)
        
        loc_options_buildings = ["Computer Laboratory", "Administration Building", "Yumul Building"]
        item_loc_buildings = ctk.CTkOptionMenu(frame2, width=250, values=loc_options_buildings, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 15), dropdown_font=ctk.CTkFont('Arial', size = 15))
        item_loc_buildings.pack(pady = (0, 10), padx = 10)
        loc_options_room = ["CL 1", "CL 2", "CL 3"]
        item_loc_room = ctk.CTkOptionMenu(frame2, width=250, values=loc_options_room, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 15), dropdown_font=ctk.CTkFont('Arial', size = 15))
        item_loc_room.pack(pady = (0, 10), padx = 10)
        
        #item quantity
        item_quantity_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
        item_quantity_label_frame.pack(fill = 'x')
        item_quantity_label = ctk.CTkLabel(item_quantity_label_frame, text = 'Quantity', font= ctk.CTkFont('Arial', size = 18))
        item_quantity_label.pack(side = 'left', pady = (10,0), padx = 10)
        
        item_quantity = tk.Spinbox(frame2, from_= 0, to= 1000, borderwidth=2, width=250, font= ctk.CTkFont('Arial', size = 16), bg='white')
        item_quantity.pack(pady = (0, 10), padx = 10)
        
        #add button
        add_button = ctk.CTkButton(frame2, text = 'Add', font= ctk.CTkFont('Arial', size = 18, weight = "bold"), text_color='white', corner_radius = 30)
        add_button.pack(pady = 20, ipady = 5)
        
        
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
        request_button = ctk.CTkButton(nav_container, command = self.open_request_toplevel, fg_color='transparent', image= request_icon, text='Requests', width= 30, text_color='black', compound="top")
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

