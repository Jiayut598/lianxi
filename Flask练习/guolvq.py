from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/show')
def show():
    girls = ['11', '222', '33', '444', '55']
    users = [
        {'username': '张三1', 'password': '111', 'addr': '北京', 'phone': '10086'},
        {'username': '张三2', 'password': '222', 'addr': '上海', 'phone': '10086'},
        {'username': '张三3', 'password': '333', 'addr': '广州', 'phone': '10086'},
        {'username': '张三4', 'password': '444', 'addr': '深圳', 'phone': '10086'},
        {'username': '张三5', 'password': '555', 'addr': '曹县', 'phone': '10086'}
    ]
    girls.append('zhangsan')
    msg = '<h1>快乐</h1>'
    n1 = 'hello world'
    return render_template('guolvq.html', girls=girls, users=users, msg=msg, n1=n1)


if __name__ == '__main__':
    app.run(debug=True)
