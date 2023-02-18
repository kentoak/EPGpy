import urllib.request
import json
import time
from pprint import pprint
import os

# limit を適宜変更のこと
urlget = "http://10.178.1.27:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
#urlget = "http://100.118.14.25:8888/api/recorded?isHalfWidth=false&offset=0&limit=10000"
response = urllib.request.urlopen(urlget)
jsonData = json.load(response)

dirPath="/mnt/hdd1/"
#dirPath="/Users/kt/mountpoint1/"
delteFlag=False

def deleteFile(url):
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

for jsonObj in reversed(jsonData["records"]):
    # "videoFilesを取り出し
    flagEncoded=False
    flagMp4s=False
    recordid=jsonObj["id"]
    print("\nrecordid:",recordid,"...",jsonObj["name"])
    #pprint(jsonObj["videoFiles"])
    for videoFileObj in jsonObj["videoFiles"]: 
        if videoFileObj["filename"]:
            filename=videoFileObj["filename"]
            _, file_extension = os.path.splitext(filename)
        if videoFileObj["type"]:
            type=videoFileObj["type"]

        print(filename,"はrecordedにある？",os.path.exists(dirPath+filename))
        if type=="ts" and file_extension==".mp4": #filenameがmp4なのにtypeが'ts'になっているものは削除
            print("形式が違います。これ削除ね")
            #url="http://100.118.14.25:8888/api/videos/:"+videoFileObj["id"]
            url="http://10.178.1.27:8888/api/videos/"+str(videoFileObj["id"])
            if delteFlag:deleteFile(url)
        
        if type=="encoded" and file_extension==".ts": #filenameがtsなのにtypeが'encoded'になっているものは削除
            print("形式が違います。これ削除ね")
            #url="http://100.118.14.25:8888/api/videos/:"+videoFileObj["id"]
            url="http://10.178.1.27:8888/api/videos/"+str(videoFileObj["id"])
            if delteFlag:deleteFile(url)
            
        if type=="ts" and not os.path.exists(dirPath+filename): #recordedにtsファイルがないのにtsをもっているものは削除
            print("tsファイルはrecordedにありません。削除ね")
            #url="http://100.118.14.25:8888/api/videos/:"+videoFileObj["id"]
            url="http://10.178.1.27:8888/api/videos/"+str(videoFileObj["id"])
            if delteFlag:deleteFile(url)
        #sizeEncoded=videoFileObj["size"]
