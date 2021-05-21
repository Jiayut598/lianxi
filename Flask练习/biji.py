from flask import Flask, url_for,request,make_response,render_template

app = Flask(__name__)

# 动态路由
# 接受string
# @app.route('/<name>')
# def first_flask(name):
#     print(name)
#     return name

# 接受int
# @app.route('/<int:age1>/<int:age2>')
# def a(age1,age2):
#     print(age1+age2)
#     return "age"

# 接受小数
# @app.route('/<float:salary>')
# def a(salary):
#     print(salary)
#     return "hello world"

# 接受url链接
# @app.route('/<path:url>')
# def a(url):
#     print(url)
#     return "url"


# 通过别名反向生成url
# @app.route('/<path:url>',endpoint='name1')
# def a(url):
#     print(url_for('name1',url=url))
#     return "hello"


# 通过app.add_url_rule()调用路由
# def first():
#     return "hello first"
#
# app.add_url_rule(rule='/index/',endpoint='name1',view_func=first,methods=['GET'])


@app.template_global()
def foo(arg):
    return '<input type="text">'


if __name__ == '__main__':
    app.run(debug=True)
