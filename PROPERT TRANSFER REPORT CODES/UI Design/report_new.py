import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from tkcalendar import *

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

def new_report_window():
    report_form = ctk.CTk()
    report_form.title("Property Transfer | Report")
    report_form.geometry("{0}x{1}+200+25".format(1000,650))
    report_form.resizable(False, False)
    report_form.configure(fg_color = 'white')
    report_form.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

    main = ctk.CTkFrame(report_form)
    main.pack(fill = 'both')
    #header frame
    header_frame = ctk.CTkFrame(main, fg_color='#313131', height=50, width=report_form.winfo_width(), corner_radius=0)
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
    label.pack(side = 'right',  pady = 10, padx = 10)
        
    #notebook
    notebook = ttk.Notebook(main)
    notebook.pack(expand=True)
    
    # create frames
    tab1 = ctk.CTkFrame(notebook, width=1000, height=500, fg_color='white')
    tab2 = ctk.CTkFrame(notebook, width=1000, height=500, fg_color='white')
    tab3 = ctk.CTkFrame(notebook, width=1000, height=500, fg_color='white')

    tab1.pack(fill='both', expand=True)
    tab2.pack(fill='both', expand=True)
    tab3.pack(fill ='both', expand =True)

    # add frames to notebook
    notebook.add(tab1, text='PTR Information')
    notebook.add(tab2, text='Items')
    notebook.add(tab3, text='Approval')
    
    #first tab
    frame = ctk.CTkFrame(tab1, height=400, corner_radius=20, fg_color='#F4F4F4')
    frame.pack(fill = 'both', pady = 5, padx = 10)
    
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
    frame2 = ctk.CTkFrame(tab1, corner_radius=20, fg_color='#F4F4F4')
    frame2.pack(fill = 'both', pady = 5, padx = 10)
    
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
    
    #second tab
    #items
    frame3 = ctk.CTkFrame(tab2,  fg_color='#F4F4F4')
    frame3.pack(fill = 'both', pady = 5, padx = 10)
    
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
    add_button = ctk.CTkButton(sub_frame4_4, text='Add', width = 60, font=ctk.CTkFont('Arial', weight='bold'),fg_color='#0077B8', text_color='white')
    add_button.pack(side = 'left', pady = 5, padx = 10)
    
    #item table
    sub_frame4_5 = ctk.CTkFrame(tab2, fg_color='#F4F4F4')
    sub_frame4_5.pack(fill = 'x', pady = 5, padx = 10)
    
    columns = ('date_acquired', 'property_no', 'name',  'description', 'quantity', 'condition')
    
    item_table_report = ttk.Treeview(sub_frame4_5, columns=columns, show='headings', height=10)
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
    frame4 = ctk.CTkFrame(tab2)
    frame4.pack(fill = 'both', pady = 5, padx = 10)
    
    sub_frame5 = ctk.CTkFrame(frame4, fg_color='transparent')
    sub_frame5.pack(fill = 'x')
    reason_label = ctk.CTkLabel(sub_frame5, text = 'Reasons for Transfer: ')
    reason_label.pack(side = 'left', pady = 5, padx = 10)
    
    reasons = ctk.CTkTextbox(frame4, height=100, fg_color='white')
    reasons.pack(fill = 'both', pady = 10, padx = 10)
    
    #third tab
    #approved by
    frame5 = ctk.CTkFrame(tab3, fg_color='#F4F4F4')
    frame5.pack(fill = 'both', pady = 5, padx = 10)
    
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
    frame6 = ctk.CTkFrame(tab3, fg_color='#F4F4F4')
    frame6.pack(fill = 'both', pady = 5, padx = 10) 
    
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
    frame7 = ctk.CTkFrame(tab3, fg_color='#F4F4F4')
    frame7.pack(fill = 'both', pady = 5, padx = 10) 
    
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
    
    #generate report
    gen_report = ctk.CTkButton(main, text = 'Generate Report', font= ctk.CTkFont('Arial', size = 15, weight = "bold"),fg_color='#0077B8', text_color='white', corner_radius = 30)
    gen_report.pack(side = 'right', pady = 5, padx = (0, 20))
    
    report_form.mainloop()
    
new_report_window()
