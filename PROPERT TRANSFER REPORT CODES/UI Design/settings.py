import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark


def settings_window():
    
    
        
    settings = ctk.CTkToplevel()
    settings.title('Property Transfer | Settings')
    settings.geometry("{0}x{1}+200+50".format(1000,600))
    settings.resizable(False, False)
    settings.configure(fg_color = 'white')
    
    from edit_item import edit_item_window
    from delete_item import delete_item_window
    
    def open_edit_item():
        edit_item_window()
    
    def open_delete_item():
        delete_item_window()
        
    #header frame
    header_frame = ctk.CTkFrame(settings, fg_color='#313131', height=50, width=settings.winfo_width(), corner_radius=0)
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
    
    label = ctk.CTkLabel(header_frame, text = 'Settings', font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
    label.pack(side = 'right',  pady = 15, padx = 15)
    
    frame1 = ctk.CTkFrame(settings, fg_color='transparent')
    frame1.pack(fill = 'x')
    
    cat_label = ctk.CTkLabel(frame1, text='Items', font=ctk.CTkFont('Arial', size=22, weight='bold'))
    cat_label.pack(side = 'left', pady = 10, padx = 20)
    
    frame2 = ctk.CTkFrame(settings, fg_color='transparent')
    frame2.pack(fill = 'x')
    
    edit_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-edit-96.png'), size=(90, 90))
    edit_item = ctk.CTkButton(frame2, command=open_edit_item, image=edit_icon ,text='Edit Item', fg_color='#F6F6F6', font=ctk.CTkFont('Arial', size=20), text_color='black', hover_color='#e0e0e0', width=200)
    edit_item.pack(side = 'left', pady = 15 ,padx = 20)
    
    delete_icon = ctk.CTkImage(Image.open('python property transfer\images\icons8-delete-90.png'), size = (90, 90))
    delete_item = ctk.CTkButton(frame2, command=open_delete_item, image=delete_icon ,text='Delete Item', fg_color='#F6F6F6', font=ctk.CTkFont('Arial', size=20), text_color='black', hover_color='#e0e0e0', width=200)
    delete_item.pack(side = 'left', pady = 15 ,padx = 20)
    
    settings.mainloop()
    
    
    

settings_window()