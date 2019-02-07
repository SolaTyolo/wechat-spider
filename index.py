import wechatsogou

ws_api =wechatsogou.WechatSogouAPI()
infoList = ws_api.search_article('南京')

print(infoList)