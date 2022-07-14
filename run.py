from flask import Flask
app = Flask(__name__)

#This file will run and return our application

@app.route('/')
def main():
    return "Python Instagram Analyzer"

if __name__ == '__main__':
    app.run()