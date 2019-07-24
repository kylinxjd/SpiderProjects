from lxml import etree
import requests, csv, jsonpath

# https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.21175956&x-zp-page-request-id=2662dbec63a5463f8f38d8665abacf11-1563246794017-262219&x-zp-client-id=31162821-d811-42ee-89f2-ab9ab82a348f


header = {
    'referer': 'https://sou.zhaopin.com/?jl=653&kw=Python&kt=3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
first_level_url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.21175956&x-zp-page-request-id=2662dbec63a5463f8f38d8665abacf11-1563246794017-262219&x-zp-client-id=31162821-d811-42ee-89f2-ab9ab82a348f'
res = requests.get(url=first_level_url, headers=header)
json_obj = res.json()['data']['results']
print(len(json_obj))

fileds_name = ['city', 'company', 'company_number', 'company_size', 'company_type', 'company_url', 'company_logo',
               'eduLevel', 'emplType', 'jobName', 'jobType', 'positionUrl', 'salary', 'timeState', 'updateDate',
               'workingExp']

with open('job.csv', 'w+') as f:
    fieldnames = fileds_name
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for item in json_obj:
        city = item['city']['display']
        company = item['company']['name']
        company_number = item['company']['number']
        company_size = item['company']['size']['name']
        company_type = item['company']['type']['name']
        company_url = item['company']['url']
        company_logo = item['companyLogo']
        # 学历
        eduLevel = item['eduLevel']['name']
        # 全职
        emplType = item['emplType']
        jobName = item['jobName']
        jobType = item['jobType']['items'][0]['name']
        positionUrl = item['positionURL']
        salary = item['salary']
        # 招聘中
        timeState = item['timeState']
        updateDate = item['updateDate']
        # 工作经验
        workingExp = item['workingExp']['name']

        writer.writerow({'city': city,
                         'company': company,
                         'company_number': company_number,
                         'company_size': company_size,
                         'company_type': company_type,
                         'company_url': company_url,
                         'company_logo': company_logo,
                         'eduLevel': eduLevel,
                         'emplType': emplType,
                         'jobName': jobName,
                         'jobType': jobType,
                         'positionUrl': positionUrl,
                         'salary': salary,
                         'timeState': timeState,
                         'updateDate': updateDate,
                         'workingExp': workingExp})
