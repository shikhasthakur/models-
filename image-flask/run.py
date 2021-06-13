from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('k.html')


@app.route('/home')
def ram():
   return render_template('result.html')

if __name__ == '__main__':
   app.run(debug = True)
