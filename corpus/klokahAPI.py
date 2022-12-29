
from urllib.request import urlopen
from urllib.parse import quote
from xml.etree import ElementTree

def klokahAPI(d=6, txt="klokah"):
    text_chinese_tag_url = [["text", "chinese", "tag", "url"]]
#   print(txt)
    t = txt.replace("'","’")
#   print(t)
    file = urlopen(url="http://web.klokah.tw/api/multiSearchResult.php?d=" + str(d) + "&txt=" + quote(t))
    for child in ElementTree.parse(file).getroot():
        if child.findall("item"):
            for item in child.findall("item"):
                text = item.find("text").text
                chinese = item.find("chinese").text
                url = None
                try:
                    url = item.find("url").text
                except:pass
                text_chinese_tag_url.append([text, chinese, child.tag, url])
    return iter(text_chinese_tag_url)

from sys import argv
from utilities import generic_concordancer
if __name__ == "__main__":
    d = argv[1]
    txt = kw = argv[2]
#   for element in klokahAPI(d=int(argv[1]), txt=argv[2]):
#       print(element)
    rows = klokahAPI(d=int(argv[1]), txt=argv[2])
    for row in generic_concordancer(kw=kw, rows=rows, target_column_num=0):
        print(row)
