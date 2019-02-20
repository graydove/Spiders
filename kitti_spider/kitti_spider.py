import requests
import re


def spider(word):
    url = []
    r = requests.get('http://www.cvlibs.net/datasets/kitti/raw_data.php?type=%s' % word)
    web = r.text
    list = re.findall('<a href=(.*?)data\\]</a>', web)
    for i in list:
        u = i.strip('>[synced+rectified ').strip('>[unsynced+urectified ')[1:-1]
        if 'sync' in u:
            url.append(u)

    filename = 'E:/Project/Spiders/kitti_spider/kitti_%s.sh' % word
    f = open(filename, 'a+')
    for i in url:
        print(i)
    # print(word + ' ' + 'is end.')
        f.write('wget' + ' ' + str(i) + ';')
    f.close()


word_list = ['city', 'residential', 'road', 'campus', 'person', 'calibration']
for i in word_list:
    spider(i)
