from unittest import result
from flask import Flask, render_template,request,redirect, jsonify
#import connector
import mysql.connector

#establish connectin
conn=mysql.connector.connect(host='localhost',user='root',password='',database='proj')

#resposible for data send and recive
cursor=conn.cursor()

#object:__name__ current filename
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
    

@app.route('/getdata')
def getdata():
    name=request.args['name']
    email=request.args['email']
    Password=request.args['Password']
    mobile=request.args['mobile']
    #query
    que="INSERT INTO users VALUES(NULL,%s,%s,%s,%s)"
    #exicution of query
    cursor.execute(que,(name,email,Password,mobile))

    conn.commit()

    return redirect('/showdata')


@app.route('/showdata')
def showdata():
    query = "SELECT * FROM users WHERE id= id"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    return jsonify(result)

@app.route('/delete')
def delete():
    user_id=request.args['id']
    q="DELETE FROM users WHERE id="+user_id
    cursor.execute(q)
    conn.commit()
    return redirect('/showdata')

@app.route('/edit')
def edit():
    user_id=request.args['id']
    q="SELECT * FROM users WHERE id="+user_id
    cursor.execute(q)
    result=cursor.fetchone()
    return render_template('/edit.html', data=result)

@app.route('/update')
def update():
    id=request.args['id']
    name=request.args['name']
    email=request.args['email']
    Password=request.args['Password']
    mobile=request.args['mobile']
    #query
    que="UPDATE users SET name=%s, email=%s, password=%s, mobile=%s WHERE id=%s"
    #exicution of query
    cursor.execute(que,(name,email,Password,mobile,id))

    conn.commit()

    return redirect('/showdata')
        

#run flask
app.run(debug=True)