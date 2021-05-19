import os

student_version = """
    ===============学生信息管理系统===============
    ------------------功能菜单------------------
    1.添加学生
    2.删除学生
    3.修改学生信息
    4.查询学生信息
    5.显示所有学生信息
    6.退出
    请输入1-6管理系统
    ------------------------------------------
    ===========================================
"""
filename = 'student.txt'
student_list = []
print(student_list)


def student_add():
    while True:
        print("增加学生")
        id = int(input('请输入ID'))
        if not id:
            break
        name = str(input('请输入学生姓名'))
        if not name:
            break
        try:
            age = int(input("请输入学生年龄"))
            sex = str(input("请输入学生性别"))
        except:
            print('输入无效')
            continue
        # 将信息保存到字典
        student = {'id': id, 'name': name, 'age': age, 'sex': sex}
        # 将信息添加到列表
        student_list.append(student)
        answer = str(input('是否继续添加 y/n\n'))
        if answer == 'y' or answer == 'Y':
            continue
        elif answer == 'n' or answer == 'N':
            print('添加成功')
            save()
            break
        else:
            print('输入无效')


def save():
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in student_list:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def student_del():
    while True:
        del_id = int(input('请输入要删除学生的id'))
        if del_id != '':
            # 判断文件是否存在
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            # 标记是否删除
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        # 字符串转字典
                        d = dict(eval(item))
                        if d['id'] != del_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{del_id}的学生被删除')
                    else:
                        print(f'没有找到id为{del_id}的学生')
            else:
                print('无学生信息')
                break
            student_show()
            answer = input('是否继续删除y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def student_alter():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
    else:
        return
    alter_id = int(input('请输入要修改学生的id'))
    if alter_id != '':
        with open(filename, 'w', encoding='utf-8') as wfile:
            for item in student_old:
                d = dict(eval(item))
                if d['id'] == alter_id:
                    print('找到学生信息开始修改')
                    # 找到学生信息
                    while True:
                        try:
                            d['name'] = input('请输入学生的姓名')
                            d['age'] = input('请输入学生的年龄')
                            d['sex'] = input('请输入学生的性别')
                            wfile.write(str(d) + '\n')
                            print('修改成功')
                            answer = input('是否继续修改其他学生信息' + '\n')
                            if answer == 'y' or answer == 'Y':
                                student_alter()
                            else:
                                break
                        except:
                            print('输入有误请重新输入')
                else:
                    wfile.write(str(d) + '\n')
    else:
        print('输入无效')


def student_select():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
    else:
        return
    alter = int(input('请输入要查询学生的ID'))
    if alter != '':
        with open(filename, 'r', encoding='utf-8') as wfile:
            for item in student_old:
                d = dict(eval(item))
                if d['id'] == alter:
                    print('学生名字为' + d['name'])
                    print('学生年龄为' + str(d['age']))
                    print('学生性别为' + d['sex'])
                else:
                    print('输入错误')


def student_show():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
    else:
        return
    print('开始查询学生信息')
    with open(filename, 'r', encoding='utf-8')as rfile:
        for item in student_old:
            d = dict(eval(item))
            print('学生名字为' + d['name'])
            print('学生年龄为' + str(d['age']))
            print('学生性别为' + d['sex'])


def student_exit():
    print("退出学生管理系统")


def main():
    while True:
        print(student_version)
        choice = int(input('输入1-6管理系统'))
        if choice == 1:
            student_add()
        elif choice == 2:
            student_del()
        elif choice == 3:
            student_alter()
        elif choice == 4:
            student_select()
        elif choice == 5:
            student_show()
        elif choice == 6:
            student_exit()
            break
        else:
            print("你输入的值不在1-6 请重新输入")


if __name__ == '__main__':
    main()
