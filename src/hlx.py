import requests
import json
def getnote():
    noteheaders={
        'Connection': 'close',
        'Host': 'floor.huluxia.com',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.8.1'
    }
    noteurl='http://floor.huluxia.com/post/detail/ANDROID/4.1.7?platform=2&gkey=000000&app_version=4.1.1.9.1&versioncode=347&market_id=tool_web&_key=&device_code=%5Bd%5D6ec2854f-f80e-4b3e-8c9a-469b40429ab2&phone_brand_type=UN&post_id=51119276&page_no=1&page_size=0&doc=1'
    text=requests.get(noteurl,headers=noteheaders).text
    note=json.loads(text)['post']
    title=note['title']
    title='<h2>'+title+'</h2>'
    detail=note['detail']
    detail=detail.replace('<text>','').replace('</text>','').replace('\n','<br>')
    note=title+detail
    return note
print(getnote())