#機能：サースクのアンケートページからアンケートのタイトルをスクレイピングし、Lineに通知する
from selenium import webdriver
import requests, bs4
import re
import time
from bs4 import BeautifulSoup
from lxml import html

#Line Notifiで通知
def line(mes):
    url = "https://notify-api.line.me/api/notify"
    token = "v1Pf5dUAeJXf1RAyXjpxorisyuIhykpztTchJ8ndJmi"
    headers = {"Authorization": "Bearer " + token}
    message = '\n' + mes
    payload = {"message":  message}
    requests.post(url, headers=headers, params=payload)

def main():
    #サースクにログイン
    driver = webdriver.Chrome(executable_path=r'/Users/matsumototakuya/Documents/chromedriver')
    driver.get('https://www.c-sqr.net/loginform.php')
    account_elem = driver.find_element_by_name('account')
    account_elem.send_keys('mattsun')
    password_elem = driver.find_element_by_name('password')
    password_elem.send_keys('takuya28')
    password_elem.submit()

    #現在のURL(アカウントのID含む)を取得
    print(driver.current_url)

    #URLから数値だけ抽出
    regex = re.compile('\d+')
    num = re.sub('\\D', '', driver.current_url)

    #アカウントIDを定義
    acid = 'cs' + num
    print('アカウントのID:' + acid)


    #アンケートページのURLを生成
    question_url = 'https://www.c-sqr.net/' + acid +'/Question_display.html'

    #アンケートページへ遷移
    driver.get(question_url)

    time.sleep(1)

    print('現在のURL:' + driver.current_url)

    time.sleep(1)

    #HTMLを取得
    html = driver.page_source

    #取得したhtmlからBeautifulSoupオブジェクトを作成し、パーサーに読み込ませる
    soup = bs4.BeautifulSoup(html, 'html.parser')

    #要素(divタグとcommon_titleクラス)で抽出
    title = soup.select('div.common_title')

    #開業コードを除去してテキストのみをリスト化
    wordlist = [x.text.replace("\n"," ").replace("\t"," ")for x in title]

    #リストから1つずつ変数textに格納
    for text in wordlist: 
        line(text)

#import時に勝手にmainが動かないようにする
if __name__ == '__main__':
    main()