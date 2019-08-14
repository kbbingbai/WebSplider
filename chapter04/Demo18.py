#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/13 18:35
# @Author :zhai shuai
"""
 作用
    一：请求拉勾网的数据，使用传统的方式进行数据的获取，这种方式并不好使用，会出错
 难点
    
 注意点
    
"""

import requests
import time
def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
    data = {
        'first': 'true',
        'pn':'1',
        'kd':'python'
    }

    headers = {
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        "X-Anit-Forge-Code": "0",
        "X-Anit-Forge-Token": "None",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Host": "www.lagou.com",
        "Origin": "https://www.lagou.com",
        "X-Requested-With": "MLHttpRequest",
        "Cookie": "user_trace_token=20190731133650-373e61b5-a9f4-4f31-a7bb-25d4830f89a3; _ga=GA1.2.722193631.1564551413; LGUID=20190731133651-3277436b-b355-11e9-862c-525400f775ce; LG_HAS_LOGIN=1; _gid=GA1.2.1263048965.1565742758; LG_LOGIN_USER_ID=102e630f6255f6ee7e022212f85c69a862af551d019d7f67ccb3c14df5dd5dd6; _putrc=1FC281F3175E19DC123F89F2B170EADC; JSESSIONID=ABAAABAAAIAACBID77491F65B7A678464B9E00386B6D57D; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B76322; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; WEBTJ-ID=20190814083349-16c8d8b8e7f25c-05923535901506-7373e61-1327104-16c8d8b8e8083e; index_location_city=%E5%8C%97%E4%BA%AC; gate_login_token=89623374585c70506ffc0de12e775d197caba64657c0b8caea95e0cc7b4df932; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2214668815%22%2C%22%24device_id%22%3A%2216c46882f6b29d-0e6ec900c8947b-c343162-1327104-16c46882f6c8c8%22%2C%22props%22%3A%7B%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2276.0.3809.100%22%7D%2C%22first_id%22%3A%2216c46882f6b29d-0e6ec900c8947b-c343162-1327104-16c46882f6c8c8%22%7D; TG-TRACK-CODE=search_code; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1565742751,1565752534,1565759941,1565773552; LGSID=20190814170552-b743f19d-be72-11e9-89bf-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=; X_HTTP_TOKEN=5e508e8a644cab9558537756517319dfb411a70604; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1565773586; LGRID=20190814170626-cb7354ad-be72-11e9-89bf-525400f775ce; SEARCH_ID=f600f8333bcd4859ae2a68d41b54f076"
    }
    for x in range(1,13):
        data['pn'] = x;
        resp = requests.post(url,headers=headers,data=data)
        print(resp.json())
        time.sleep(10)


if __name__ == '__main__':
    request_list_page()