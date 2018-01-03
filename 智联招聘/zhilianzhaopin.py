import json,re
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
from requests import RequestException
def get_page_index(offset, keyword):
    data = {
        'jl': '北京',
        'keyword': keyword,
        'p': 1,
        'isadv': offset
    }
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
    print(urlencode(data))
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'
    try:
        response = requests.get(url=url,headers=headers,params=data)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求  jj')
        return None
def xiangxiurl(html):
    link = re.findall(r'href="(http[^\s]*?htm)', html)
    return link
def jiequ(url1):
    s = ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    html    =requests.get(url=url1,headers=headers).text
    print(html)
    soup = BeautifulSoup( html,'lxml')
    公司名称 = soup.select('div.tab-inner-cont > h5 >a ')[0].text
    职位名称 = soup.select('div.inner-left  > h1 ')[0].text
    职位待遇= soup.select('div.content > span')
    for x in 职位待遇:s = s + x.text
    职位月薪 = soup.select(' div.terminalpage-left > ul.terminal-ul > li > strong')[0].text
    工作地点 = soup.select('ul.terminal-ul > li > strong  ')[1].text
    发布日期=soup.select('strong > span#span4freshdate ')[0].text
    工作性质 = soup.select('ul.terminal-ul > li > strong ')[3].text
    工作经验 = soup.select('ul.terminal-ul > li > strong ')[4].text
    最低学历 = soup.select('ul.terminal-ul > li > strong ')[5].text
    招聘人数 = soup.select('ul.terminal-ul > li > strong ')[6].text
    职位类别 = soup.select('ul.terminal-ul > li > strong ')[7].text
    职位描述 = soup.select('div.tab-inner-cont > p')
    for x in range(24, 30):
        print(职位描述[x].text)
    公司规模 = soup.select('div.tab-inner-cont > div > p > span ')
    公司性质 = soup.select()
    公司行业 = soup.select()
    公司地址= soup.select()
    return 公司名称,职位名称,职位待遇,职位月薪,工作地点,发布日期,工作性质,工作经验,最低学历,招聘人数,职位类别,职位描述,公司规模,公司性质,公司行业,公司地址
def main():
    html=get_page_index(0,'哈药集团有限公司')
    url=xiangxiurl(html)
    for ur in url:
        print(ur)
        print(jiequ(ur))

if __name__=='__main__':
    main()