from flask import Flask
from square import Square

app = Flask(__name__)
@app.route('/')
def index(name = 'student'):
  return "welcome {} to akirachix".format(name)

@app.route('/welcome/<name>')
def welcome(name = 'student'):
  return "welcome {} to akirachix".format(name)

@app.route("/square/<int:length>/<int:width>")
@app.route("/square/<float:length>/<float:width>")
@app.route("/square/<float:length>/<int:width>")
@app.route("/square/<int:length>/<float:width>")
def square (length = 0, width=0):
  squ = Square( length,width) 
  return "Area of Square is {}".format(squ.area()) 

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)


from flask import Flask
from circle import Circle
app = Flask(__name__)

@app.route("/circle/<int:radius>/<int:diameter>")
@app.rout("/circle/<float:radius>/<float:diameter>")
@app.route("/circle/<float:radius>/<int:diameter>")
@app.route("/circle/<int:radius>/<float:diameter>")

def circle (radius = 0, diameter= 0):
  cir = Circle( radius,diameter) 
  return "Area of Circle is {}".format(cir.area()) 

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)


from flask import Flask
from rectangle import Rectangle
app = Flask(__name__)

@app.route("/rectangle/<int:length>/<int:width>")
@app.route("/rectangle/<float:length>/<float:width>")
@app.route("/rectangle/<float:length>/<int:width>")
@app.route("/rectangle/<int:length>/<float:width>")
def rectangle (length = 0, width= 0):
  rec = Rectangle( length,width) 
  return "Area of rectangle is {}".format(rec.area()) 

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)


from flask import Flask
from square import Square
app = Flask(__name__)

@app.route("/triangle/<int:length>/<int:width>")
@app.route("/triangke/<float:length>/<float:width>")
@app.route("/triangle/<float:length>/<int:width>")
@app.route("/triangle/<int:length>/<float:width>")
def triangle (length = 0, width=0):
  tri = Triangle( length,width) 
  return "Area of Triangle is {}".format(tri.area()) 

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)





