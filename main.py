from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app=Flask(__name__)

#app.config['SQLALCHEMY_DATABSE_URI']='mysql://root:@localhost/narvis'
#db=SQLAlchemy(app)

'''class devices(db.Model):
    Xiaomi=db.Column(db.String(50),primary_key=True)
    Asus=db.Column(db.String(50),nullable=False)
    Realme=db.Column(db.String(50),nullable=False)
    Motorola=db.Column(db.String(50),nullable=False)'''

host='localhost'
user = 'root'
password = ''
db = 'narvis'

@app.route("/")

def index ():
    return render_template('index.html')


@app.route("/devices/",methods=['GET'])

def devices() :
    con = pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')
    cur = con.cursor()
    cur.execute("SELECT * FROM device")
    device = cur.fetchall()
    return render_template('devices.html', device=device)
app.run(debug=True)  





