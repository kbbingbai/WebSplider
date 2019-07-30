#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/28 12:13
# @Author :zhai shuai
"""
 作用
    一：urllib--request--Request
    二；拉取拉勾网的数据******
    三：拉勾网做的反爬虫做的比较的好
 难点
    1 拉取拉勾网反爬虫很强，讲者用了User-Agent和Referer 就可以把数据给爬取下来，
    我的不可以，必须是带cookie才可以，且cookie带过去有时候也不行
    
 注意点
    一 如果请求当中需要带一些参数，或者其它的东西，就不能使用 request.urlopen(),就需要用到这个类
        Request

    
"""

from urllib import request,parse
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC",
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    "Cookie": "user_trace_token=20190728121554-67640ce2-bcc2-4a05-94a4-ad10578b9774; _ga=GA1.2.1415158968.1564287357; LGSID=20190728121555-64c07703-b0ee-11e9-a4f4-5254005c3644; LGUID=20190728121555-64c07a5f-b0ee-11e9-a4f4-5254005c3644; LG_HAS_LOGIN=1; _putrc=1FC281F3175E19DC123F89F2B170EADC; JSESSIONID=ABAAABAABEEAAJA222F9576DACD4B4CB7AB053B2A5C6395; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B76322; hasDeliver=0; gate_login_token=6c9020e33361fdbd937e4bd1665e43047c67259a46693c3d331fc20b15685679; _gid=GA1.2.1747468191.1564287419; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1564287357,1564287437; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; WEBTJ-ID=20190728121746-16c36cc7d5216f-02577836ee7337-c343162-1327104-16c36cc7d5371; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; SEARCH_ID=82d9f33c371345348497bac71bb719ef; X_HTTP_TOKEN=f4999c7d4b75bd00401192465196dcfc26090002aa; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1564291107; LGRID=20190728131824-1fdac6b3-b0f7-11e9-a4f4-5254005c3644"
}
data = {
    "first":'true',
    "pn": 1,
    "kd": "python"
}
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'

req = request.Request(url,headers=header,data=parse.urlencode(data).encode(),method="POST")
resp = request.urlopen(req)
print(resp.read().decode())

