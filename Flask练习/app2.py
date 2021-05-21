from flask import Flask
# import settings

app = Flask(__name__)
# print(app.config)
# app.config.from_object(settings)

@app.route('/')
def index():
    return '<h1>hello Flask1</h1>'
@app.route('/')
def index1():
    return 'hello Flask2'
@app.route('/')
def index2():
    return 'hello Flask3'

if __name__ == '__main__':
    app.run(port=5001,host='0.0.0.0')
