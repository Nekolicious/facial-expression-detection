from flask import Flask, render_template
import scan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan/')
def scanface():
    scan.scanExp()
    return render_template('index.html')

@app.route('/test/')
def test():
    print('Click!')
    return 'Clicked boy!'

if __name__ == '__main__' :
    app.run(debug=True)