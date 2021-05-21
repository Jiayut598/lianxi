from flask import Flask, views, url_for
from werkzeug.routing import BaseConverter

# 正则匹配url

app = Flask(import_name=__name__)


class RegexConverter(BaseConverter):
    '''
    自定义匹配正则表达式
    '''

    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        val = super(RegexConverter, self).to_url(value)
        return val


app.url_map.converters['regex'] = RegexConverter


@app.route('/index/<regex("\d+"):nid>')
def index(nid):
    print(url_for("index", nid='888'))
    return "Index"


if __name__ == '__main__':
    app.run(port=5001)
