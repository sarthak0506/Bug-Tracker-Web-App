from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB = 'bug_tracker.db'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS issues (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'Open',
                    priority TEXT DEFAULT 'Medium',
                    assignee TEXT,
                    date TEXT
                )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM issues ORDER BY id DESC")
    issues = c.fetchall()
    conn.close()
    return render_template('index.html', issues=issues)

@app.route('/add', methods=['GET', 'POST'])
def add_issue():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['description']
        priority = request.form['priority']
        assignee = request.form['assignee']
        date = datetime.now().strftime('%Y-%m-%d')
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO issues (title, description, priority, assignee, date) VALUES (?, ?, ?, ?, ?)",
                  (title, desc, priority, assignee, date))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_issue.html')

@app.route('/update/<int:id>/<status>')
def update_status(id, status):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE issues SET status=? WHERE id=?", (status, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_issue(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM issues WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
