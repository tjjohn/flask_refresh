from flask import Flask,url_for,redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/1')
def page1():
   return " you are in page1"


@app.route('/2')
def page2():
   return "you are in page2"

@app.route('/3/<int:va1>')
def int_value_fun(va1):
   return "you are in "+str(va1)+"page"

@app.route('/random/<int:va>')
def urlbindfun(va):
   if va==1:
      return redirect(url_for("page1"))
   elif(va==2):
      return redirect(url_for("page2"))
   else:
      return redirect(url_for("int_value_fun",va1=va))


if __name__ == '__main__':
   app.run()