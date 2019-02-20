import requests
import re

f = open('D:/TJUPTRip/Drawing.Jianghu.Zhi.Bu.Liang.Ren.txt', 'a+')
url = 'http://www.iqiyi.com/a_19rrhc0gyd.html'

r = requests.get(url)
urls = re.findall('<a href="(.*?) target="_blank" data-pb="r=大头部播放&c1=4&rtgt=iqiyi"', r.text)
urls = list(set(urls))

zhmodel = re.compile(u'[\u4e00-\u9fa5]')
urls2 = []
for i in urls:
    match = zhmodel.search(i)
    if not match:
        urls2.append(i)
# print(r.text)
urls_dic = {}
for i in urls2:
    num_i = int(i.split('title=')[-1].strip("")[1:-1])
    urls_dic[num_i] = i.split('title=')[0][:-2]

# print(urls_fin)
urls_sort = sorted(urls_dic.keys())
urls_fin = [urls_dic[i] for i in urls_sort]
for i in urls_fin:
    f.write(i + '\n')
print(urls_fin)