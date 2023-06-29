import pyrebase
import customtkinter as ctk

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

root = ctk.CTk()
root.title('Property Transfer | Edit Items')
root.geometry("{0}x{1}+350+50".format(700,525))
root.resizable(False, False)

report_scroll_frame = ctk.CTkScrollableFrame(root, fg_color='white', height=560)
report_scroll_frame.pack(fill = 'both')
item_db = db.child("items_info").order_by_child("DETECT").equal_to("TRUE").get()
for dt in item_db.each():
        
        frame = ctk.CTkFrame(report_scroll_frame, fg_color='#313131', height=50, width=300, corner_radius=0)
        frame.pack(fill = 'y', side='top', pady=(5,0))
        frame2 = ctk.CTkFrame(frame, fg_color='#313131', width=100, corner_radius=0)
        frame2.pack(side='left')
        label = ctk.CTkLabel(frame2, text = dt.val()['NO'], font= ctk.CTkFont('Arial', size = 25, weight = "bold"), text_color='white')
        label.pack(side = 'left',  pady = 15, padx = 15)
       


root.mainloop()     