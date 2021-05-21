from flask import Flask, render_template

app = Flask(__name__)
print(app.config)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def get():
    return '哈哈哈哈'


if __name__ == '__main__':
    app.run()