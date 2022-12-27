from sys import argv
pdfs = argv[1:]

from PyPDF2 import PdfReader
for pdf in pdfs:
    reader = PdfReader(pdf)
    page = reader.pages[0]

    text = page.extract_text()
    lines = text.split("\n")
    meta, title = lines[:2]
    print(meta)
    print(title)

    body = "".join(lines[2:])

    a = body.find("作者：")
    b = body.find("☆詞彙學習☆")
    content = body[:a]
    author = body[a:b]
    print(content)#.split("。")[:-1])
#   for sentence in content.split("。")[:-1]:
 #      print(sentence+"。")
    print(author)
