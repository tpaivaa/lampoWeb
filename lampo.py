from flask import Flask
import lammot as l
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!\n Kaikkea soopaa'

@app.route('/lampo')
def lampotila():
    lampotila = l.getlampotila()
    return lampotila

@app.route('/soile')
def soileLenkit():
    soile = l.getsoile()
    return soile


if __name__ == '__main__':
    app.run(host='localhost')
