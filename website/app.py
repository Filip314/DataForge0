from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) #intialize the app

conn = sqlite3.connect('database.db') #create a database file
conn.execute('''
        CREATE TABLE IF NOT EXISTS offers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            details TEXT NOT NULL
        )
''')

def get_software(i): # Returns software in the i-th row from database.db
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT details FROM offers LIMIT 1 OFFSET ?", (i,))
        software = cursor.fetchone()
        if software:
            return software[0]
        else:
            return "No more software waiting to be added"


@app.route('/', methods=['GET', 'POST'])
def home(): #main function on HTML GET request
    if request.method == 'POST': #If POST request from the user:
        full_name = request.form['real_name'] #Save user input in variables
        email = request.form['email']
        details = request.form['details']
        conn = sqlite3.connect('database.db') #open the database file
        conn.execute('INSERT INTO offers (full_name, email, details) VALUES (?, ?, ?)', (full_name, email, details)
        ) #write saved user inputs into the database
        conn.commit()
    return render_template('index.html') #Show the website html NOTE: Interchangible: index.html(stable version), new_index_unstable.html(newer possibly unstable version)

@app.route('/documents')
def docs():
    return render_template('documents.html')

@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/other_software')
def other_software():
    return render_template('other_software.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/waiting-list', methods=['GET', 'POST'])
def waitingList():
     
    return render_template('waiting_list.html', software1=get_software(0), software2=get_software(1), software3=get_software(2), software4=get_software(3), software5 = get_software(5)) #renders the waiting list

@app.route('/cart/')
def shoppingCart():
    return render_template('shopping_cart.html')

app.run()
