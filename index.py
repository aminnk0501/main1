import email
from multiprocessing import connection
from pydoc import render_doc
import sqlite3
from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def index():
    return 'messege'


@app.route('/mylog')
def mylog():
    return render_template('mylog.html')


@app.route('/save' ,methods=['POST'])
def savedata():
    if request.method=='POST':
        email=request.form['email']
        address=request.form['add1']
        address2=request.form['add2']
        city=request.form['city']
        state=request.form['state']
        zip=request.form['zip']
        message=request.form['msg']
        with sqlite3.connect('employee.db') as con:
            cur=con.cursor()
            cur.execute('insert into emp(address,address2,email,city,zip,state,message) values(?,?,?,?,?,?,?)',(address,address2,email,city,zip,state,message))
            con.commit()
    return "saved"

@app.route('/empview')
def empview():
    con=sqlite3.connect('employee.db')
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute('select * from emp')
    aa=cur.fetchall()
    return render_template('empview.html',x=aa)




if __name__ == '__main__':
    app.run(debug=True)