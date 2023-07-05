import tkinter as tk
import customtkinter as ctk
from PIL import Image
import pyrebase

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

def clear_frame(request_admin):
    for widget in request_admin.frame.winfo_children():
        widget.destroy()

def show_pending_content(request_admin):
    # Clear the frame
    clear_frame(request_admin)

    # Rectangle 1
    # Create and pack the content frame for Pending section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Pending',
        fg_color='red',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark red',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=800)

    # Rectangle 2
    # Create and pack the content frame for Pending section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Pending',
        fg_color='red',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark red',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=800)
    
    # Rectangle 3
    # Create and pack the content frame for Pending section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Pending',
        fg_color='red',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark red',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=800)

def show_approved_content(request_admin):
    # Clear the frame
    clear_frame(request_admin)

    # Rectangle 1
    # Create and pack the content frame for Approved section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Approved',
        fg_color='green',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark green',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=790)

    # Rectangle 2
    # Create and pack the content frame for Approved section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Approved',
        fg_color='green',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark green',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=790)
    
    # Rectangle 3
    # Create and pack the content frame for Approved section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Approved',
        fg_color='green',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark green',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=790)
    
    # Rectangle 4
    # Create and pack the content frame for Approved section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Approved',
        fg_color='green',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark green',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=790)
    
    # Rectangle 5
    # Create and pack the content frame for Approved section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Approved',
        fg_color='green',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark green',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=790)
    
    # Rectangle 6
    # Create and pack the content frame for Approved section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Approved',
        fg_color='green',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark green',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=790)
    
    # Rectangle 7
    # Create and pack the content frame for Approved section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Approved',
        fg_color='green',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark green',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=790)
    
    # Rectangle 8
    # Create and pack the content frame for Approved section
    rectangle_frame = ctk.CTkFrame(request_admin.frame, fg_color='#DEDEDE', height=95, width=1834, border_width=2, border_color='maroon', corner_radius=0)
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

    #Open button
    request_admin.open_button = ctk.CTkButton(
        rectangle_frame,
        text='Approved',
        fg_color='green',
        font=ctk.CTkFont('Arial', size=16, weight="bold"),
        text_color='white',
        width=20,
        hover_color='dark green',
        corner_radius=10
    )
    request_admin.open_button.place(y=20, x=790)

def request_admin_window():

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
    
    request_admin = ctk.CTk()
    request_admin.title("Property Transfer | Request")
    request_admin.geometry("{0}x{1}+200+50".format(1000, 550))
    request_admin.resizable(False, False)
    request_admin.configure(fg_color='white')
    request_admin.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')

    # header frame
    header_frame = ctk.CTkFrame(request_admin, fg_color='#313131', height=50, width=request_admin.winfo_width(), corner_radius=0)
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
    button_frame = ctk.CTkFrame(request_admin, height=50, width=request_admin.winfo_width(), corner_radius=0)
    button_frame.pack(fill='both', side='top')

    # Pending button
    request_admin.pending_button = ctk.CTkButton(
        button_frame,
        text='Pending (3)',
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        corner_radius=10,
        command=lambda: show_pending_content (request_admin)
    )
    request_admin.pending_button.pack(side='left', pady=10, padx=10, anchor='center', expand=True)

    # Center line separator
    center_line_frame = ctk.CTkFrame(button_frame, width=2, height=10, fg_color='black')
    center_line_frame.pack(side='left', padx=5, fill='y', expand=True)

    # Approved button
    request_admin.approved_button = ctk.CTkButton(
        button_frame,
        text='Approved',
        font=ctk.CTkFont('Arial', size=14, weight="bold"),
        corner_radius=10,
        command=lambda: show_approved_content (request_admin)
    )
    request_admin.approved_button.pack(side='right', pady=10, padx=10, anchor='center', expand=True)

    label = ctk.CTkLabel(header_frame, text='Requests', font=ctk.CTkFont('Arial', size=25, weight="bold"), text_color='white')
    label.pack(side='right', pady=15, padx=15)

    self_scroll_frame = ctk.CTkScrollableFrame(request_admin, fg_color='white', height=560)
    self_scroll_frame.pack(fill='both')

    # Frame inside the scrollable frame
    request_admin.frame = ctk.CTkFrame(self_scroll_frame, height=400, corner_radius=20, fg_color='#F4F4F4')
    request_admin.frame.pack(fill='both', pady=5, padx=15)

    sub_frame = ctk.CTkFrame(request_admin.frame, fg_color='transparent')
    sub_frame.pack(fill='x')

    show_pending_content(request_admin)
    
    request_admin.mainloop()

request_admin_window()
