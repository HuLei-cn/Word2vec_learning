import re
import urllib.request
​
#遍历论文的数量
for t in range(1, 779):
    #不同会议及不同年份的url不同，需要进行修改
    url = 'https://aclanthology.org/2020.acl-main.%d.bib' % t 
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    # print(html)
    pattern_1 = r'title = "(.*?)"' #匹配论文标题
    pattern_2 = r'abstract = "(.*)"' #匹配论文摘要
    url1 = re.search(pattern_1, html)
    url2 = re.search(pattern_2, html)
    a1 = url1.group(1)
    a2 = url2.group(1)
    a1 = a1.replace('{', '') #删除多余字符
    a1 = a1.replace('}', '')
    a1 = a1.replace('/', ' ')
    a1 = a1.replace('\\', ' ')
    a1 = a1.replace('?', ' ')
    a1 = a1.replace('<', ' ')
    a1 = a1.replace('>', ' ')
    a1 = a1.replace('*', ' ')
    a1 = a1.replace('"', ' ')
    a1 = a1.replace('|', ' ')
    a1 = a1.replace(':', ' ')
    f = open('E:/Desktop/papers/ACL/year20/' + a1 + '.txt', 'a+') #写入文件中，以论文标题命名，摘要作为内容
    f.write(a2)
    f.close()
    print('正在下载第%d篇：' % t + a1) #显示下载进度
