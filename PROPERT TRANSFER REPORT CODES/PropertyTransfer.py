from tkinter import *
import customtkinter as ctk
from PIL import ImageTk,Image
from login import login_window

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark

main = ctk.CTk()
main.title("Property Transfer | Main")
main.geometry("{0}x{1}+200+50".format(1000, 600))
main.resizable(False, False)
main.configure(fg_color = 'white')
main.iconbitmap('PTR.ico')

main_openimg = Image.open(r'bg.png')
#resize_image = openimage1.resize(( main.winfo_width(),main.winfo_height()))
main_resize_image = main_openimg.resize((main.winfo_screenwidth(),main.winfo_screenheight()))
main_img1=ImageTk.PhotoImage(main_resize_image)
'''l1=ctk.CTkLabel(master=main,image=img1 )
l1.pack()'''
main_label1= Label(main, image=main_img1)
main_label1.image = main_img1
main_label1.pack()

def open_app():
    main.withdraw()
    login_window()
    
    
main_bttn= ctk.CTkButton(
    main_label1, 
    command=open_app, 
    width=200, 
    height=40, 
    compound="left", 
    corner_radius= 30, 
    fg_color='maroon', 
    text_color='white', 
    hover_color='#4F0000', 
    font = ctk.CTkFont (
        'Arial', 
        weight="bold"
        ), 
    text="GET STARTED" 
    )

main_bttn.place(x=610, y=350)

main.mainloop()