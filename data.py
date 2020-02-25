from flask import Flask, render_template, request,url_for,make_response,redirect
import sqlite3 as sqlite3
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route("/add")  
def add():  
    return render_template("add.html")

@app.route('/saveusr',methods= ['POST', 'GET'])
def saveusr():
   msg="msg"
   if request.method == 'POST':
      try:
         username=request.form["username"]
         password=request.form["password"]
         
         with sqlite3.connect("database.db") as con:
            cur=con.cursor()
            cur.execute("INSERT into saves(username,password) VALUES(?,?)",(username,password))
            con.commit()
            msg="Recorded successfully"

      

      finally:
       return render_template("aftlog.html")
       con.close()    

@app.route('/savedetails',methods = ['POST', 'GET'])
def saveDetails():
   msg="msg"
   if request.method == 'POST':
      try:
         name = request.form["name"]
         lastNme = request.form["lastNme"]
         city = request.form["city"]
         country = request.form["country"]
         
         with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT into users (name,lastNme,city,country)"
               "VALUES (?,?,?,?)",(name,lastNme,city,country) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("success.html")
         con.close()

@app.route('/about',methods=['GET'])
def about():
    
     return render_template('about.html')

@app.route('/faq',methods=['GET'])     
def faq():
    
     return render_template('faq.html')
@app.route('/userview')
def userview():
   con=sqlite3.connect("database.db")
   con.row_factory=sqlite3.Row
   cur=con.cursor()
   cur.execute("select * from saves")

   rows=cur.fetchall()
   return render_template("userview.html",rows= rows)

@app.route('/view')
def list():
   con = sqlite3.connect("database.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from users")
   
   rows = cur.fetchall()
   return render_template("view.html",rows = rows)

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('aftlog'))
    return render_template('login.html', error=error)

@app.route('/aftlog')
def aftlog():
   return render_template('aftlog.html')


@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("database.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from users where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg)  



if __name__ == '__main__':
   app.run(debug = True)

