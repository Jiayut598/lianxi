from flask import Flask, render_template

app = Flask(__name__)


class Girl():
    def __init__(self, name, addr):
        self.name = name
        self.gender = '女'
        self.addr = addr

    def __str__(self):
        return self.name


@app.route('/show')
def show():
    name = '贾毓涛'  # str
    age = 18  # int
    friends = ['one', 'two', 'three', 'four']  # list
    dict1 = {'gift': 'shouzhuo', 'gift1': 'xianhua', 'gift2': 'feilieluo'}  # dict

    # 创建对象
    girlfriend = Girl('Girl1', '安徽')
    return render_template('bianliang.html', name=name, age=age, friends=friends, dict1=dict1, girl=girlfriend)


if __name__ == '__main__':
    app.run(debug=True)
