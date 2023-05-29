from flask import Flask,request,render_template
from flask_mysqldb import MySQLdb

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'shaikfarjana7777.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'shaikfarjana7777'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aspen123'
app.config['MYSQL_DATABASE_NAME'] = 'shaikfarjana7777$student'

db = MySQLdb.connect(app.config['MYSQL_DATABASE_HOST'], app.config['MYSQL_DATABASE_USER'], app.config['MYSQL_DATABASE_PASSWORD'], app.config['MYSQL_DATABASE_NAME'])

@app.route('/get_word')
def get_word():
    cursor = db.cursor()
    cursor.execute('SELECT word FROM words')
    word = cursor.fetchone()[0]
    return word
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin', methods=['POST'])
def admin_post():
    u_word = request.form.get('word')
    cursor = db.cursor()
    update_query = "UPDATE words SET word = %s WHERE id = %s"
    cursor.execute(update_query,(u_word,1))
    db.commit()
    return u_word
    #return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)



