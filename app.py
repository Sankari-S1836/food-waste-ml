from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Helper function to get DB connection
def get_db_connection():
    conn = sqlite3.connect('pantry.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None  # Initialize error as None

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
                         (name, email, password))
            conn.commit()
            return redirect('/login')
        except sqlite3.IntegrityError:
            error = "Email already exists! ❗"
        finally:
            conn.close()

    return render_template('register.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['name'] = user['name']
            return redirect('/dashboard')
        else:
            return "Invalid login."
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    conn = get_db_connection()
    items = conn.execute('SELECT * FROM pantry_items WHERE user_id = ?', (session['user_id'],)).fetchall()
    conn.close()
    return render_template('dashboard.html', name=session['name'], items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        item_name = request.form['item_name']  # get from form input named 'name'
        quantity = request.form['quantity']
        expiry_date = request.form['expiry_date']

        conn = get_db_connection()
        conn.execute('INSERT INTO pantry_items (item_name, quantity, expiry_date, user_id) VALUES (?, ?, ?, ?)',
                     (item_name, quantity, expiry_date, session['user_id']))
        conn.commit()
        conn.close()

        return redirect('/dashboard')

    return render_template('add.html')

from flask import render_template, session, redirect
from datetime import datetime, timedelta
from database import get_db_connection

@app.route('/view')
def view_pantry():
    if 'user_id' not in session:
        return redirect('/login')

    conn = get_db_connection()
    items = conn.execute('SELECT * FROM pantry_items WHERE user_id = ?', (session['user_id'],)).fetchall()
    conn.close()

    # Add status based on expiry date
    processed_items = []
    for item in items:
        expiry = item['expiry_date']
        today = datetime.today().date()

        # Determine status
        if expiry:
            expiry_date = datetime.strptime(expiry, '%Y-%m-%d').date()
            if expiry_date < today:
                status = 'expired'
            elif (expiry_date - today).days <= 3:
                status = 'expiring-soon'
            else:
                status = 'fresh'
        else:
            status = 'no-expiry'

        # Append with status
        processed_items.append({
            'item_name': item['item_name'],
            'quantity': item['quantity'],
            'expiry_date': expiry,
            'status': status
        })

    return render_template('view.html', items=processed_items)


@app.route('/remove', methods=['GET', 'POST'])
def remove_item():
    if 'user_id' not in session:
        return redirect('/login')

    conn = get_db_connection()
    if request.method == 'POST':
        item_id = request.form['item_id']
        conn.execute('DELETE FROM pantry_items WHERE id = ? AND user_id = ?', (item_id, session['user_id']))
        conn.commit()

    items = conn.execute('SELECT * FROM pantry_items WHERE user_id = ?', (session['user_id'],)).fetchall()
    conn.close()

    return render_template('remove.html', items=items)

@app.route('/update-stocks', methods=['GET', 'POST'])
def update_stocks():
    if 'user_id' not in session:
        return redirect('/login')

    conn = get_db_connection()
    if request.method == 'POST':
        items = conn.execute('SELECT id FROM pantry_items WHERE user_id = ?', (session['user_id'],)).fetchall()

        for item in items:
            field_name = f'update_{item["id"]}'
            new_quantity = request.form.get(field_name)

            if new_quantity is not None:
                if new_quantity.strip() == '' or new_quantity.strip() == '0' or new_quantity.strip().startswith('0 '):
                    # Delete if quantity is 0 or blank
                    conn.execute('DELETE FROM pantry_items WHERE id = ? AND user_id = ?', (item["id"], session['user_id']))
                else:
                    # Update the quantity string directly
                    conn.execute('UPDATE pantry_items SET quantity = ? WHERE id = ? AND user_id = ?', 
                                 (new_quantity.strip(), item["id"], session['user_id']))
        conn.commit()
        conn.close()
        return redirect('/dashboard')

    # GET request
    items = conn.execute('SELECT * FROM pantry_items WHERE user_id = ?', (session['user_id'],)).fetchall()
    conn.close()
    return render_template('update.html', items=items)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
