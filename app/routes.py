from flask import Flask,jsonify, render_template,send_from_directory,request
from bs4 import BeautifulSoup
import json
import requests

app = Flask(__name__,static_folder='static')

def result(k):
  r = requests.get(k)
  soup = BeautifulSoup(r.content,"html.parser")
  k = soup.find_all("table")
  fhandle = open('templates/text.html',"w",encoding='utf-8')
  fhandle.write("<html encoding='UTF-8'>")
  #fhandle.write(str(k[1]))
  fhandle.write(str(k[2]))
  fhandle.write(str(k[3]))
  fhandle.write(str(k[4]))
  fhandle.write("</html>")
  fhandle.close()

 @app.route('/')
def home():
  return render_template('home.html')

@app.route('/about',methods=['POST'])
def about():
  if request.method == 'POST':
    usn = request.form.get('usnvalue')
    context = {'usn':usn}
    result('http://results.vtualerts.com/get_res.php?usn='+usn)
  return render_template('about.html',**context)

if __name__ == '__main__':
  app.run(debug=False)
