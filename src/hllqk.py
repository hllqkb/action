#!/usr/bin/python3
#by hllqk daily action on github mail to me
import time 
import smtplib
import os
import requests
import json
import re
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.utils import formataddr
#config
pixivproxy=os.environ['PROXY']
pixiv='https://setu.yuban10703.xyz/setu?r18=1&num=10&replace_url='+pixivproxy
weurl='http://www.weather.com.cn/data/sk/101240709.html'
starttime=1660578304
nowtime=int(time.time())
hasrun=nowtime-starttime
hasrun=hasrun//(24*60*60)
we=requests.get(weurl)
we.encoding='utf-8'
city=we.json()['weatherinfo']['city']
wd=we.json()['weatherinfo']['WD']
temp=we.json()['weatherinfo']['temp']
onesay='https://v1.hitokoto.cn/?c=a'
blog='https://hllqk.vercel.app/'
getonesay=requests.get(onesay)
getonesay=getonesay.text
getonesay=json.loads(getonesay)
onesay=getonesay['hitokoto']
runtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
timemsg='程序运行时间(UTC):'+runtime
my_sender='shuia@shuia.tk'    # 发件人邮箱账号
# 发件人邮箱密码
my_pass=os.environ['PASS']
my_user='3408006879@qq.com'      # 收件人邮箱账号，我这边发送给自己
bangumi='https://bangumi.bilibili.com/api/timeline_v2_global'
headers={
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'User-Agent':'Mozilla/5.0(WindowsNT6.1;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/69.0.3497.100Safari/537.36',
'Accept':'*/*',
'Referer':'http://cambb.cc/forum.php?mod=forumdisplay&fid=37',
'X-Requested-With':'XMLHttpRequest',
'Connection':'keep-alive',
'Host':'cambb.cc',
'Cookie':'prhF_2132_saltkey=AzXzRRx7; prhF_2132_lastvisit=1541264796; prhF_2132_nofavfid=1; prhF_2132_smile=1D1; sucuri_cloudproxy_uuid_79c74ae60=0b002e4f44799010d471d1ac30792e43; prhF_2132_auth=d52cMREMy0bxoLJZpaewtEdQ5OoPl%2FMq7ObQuI3%2B%2FtX9wT3KnvTSpZ%2BLHVYBg63fBnzztNHCgpudNYlBodYOPRfY; prhF_2132_lastcheckfeed=5862%7C1541315119; prhF_2132_home_diymode=1; prhF_2132_visitedfid=37D40D2D36; vClickLastTime=a%3A4%3A%7Bi%3A0%3Bb%3A0%3Bi%3A2414%3Bi%3A1541260800%3Bi%3A2459%3Bi%3A1541260800%3Bi%3A2433%3Bi%3A1541260800%3B%7D; prhF_2132_st_p=5862%7C1541318034%7Ce7c1eea8356bda291aed74ccdb20537d; prhF_2132_viewid=tid_2303; prhF_2132_sid=zHIuFg; prhF_2132_lip=182.148.204.234%2C1541317606; prhF_2132_ulastactivity=2369H6awa8fQve9%2BQr8p8MzIVU3ieAbL9rm7Idao%2FRlbwrDEtV2S; prhF_2132_checkpm=1; prhF_2132_sendmail=1; prhF_2132_st_t=5862%7C1541339179%7C6fbad6f782ca1ec63109b566edb0888c; prhF_2132_forum_lastvisit=D_36_1541269244D_40_1541315980D_37_1541339179; prhF_2132_lastact=1541339180%09misc.php%09patch'
}
#functions
def getpixiv():
    plist=[]
    get=requests.get(pixiv)
    get=get.text
    pjson=json.loads(get)
    pj=pjson['data']
    lenp=len(pj)
    for i in range(lenp):
        try:
            url=pixivproxy+pj[i]['urls']['medium']
            plist.append(url)
        except:
            pass
    return plist
def getnewbangumi():
    #deprecated
    bang=requests.get(bangumi)
    bang=bang.text
    bang=json.loads(bang)
    new=bang['result'][0]
    cover=new['cover']
    title=new['title']
    r={'c':cover,'t':title}
    return r
def getnewpost():
    htmlp=requests.get(blog)
    soup=BeautifulSoup(htmlp.text,'html.parser')
    apost=soup.find('a',class_='article-title')
    apost=str(apost)
    re1 = 'href=\"(.*?)\"'
    re2=re.findall(re1,apost)[0]
    blogurl=blog+re2
    r=apost.replace(re2, blogurl)
    return r
def getBingImg():
    try:
        headers={
            'Content-Type':'application/json; charset=utf-8',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', #不是必须
        }
        response = requests.get(
            "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=7&mkt=zh-CN",
            headers=headers, #请求头
            timeout=3, #设置请求超时时间
        )
        response = json.loads(response.text) #转化为json
        imgList = []
        for item in response['images']:
            imgList.append({
                'copyright':item['copyright'], #版权
                'date':item['enddate'][0:4]+'-'+item['enddate'][4:6]+'-'+item['enddate'][6:], #时间
                'urlbase':'https://cn.bing.com'+item['urlbase'], #原始图片链接
                'url':'https://cn.bing.com'+item['url'], #图片链接
            })
        return imgList #返回一个数据数组
    except:
        return False
img=getBingImg()
copyright=img[0]['copyright']
imgurl=img[0]['url']
#mailmsg
mailmsg='<h1>早上好HLLQK</h1>'+\
onesay+\
"<img src='"+imgurl+"'></img><br>"+copyright+\
'<h2>天气状况</h2>城市:'+city+' 风向:'+wd+' 温度:'+temp+\
'<p>冷的时候冷死，热的时候热死</p>'+\
'<h2>你的Github常用语言:</h2>'+"<img src='https://github-readme-stats.vercel.app/api/top-langs/?username=hllqk&layout=compact&hide_border=true&langs_count=10' width='410px'>"+\
'<p>从入门到入土</p>'+\
'<h2>原神历程</h2>'+"<img src='https://genshin-card.getloli.com/9/257461679.png'>"+\
'<p>旅途总会迎来终点 不必匆忙</p>'+\
'<h2>最新博客帖子</h2>'+getnewpost()+'<br>'+\
'<p>有坚持写博客吗？</p>'+\
'<h2>推荐色图</h2>'
img=getpixiv()
for url in img:
    imgurl='<img title=\'图片加载中\' alt=\'图片无法加载\' src=\''+url+'\'></img>'
    mailmsg=mailmsg+imgurl
end='<p>每天色图，好耶！</p>'+\
'<h2>END</h2>程序已经运行'+str(hasrun)+'天<br>时间总是在不经意中流逝<br>'+\
timemsg
mailmsg=mailmsg+end
def mail():
    ret=True
    try:
        msg=MIMEText(mailmsg,'html','utf-8')
        msg['From']=formataddr(["hllqk Github Action",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["master",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="每日邮件push"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.ym.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
