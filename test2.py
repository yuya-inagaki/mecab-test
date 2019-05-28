#####################################
#                                   #
#     MeCabのインストールチェック用     #
#                                   #
#####################################

import re
import bs4
import sys
import MeCab
import urllib.request
from pprint import pprint

# 指定したURLをセット
if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    print("URLを指定してください")
    exit()

# URLにアクセスし、ソースコードを取得＆パース
soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

# title, description, h1を抜き出し処理対象としてセット
title = soup.title.string
description = soup.find(attrs={"name": re.compile(r'Description', re.I)}).attrs['content']
h1 = soup.h1.string
contents = title + description + h1
output_words = []

# MeCabでキーワードを抽出する
m = MeCab.Tagger()
keywords = m.parse(contents)

for row in keywords.split("\n"):
    word = row.split("\t")[0]
    if word == "EOS":
        break
    else:
        pos = row.split("\t")[1].split(",")[0]
        if pos == "名詞":
            output_words.append(word)

# ユニークにして出力
pprint(list(set(output_words)))
