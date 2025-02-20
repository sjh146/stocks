# 정의서 : 구글RSS 기능 구현

# 1. 키워드 앤드 문장을 엑셀로 등록(구글 드라이버, file) 
# 2. 매일 관련 키워드로 찾은 기사를 찾는다. (셀레니움, beautifulsoup, requests)
# 3. 뉴스 요약
# 4. 매일 텔레그램과 이메일로 기사를 보낸다. (텔레봇, 이메일봇)

# 모듈 1. 키워드 등록
import pandas as pd 
# 모듈 2. 뉴스 서칭
import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
# 모듈 3. 뉴스 요약
# 모듈 4. 뉴스 송부
import time
import telepot

########################## 모듈 1. 키워드 등록 ##########################################################

# pandas로 쉽게 엑셀을 열수있을것 같은데 안됨
# 이유를 확인해 보니, 이제 xlsx는 지원을 안한다고 함. xls를 사용해야함. 
# xlrd.biffh.XLRDError: Excel xlsx file; not supported

file = 'keyword.csv' # xlsx -> xls로 변경
df = pd.read_csv(file)
print(type(df))
print(df.keys())
print(df.index) 
print(df.columns)

for k in range(0,14):
    keyword = df.at[k,'검색키워드']
    print('{}번째 키워드 입니다 : {}'.format(k+1, keyword))
    # b = df.at[1,'검색키워드']

    ################### 모듈 2. 뉴스 서칭 ##############################################################

    # search는 네이버에 집어넣는 검색어 문구이므로, 모듈 1에서 불러온 keyword를 넣어준다
    search = keyword 
    # 네이버에서 검색 주소를 가져와서 사용한다.
    # url = f'https://m.search.naver.com/search.naver?where=m_newsw&sm=mtb_jum&query={quote_plus(search)}'
    # print(url)
    # html = urlopen(url).read()
    # print(html)
    # soup = BeautifulSoup(html, 'html.parser') # html.parser로 수프를 끓여준다
    # total = soup.select('.api_save_group._keep_wrap') # 네이버에서 블로그 관련 selector만 허용해서 뉴스는 가져올 수 없음.

    # url = f'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query={quote_plus(search)}'
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={quote_plus(search)}'    
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    # total = soup.select('.api_txt_lines.total_tit')
    total = soup.select('.api_txt_lines.dsc_txt_wrap')
    searchList = []
    print(total)

    searchList = [] # 써치 결과를 넣을 리스트

    for i in total:
        temp = []
        temp.append(i.text)
        temp.append(i.attrs['href'])
        searchList.append(temp)

    f = open(f'{search}.csv', 'w', encoding='utf-8', newline='')
    csvWriter = csv.writer(f)
    for i in searchList:
        csvWriter.writerow(i)
    f.close()
    result = pd.DataFrame(searchList)
    print(result)
    print('리스트 작성이 완료되었습니다.')

    ########################## 모듈 4. 뉴스 송부  ######################################################
    # 텔레그램 봇 구동

    token = "7903260976:AAEQtnBt1kBNGxdidPx6cHreMo5QgDSEXpM" 
    mc = "454953244"
    bot = telepot.Bot(token)

    print(result.index)
    print(result.columns)
    c = result.at[0,1]
    d = result.at[1,1]
    print(c)
    print(d)
    # bot.sendMessage(chat_id = '@economystory', text = result.at[0,1]) 
    for i in range(0,10):
        bot.sendMessage(chat_id = "-1002411723910", text = result.at[i,1]) 
        print('텔레그램으로 {}번 전송됐습니다.'.format(i+1))
        time.sleep(3) # 텔레그램에서 너무 많이 보내면 차단을 하니, 3초 간격을 두고 송부한다. 2초도 어느정도 하다 차단됨.


    # # # 모듈 3. 뉴스 요약(미구현)

    # # from gensim.summarization.summarizer import summarize
    # # from newspaper import Article
    # # # url = "https://news.v.daum.net/v/20180206160003332"
    # # url = "https://news.v.daum.net/v/20180206160003332"
    # # news = Article(url, language = "ko")
    # # news.download()
    # # news.parse()

    # # summarize(news.text, word_count = 50)
    # # print(news.text)