import customtkinter as ctk
import tkinter as tk
from PIL import Image

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

def delete_item_window():

    delete_item = ctk.CTkToplevel()
    delete_item.title('Property Transfer | Edit Items')
    delete_item.geometry("{0}x{1}+350+50".format(700,525))
    delete_item.resizable(False, False)
    delete_item.configure(fg_color = 'white')
    
    #header frame
    header_frame = ctk.CTkFrame(delete_item, fg_color='#313131', height=50, width=delete_item.winfo_width(), corner_radius=0)
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
    
    label = ctk.CTkLabel(header_frame, text = 'Delete Items', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
    label.pack(side = 'right',  pady = 15, padx = 15)
    
    frame1 = ctk.CTkFrame(delete_item, fg_color='transparent')
    frame1.pack(fill = 'x')
    
    search_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-search-100.png'), size = (20, 20))
    search_button = ctk.CTkButton(frame1, text=None, image=search_icon, fg_color='transparent', width=20, hover_color='#e0e0e0')
    search_button.pack(side = 'right', pady = 10, padx = (0,20))
    
    search_box = ctk.CTkEntry(frame1, placeholder_text='Search item', width=200, fg_color='white')
    search_box.pack(side = 'right', pady = 10, padx = 5)
    
    #for input
    frame2 = ctk.CTkFrame(delete_item, fg_color='transparent')
    frame2.pack(fill = 'x', pady = 20)
    
    number_label = ctk.CTkLabel(frame2, text='Property Number:', font=ctk.CTkFont('Arial', size=18))
    number_label.pack(side = 'left', pady = 10, padx = 50)
    
    loc_label = ctk.CTkLabel(frame2, text='Current Location:', font=ctk.CTkFont('Arial', size=18))
    loc_label.pack(side = 'right', pady = 10, padx = 160)
    
    #input
    frame3 = ctk.CTkFrame(delete_item, fg_color='transparent')
    frame3.pack(fill = 'x')
    
    property_no = ctk.CTkEntry(frame3, width=200, fg_color='white')
    property_no.pack(side = 'left', padx = 50)
    
    loc_options_buildings = ["Computer Laboratory 1", "Computer Laboratory 2", "Computer Laboratory 3", "Other"]
    item_loc_buildings = ctk.CTkOptionMenu(frame3, width=250, values=loc_options_buildings, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 15), dropdown_font=ctk.CTkFont('Arial', size = 15))
    item_loc_buildings.pack(side = 'right', pady = (0, 10), padx = 50)
    
    #input
    frame4 = ctk.CTkFrame(delete_item, fg_color='transparent')
    frame4.pack(fill = 'x')
    
    item_loc_room = ctk.CTkEntry(frame4, width=250, fg_color= 'white', font= ctk.CTkFont('Arial', size = 15), placeholder_text='Please Specify')
    item_loc_room.pack(side = 'right', pady = (0, 10), padx = 50)
    
    frame5 = ctk.CTkFrame(delete_item, fg_color='transparent')
    frame5.pack(fill = 'x')
    
    name_label = ctk.CTkLabel(frame5, text='Name', font=ctk.CTkFont('Arial', size=18) )
    name_label.pack(side = 'left', pady = 10, padx = 50)
    
    quantity_label = ctk.CTkLabel(frame5, text='Quantity', font=ctk.CTkFont('Arial', size=18) )
    quantity_label.pack(side = 'right', pady = 10, padx = 235)
    
    #input
    frame5 = ctk.CTkFrame(delete_item, fg_color='transparent')
    frame5.pack(fill = 'x')
    
    property_name = ctk.CTkEntry(frame5, width=200, fg_color='white')
    property_name.pack(side = 'left', padx =50)
    
    item_quantity = tk.Spinbox(frame5, from_= 0, to= 1000, borderwidth=2, font= ctk.CTkFont('Arial', size = 16), bg='white')
    item_quantity.pack(side = 'right', pady = 10, padx = (100, 150))
    
    frame6 = ctk.CTkFrame(delete_item, fg_color='transparent')
    frame6.pack(fill = 'x')
    
    desc_label = ctk.CTkLabel(frame6, text='Description', font=ctk.CTkFont('Arial', size=18))
    desc_label.pack(side = 'left', pady = 10, padx = 50)
    
    #input
    frame7 = ctk.CTkFrame(delete_item, fg_color='transparent')
    frame7.pack(fill = 'x')
    
    description = ctk.CTkEntry(frame7, width=200, fg_color='white')
    description.pack(side = 'left', pady = 10, padx = 50)
    
    delete = ctk.CTkButton(delete_item, text='Delete', font=ctk.CTkFont('Arial', size = 18, weight='bold'), fg_color='#EE2A2A', hover_color='#B51818')
    delete.pack(side = 'right', padx = 20)
    
    delete_all = ctk.CTkButton(delete_item, text='Delete All', font=ctk.CTkFont('Arial', size = 18, weight='bold'), text_color='black',fg_color='#f6f6f6', hover_color='#B51818')
    delete_all.pack(side = 'right', padx = 20)
    
    delete_item.mainloop()
    
    
    
#delete_item_window()