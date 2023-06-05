import tkinter as tk
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark


class request_admin_window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Property Transfer | Requests")
        self.geometry("{0}x{1}+200+50".format(1000, 600))
        self.resizable(False, False)
        self.configure(fg_color='white')
        self.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

        # header frame
        header_frame = ctk.CTkFrame(self, fg_color='#313131', height=50, width=self.winfo_width(), corner_radius=0)
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

        # Frame below the header
        button_frame = ctk.CTkFrame(self, height=50, width=self.winfo_width(), corner_radius=0)
        button_frame.pack(fill='both', side='top')

        # Pending button
        self.pending_button = ctk.CTkButton(button_frame, text='Pending (3)', font=ctk.CTkFont('Arial', size=14, weight="bold"), corner_radius=10, command=self.show_pending_content)
        self.pending_button.pack(side='left', pady=10, padx=10, anchor='center', expand=True)

        # Center line separator
        center_line_frame = ctk.CTkFrame(button_frame, width=2, height=10, fg_color='black')
        center_line_frame.pack(side='left', padx=5, fill='y', expand=True)

        # Approved button
        self.approved_button = ctk.CTkButton(button_frame, text='Approved', font=ctk.CTkFont('Arial', size=14, weight="bold"), corner_radius=10, command=self.show_approved_content)
        self.approved_button.pack(side='right', pady=10, padx=10, anchor='center', expand=True)

        label = ctk.CTkLabel(header_frame, text='Requests', font=ctk.CTkFont('Arial', size=25, weight="bold"), text_color='white')
        label.pack(side='right', pady=15, padx=15)

        self_scroll_frame = ctk.CTkScrollableFrame(self, fg_color='white', height=560)
        self_scroll_frame.pack(fill='both')
        
        # Frame inside the scrollable frame
        self.frame = ctk.CTkFrame(self_scroll_frame, height=400, corner_radius=20, fg_color='#F4F4F4')
        self.frame.pack(fill='both', pady=5, padx=15)

        sub_frame = ctk.CTkFrame(self.frame, fg_color='transparent')
        sub_frame.pack(fill='x')
        
    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
            
    def show_pending_content(self):
        # Clear the frame
        self.clear_frame()

        # Rectangle 1
        # Create and pack the content frame for Pending section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Pending", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Red')
        pending_label.place(x=800, y=10)
        
        # Rectangle 2
        # Create and pack the content frame for Pending section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Pending", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Red')
        pending_label.place(x=800, y=10)
        
        # Rectangle 3
        # Create and pack the content frame for Pending section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Pending", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Red')
        pending_label.place(x=800, y=10)

        

        
        
    def show_approved_content(self):
        # Clear the frame
        self.clear_frame()

        # Rectangle 1
        # Create and pack the content frame for Approved section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Approved", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Green')
        pending_label.place(x=800, y=10)
        
        # Rectangle 2
        # Create and pack the content frame for Approved section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Approved", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Green')
        pending_label.place(x=800, y=10)
        
        # Rectangle 3
        # Create and pack the content frame for Approved section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Approved", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Green')
        pending_label.place(x=800, y=10)
        
        # Rectangle 4
        # Create and pack the content frame for Approved section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Approved", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Green')
        pending_label.place(x=800, y=10)
        
        # Rectangle 5
        # Create and pack the content frame for Approved section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Approved", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Green')
        pending_label.place(x=800, y=10)
        
        # Rectangle 6
        # Create and pack the content frame for Approved section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Approved", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Green')
        pending_label.place(x=800, y=10)
        
        # Rectangle 7
        # Create and pack the content frame for Approved section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Approved", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Green')
        pending_label.place(x=800, y=10)
        
        # Rectangle 8
        # Create and pack the content frame for Approved section
        rectangle_frame = ctk.CTkFrame(self.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
        rectangle_frame.pack(pady=5, padx=20)

        # Content inside the rectangle frame
        prof_label = ctk.CTkLabel(rectangle_frame, text='Prof. Andie Zurbano', font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        prof_label.place(x=20, y=30)

        items_label = ctk.CTkLabel(rectangle_frame, text="Items:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        items_label.place(x=20, y=60)

        items_label = ctk.CTkLabel(rectangle_frame, text="Keyboard, Mouse, PC Set", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        items_label.place(x=70, y=60)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Transfer type:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        transfer_type_label.place(x=500, y=30)

        transfer_type_label = ctk.CTkLabel(rectangle_frame, text="Reasignment", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        transfer_type_label.place(x=610, y=30)

        date_label = ctk.CTkLabel(rectangle_frame, text="Date:", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Black')
        date_label.place(x=500, y=60)

        date_label = ctk.CTkLabel(rectangle_frame, text="05/25/2023", font=ctk.CTkFont('Arial', size=16, weight="normal"), text_color='Black')
        date_label.place(x=550, y=60)

        pending_label = ctk.CTkLabel(rectangle_frame, text="Approved", font=ctk.CTkFont('Arial', size=16, weight="bold"), text_color='Green')
        pending_label.place(x=800, y=10)

        
        
        

if __name__ == '__main__':
    root = tk.Tk()
    request_admin_window(root)
    root.mainloop()

        