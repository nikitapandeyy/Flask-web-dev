#creating A Minimal Application
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/products')
def products():
    return 'this is a product'

#creating main file to run
if __name__=="__main__":
  app.run(host='0.0.0.0', port=5000,debug=True)