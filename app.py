from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Used for flash messages

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="course_registration"
    )

# Route: Show Registration Form
@app.route('/')
def index():
    return render_template('index.html')

# Route: Handle Form Submission
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']

    if not name or not email or not phone or not course:
        flash("All fields are required!", "danger")
        return redirect('/')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert data into MySQL
        query = "INSERT INTO students (name, email, phone, course) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, phone, course))

        conn.commit()
        cursor.close()
        conn.close()

        flash("Registration successful!", "success")
    except mysql.connector.Error as e:
        flash(f"Database error: {e}", "danger")

    return redirect('/students')

# Route: Display Registered Students
@app.route('/students')
def students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
