from flask import Flask, url_for

app = Flask(__name__)


# def auth(func):
#     print('在上面')
#     def inner(*args,**kwargs):
#         return func(*args,**kwargs)
#     return inner
#
# @app.route('/',methods=['GET'])
# @auth
# def first():
#     print('ffff')
#     return 'hello world'

@app.route('/')
def one():
    return '''
    <ul>
        <li><a href='/test'>test</a></li>
        <li><a href='/friend'>firend</a></li>
    </ul>
    '''


@app.route('/test')
def two():
    return 'this is test'


@app.route('/friend')
def three():
    return '<h1>this is my friend</h1>'


if __name__ == '__main__':
    app.run()
