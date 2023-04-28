import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./env/kgan.json')

#Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://puplopez-ptp-default-rtdb.firebaseio.com'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
#database = db.reference('restricted_access/secret_document')


from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic5():
    if request.method == 'POST':
        
        if request.form['submit'] == 'signup':
            email = request.form['email']
            pw = request.form['pw']
            
            # Get a database reference to our blog.
            database = db.reference('users_info')
            users_ref = database.child(pw)
            users_ref.set({
                "Email": email,
                "Pw": pw
            })
           
            return render_template('main.html')
            
        elif request.form['submit'] == 'add':
            name = request.form['name']
            id = request.form['id']

                
            # Get a database reference to our blog.
            database = db.reference('users_info')
            users_ref = database.child(id)
            users_ref.set({

                "NAME": name,
                "ID": id
            })
           
            return render_template('main.html', t= database.get())
        elif request.form['submit'] == 'delete':
            
             id = request.form['id']
             database = db.reference('users_info')
             users = database.child(id)
             users.delete()
             return render_template('main.html', t= database.get() )
             
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)