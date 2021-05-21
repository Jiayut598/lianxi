from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/show')
def show():
    girls = ['梁先', '贾娜', '郭越', '王冉', '郝育娇']
    users = [
        {'username': '张三1', 'password': '111', 'addr': '北京', 'phone': '10086'},
        {'username': '张三2', 'password': '222', 'addr': '上海', 'phone': '10086'},
        {'username': '张三3', 'password': '333', 'addr': '广州', 'phone': '10086'},
        {'username': '张三4', 'password': '444', 'addr': '深圳', 'phone': '10086'},
        {'username': '张三5', 'password': '555', 'addr': '曹县', 'phone': '10086'}
    ]
    return render_template('One.html', girls=girls, users=users)


if __name__ == '__main__':
    app.run(debug=True)
