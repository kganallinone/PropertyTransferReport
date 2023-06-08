import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image
from tkcalendar import *
from ttkthemes import ThemedStyle

#history window
class history_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | History")
        self.geometry("{0}x{1}+200+50".format(1000, 550))
        self.resizable(False, False)
        self.configure(fg_color='white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

        #header frame
        header_frame = ctk.CTkFrame(self, fg_color='#313131', height=50, width=self.winfo_width(), corner_radius=0)
        header_frame.pack(fill='both', side='top')

        #app logo
        app_logo = ctk.CTkImage(Image.open('python property transfer\images\icons8-data-transfer-483-white.png'), size=(25, 25))
        app_logo_label = ctk.CTkLabel(header_frame, image=app_logo, text=None)
        app_logo_label.pack(side='left', pady=10, padx=10)

        #app name
        app_name1 = ctk.CTkLabel(header_frame, text='PROPERTY', font=ctk.CTkFont('Arial', size=22, weight="bold"), text_color='white')
        app_name1.pack(side='left', pady=10, padx=10)
        app_name2 = ctk.CTkLabel(header_frame, text='TRANSFER', font=ctk.CTkFont('Arial', size=22, weight="bold"), text_color='#ee4444')
        app_name2.pack(side='left', pady=10)

        label = ctk.CTkLabel(header_frame, text='History', font=ctk.CTkFont('Arial', size=25, weight="bold"), text_color='white')
        label.pack(side='right', pady=15, padx=15)

        #item table
        columns = ('user_received', 'date', 'item', 'type', 'quantity', 'user_approved')

        item_table_report = ttk.Treeview(self, columns=columns, show='headings', height=22)
        item_table_report.pack(fill='both' ,pady=10, padx=10)

        # Configure column widths
        column_widths = [100, 100, 100, 100, 100, 100]
        for col, width in zip(columns, column_widths):
            item_table_report.column(col, width=width)

        # Configure column headings
        headings = ['User Received', 'Date', 'Item', 'Type', 'Quantity', 'User Approved']
        for col, heading in zip(columns, headings):
            item_table_report.heading(col, text=heading, anchor='center')

        # Sample data
        data = [
            ('Prof. Andrea Zurbano', '06-24-2023', 'Keyboard', 'Relocate', 5, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-24-2023', 'Mouse', 'Relocate', 3, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-24-2023', 'PC Set', 'Relocate', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-10-2023', 'AVR', 'Reassignment', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-10-2023', 'Mouse', 'Reassignment', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-24-2023', 'Keyboard', 'Relocate', 5, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-24-2023', 'Mouse', 'Relocate', 3, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-24-2023', 'PC Set', 'Relocate', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-10-2023', 'AVR', 'Reassignment', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-10-2023', 'Mouse', 'Reassignment', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-24-2023', 'Keyboard', 'Relocate', 5, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-24-2023', 'Mouse', 'Relocate', 3, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-24-2023', 'PC Set', 'Relocate', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-10-2023', 'AVR', 'Reassignment', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-10-2023', 'Mouse', 'Reassignment', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-24-2023', 'Keyboard', 'Relocate', 5, 'Prof. Lynel P. Tabien'),
            ('Prof. Andrea Zurbano', '06-24-2023', 'Mouse', 'Relocate', 3, 'Prof. Lynel P. Tabien'),
            ('Prof. Lynel P Tabien', '06-24-2023', 'PC Set', 'Relocate', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Lynel P Tabien', '06-10-2023', 'AVR', 'Reassignment', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Lynel P Tabien', '06-10-2023', 'Mouse', 'Reassignment', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Lynel P Tabien', '06-24-2023', 'Keyboard', 'Relocate', 5, 'Prof. Lynel P. Tabien'),
            ('Prof. Lynel P Tabien', '06-24-2023', 'Mouse', 'Relocate', 3, 'Prof. Lynel P. Tabien'),
            ('Prof. Lynel P Tabien', '06-24-2023', 'PC Set', 'Relocate', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Lynel P Tabien', '06-10-2023', 'AVR', 'Reassignment', 2, 'Prof. Lynel P. Tabien'),
            ('Prof. Lynel P Tabien', '06-10-2023', 'Mouse', 'Reassignment', 2, 'Prof. Lynel P. Tabien'),
        ]

        # Insert data into the table
        for row in data:
            item_table_report.insert('', 'end', values=row)

        # Center the data in each column
        for col in columns:
            item_table_report.column(col, anchor='center')
        
history_window = history_window()
history_window.mainloop()
