#####################################
#                                   #
#     MeCabのインストールチェック用     #
#                                   #
#####################################


import requests
import pandas as pd
from bs4 import BeautifulSoup

import MeCab


# main
if __name__ == '__main__':
    # URL & File Name
    URL = input("URLを入力してください\n")

    ##HTML取得
    html=requests.get(URL).text
    soup=BeautifulSoup(html,"html.parser")
    #print(soup.prettify)

    ##scriptやstyleを含む要素を削除する
    for script in soup(["script", "style"]):
        script.decompose()
    #print(soup)

    ##テキストのみを取得=タグは全部取る
    text=soup.get_text()
    #print(text)

    ##textを改行ごとにリストに入れて、リスト内の要素の前後の空白を削除
    lines= [line.strip() for line in text.splitlines()]
    #print(lines)

    ##リストの空白要素以外をすべて文字列に戻す
    text="\n".join(line for line in lines if line)
    print(text)

    print("==================================")

    m = MeCab.Tagger()
    print(m.parse(text))
