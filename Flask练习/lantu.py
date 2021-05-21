from flask import Blueprint

test_zhanggen = Blueprint('oss_api_zhanggen', __name__)


@test_zhanggen.route('/index/', methods=['GET', 'POST'])
def index():
    return "测试/张根/index"


@test_zhanggen.route('/home/', methods=['GET', 'POST'])
def home():
    return "测试/张根/home"


app.register_blueprint(blueprint=api_zhanggen.test_zhanggen, url_prefix='/test/zhanggen')
