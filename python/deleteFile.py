import urllib.request
import json
import time

# limit を適宜変更のこと
#urlget = "http://10.178.1.27:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
urlget = "http://10.178.1.27:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
# 録画一覧を得る
response = urllib.request.urlopen(urlget)
jsonData = json.load(response)
# 録画ごとにループ

def main(recordID):
    for jsonObj in reversed(jsonData["records"]):
        # "videoFilesを取り出し
        flagEncoded=False
        flagTs=False
        recordid=jsonObj["id"]
        print("recordid:",recordid)
        if recordid==recordID:
            print("recordid:",recordid)
            print("これ、消します")
            #url="http://10.178.1.27:8888/api/videos/"+str(recordid)
            url="http://10.178.1.27:8888/api/recorded/"+str(recordid)
            #url="http://10.178.1.27:8888/api/recorded/detail/"+str(recordid)
            headers = {"Content-Type": "application/json"}
            res=urllib.request.Request(url,json.dumps(jsonObj).encode(),headers,method="DELETE")
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

if __name__ == "__main__":
    recordID=input(" recordIDを入力してください: ")
    main(int(recordID))