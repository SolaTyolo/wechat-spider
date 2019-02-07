from flask import Flask
import wechatsogou
import json

app = Flask(__name__)

@app.route('/search/<attribute>' , methods=['GET'])
def hello_world(attribute):
    ws_api =wechatsogou.WechatSogouAPI()
    infoList = ws_api.search_article(attribute)
    return json.dumps(infoList , ensure_ascii=False)

if __name__ == '__main__':
    app.run()