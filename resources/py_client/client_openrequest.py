import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from tkcalendar import *
from tkinter import messagebox
import pyrebase
from openpyxl import load_workbook
import datetime


ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
current_datetime = datetime.datetime.now()
current_day = current_datetime.strftime("%Y-%m-%d")
current_time = current_datetime.strftime("%H:%M:%S")

def showptr_window(getptr):
    
    global suggestions_frame
    suggestions_frame = None
    suggestions_frame = None
    report_form = ctk.CTkToplevel()
    report_form.title("Property Transfer | Document Info")
    report_form.geometry("{0}x{1}+200+100".format(1000,500))
    report_form.resizable(False, False)
    report_form.configure(fg_color = 'white')

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
    
    wb = load_workbook("./resources/user/data/UserLog.xlsx", data_only=True)
    sh = wb["User email"]
    email = sh["A1"].value
    print(email)

    #<-------------------------ITEM SUGGESTION------------------------------------>
       
        
        
            
    
    main = ctk.CTkFrame(report_form)
    main.pack(fill = 'both')
    #header frame
    header_frame = ctk.CTkFrame(main, fg_color='#313131', height=50, width=report_form.winfo_width(), corner_radius=0)
    header_frame.pack(fill = 'both', side='top')

    #app logo
    app_logo = ctk.CTkImage(Image.open('resources\images\DEFAULT\PTRLogo_White.png'), size=(25, 25))
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
    info_frame = ctk.CTkFrame(tab1, fg_color='white')
    info_frame.pack(fill = 'x', pady = 5, padx = 5)
    
    sub_info_frame = ctk.CTkFrame(info_frame, height=50 , corner_radius=20, fg_color='#F4F4F4')
    sub_info_frame.pack(fill = 'x', pady = 5, padx = 5)
    
    generated_db = db.child("generated_files").order_by_child("PTR").equal_to(getptr).get()
    for dt in generated_db.each():
        db_ptr = dt.val()['PTR']
        db_email = dt.val()['EMAIL']
        db_fc = dt.val()['FC']
        db_type = dt.val()['TRANSFER']
        db_created = dt.val()['CREATED']
        db_remarks = dt.val()['REMARKS']
        db_from = dt.val()['FROM'].title()
        db_to = dt.val()['TO'].title()
        db_dt = dt.val()['DT']
        reason = dt.val()['REASON1']+dt.val()['REASON2']+dt.val()['REASON3']
        db_riname = dt.val()['RINAME'].title()
        db_ridt = dt.val()['RIDT']
        db_rides = dt.val()['RIDES']
        db_rname = dt.val()['RNAME'].title()
        db_rdt = dt.val()['RDT']
        db_rdes = dt.val()['RDES']
        db_name = dt.val()['NAME'].title()
        db_adt = dt.val()['ADT']
        db_des = dt.val()['DES']
        items = [
        (dt.val()['DA1'], dt.val()['PN1'], dt.val()['N1'], dt.val()['DESC1'], dt.val()['AM1'], dt.val()['CON1'], dt.val()['LOC1']),
        (dt.val()['DA2'], dt.val()['PN2'], dt.val()['N2'], dt.val()['DESC2'], dt.val()['AM2'], dt.val()['CON2'], dt.val()['LOC2']),
        (dt.val()['DA3'], dt.val()['PN3'], dt.val()['N3'], dt.val()['DESC3'], dt.val()['AM3'], dt.val()['CON3'], dt.val()['LOC3']),
        (dt.val()['DA4'], dt.val()['PN4'], dt.val()['N4'], dt.val()['DESC4'], dt.val()['AM4'], dt.val()['CON4'], dt.val()['LOC4']),
        (dt.val()['DA5'], dt.val()['PN5'], dt.val()['N5'], dt.val()['DESC5'], dt.val()['AM5'], dt.val()['CON5'], dt.val()['LOC5']),
        (dt.val()['DA6'], dt.val()['PN6'], dt.val()['N6'], dt.val()['DESC6'], dt.val()['AM6'], dt.val()['CON6'], dt.val()['LOC6']),
        (dt.val()['DA7'], dt.val()['PN7'], dt.val()['N7'], dt.val()['DESC7'], dt.val()['AM7'], dt.val()['CON7'], dt.val()['LOC7']),
        (dt.val()['DA8'], dt.val()['PN8'], dt.val()['N8'], dt.val()['DESC8'], dt.val()['AM8'], dt.val()['CON8'], dt.val()['LOC8']),
        (dt.val()['DA9'], dt.val()['PN9'], dt.val()['N9'], dt.val()['DESC9'], dt.val()['AM9'], dt.val()['CON9'], dt.val()['LOC9']),
        (dt.val()['DA10'], dt.val()['PN10'], dt.val()['N10'], dt.val()['DESC10'], dt.val()['AM10'], dt.val()['CON10'], dt.val()['LOC10']),
        (dt.val()['DA11'], dt.val()['PN11'], dt.val()['N11'], dt.val()['DESC11'], dt.val()['AM11'], dt.val()['CON11'], dt.val()['LOC11']),
        (dt.val()['DA12'], dt.val()['PN12'], dt.val()['N12'], dt.val()['DESC12'], dt.val()['AM12'], dt.val()['CON12'], dt.val()['LOC12']),
        (dt.val()['DA13'], dt.val()['PN13'], dt.val()['N13'], dt.val()['DESC13'], dt.val()['AM13'], dt.val()['CON13'], dt.val()['LOC13']),
        (dt.val()['DA14'], dt.val()['PN14'], dt.val()['N14'], dt.val()['DESC14'], dt.val()['AM14'], dt.val()['CON14'], dt.val()['LOC14']),
        (dt.val()['DA15'], dt.val()['PN15'], dt.val()['N15'], dt.val()['DESC15'], dt.val()['AM15'], dt.val()['CON15'], dt.val()['LOC15']),
        (dt.val()['DA16'], dt.val()['PN16'], dt.val()['N16'], dt.val()['DESC16'], dt.val()['AM16'], dt.val()['CON16'], dt.val()['LOC16']),
        (dt.val()['DA17'], dt.val()['PN17'], dt.val()['N17'], dt.val()['DESC17'], dt.val()['AM17'], dt.val()['CON17'], dt.val()['LOC17'])
        
        ]
        
    user_db = db.child("user_accounts").order_by_child("EMAIL").equal_to(db_email).get()
    for dt in user_db.each():
        db_id = dt.val()['ID']
        db_fn = dt.val()['FN'].title()
        db_ln = dt.val()['LN'].title()    
        
    label_type = ctk.CTkLabel(sub_info_frame, text=db_type, text_color='black', font=('Arial', 22, 'bold'))
    label_type.pack(side='left',padx=(10, 5), pady=(3,3),ipadx=0, ipady=0, anchor='w')    
    label_key = ctk.CTkLabel(sub_info_frame, text=" | PTR No: "+db_ptr+" | Received by: "+db_riname, text_color='black', font=('Arial', 22))
    label_key.pack(side='left', padx=(3,0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
    
    sub_info2_frame = ctk.CTkFrame(info_frame, height=50 , corner_radius=20, fg_color='#F4F4F4')
    sub_info2_frame.pack(fill = 'x', pady = 5, padx = 5)
    label_name = ctk.CTkLabel(sub_info2_frame, text="Requested by: "+db_ln+", "+db_fn+" (YOU) ● STATUS: "+db_remarks, text_color='black', font=('Arial', 13))
    label_name.pack(side='left',padx=(10, 0), pady=(0,0),ipadx=0, ipady=0, anchor='w')
    
    frame = ctk.CTkFrame(tab1, height=400, corner_radius=20, fg_color='#F4F4F4')
    frame.pack(fill = 'both', pady = 5, padx = 10)
    
    sub_frame = ctk.CTkFrame(frame, fg_color='transparent')
    sub_frame.pack(fill = 'x', pady = 5, padx = 5)
    
    entity_label = ctk.CTkLabel(sub_frame, text='Entity Name: ')
    entity_label.pack(side = 'left', pady = 5, padx = 10)
    
    entities = ["Polytechnic University of the Philippines - Lopez Branch"]
    entity_name = ctk.CTkOptionMenu(sub_frame, width=300, values=entities, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 12), dropdown_font=ctk.CTkFont('Arial', size = 12))
    entity_name.pack(side = 'left', pady = 5, padx = 10)
    
    fund_cluster_label = ctk.CTkLabel(sub_frame, text='Fund Cluster: ')
    fund_cluster_label.pack(side = 'left', pady = 5, padx = (170,0))
    fund_cluster= ctk.CTkEntry(sub_frame, fg_color='white', state="readonly")
    fund_cluster.pack(side = 'left', pady = 5, padx = 10)
    fund_cluster.configure(state="normal")  # Set the entry to normal state
    fund_cluster.delete(0, ctk.END)  # Clear the existing value
    fund_cluster.insert(0, db_fc)  # Set the new value
    fund_cluster.configure(state="readonly")  # Set the entry back to readonly state
    
    sub_frame2 = ctk.CTkFrame(frame, fg_color='transparent')
    sub_frame2.pack(fill = 'x', pady = 5, padx = 10)
    
    from_label = ctk.CTkLabel(sub_frame2, text='From Accountable Officer/Agency Cluster Fund: ')
    from_label.pack(side = 'left', pady = 5, padx = 10)
    from_ao_afc = ctk.CTkEntry(sub_frame2, width = 300, fg_color='white', state="readonly")
    from_ao_afc.pack(side = 'left', pady = 5, padx = 10)
    from_ao_afc.configure(state="normal")  # Set the entry to normal state
    from_ao_afc.delete(0, ctk.END)  # Clear the existing value
    from_ao_afc.insert(0, db_from)  # Set the new value
    from_ao_afc.configure(state="readonly")  # Set the entry back to readonly state
    
    ptr_label = ctk.CTkLabel(sub_frame2, text='PTR No.: ')
    ptr_label.pack(side = 'left', pady = 5, padx = 10)
    
    ptr_no = ctk.CTkEntry(sub_frame2, fg_color='white' , width = 155, state="readonly")
    ptr_no.pack(side = 'left', pady = 5, padx = 10)
    ptr_no.configure(state="normal")  # Set the entry to normal state
    ptr_no.delete(0, ctk.END)  # Clear the existing value
    ptr_no.insert(0, db_ptr)  # Set the new value
    ptr_no.configure(state="readonly")  # Set the entry back to readonly state
    
    sub_frame3 = ctk.CTkFrame(frame, fg_color='transparent')
    sub_frame3.pack(fill = 'x', pady = 5, padx = 10)
    
    to_label = ctk.CTkLabel(sub_frame3, text='To Accountable Officer/Agency Cluster Fund: ')
    to_label.pack(side = 'left', pady = 5, padx = 10)
    to_ao_afc = ctk.CTkEntry(sub_frame3, width = 300, fg_color='white',state="readonly")
    to_ao_afc.pack(side = 'left', pady = 5, padx = 10)
    to_ao_afc.configure(state="normal")  # Set the entry to normal state
    to_ao_afc.delete(0, ctk.END)  # Clear the existing value
    to_ao_afc.insert(0, db_to)  # Set the new value
    to_ao_afc.configure(state="readonly")  # Set the entry back to readonly state
    
    date_label = ctk.CTkLabel(sub_frame3, text='Date: ')
    date_label.pack(side = 'left', pady = 5, padx = 24)
    date = ctk.CTkEntry(sub_frame3, width = 150, fg_color='white',state="readonly")
    date.pack(side = 'left', pady = 5, padx = 10, ipady =2, ipadx = 2)
    date.pack(side = 'left', pady = 5, padx = 10)
    date.configure(state="normal")  # Set the entry to normal state
    date.delete(0, ctk.END)  # Clear the existing value
    date.insert(0, db_dt)  # Set the new value
    date.configure(state="readonly")  # Set the entry back to readonly state
    #transfer types
    frame2 = ctk.CTkFrame(tab1, corner_radius=20, fg_color='#F4F4F4')
    frame2.pack(fill = 'both', pady = 5, padx = 10)
    
    sub_frame4 = ctk.CTkFrame(frame2, fg_color='transparent')
    sub_frame4.pack(fill = 'x')
    
    transfer_type_label = ctk.CTkLabel(sub_frame4, text='Transfer Type (Select Only One): ')
    transfer_type_label.pack(side = 'left', pady = 10, padx = 10)
    
    
    transfer_var1 = ctk.StringVar()
    transfer_var2 = ctk.StringVar()
    transfer_var3 = ctk.StringVar()
    transfer_var4 = ctk.StringVar()
    transfer_var1.set("on")
    
    if db_type == 'Donation':
        transfer_var1.set("on")
        transfer_var2.set("off")
        transfer_var3.set("off")
        transfer_var4.set("off") 
        
        transfer_1 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Donation', variable=transfer_var1, onvalue="on", offvalue="off")
        transfer_1.pack(side='left', pady=5, padx=10)

        transfer_2 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Relocate', variable=transfer_var2, onvalue="on", offvalue="off")
        transfer_2.pack(side='left', pady=5, padx=10)

        transfer_3 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Reassign', variable=transfer_var3, onvalue="on", offvalue="off")
        transfer_3.pack(side='left', pady=5, padx=10)

        transfer_4 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Others (Specify): ',  variable=transfer_var4, onvalue="on", offvalue='off')
        transfer_4.pack(side='left', pady=5, padx=10)
        
    elif db_type == 'Relocate':
        transfer_var2.set("on")
        transfer_var1.set("off")
        transfer_var3.set("off")
        transfer_var4.set("off") 
         
        transfer_1 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Donation', variable=transfer_var1, onvalue="on", offvalue="off")
        transfer_1.pack(side='left', pady=5, padx=10)

        transfer_2 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Relocate', variable=transfer_var2, onvalue="on", offvalue="off")
        transfer_2.pack(side='left', pady=5, padx=10)

        transfer_3 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Reassign', variable=transfer_var3, onvalue="on", offvalue="off")
        transfer_3.pack(side='left', pady=5, padx=10)

        transfer_4 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Others (Specify): ',  variable=transfer_var4, onvalue="on", offvalue='off')
        transfer_4.pack(side='left', pady=5, padx=10)  
    elif db_type == 'Reassign':
        transfer_var3.set("on")
        transfer_var1.set("off")
        transfer_var2.set("off")
        transfer_var4.set("off")
        
        transfer_1 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Donation', variable=transfer_var1, onvalue="on", offvalue="off")
        transfer_1.pack(side='left', pady=5, padx=10)

        transfer_2 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Relocate', variable=transfer_var2, onvalue="on", offvalue="off")
        transfer_2.pack(side='left', pady=5, padx=10)

        transfer_3 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Reassign', variable=transfer_var3, onvalue="on", offvalue="off")
        transfer_3.pack(side='left', pady=5, padx=10)

        transfer_4 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Others (Specify): ',  variable=transfer_var4, onvalue="on", offvalue='off')
        transfer_4.pack(side='left', pady=5, padx=10)
    else:
        transfer_var4.set("on")
        transfer_var1.set("off")
        transfer_var2.set("off")
        transfer_var3.set("off")
        
        transfer_1 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Donation', variable=transfer_var1, onvalue="on", offvalue="off")
        transfer_1.pack(side='left', pady=5, padx=10)

        transfer_2 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Relocate', variable=transfer_var2, onvalue="on", offvalue="off")
        transfer_2.pack(side='left', pady=5, padx=10)

        transfer_3 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Reassign', variable=transfer_var3, onvalue="on", offvalue="off")
        transfer_3.pack(side='left', pady=5, padx=10)

        transfer_4 = ctk.CTkCheckBox(sub_frame4, state="disabled", text='Others (Specify): ',  variable=transfer_var4, onvalue="on", offvalue='off')
        transfer_4.pack(side='left', pady=5, padx=10)

        transfer_4_entry = ctk.CTkEntry(sub_frame4, fg_color='white',state="readonly")
        transfer_4_entry.pack(side='left', pady=5, padx=10)
        transfer_4_entry.configure(state="normal")  # Enable text editing initially
        transfer_4_entry.delete(0, ctk.END)  # Clear the existing value
        transfer_4_entry.insert(0, db_type)  # Set the new value
        transfer_4_entry.configure(state="readonly")  # Set the entry back to readonly state
        
        

    
    
    #second tab
    #items
    frame3 = ctk.CTkFrame(tab2,  fg_color='#F4F4F4')
    frame3.pack(fill = 'both', pady = 5, padx = 10)
    
    sub_frame4_3 = ctk.CTkFrame(frame3, fg_color='#F4F4F4')
    sub_frame4_3.pack(fill = 'x')
    
    
    
    item_label = ctk.CTkLabel(sub_frame4_3, text='Items')
    item_label.pack(side = 'left', pady = 5, padx = 10)

    
    
    
    
    #item table
    sub_frame4_5 = ctk.CTkFrame(tab2, fg_color='#F4F4F4')
    sub_frame4_5.pack(fill = 'x', pady = 5, padx = 10)
    
    columns = ('date_acquired', 'property_no', 'name',  'description', 'quantity', 'condition','location')
    
    item_table_report = ttk.Treeview(sub_frame4_5, columns=columns, show='headings', height=10)
    item_table_report.pack(fill=tk.BOTH)
    
    item_table_report.column('date_acquired', width = 100)
    item_table_report.column('property_no', width = 100)
    item_table_report.column('name', width = 100)
    item_table_report.column('description', width = 100)
    item_table_report.column('quantity', width = 100)
    item_table_report.column('condition', width = 100)
    item_table_report.column('location', width = 100)
    
    item_table_report.heading('date_acquired', text='Date Acquired')
    item_table_report.heading('property_no', text='Property No.')
    item_table_report.heading('name', text='Name')
    item_table_report.heading('description', text='Description')
    item_table_report.heading('quantity', text='Quantity')
    item_table_report.heading('condition', text='Condition')
    item_table_report.heading('location', text='Location')
    # Get all item IDs
    item_ids = item_table_report.get_children()

    # Delete each item
    for item_id in item_ids:
        item_table_report.delete(item_id)
        
    for item in items:
        item_table_report.insert('', 'end', values=item)
    #reasons
    frame4 = ctk.CTkFrame(tab2)
    frame4.pack(fill = 'both', pady = 5, padx = 10)
    
    sub_frame5 = ctk.CTkFrame(frame4, fg_color='transparent')
    sub_frame5.pack(fill = 'x')
    reason_label = ctk.CTkLabel(sub_frame5, text = 'Reasons for Transfer: ')
    reason_label.pack(side = 'left', pady = 5, padx = 10)
    
    
        
    entry = ctk.CTkTextbox(frame4, height=90, fg_color='white', wrap="word", state="disabled")
    entry.pack(fill='both', pady=10, padx=10)

    entry.configure(state="normal")  # Enable text editing initially
    entry.delete(1.0, ctk.END)  # Clear the existing value
    entry.insert(1.0, reason)  # Set the new value
    entry.configure(state="disabled")  # Set the entry back to readonly state

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
    approve_name = ctk.CTkEntry(sub_frame6_2, width = 300, fg_color='white', state="readonly")
    approve_name.pack(side = 'left', pady = 3, padx = 10)
    approve_name.pack(fill="both", expand=True)
    approve_name.configure(state="normal")  # Set the entry to normal state
    approve_name.delete(0, ctk.END)  # Clear the existing value
    approve_name.insert(0, db_name)  # Set the new value
    approve_name.configure(state="readonly")  # Set the entry back to readonly state
    
    
    designation_label = ctk.CTkLabel(sub_frame6_2, text = 'Designation: ')
    designation_label.pack(side = 'left', pady = 3, padx = 10)
    approve_designation = ctk.CTkEntry(sub_frame6_2, width = 200, fg_color='white', state="readonly")
    approve_designation.pack(side = 'left', pady = 3, padx = 10)
    approve_designation.configure(state="normal")  # Set the entry to normal state
    approve_designation.delete(0, ctk.END)  # Clear the existing value
    approve_designation.insert(0, db_des)  # Set the new value
    approve_designation.configure(state="readonly")  # Set the entry back to readonly state
    
    
    approve_date_label = ctk.CTkLabel(sub_frame6_2, text = 'Date: ')
    approve_date_label.pack(side = 'left', pady = 3, padx = 10)
    approve_date = ctk.CTkEntry(sub_frame6_2, width = 150, fg_color='white',state="readonly")
    approve_date.pack(side = 'left', pady = 3, padx = 10)
    approve_date.configure(state="normal")  # Set the entry to normal state
    approve_date.delete(0, ctk.END)  # Clear the existing value
    approve_date.insert(0, db_adt)  # Set the new value
    approve_date.configure(state="readonly")  # Set the entry back to readonly state
    
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
    release_name = ctk.CTkEntry(sub_frame7_2, width = 300, fg_color='white', state="readonly")
    release_name.pack(side = 'left', pady = 3, padx = 10)
    release_name.configure(state="normal")  # Set the entry to normal state
    release_name.delete(0, ctk.END)  # Clear the existing value
    release_name.insert(0, db_rname)  # Set the new value
    release_name.configure(state="readonly")  # Set the entry back to readonly state
    
    
    designation_label = ctk.CTkLabel(sub_frame7_2, text = 'Designation: ')
    designation_label.pack(side = 'left', pady = 3, padx = 10)
    release_designation = ctk.CTkEntry(sub_frame7_2, width = 200, fg_color='white', state="readonly")
    release_designation.pack(side = 'left', pady = 3, padx = 10)
    release_designation.configure(state="normal")  # Set the entry to normal state
    release_designation.delete(0, ctk.END)  # Clear the existing value
    release_designation.insert(0, db_rdes)  # Set the new value
    release_designation.configure(state="readonly")  # Set the entry back to readonly state
    
    
    release_date_label = ctk.CTkLabel(sub_frame7_2, text = 'Date: ')
    release_date_label.pack(side = 'left', pady = 3, padx = 10)
    release_date = ctk.CTkEntry(sub_frame7_2,  width = 150, fg_color='white',state="readonly" )
    release_date.pack(side = 'left', pady = 3, padx = 10)
    release_date.configure(state="normal")  # Set the entry to normal state
    release_date.delete(0, ctk.END)  # Clear the existing value
    release_date.insert(0, db_rdt)  # Set the new value
    release_date.configure(state="readonly")  # Set the entry back to readonly state
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
    receive_name = ctk.CTkEntry(sub_frame8_2, width = 300, fg_color='white', state="readonly")
    receive_name.pack(side = 'left', pady = 2, padx = 10)
    receive_name.configure(state="normal")  # Set the entry to normal state
    receive_name.delete(0, ctk.END)  # Clear the existing value
    receive_name.insert(0, db_riname)  # Set the new value
    receive_name.configure(state="readonly")  # Set the entry back to readonly state
    
    designation_label = ctk.CTkLabel(sub_frame8_2, text = 'Designation: ')
    designation_label.pack(side = 'left', pady = 2, padx = 10)
    receive_designation = ctk.CTkEntry(sub_frame8_2, width= 200, fg_color='white', state="readonly")
    receive_designation.pack(side = 'left', pady = 2, padx = 10)
    receive_designation.configure(state="normal")  # Set the entry to normal state
    receive_designation.delete(0, ctk.END)  # Clear the existing value
    receive_designation.insert(0, db_rides)  # Set the new value
    receive_designation.configure(state="readonly")  # Set the entry back to readonly state
    
    
    receive_date_label = ctk.CTkLabel(sub_frame8_2, text = 'Date: ')
    receive_date_label.pack(side = 'left', pady = 5, padx = 10)
    receive_date = ctk.CTkEntry(sub_frame8_2,  width = 150, fg_color='white',state="readonly" )
    receive_date.pack(side = 'left', pady = 2, padx = 10)
    receive_date.configure(state="normal")  # Set the entry to normal state
    receive_date.delete(0, ctk.END)  # Clear the existing value
    receive_date.insert(0, db_ridt)  # Set the new value
    receive_date.configure(state="readonly")  # Set the entry back to readonly state
    
            
    def callback():
        from resources.py_client.client_requestlist import requestlist_window    
        try:
            report_form.withdraw()
            requestlist_window()
            
        except Exception as e:
            if messagebox.askok("ERROR", e ):
                print(e)
                

    report_form.protocol("WM_DELETE_WINDOW", callback)
    report_form.mainloop()

    
            
                
#showptr_window()
