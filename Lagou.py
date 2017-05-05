import requests
import re
import os
import json
import time
import xlwt


def get_html(pn):
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%AD%A6%E6%B1%89&first=ture&pn={}&kd=iOS'.format(pn)
    user_agens = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    cookie = 'JSESSIONID=C4A6533D92AA2F92B0A40FB07FA658B9; user_trace_token=20170503135534-e36ff7567cb84ba4b6fb0dd50525470a; _gat=1; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D0zI5P_Qo3_BY1n65Oj2vBGJNjF-_Rv0MIj7HW2xb3_u%26wd%3D%26eqid%3Da98c06710002373c00000005590970d2; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20170503135534-1fc29cae-2fc5-11e7-930a-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; _gid=GA1.2.1213770582.1493790940; _ga=GA1.2.617553814.1493790935; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1493712299,1493790935; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1493790940; LGSID=20170503135534-1fc29b10-2fc5-11e7-930a-525400f775ce; LGRID=20170503135540-230e25d2-2fc5-11e7-b52e-5254005c3644; SEARCH_ID=ef9373257f374cffba50dcbfc6e6ec82'
    heads = {'User_agent':user_agens,'cookie':cookie}
    try:
        print url
        time.sleep(10)
        response = requests.get(url,headers =heads)
        print response.status_code
        response.encoding = response.apparent_encoding
        data = json.loads(response.text)
        return data
    except:
        return None

def parse_html(text,info_list):
    info = text['content']['positionResult']['result']

    if info:
        for item in info:
            company_info = []
            company_info.append(item['companyFullName'])
            company_info.append(item['positionName'])
            company_info.append(item['companySize'])
            company_info.append(item['district'])
            company_info.append(item['businessZones'])
            company_info.append(item['salary'])
            company_info.append(item['positionAdvantage'])
            company_info.append(item['companyLabelList'])
            company_info.append(item['financeStage'])
            company_info.append(item['workYear'])
            company_info.append(item['education'])
            info_list.append(company_info)
            print company_info

    return info_list


def save_info(companys,name):
    book = xlwt.Workbook()
    sheet = book.add_sheet(name,cell_overwrite_ok=True)

    print 'get data success'
    heads = [u'companyFullName',u'positionName',u'companySize',u'district',u'businessZones',u'salary',u'positionAdvantage',u'companyLabelList',u'financeStage',u'workYear',u'education']

    row = 0
    for head in heads:
        sheet.write(0,row,head)
        row +=1

    info_line = 1
    for company in companys:
        info_row = 0
        for info in company:
            sheet.write(info_line,info_row,info)
            info_row +=1
        info_line +=1
    book.save(str(name)+'.xls')
    print 'Write success'







def main():
    info_list = []
    name = 'wuhaniOS'
    for pn in range(1,6):
        text = get_html(pn)
        parse_html(text,info_list)
    save_info(info_list,name)



if __name__ == '__main__':
    main()