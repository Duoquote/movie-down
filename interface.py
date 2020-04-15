import sys, json, re, requests
from puhu import getPlist
from bs4 import BeautifulSoup

pageID = re.search(r"item_id: ?\"(?P<id>\d+)\"", requests.get("https://puhutv.com/yabanci-filmler").text).groupdict()["id"]
endpoint = "https://puhutv.com/ajax/widget/render?cms_design_widget_id=4121&content_pool_id_page_no={}&info_item_id={}"
i = 1
mov = []
current = 0
total = 0
while True:
    pageData = BeautifulSoup(requests.get(endpoint.format(i, pageID)).text, "html.parser")
    elems = pageData.find("div", {"class": "category-main-content-right"}).find_all("li")
    if not total:
        total = int(re.search(r"^(?P<count>\d+?) ", pageData.find_all("h2")[-1].text).groupdict()["count"])
    for elem in elems:
        curMov = {}
        curMov["url"] = elem.find("a").attrs["href"]
        curMov["label"] = elem.find("div", {"class": "name"}).text
        mov.append(curMov)
    current += len(elems)
    if current >= total:
        break
    i += 1

i = 0
for movie in mov:
    print("[{}] {}".format(i, movie["label"]))
    i += 1
print("Film id sini seciniz: ", end="")
film = int(input())

pList = getPlist(mov[film]["url"])

for i in pList:
    fileName = mov[film]["url"][1:] + "-" + i + ".m3u8"
    ffmpegCMD = "ffmpeg -protocol_whitelist file,https,tls,tcp -i {} {}.mkv"
    with open(fileName, "w", encoding="utf-8") as f:
        f.write(pList[i])
        print("Film: [{}]".format(mov[film]["label"]))
        print("Kalite '{}', [{}] adı ile dosyaya kaydedildi.".format(i, fileName))
        print("FFMPEG Komutu:")
        print(ffmpegCMD.format(fileName, fileName.split(".")[0]))
        print("--------------------------------------")

#getPlist("/ejderha-gozler-izle")
