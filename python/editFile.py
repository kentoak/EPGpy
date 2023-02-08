import urllib.request
import json
import time
from pprint import pprint
import requests

# limit を適宜変更のこと
#urlget = "http://10.178.1.27:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
urlget = "http://10.178.1.27:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
# 録画一覧を得る
response = urllib.request.urlopen(urlget)
jsonData = json.load(response)
# 録画ごとにループ
for jsonObj in reversed(jsonData["records"]):
    # "videoFilesを取り出し
    flagEncoded=False
    flagTs=False
    recordid=jsonObj["id"]
    #print("recordid:",recordid)
    if recordid==529:
        pprint(jsonObj["videoFiles"])
        url="http://10.178.1.27:8888/api/recorded/"+str(recordid)+"?isHalfWidth=true"
        url1="http://10.178.1.27:8888/api/recorded/"+str(recordid)+"?isHalfWidth=true"
        #url1="http://10.178.1.27:8888/api/videos/"+str(recordid)+"?isHalfWidth=true"
        #url1="http://10.178.1.27:8888/api/recorded/"+str(recordid)
        #url1="http://10.178.1.27:8888/api/recorded/detail/"+str(recordid)
        #url1="http://10.178.1.27:8888/api/videos/"+str(recordid)
        #headers = {"Content-Type": "application/json"}
        headers = {"Content-Type": "multipart/form-data"}
        res1=requests.get(url)
        dat=res1.json()
        print(dat)
        dat["name"]="KateDouglass"
        #dat["videoFiles"][0]["name"]="mp4"
        #dat["videoFiles"][0]["type"]="mp4"
        data = urllib.parse.urlencode(dat).encode("utf-8")
        print(dat)
        res=urllib.request.Request(url,data,headers,method="PUT")
        #response = requests.put(url1, json=json.dumps(dat))
        #response = requests.put(url1, json=json.dumps(dat))
        response = requests.put(url1, params=json.dumps(dat))
        print(response.url)
        print(response.text)
        #response = requests.post(url1, json=json.dumps(dat))
        if response.status_code == 200:
            print("データを更新しました")
        else:
            print("エラー：", response.status_code)
        #urllib.request.urlopen(res)
        #res=urllib.request.Request(url,data,headers,method="POST")
        try:
            with urllib.request.urlopen(res) as f:
                pass
            print(f.status,end="")
            if (200==f.status):
                print(" OK",end="")
            else:
                print(" Error",end=" ")
        except urllib.error.HTTPError as err:
            print(" Error",end=" ")
            print(err.code,end=" ")
        except urllib.error.URLError as err:
            print(" Error",end="")
            print(err.reason)

    # for videoFileObj in jsonObj["videoFiles"]:
    #     print(videoFileObj["filename"])
    #     print("id:",videoFileObj["id"],videoFileObj["type"])