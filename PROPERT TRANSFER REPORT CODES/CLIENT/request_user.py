import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from tkcalendar import *
import tkinter.font as tkFont
from ttkthemes import ThemedStyle
import pyrebase

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

def request_user_window():

    config = {
        "apiKey": "AIzaSyCyCtXg05ff-tocdUaxjBFfa550TLfKZQ4",
        "authDomain": "puplopez-ptp.firebaseapp.com",
        "databaseURL": "https://puplopez-ptp-default-rtdb.firebaseio.com",
        "projectId": "puplopez-ptp",
        "storageBucket": "puplopez-ptp.appspot.com",
        "messagingSenderId": "638312293451",
        "appId": "1:638312293451:web:79e9405d11db0496f599ce",
        "measurementId": "G-9Z3SPKFR9V"
    }
    
    firebase = pyrebase.initialize_app(config)
    
    db = firebase.database()

    email = "martinancaja@gmail.com"
    request_db = db.child("user_accounts").order_by_child("EMAIL").equal_to(email).get()
    for dt in request_db.each():
        userstype = dt.val()['TYPE']
        usersfn = dt.val()['FN']
        usermi = dt.val()['MI']
        userln = dt.val()['LN']
        usersemail = dt.val()['EMAIL']
        
    request_user = ctk.CTk()
    request_user.title("Property Transfer | Request")
    request_user.geometry("{0}x{1}+200+50".format(1000, 550))
    request_user.resizable(False, False)
    request_user.configure(fg_color='white')
    request_user.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

    # main frame
    request_user.main_frame = ctk.CTkFrame(request_user)
    request_user.main_frame.pack(fill='both', expand=True)

    # header frame
    header_frame = ctk.CTkFrame(request_user.main_frame, fg_color='#313131', height=50, width=request_user.winfo_width(), corner_radius=0)
    header_frame.pack(fill='both', side='top')

    # app logo
    app_logo = ctk.CTkImage(Image.open('python property transfer\images\icons8-data-transfer-483-white.png'), size=(25, 25))
    app_logo_label = ctk.CTkLabel(header_frame, image=app_logo, text=None)
    app_logo_label.pack(side='left', pady=10, padx=10)

    # app name
    app_name1 = ctk.CTkLabel(header_frame, text='PROPERTY', font=ctk.CTkFont('Arial', size=22, weight="bold"), text_color='white')
    app_name1.pack(side='left', pady=10, padx=10)
    app_name2 = ctk.CTkLabel(header_frame, text='TRANSFER', font=ctk.CTkFont('Arial', size=22, weight="bold"), text_color='#ee4444')
    app_name2.pack(side='left', pady=10)

    # label
    label = ctk.CTkLabel(header_frame, text='Requests', font=ctk.CTkFont('Arial', size=25, weight="bold"), text_color='white')
    label.pack(side='right', pady=15, padx=15)

    # First Frame
    request_user.frts_frame = ctk.CTkFrame(request_user.main_frame)
    request_user.frts_frame.pack(fill='both')
    
    #date label
    date = DateEntry(request_user.frts_frame, font= ctk.CTkFont('Arial', size = 14) )
    date.pack(side = 'right', pady = 5, padx = 10, ipady =2, ipadx = 2)
    date_label = ctk.CTkLabel(request_user.frts_frame, text='Date:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
    date_label.pack(side = 'right', pady = 5)
    
    # Second Frame
    request_user.scnd_frame = ctk.CTkFrame(request_user.main_frame)
    request_user.scnd_frame.pack(fill='both')
    
    #name label
    name_label = ctk.CTkLabel(request_user.scnd_frame, text='Name:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
    name_tbox = ctk.CTkLabel(request_user.scnd_frame, text=usersfn + " " + usermi + " " + userln, font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    name_label.pack(side = 'left', pady = 5, padx=10)
    name_tbox.place(y = 5, x = 78)
    
    #email label
    email_tbox = ctk.CTkLabel(request_user.scnd_frame, text=usersemail, font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    email_label = ctk.CTkLabel(request_user.scnd_frame, text='Email:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
    email_label.pack(side='right', pady=5, padx=380)
    email_tbox.place(y = 5, x=624)
    
    # Third Frame
    request_user.trhd_frame = ctk.CTkFrame(request_user.main_frame)
    request_user.trhd_frame.pack(fill='both')
    
    #user label
    user_label = ctk.CTkLabel(request_user.trhd_frame, text='User type:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
    user_tbox = ctk.CTkLabel(request_user.trhd_frame, text=userstype, font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    user_label.pack(side='left', pady=5, padx=10)
    user_tbox.place(y = 5, x = 78)
    
    #request label
    reqtype_label = ctk.CTkLabel(request_user.trhd_frame, text='Request type: (Check only one)', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
    reqtype_tbox = ctk.CTkLabel(request_user.trhd_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
    reqtype_label.pack(side='right', pady=5, padx=214)
    reqtype_tbox.place(y = 5, x=580)

    # Fourth Frame
    frth_frame = ctk.CTkFrame(request_user.main_frame)
    frth_frame.pack(fill='both')
    
    # Transfer type variable
    trans_type_var = ctk.StringVar()
    
    #from label
    from_label = ctk.CTkLabel(frth_frame, text='From:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
    from_label1 = ctk.CTkLabel(frth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
    from_label.pack(side='left', pady=5, padx=16)
    from_label1.place(y = 5, x=10)
    
    entities = ["ICT Lab 1", 
                "ICT Lab 2", 
                "ICT Lab 3",
                "Building A",
                "Building B",
                "Building C",
                "Building D",
                "Building E"
                ]
    from_tbox = ctk.CTkOptionMenu(
        frth_frame, 
        width=150, 
        values=entities, 
        fg_color= 'white', 
        text_color='black', 
        dropdown_fg_color='white', 
        font= ctk.CTkFont('Arial', size = 14), 
        dropdown_font=ctk.CTkFont('Arial', size = 14)
        )
    from_tbox.place(y = 5, x = 78)
    
    # Function to handle checkbox selection
    def handle_checkbox_selection(checkbox_value):
        if checkbox_value == 'Reassignment':
            donation_checkbox.deselect()
            relocate_checkbox.deselect()
            trans_type1.deselect()
            trans_type_entry.configure(state='disabled')
        elif checkbox_value == 'Donation':
            reassignment_checkbox.deselect()
            relocate_checkbox.deselect()
            trans_type1.deselect()
            trans_type_entry.configure(state='disabled')
        elif checkbox_value == 'Relocate':
            reassignment_checkbox.deselect()
            donation_checkbox.deselect()
            trans_type1.deselect()
            trans_type_entry.configure(state='disabled')
        else:
            reassignment_checkbox.deselect()
            relocate_checkbox.deselect()
            donation_checkbox.deselect()
            trans_type_entry.configure(state='normal')
    
    #transfer type label
    reassignment_checkbox = ctk.CTkCheckBox(
        frth_frame, 
        text='Reassignment', 
        variable=trans_type_var, 
        onvalue='Reassignment', 
        command=lambda: handle_checkbox_selection('Reassignment')
        )
    reassignment_checkbox.pack(side = 'right', pady = 5, padx = 180)
    
    donation_checkbox = ctk.CTkCheckBox(
        frth_frame, 
        text='Donation', 
        variable=trans_type_var, 
        onvalue='Donation', 
        command=lambda: handle_checkbox_selection('Donation'))
    donation_checkbox.place(y = 5, x=580)
    
    # Fifth Frame
    ffth_frame = ctk.CTkFrame(request_user.main_frame)
    ffth_frame.pack(fill='both')
    
    #to label
    to_label = ctk.CTkLabel(ffth_frame, text='To:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
    to_label1 = ctk.CTkLabel(ffth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
    to_label.pack(side='left', pady=5, padx=16)
    to_label1.place(y = 5, x=10)
    
    entities = ["ICT Lab 1", 
                "ICT Lab 2", 
                "ICT Lab 3",
                "Building A",
                "Building B",
                "Building C",
                "Building D",
                "Building E"
                ]
    from_tbox = ctk.CTkOptionMenu(ffth_frame, width=150, values=entities, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 14), dropdown_font=ctk.CTkFont('Arial', size = 14))
    from_tbox.place(y = 5, x = 78)
    
    relocate_checkbox = ctk.CTkCheckBox(
        ffth_frame, 
        text='Relocate', 
        variable=trans_type_var, 
        onvalue='Relocate', 
        command=lambda: handle_checkbox_selection('Relocate'))
    relocate_checkbox.place(y = 5, x=580)
    
    #transfer type label
    trans_type1 = ctk.CTkCheckBox(
        ffth_frame, 
        text='Others (Specify):', 
        variable=trans_type_var, 
        onvalue='Others', 
        command=lambda: handle_checkbox_selection('Others'))
    trans_type_entry = ctk.CTkEntry(ffth_frame, fg_color='white')
    trans_type1.pack(side = 'right', pady = 5, padx = 166)
    trans_type_entry.place(y = 5, x=840)
    trans_type_entry.configure(state='disabled')
    
    #Sixth Frame
    request_user.sxth_frame = ctk.CTkFrame(request_user.main_frame)
    request_user.sxth_frame.pack(fill='both')
    
    #Items selected label
    is_label = ctk.CTkLabel(request_user.sxth_frame, text='Items selected:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
    is_label1 = ctk.CTkLabel(request_user.sxth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
    is_label.pack(side='left', pady=5, padx=16)
    is_label1.place(y = 5, x=10)
    
    #Button
    select_items_button = ctk.CTkButton(
        request_user.sxth_frame,
        text="Select items",
        font=ctk.CTkFont('Arial', size=14, weight="normal"),
        fg_color='red',
        command=lambda: open_select_items_window(request_user),  # Add a command to the button
        corner_radius=10,  # Adjust the value for the desired roundness
        width=20,
        hover_color='dark red' # Change the background color on hover to dark red
    )
    select_items_button.place(y = 5, x=474)
    
    #Reason for transfer label
    retra_label = ctk.CTkLabel(request_user.sxth_frame, text='Reason for request:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
    retra_tbox = ctk.CTkLabel(request_user.sxth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
    retra_label.pack(side='right', pady=5, padx=288)
    retra_tbox.place(y = 5, x=580)   
    
    #Seventh Frame
    request_user.svnth_frame = ctk.CTkFrame(request_user.main_frame)
    request_user.svnth_frame.pack(fill='both')
    
    columns = ('items_list', 'quantity')
    
    item_table_report = ttk.Treeview(request_user.svnth_frame, columns=columns, show='headings', height=10)
    item_table_report.pack(side = 'left')
    item_table_report.place(y = 5, x=10)
    
    item_table_report.column('items_list', width = 460)
    item_table_report.column('quantity', width = 100)
    
    item_table_report.heading('items_list', text='Items List')
    item_table_report.heading('quantity', text='Quantity')
    
    #Text box
    textbox_entry = ctk.CTkTextbox(request_user.svnth_frame, font=ctk.CTkFont('Arial', size=14), width=410, height=200)
    textbox_entry.pack(side='right')
    textbox_entry.place(y = 5, x=580)
    
    #Eigth Frame
    request_user.egth_frame = ctk.CTkFrame(request_user.main_frame)
    request_user.egth_frame.pack(fill='both')
    
    #Button
    submit_request_button = ctk.CTkButton(
    request_user.egth_frame,
    text="Submit Request",
    font=ctk.CTkFont('Arial', size=14, weight="bold"),
    fg_color='green',
    corner_radius=10,  # Adjust the value for the desired roundness
    height=30,
    hover_color='dark green'  # Change the background color on hover to dark red
    )
    submit_request_button.pack(side= 'right')
    submit_request_button.pack(pady=6, padx=10)
    
    #Nineth Frame
    request_user.nnth_frame = ctk.CTkFrame(request_user.main_frame)
    request_user.nnth_frame.pack(fill='both')
    
    #footer frame
    footer_frame = ctk.CTkFrame(request_user.nnth_frame, fg_color='maroon', height=50, width=request_user.winfo_width(), corner_radius=0)
    footer_frame.pack(fill='both', side='bottom')
    
    request_user.mainloop()
    
def open_select_items_window(request_user):
    request_user = tk.Toplevel()
    request_user.title("Select Items")
    request_user.geometry("500x400")  
    request_user.geometry("{0}x{1}+300+150".format(800, 400))
    request_user.resizable(False, False)
    request_user.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')
    
    #main frame
    request_user.main_frame = ctk.CTkFrame(request_user)
    request_user.main_frame.pack(fill='both', expand=True)
    
    #First frame
    request_user.frt_frame = ctk.CTkFrame(request_user.main_frame)
    request_user.frt_frame.pack(fill='both')

    #header frame
    header_frame = ctk.CTkFrame(request_user.frt_frame, fg_color='maroon', height=30, width=request_user.winfo_width(), corner_radius=0)
    header_frame.pack(fill='both', side='top')
    
    avail_label = ctk.CTkLabel(header_frame, text='Available Items', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='white')
    avail_label.pack(side='top', pady=2)
    
    ##############################################
    
    request_user.self_scroll_frame = ctk.CTkScrollableFrame(request_user.main_frame, fg_color='white', height=300)
    request_user.self_scroll_frame.pack(fill='both')
    
    #Rectangle 1 ###################################
    request_user.rectangle_frame = ctk.CTkFrame(request_user.self_scroll_frame, fg_color='#DEDEDE', height=80, width=1834, border_width=2, border_color='maroon', corner_radius=0)
    request_user.rectangle_frame.pack(fill='both')
    
    checkbox_item = ctk.CTkCheckBox(request_user.rectangle_frame, text='\t AVR', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    checkbox_item.place(y=28, x=20)
    
    item_stocks = ctk.CTkLabel(request_user.rectangle_frame, text='Items: 50', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    item_stocks.place(y=28, x=360)
    
    item_qty = ctk.CTkLabel(request_user.rectangle_frame, text='Quantity:', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    item_qty.place(y=28, x=616)
    
    item_entry =  ctk.CTkEntry(request_user.rectangle_frame, width=80, fg_color='white')
    item_entry.place(y=28, x=680)
    
    #Rectangle 2 ###################################
    request_user.rectangle_frame = ctk.CTkFrame(request_user.self_scroll_frame, fg_color='#DEDEDE', height=80, width=1834, border_width=2, border_color='maroon', corner_radius=0)
    request_user.rectangle_frame.pack(fill='both', pady=2) 
    
    checkbox_item = ctk.CTkCheckBox(request_user.rectangle_frame, text='\t keyboard', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    checkbox_item.place(y=28, x=20)
    
    item_stocks = ctk.CTkLabel(request_user.rectangle_frame, text='Items: 20', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    item_stocks.place(y=28, x=360)
    
    item_qty = ctk.CTkLabel(request_user.rectangle_frame, text='Quantity:', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    item_qty.place(y=28, x=616)
    
    item_entry =  ctk.CTkEntry(request_user.rectangle_frame, width=80, fg_color='white')
    item_entry.place(y=28, x=680)
    
    #Rectangle 3 ###################################
    request_user.rectangle_frame = ctk.CTkFrame(request_user.self_scroll_frame, fg_color='#DEDEDE', height=80, width=1834, border_width=2, border_color='maroon', corner_radius=0)
    request_user.rectangle_frame.pack(fill='both', pady=2) 
    
    checkbox_item = ctk.CTkCheckBox(request_user.rectangle_frame, text='\t Mouse', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    checkbox_item.place(y=28, x=20)
    
    item_stocks = ctk.CTkLabel(request_user.rectangle_frame, text='Items: 20', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    item_stocks.place(y=28, x=360)
    
    item_qty = ctk.CTkLabel(request_user.rectangle_frame, text='Quantity:', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    item_qty.place(y=28, x=616)
    
    item_entry =  ctk.CTkEntry(request_user.rectangle_frame, width=80, fg_color='white')
    item_entry.place(y=28, x=680)
    
    #Rectangle 4 ###################################
    request_user.rectangle_frame = ctk.CTkFrame(request_user.self_scroll_frame, fg_color='#DEDEDE', height=80, width=1834, border_width=2, border_color='maroon', corner_radius=0)
    request_user.rectangle_frame.pack(fill='both', pady=2) 
    
    checkbox_item = ctk.CTkCheckBox(request_user.rectangle_frame, text='\t PC Set', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    checkbox_item.place(y=28, x=20)
    
    item_stocks = ctk.CTkLabel(request_user.rectangle_frame, text='Items: 30', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    item_stocks.place(y=28, x=360)
    
    item_qty = ctk.CTkLabel(request_user.rectangle_frame, text='Quantity:', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    item_qty.place(y=28, x=616)
    
    item_entry =  ctk.CTkEntry(request_user.rectangle_frame, width=80, fg_color='white')
    item_entry.place(y=28, x=680)
    
    #Rectangle 5 ###################################
    request_user.rectangle_frame = ctk.CTkFrame(request_user.self_scroll_frame, fg_color='#DEDEDE', height=80, width=1834, border_width=2, border_color='maroon', corner_radius=0)
    request_user.rectangle_frame.pack(fill='both', pady=2) 
    
    checkbox_item = ctk.CTkCheckBox(request_user.rectangle_frame, text='\t UPS', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    checkbox_item.place(y=28, x=20)
    
    item_stocks = ctk.CTkLabel(request_user.rectangle_frame, text='Items: 100', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    item_stocks.place(y=28, x=360)
    
    item_qty = ctk.CTkLabel(request_user.rectangle_frame, text='Quantity:', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
    item_qty.place(y=28, x=616)
    
    item_entry =  ctk.CTkEntry(request_user.rectangle_frame, width=80, fg_color='white')
    item_entry.place(y=28, x=680)
    
    #################################################

    #Third frame
    request_user.thrd_frame = ctk.CTkFrame(request_user.main_frame)
    request_user.thrd_frame.pack(fill='x')
    
    #Button
    add_button = ctk.CTkButton(
    request_user.thrd_frame,
    text="Add",
    font=ctk.CTkFont('Arial', size=14, weight="bold"),
    fg_color='green',
    corner_radius=10,  # Adjust the value for the desired roundness
    height=30,
    width=70,
    hover_color='dark green'  # Change the background color on hover to dark red
    )
    add_button.place(y=14, x=714)
    
    #Button
    cancel_button = ctk.CTkButton(
    request_user.thrd_frame,
    text="Cancel",
    font=ctk.CTkFont('Arial', size=14, weight="bold"),
    fg_color='gray',
    corner_radius=10,  # Adjust the value for the desired roundness
    height=30,
    width=20,
    hover_color='dark gray'  # Change the background color on hover to dark red
    )
    cancel_button.place(y=14, x=638)
 
request_user_window()
