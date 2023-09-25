from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import mysql.connector
#from mysql.connector import error

app = Flask(__name__)

# Configure the Flask app
app.config['SECRET_KEY'] = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# User model
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username


@login_manager.user_loader
def load_user(user_id):
    # Replace with your database connection details
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Root@123',
            database='vps'
        )

        cursor = connection.cursor()
        cursor.execute("SELECT id, username FROM user WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            return User(user_data[0], user_data[1])
    except error.DatabaseError as e:
        print("Database connection error:", e)
    finally:
        cursor.close()
        connection.close()


# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
