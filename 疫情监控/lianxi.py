import requests
import json
import csv
import pymysql


def li():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    d = json.loads(data)
    # print(d)

    data_all = json.loads(d['data'])
    details = []
    update_time = data_all['lastUpdateTime']
    data_country = data_all['areaTree']
    data_province = data_country[0]['children']
    with open('疫情.csv', 'w+', encoding='utf-8') as fp_csv:
        writer = csv.writer(fp_csv, delimiter=',')
        sheet_title = ['更新时间', '省', '市', '确诊', '新增', '治愈', '死亡']
        writer.writerow(sheet_title)
        for pro_infos in data_province:
            province = pro_infos['name']
            for cicy_infos in pro_infos['children']:
                city = cicy_infos['name']
                total = cicy_infos['total']
                confirm = total['confirm']
                today = cicy_infos['today']
                confirm_add = today['confirm']
                heal = total['heal']
                dead = total['dead']
                details.extend([update_time, province, city, confirm, confirm_add, heal, dead])
                # print(update_time, province, city, confirm, confirm_add, heal, dead)
                sheet_data = [(update_time, province, city, confirm, confirm_add, heal, dead)]
                writer.writerows(sheet_data)
                conn = pymysql.connect(
                    host='192.168.1.65',
                    user='pymysql',
                    password='123',
                    db='pythonDB'
                )
                cursor = conn.cursor()
                sql = 'insert into details(update_time, province, city, confirm, confirm_add, heal, dead) values (%s, %s,%s, %s, %s, %s,%s);'
                cursor.execute(sql, (update_time, province, city, confirm, confirm_add, heal, dead))
                conn.commit()
                cursor.close()
                conn.close()


li()
