import requests, json, re

# https://puhutv.com/ajax/widget/render?cms_design_widget_id=4121&&content_pool_id_page_no=3&exclude_item_ids=&info_item_id=791523&sort=

def getPlist(id):
    infoURL = "https://dygvideo.dygdigital.com/api/video_info?akamai=true&PublisherId=29&ReferenceId={}&SecretKey=NtvApiSecret2014*"
    url = "https://puhutv.com{}".format(id)
    puhuID = re.search(r"'(?P<id>PUHU(_.+?)+)'", requests.get(url).text).groupdict()["id"]
    videoData = json.loads(requests.get(infoURL.format(puhuID)).text)
    videoBase = videoData["data"]["flavors"]["hls"].split("playlist.m3u8")[0]
    m3u8 = [i for i in requests.get(videoData["data"]["flavors"]["hls"]).text.split("\n") if not i.startswith("#")][:-1]
    m3u8 = {re.search(r"^.*?P?(?P<quality>(1080|240|360|144|720|480))(\.mp4)?.*", i, re.MULTILINE).groupdict()["quality"]: videoBase + i for i in m3u8}
    pData = {}
    for playlist in m3u8:
        data = re.sub(r"^#.*\n/rtuk.*\n", "", requests.get(m3u8[playlist]).text, 0, re.MULTILINE)
        pList = ""
        for line in data.split("\n"):
            if line:
                if not line.startswith("#"):
                    pList += videoBase + line + "\n"
                else:
                    pList += line + "\n"
                    pData[playlist] = pList
    return pData
