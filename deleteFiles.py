import urllib.request
import json
import time
import sys

# limit を適宜変更のこと
#urlget = "http://10.178.1.27:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
urlget = "http://10.178.1.27:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
# 録画一覧を得る
response = urllib.request.urlopen(urlget)
jsonData = json.load(response)
delteFlag=False
input_data = sys.argv[1:]
print("input is ", input_data)
if input_data[0]=="1":
    delteFlag=True

def main():
    # 録画ごとにループ
    if delteFlag:
        print("不要ファイルを本当に削除します...")
        time.sleep(3)

    for jsonObj in reversed(jsonData["records"]):
        # "videoFilesを取り出し
        recordid=jsonObj["id"]
        #print("recordid:",recordid)
        if not jsonObj["videoFiles"]:
            print("recordid:",recordid,"filename:",jsonObj["name"])
            print("これファイルないね、消します")
            if delteFlag:
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
                print("\n")
            
if __name__ == "__main__":
	main()