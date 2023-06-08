import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from tkcalendar import *
import tkinter.font as tkFont
from ttkthemes import ThemedStyle

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

class request_user_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | Requests")
        self.geometry("{0}x{1}+200+50".format(1000, 600))
        self.resizable(False, False)
        self.configure(fg_color='white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

        # main frame
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill='both', expand=True)

        # header frame
        header_frame = ctk.CTkFrame(main_frame, fg_color='#313131', height=50, width=self.winfo_width(), corner_radius=0)
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
        frts_frame = ctk.CTkFrame(main_frame)
        frts_frame.pack(fill='both')
        
        #date label
        
        date_label = ctk.CTkLabel(frts_frame, text='Date: 05/25/2023', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        date_label.pack(side = 'right', pady = 5, padx=10)
        
        # Second Frame
        scnd_frame = ctk.CTkFrame(main_frame)
        scnd_frame.pack(fill='both')
        
        #name label
        name_label = ctk.CTkLabel(scnd_frame, text='Name:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        name_tbox = ctk.CTkLabel(scnd_frame, text='Martin Louies Ancaja', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        name_label.pack(side = 'left', pady = 5, padx=10)
        name_tbox.place(y = 5, x = 78)
        
        #email label
        email_tbox = ctk.CTkLabel(scnd_frame, text='martinlouiesancaja@gmail.com', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        email_label = ctk.CTkLabel(scnd_frame, text='Email:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        email_label.pack(side='right', pady=5, padx=380)
        email_tbox.place(y = 5, x=624)

        # Third Frame
        trhd_frame = ctk.CTkFrame(main_frame)
        trhd_frame.pack(fill='both')
        
        #user label
        user_label = ctk.CTkLabel(trhd_frame, text='User type:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        user_tbox = ctk.CTkLabel(trhd_frame, text='Faculty', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        user_label.pack(side='left', pady=5, padx=10)
        user_tbox.place(y = 5, x = 78)
        
        #request label
        reqtype_label = ctk.CTkLabel(trhd_frame, text='Request type:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        reqtype_label1 = ctk.CTkLabel(trhd_frame, text='Relocate', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        reqtype_tbox = ctk.CTkLabel(trhd_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        reqtype_label.pack(side='right', pady=5, padx=326)
        reqtype_label1.place(y = 5, x=678)
        reqtype_tbox.place(y = 5, x=580)
        
        # Fourth Frame
        frth_frame = ctk.CTkFrame(main_frame)
        frth_frame.pack(fill='both')
        
        #from label
        from_label = ctk.CTkLabel(frth_frame, text='From:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        from_label1 = ctk.CTkLabel(frth_frame, text='ICT Lab 1', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        from_tbox = ctk.CTkLabel(frth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        from_label.pack(side='left', pady=5, padx=16)
        from_label1.place(y = 5, x = 78)
        from_tbox.place(y = 5, x=10)
        
        #to label
        to_label = ctk.CTkLabel(frth_frame, text='To:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        to_label1 = ctk.CTkLabel(frth_frame, text='ICT Lab 3', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='black')
        to_tbox = ctk.CTkLabel(frth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        to_label.pack(side='right', pady=5, padx=394)
        to_label1.place(y = 5, x=678)
        to_tbox.place(y = 5, x=580)
        
        #Sixth Frame
        sxth_frame = ctk.CTkFrame(main_frame)
        sxth_frame.pack(fill='both')
        
        #Items selected label
        is_label = ctk.CTkLabel(sxth_frame, text='Items selected:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        is_label1 = ctk.CTkLabel(sxth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        is_label.pack(side='left', pady=5, padx=16)
        is_label1.place(y = 5, x=10)
        
        #Reason for transfer label
        retra_label = ctk.CTkLabel(sxth_frame, text='Reason for request:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        retra_tbox = ctk.CTkLabel(sxth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        retra_label.pack(side='right', pady=5, padx=288)
        retra_tbox.place(y = 5, x=580)
        
        #Seven
        #Eigth Frame
        seven_frame = ctk.CTkFrame(main_frame)
        seven_frame.pack(fill='x')
        
        custom_height = 182  # Set the desired height value
        seven_frame.configure(height=custom_height)
        seven_frame.pack_propagate(0)
        
        #item table
        columns = ('items_list', 'quantity')

        item_table_report = ttk.Treeview(seven_frame, columns=columns, show='headings', height=7)
        item_table_report.pack(side = 'left')
        item_table_report.place( x=10)

        # Configure column widths
        column_widths = [460, 100]
        for col, width in zip(columns, column_widths):
            item_table_report.column(col, width=width)

        # Configure column headings
        headings = ['Items List', 'Quantity']
        for col, heading in zip(columns, headings):
            item_table_report.heading(col, text=heading, anchor='center')

        # Sample data
        data = [
            ('Keyboard', 10, ),
            ('Mouse', 5, ),
            ('AVR', 10, ),
            ('PC Set', 4, ),
            ('Headset', 20, ),
            ('Keyboard', 10, ),
            ('Mouse', 5, ),
            ('AVR', 10, ),
            ('PC Set', 4, ),
            ('Headset', 20, ),
            ('Keyboard', 10, ),
            ('Mouse', 5, ),
            ('AVR', 10, ),
            ('PC Set', 4, ),
            ('Headset', 20, ),
        ]

        # Insert data into the table
        for row in data:
            item_table_report.insert('', 'end', values=row)

        # Center the data in each column
        for col in columns:
            item_table_report.column(col, anchor='center')
        
        #Text box
        textbox_entry = ctk.CTkTextbox(seven_frame, font=ctk.CTkFont('Arial', size=14), width=410, height=165)
        textbox_entry.pack(side='right')
        textbox_entry.place( x=580)
        
        #Eigth Frame
        egth_frame = ctk.CTkFrame(main_frame)
        egth_frame.pack(fill='both')
        
        #Aprroved person
        app_pers = ctk.CTkLabel(egth_frame, text='Approved by: \nPrinted Name:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        app_pers2 = ctk.CTkEntry(egth_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=250)
        app_pers1 = ctk.CTkLabel(egth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        app_pers.pack(side='left', pady=5, padx=16)
        app_pers2.place(y=8, x=150)
        app_pers1.place(y = 0, x=10)
        
        #Designation
        app_desg = ctk.CTkLabel(egth_frame, text='Designation:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        app_desg2 = ctk.CTkEntry(egth_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=200)
        app_desg1 = ctk.CTkLabel(egth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        app_desg.place(y=8, x=450)
        app_desg2.place(y=8, x=534)
        app_desg1.place(y = 8, x=444)
        
        #Date
        date = DateEntry(egth_frame, font= ctk.CTkFont('Arial', size = 14) )
        date.pack(side = 'right', pady = 5, padx = 10, ipady =2, ipadx = 2)
        date_label = ctk.CTkLabel(egth_frame, text='Date:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        date_label.pack(side = 'right', pady = 5)
        
        #Nine Frame
        nine_frame = ctk.CTkFrame(main_frame)
        nine_frame.pack(fill='both')
        
        #Aprroved person
        app_pers = ctk.CTkLabel(nine_frame, text='Released/Issued by:\nPrinted Name:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        app_pers2 = ctk.CTkEntry(nine_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=250)
        app_pers1 = ctk.CTkLabel(nine_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        app_pers.pack(side='left', pady=5, padx=16)
        app_pers2.place(y=8, x=150)
        app_pers1.place(y = 0, x=10)
        
        #Designation
        app_desg = ctk.CTkLabel(nine_frame, text='Designation:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        app_desg2 = ctk.CTkEntry(nine_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=200)
        app_desg1 = ctk.CTkLabel(nine_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        app_desg.place(y=8, x=450)
        app_desg2.place(y=8, x=534)
        app_desg1.place(y = 8, x=444)
        
        #Date
        date = DateEntry(nine_frame, font= ctk.CTkFont('Arial', size = 14) )
        date.pack(side = 'right', pady = 5, padx = 10, ipady =2, ipadx = 2)
        date_label = ctk.CTkLabel(nine_frame, text='Date:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        date_label.pack(side = 'right', pady = 5)
        
        #Ten Frame
        ten_frame = ctk.CTkFrame(main_frame)
        ten_frame.pack(fill='both')
        
        #Aprroved person
        app_pers = ctk.CTkLabel(ten_frame, text='Received by: \nPrinted Name:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        app_pers2 = ctk.CTkEntry(ten_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=250)
        app_pers1 = ctk.CTkLabel(ten_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        app_pers.pack(side='left', pady=5, padx=16)
        app_pers2.place(y=8, x=150)
        app_pers1.place(y = 0, x=10)
        
        #Designation
        app_desg = ctk.CTkLabel(ten_frame, text='Designation:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        app_desg2 = ctk.CTkEntry(ten_frame, fg_color='white', font=ctk.CTkFont('Arial', size=14, weight="normal"), width=200)
        app_desg1 = ctk.CTkLabel(ten_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        app_desg.place(y=8, x=450)
        app_desg2.place(y=8, x=534)
        app_desg1.place(y = 8, x=444)
        
        #Date
        date = DateEntry(ten_frame, font= ctk.CTkFont('Arial', size = 14) )
        date.pack(side = 'right', pady = 5, padx = 10, ipady =2, ipadx = 2)
        date_label = ctk.CTkLabel(ten_frame, text='Date:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        date_label.pack(side = 'right', pady = 5)
        
        #Eleven Frame
        eleven_frame = ctk.CTkFrame(main_frame, fg_color='gray', corner_radius=0,)
        eleven_frame.pack(fill='x')
        
        # Button
        approved_button = ctk.CTkButton(
        eleven_frame,
        text="Approved",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='green',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=32,
        hover_color='dark green'  # Change the background color on hover to dark red
        )
        approved_button.pack(side= 'right')
        approved_button.pack(pady=5, padx=10)
        
if __name__ == '__main__':
    root = tk.Tk()
    request_user_window(root)
    root.mainloop()
