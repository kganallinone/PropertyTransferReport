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
        date = DateEntry(frts_frame, font= ctk.CTkFont('Arial', size = 14) )
        date.pack(side = 'right', pady = 5, padx = 10, ipady =2, ipadx = 2)
        date_label = ctk.CTkLabel(frts_frame, text='Date:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        date_label.pack(side = 'right', pady = 5)
        
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
        reqtype_label = ctk.CTkLabel(trhd_frame, text='Request type: (Check only one)', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        reqtype_tbox = ctk.CTkLabel(trhd_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        reqtype_label.pack(side='right', pady=5, padx=214)
        reqtype_tbox.place(y = 5, x=580)
        
        # Fourth Frame
        frth_frame = ctk.CTkFrame(main_frame)
        frth_frame.pack(fill='both')
        
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
        from_tbox = ctk.CTkOptionMenu(frth_frame, width=150, values=entities, fg_color= 'white', text_color='black', dropdown_fg_color='white', font= ctk.CTkFont('Arial', size = 14), dropdown_font=ctk.CTkFont('Arial', size = 14))
        from_tbox.place(y = 5, x = 78)
        
        #transfer type label
        trans_type = ctk.CTkCheckBox(frth_frame, text='Reassignment')
        trans_type.pack(side = 'right', pady = 5, padx = 180)
        
        trans_type = ctk.CTkCheckBox(frth_frame, text='Donation')
        trans_type.place(y = 5, x=580)
        
        # Fifth Frame
        ffth_frame = ctk.CTkFrame(main_frame)
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
        
        #transfer type label
        trans_type1 = ctk.CTkCheckBox(ffth_frame, text='Others (Specify):')
        trans_type = ctk.CTkEntry(ffth_frame, fg_color='white')
        trans_type1.pack(side = 'right', pady = 5, padx = 166)
        trans_type.place(y = 5, x=840)
        
        trans_type = ctk.CTkCheckBox(ffth_frame, text='Relocate')
        trans_type.place(y = 5, x=580)
        
        # Sixth Frame
        sxth_frame = ctk.CTkFrame(main_frame)
        sxth_frame.pack(fill='both')
        
        #Items selected label
        is_label = ctk.CTkLabel(sxth_frame, text='Items selected:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        is_label1 = ctk.CTkLabel(sxth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        is_label.pack(side='left', pady=5, padx=16)
        is_label1.place(y = 5, x=10)
        
        # Button
        select_items_button = ctk.CTkButton(
            sxth_frame,
            text="Select items",
            font=ctk.CTkFont('Arial', size=14, weight="normal"),
            fg_color='red',
            command=self.open_select_items_window,  # Add a command to the button
            corner_radius=10,  # Adjust the value for the desired roundness
            width=20,
            hover_color='dark red' # Change the background color on hover to dark red
        )
        select_items_button.place(y = 5, x=474)
        
        #Reason for transfer label
        retra_label = ctk.CTkLabel(sxth_frame, text='Reason for request:', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='black')
        retra_tbox = ctk.CTkLabel(sxth_frame, text='*', font=ctk.CTkFont('Arial', size=14, weight="normal"), text_color='red')
        retra_label.pack(side='right', pady=5, padx=288)
        retra_tbox.place(y = 5, x=580)
        
        #Seventh Frame
        svnth_frame = ctk.CTkFrame(main_frame)
        svnth_frame.pack(fill='both')
        
        columns = ('items_list', 'quantity')
        
        item_table_report = ttk.Treeview(svnth_frame, columns=columns, show='headings', height=10)
        item_table_report.pack(side = 'left')
        item_table_report.place(y = 5, x=10)
        
        item_table_report.column('items_list', width = 460)
        item_table_report.column('quantity', width = 100)
        
        item_table_report.heading('items_list', text='Items List')
        item_table_report.heading('quantity', text='Quantity')
        
        #Text box
        textbox_entry = ctk.CTkTextbox(svnth_frame, font=ctk.CTkFont('Arial', size=14), width=410, height=200)
        textbox_entry.pack(side='right')
        textbox_entry.place(y = 5, x=580)
        
        
        #Eigth Frame
        egth_frame = ctk.CTkFrame(main_frame)
        egth_frame.pack(fill='both')
        
        # Button
        submit_request_button = ctk.CTkButton(
        egth_frame,
        text="Submit Request",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='green',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=40,
        hover_color='dark green'  # Change the background color on hover to dark red
        )
        submit_request_button.pack(side= 'right')
        submit_request_button.pack(pady=20, padx=10)
        
        #Nineth Frame
        nnth_frame = ctk.CTkFrame(main_frame)
        nnth_frame.pack(fill='both')
        
        #footer frame
        footer_frame = ctk.CTkFrame(nnth_frame, fg_color='maroon', height=50, width=self.winfo_width(), corner_radius=0)
        footer_frame.pack(fill='both', side='bottom')
    
    def open_select_items_window(self):
        self = tk.Toplevel()
        self.title("Select Items")
        self.geometry("500x400")  
        self.geometry("{0}x{1}+300+150".format(800, 400))
        self.resizable(False, False) 

        # main frame
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill='both', expand=True)

        #First frame
        frt_frame = ctk.CTkFrame(main_frame)
        frt_frame.pack(fill='both')

        #header frame
        header_frame = ctk.CTkFrame(frt_frame, fg_color='maroon', height=30, width=self.winfo_width(), corner_radius=0)
        header_frame.pack(fill='both', side='top')
        
        avail_label = ctk.CTkLabel(header_frame, text='Available Items', font=ctk.CTkFont('Arial', size=14, weight="bold"), text_color='white')
        avail_label.pack(side='top', pady=2)
        
        
        self_scroll_frame = ctk.CTkScrollableFrame(main_frame, fg_color='white', height=286)
        self_scroll_frame.pack(fill='both')
        
        # Frame inside the scrollable frame
        self.frame = ctk.CTkFrame(self_scroll_frame, height=400, fg_color='#F4F4F4')
        self.frame.pack(fill='both', pady=5)

        sub_frame = ctk.CTkFrame(self.frame)
        sub_frame.pack(fill='x')
        
        rectangle_frame = ctk.CTkFrame(sub_frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(fill='both')
        
        check_box = ctk.CTkCheckBox(rectangle_frame, text='\t\t\tKeyboard \t\t\tItems: 20', font=ctk.CTkFont('Arial', size=14, weight="bold"))
        check_box.place(y = 35, x=10)
        
        # Label to display the current value
        current_value = 0
        value_label = tk.Label(rectangle_frame, text=current_value, font=ctk.CTkFont("Arial", 14, weight="bold"), fg="black")
        value_label.pack(side='right')
        value_label.place(y=35, x=714)
        
        # Function to increment the value
        def increment_value():
            nonlocal current_value
            current_value += 1
            value_label.config(text=current_value)
            
            # Function to decrement the value
        def decrement_value():
            nonlocal current_value
            current_value -= 1
            value_label.config(text=current_value)
        
        #Button
        minus_button = ctk.CTkButton(
        rectangle_frame,
        text="-",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='gray',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=20,
        width=30,
        hover_color='dark gray',  # Change the background color on hover to dark red
        command=decrement_value  # Associate the decrement function with the button
        )
        minus_button.pack(side= 'right')
        minus_button.pack(pady=35, padx=10)
        
        #Button
        plus_button = ctk.CTkButton(
        rectangle_frame,
        text="+",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='gray',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=20,
        width=20,
        hover_color='dark gray',  # Change the background color on hover to dark red
        command=increment_value  # Associate the decrement function with the button
        )
        plus_button.pack(side= 'right')
        plus_button.pack(pady=35, padx=20)
        
        #Third frame
        thrd_frame = ctk.CTkFrame(main_frame)
        thrd_frame.pack(fill='x')
        
        # Button
        add_button = ctk.CTkButton(
        thrd_frame,
        text="Add",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='green',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=30,
        width=80,
        hover_color='dark green'  # Change the background color on hover to dark red
        )
        add_button.pack(side= 'right')
        add_button.pack(pady=5, padx=10)
        
        # Button
        cancel_button = ctk.CTkButton(
        thrd_frame,
        text="Cancel",
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        fg_color='gray',
        corner_radius=10,  # Adjust the value for the desired roundness
        height=30,
        width=20,
        hover_color='dark gray'  # Change the background color on hover to dark red
        )
        cancel_button.pack(side= 'right')
        cancel_button.pack(pady=20, padx=10)
        
        
        
        
        
        
if __name__ == '__main__':
    root = tk.Tk()
    request_user_window(root)
    root.mainloop()
