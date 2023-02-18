import urllib.request
import json
import time
from pprint import pprint

# limit を適宜変更のこと
#urlget = "http://10.178.1.27:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
urlget = "http://100.118.14.25:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
# 録画一覧を得る
response = urllib.request.urlopen(urlget)
jsonData = json.load(response)
# 録画ごとにループ
for jsonObj in reversed(jsonData["records"]):
    # "videoFilesを取り出し
    flagEncoded=False
    flagMp4s=False
    recordid=jsonObj["id"]
    print("\nrecordid:",recordid)
    pprint(jsonObj["videoFiles"])
