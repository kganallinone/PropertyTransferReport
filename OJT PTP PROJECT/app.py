#importing required modules
import pyrebase
import tkinter
from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk,Image

# Config/Setup
config = {
    "apiKey": "AIzaSyCyCtXg05ff-tocdUaxjBFfa550TLfKZQ4",
    "authDomain": "puplopez-ptp.firebaseapp.com",
    "projectId": "puplopez-ptp",
    "databaseURL": "https://puplopez-ptp-default-rtdb.firebaseio.com/",
    "storageBucket": "puplopez-ptp.appspot.com",
    "messagingSenderId": "638312293451",
    "appId": "1:638312293451:web:79e9405d11db0496f599ce",
    "measurementId": "G-9Z3SPKFR9V"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
# Get a reference to the auth service
auth = firebase.auth()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("600x600")
app.title('Register')


#LOG-IN FUNCTION
def button_function():
   
    login_email = login_entry1.get()
    login_password = login_entry2.get()
    login_key = login_email.replace("@gmail.com", "")
    login_data = {"email": login_email, "id": id, "pw": login_password }
    
    get_data = db.child("user_accounts").child(login_key).get()
    
    if login_key== get_data.key():
        app.destroy()            # destroy current window and creating new one 
        w = customtkinter.CTk()  
        w.geometry("1280x720")
        w.title('Welcome')
        l1=customtkinter.CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
        l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
        w.mainloop()
    
    else:
        
        answer=messagebox.askyesno("Question","Complete your data")
        print(answer)


#REGISTER FUNCTION
def button_function2():
    id = entry1.get()
    email = entry2.get()
    password = entry3.get()
    key = email.replace("@gmail.com", "")
    auth.create_user_with_email_and_password(email, password)
    data = {"email": email, "id": id, "pw": password }
    db.child("user_accounts").child(key).set(data)
    
    if id != "":
        answer=messagebox.askyesno("Question", data)
        print(answer)
    else:
        answer=messagebox.askyesno("Question", "ERROR")
        print(answer)
    

app_openimg = Image.open("7.jpg")
#resize_image = openimage1.resize(( app.winfo_width(),app.winfo_height()))
app_resize_image = app_openimg.resize((app.winfo_screenwidth(),app.winfo_screenheight()))
app_img1=ImageTk.PhotoImage(app_resize_image)
'''l1=customtkinter.CTkLabel(master=app,image=img1 )
l1.pack()'''
app_label1= Label(image=app_img1)
app_label1.image = app_img1
app_label1.pack()

#LOG IN AREA
login_frame1=customtkinter.CTkFrame(master=app_label1, width=420, height=460, corner_radius=15)
login_frame1.place(relx=0.3, rely=0.5, anchor=tkinter.E)

login_label1=customtkinter.CTkLabel(master=login_frame1, text="Login your Account",font=('Century Gothic',20))
login_label1.place(x=50, y=45)

login_entry1=customtkinter.CTkEntry(master=login_frame1, width=320, placeholder_text='Email')
login_entry1.place(x=50, y=165)

login_entry2=customtkinter.CTkEntry(master=login_frame1, width=320, placeholder_text='Password', show="*")
login_entry2.place(x=50, y=220)

login_label2=customtkinter.CTkLabel(master=login_frame1, text="Forget password?",font=('Century Gothic',12))
login_label2.place(x=155,y=255)

#Create custom button
login_bttn1 = customtkinter.CTkButton(master=login_frame1, width=320, text="Login", command=button_function, corner_radius=6)
login_bttn1.place(x=50, y=300)


login_img1=customtkinter.CTkImage(Image.open("Google__G__Logo.svg.webp").resize((20,20), Image.ANTIALIAS))
login_img2=customtkinter.CTkImage(Image.open("124010.png").resize((20,20), Image.ANTIALIAS))
login_bttn2= customtkinter.CTkButton(master=login_frame1, image=login_img1, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
login_bttn2.place(x=50, y=350)

login_bttn3= customtkinter.CTkButton(master=login_frame1, image=login_img2, text="Facebook", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
login_bttn3.place(x=270, y=350)



#REGISTER AREA
frame=customtkinter.CTkFrame(master=app_label1, width=420, height=460, corner_radius=15)
frame.place(relx=0.7, rely=0.5, anchor=tkinter.W)

l2=customtkinter.CTkLabel(master=frame, text="Register your Account",font=('Century Gothic',20))
l2.place(x=50, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=320, placeholder_text='Faculty ID')
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=320, placeholder_text='Email')
entry2.place(x=50, y=165)

entry3=customtkinter.CTkEntry(master=frame, width=320, placeholder_text='Password', show="*")
entry3.place(x=50, y=220)

l3=customtkinter.CTkLabel(master=frame, text="You don't have account? REGISTER NOW!",font=('Century Gothic',12))
l3.place(x=50,y=255)

#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=320, text="Sign UP", command=button_function2, corner_radius=6)
button1.place(x=50, y=300)






# You can easily integrate authentication system 

app.mainloop()
