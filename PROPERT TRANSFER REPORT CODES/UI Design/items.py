import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image
import tkcalendar
from ttkthemes import ThemedStyle

ctk.set_appearance_mode("system")  # Modes: system (default), light, dark

def items_window():

    items = ctk.CTkToplevel()
    items.title("Property Transfer | Items")
    items.geometry("{0}x{1}+200+50".format(1000, 600))
    items.resizable(False, False)
    items.configure(fg_color = 'white')
    items.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

    s = ThemedStyle(items)
    s.theme_use('breeze')
    
    #header frame
    header_frame = ctk.CTkFrame(items, fg_color='#313131', height=50, width=items.winfo_width(), corner_radius=0)
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
    frame = ctk.CTkFrame(items, width = 700)
    frame.pack(fill = 'both', side = 'left', padx = 15, pady = 15)
    
    columns = ('property_no', 'name', 'description', 'current_loc', 'quantity')
    
    item_table = ttk.Treeview(frame, columns=columns, show='headings', height=24)
    item_table.pack(fill=tk.BOTH)
    
    item_table.column('property_no', width=150)
    item_table.column('name', width=150)
    item_table.column('description', width=150)
    item_table.column('current_loc', width=150)
    item_table.column('quantity', width= 100)
    
    item_table.heading('property_no', text='Property No.')
    item_table.heading('name', text='Name')
    item_table.heading('description', text='Description')
    item_table.heading('current_loc', text='Current Location')
    item_table.heading('quantity', text='Quantity')
    
    #for input
    frame2 = ctk.CTkFrame(items, width = 300, fg_color='#f5f7f7', corner_radius=20)
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
    
    loc_options_buildings = ["Computer Laboratory 1", "Computer Laboratory 2", "Computer Laboratory 3", "Other"]
    item_loc_buildings = ctk.CTkOptionMenu(frame2, width=250, values=loc_options_buildings, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 15), dropdown_font=ctk.CTkFont('Arial', size = 15))
    item_loc_buildings.pack(pady = (0, 10), padx = 10)
    item_loc_room = ctk.CTkEntry(frame2, width=250, fg_color= 'white', font= ctk.CTkFont('Arial', size = 15), placeholder_text='Please Specify')
    item_loc_room.pack(pady = (0, 10), padx = 10)
    
    #item quantity
    item_quantity_label_frame = ctk.CTkFrame(frame2, fg_color='transparent')
    item_quantity_label_frame.pack(fill = 'x')
    item_quantity_label = ctk.CTkLabel(item_quantity_label_frame, text = 'Quantity', font= ctk.CTkFont('Arial', size = 18))
    item_quantity_label.pack(side = 'left', pady = (10,0), padx = 10)
    
    item_quantity = tk.Spinbox(frame2, from_= 0, to= 1000, borderwidth=2, width=250, font= ctk.CTkFont('Arial', size = 16), bg='white')
    item_quantity.pack(pady = (0, 10), padx = 10)
    
    #add button
    add_button = ctk.CTkButton(frame2, text = 'Add', font= ctk.CTkFont('Arial', size = 18, weight = "bold"),fg_color='#0077B8', text_color='white', corner_radius = 30)
    add_button.pack(pady = 20, ipady = 5)
    
    items.mainloop()
    
items_window()

