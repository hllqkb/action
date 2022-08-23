import requests
from requests.cookies import RequestsCookieJar
def login(user,password):
    url='https://my.freenom.com/dologin.php'
    headers={
  "Host": "my.freenom.com",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:103.0) Gecko/20100101 Firefox/103.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
  "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
  "Accept-Encoding": "gzip, deflate, br",
  "Content-Type": "application/x-www-form-urlencoded",
  "Content-Length": "111",
  "Origin": "https://my.freenom.com",
  "Connection": "keep-alive",
  "Referer": "https://my.freenom.com/clientarea.php",
  "Cookie": "G_ENABLED_IDPS=google; __zlcmid=1BalAXx3Y2iL0EP; WHMCSZH5eHTGhfvzP=evs7f3mo1ijcti618bt168nfl1; __utma=76711234.343324833.1661244181.1661244181.1661244181.1; __utmb=76711234.2.10.1661244181; __utmc=76711234; __utmz=76711234.1661244181.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1",
  "Upgrade-Insecure-Requests": "1",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-User": "?1",
  "TE": "trailers"
}
    data={
        'token':"",
'username':	user,
'password':	password,
'rememberme':	"on"
    }
    session=requests.Session()
    # 拒绝302重定向，避免太快了，抓不到cookie
    res=session.post(url,data=data,headers=headers,allow_redirects=False)
    cookies=res.cookies
    cookies = requests.utils.dict_from_cookiejar(cookies)
    return cookies
#print(login("3408006879@qq.com","Qw1357924680"))