from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


# 使用的是flask_student库  student表 建表语句为

# create table student(
# id int primary key auto_increment,
# name varchar(255) not null,
# sex varchar(255) check(sex='男' or sex='女'),
# python int(20) not null,
# linux int(20) not null,
# shell int(20) not null
# );

def get_mysql():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='pymysql',
        password='123',
        db='flask_student',
        charset='utf8'
    )
    cursor = conn.cursor()
    return conn, cursor


def close_mysql(conn, cursor):
    if conn:
        conn.close()
    if cursor:
        cursor.close()


@app.route('/')
def hh():
    return render_template('student_login.html')




@app.route('/stu', methods=['GET', 'POST'])
def stu():
    num = request.form.get('use')
    if int(num) == 1:
        return render_template('add.html')
    elif int(num) == 2:
        return render_template('del.html')
    elif int(num) == 3:
        return render_template('update.html')
    elif int(num) == 4:
        return render_template('select.html')
    elif int(num) == 5:
        return render_template('show.html')
    else:
        return "hahaha"


@app.route('/add', methods=['POST', 'GET'])
def add():
    conn, cursor = get_mysql()
    name = str(request.form.get('add_name'))
    sex = str(request.form.get('add_sex'))
    python = int(request.form.get('add_python'))
    linux = int(request.form.get('add_linux'))
    shell = int(request.form.get('add_shell'))
    print(name, shell, sex, linux, python)
    sql = "insert into student(name,sex,python,linux,shell) values(%s,%s,%s,%s,%s);"
    cursor.execute(sql, (name, sex, python, linux, shell))
    conn.commit()
    conn.close()
    cursor.close()
    return render_template('student_login.html')


@app.route('/del', methods=['POST', 'GET'])
def deal():
    conn, cursor = get_mysql()
    old_id = request.form.get('del_name')
    print(old_id)
    sql = 'delete from student where id = (%s);'
    cursor.execute(sql, old_id)
    conn.commit()
    conn.close()
    cursor.close()
    return render_template('student_login.html')


@app.route('/select', methods=['POST', 'GET'])
def select():
    conn, cursor = get_mysql()
    select_id = request.form.get('select_name')
    print(select_id)
    sql = 'select id,name,sex,python,linux,shell from student where id = (%s);'
    cursor.execute(sql, select_id)
    a = cursor.fetchall()
    conn.commit()
    for n in a:
        student_id = n[0]
        student_name = n[1]
        student_sex = n[2]
        student_python = n[3]
        student_linux = n[4]
        student_shell = n[5]
    conn.close()
    cursor.close()
    return render_template('student_login.html', student_id=student_id, student_name=student_name, student_sex=student_sex,
                           student_python=student_python, student_linux=student_linux, student_shell=student_shell)


@app.route('/update', methods=['POST', 'GET'])
def update():
    conn, cursor = get_mysql()
    update_id = request.form.get('update_id')
    update_name = request.form.get('update_name')
    update_sex = request.form.get('update_sex')
    update_python = request.form.get('update_python')
    update_linux = request.form.get('update_linux')
    update_shell = request.form.get('update_shell')
    print(update_id, update_name, update_sex, update_python, update_linux, update_shell)
    sql = 'update student set name=(%s),sex=(%s),python=(%s),linux=(%s),shell=(%s) where id =(%s);'
    cursor.execute(sql, (update_name, update_sex, update_python, update_linux, update_shell, update_id))
    conn.commit()
    conn.close()
    cursor.close()
    return render_template('student_login.html')


@app.route('/show', methods=['POST', 'GET'])
def show():
    conn, cursor = get_mysql()
    sql = 'select * from student;'
    cursor.execute(sql)
    a = cursor.fetchall()
    print(a)
    return render_template('show.html', datas=a)


if __name__ == '__main__':
    app.run(debug=True)
