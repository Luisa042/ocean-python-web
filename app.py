from flask import Flask

app = Flask('hey')

@app.route('/')
def hello():
    return 'hello world'