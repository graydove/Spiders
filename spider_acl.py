import requests
import re

'''
Reference URL:

'''


def get_pdf(year):
    r = requests.get('http://www.aclweb.org/anthology/P/P%s/' % str(year)[-2:])
    title = re.findall('<i>(.*?)</i>', r.text)[1:]
    url = re.findall('<p><a href="(.*?)">(.*?)</a>', r.text)[1:]
    pdf_url = ['http://www.aclweb.org/anthology/P/P%s/' % str(year)[-2:] + x[0] for x in url]
    print title
    print len(title)
    print pdf_url
    print len(pdf_url)
    # for i in range(len(pdf_url)):
    #     print(i+1)
    #     print(pdf_url[i])

    for i in range(len(pdf_url)):
        f = open('C:/Users/temp/Desktop/ACL%s.sh' % year, 'a+', encoding='utf-8')
        file_title = str(title[i].split('/')[0]).strip(' ')
        file_title = file_title.replace(' ', '_').replace('(', '\(').replace(')', '\)').replace('\'', '\\\'')
        file_title = file_title.replace(':', '_').replace('&', '_')
        f.write('wget' + ' ' + pdf_url[i] + ' ' + '-O' + ' ' + file_title + '.pdf;' + '\n')
        f.close()


year = 2018
get_pdf(year)
