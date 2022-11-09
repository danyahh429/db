from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/temp')
def index():
   return render_template('index.html')

@app.route('/view')
def view():
   return render_template('view.html')

@app.route('/demo')
def demo():
   return render_template('demo.html')

if __name__ == '__main__':
   app.run()