#!/bin/env python3
import requests
import subprocess
import re
import json
from iterfzf import iterfzf
import shutil
TERM_WIDTH = shutil.get_terminal_size().columns
def grep(pattern,string):
    A = ""
    for i in string :
        if i == "\n" :
            if pattern in A :
                return A
            A = ""
        else :
            A += i

#test_search="https://www.youtube.com/results?search_query=luke+smith"
test_search = "https://www.youtube.com/results?search_query="+(input("What do you want to search for ? :").replace(" ","+"))
response = requests.get(test_search)

# NOTE : THis is for debugging 
# with open('./test.html','w') as FILE:
#     FILE.write(response.text)
# with open('./test.html') as FILE:
#     response_text = FILE.read().replace('</script>','\n</script>\n')

response_text = response.text.replace('</script>','\n</script>\n')
jsonData = grep("var ytInitialData = ",response_text)
jsonData = jsonData.replace("var ytInitialData = ","var ytInitialData = \n").split('\n')
jsonData = jsonData[1][:-1]
jsonData = json.loads(jsonData)

# NOTE: This is also for debugging
# with open('test.json','w') as FILE :
#     json.dump(jsonData,FILE)


contents = (jsonData["contents"]['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']["contents"][0]['itemSectionRenderer']["contents"])
videoContents = []
VideoIds = []
VideoTitles = []
VideoChannels = []
for i in contents :
    if "videoRenderer" in i :
        videoContents.append(i)
        VideoIds.append("https://www.youtube.com/watch?v="+i["videoRenderer"]['videoId'])
        VideoTitles.append(i["videoRenderer"]['title']['runs'][0]['text'])
        VideoChannels.append(i["videoRenderer"]['longBylineText']['runs'][0]['text'])

def Lookup_Videos() :
    for i in range(len(VideoIds)) :
        yield (f'{VideoTitles[i].ljust(int(2*TERM_WIDTH/5))} {VideoChannels[i].rjust(int(TERM_WIDTH/5))} \t{VideoIds[i].rjust(42)}')

selected = iterfzf(Lookup_Videos())
selected = selected.split()
selected = selected[-1]
subprocess.run(["mpv",selected])
