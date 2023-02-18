import urllib.request
import json
import time

# limit を適宜変更のこと
#urlget = "http://10.178.1.27:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
urlget = "http://100.118.14.25:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
# 録画一覧を得る
response = urllib.request.urlopen(urlget)
jsonData = json.load(response)
# 録画ごとにループ
for jsonObj in jsonData["records"]:
    # "videoFilesを取り出し
    flagEncoded=False
    flagTs=False
    recordid=jsonObj["id"]
    for videoFileObj in jsonObj["videoFiles"]:
      if ("encoded" == videoFileObj["type"]):
          flagEncoded=True
          #sizeEncoded=videoFileObj["size"]
      if ("ts" == videoFileObj["type"]):
          flagTs=True
          idTs=videoFileObj["id"]
          nameTs=videoFileObj["filename"]
    if (False==flagEncoded and True==flagTs):
    # "videoFiles":"type":"encoded"が存在しなくて "type":"ts"がある場合
      print("recordid:",recordid,"idTs:",idTs,nameTs)

