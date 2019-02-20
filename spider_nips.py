import requests
import re

'''
Reference URL:

'''


def get_pdf(year):
    r = requests.get('http://papers.nips.cc/book/advances-in-neural-information-processing-systems-30-%s' % year)
    all = re.findall('<li><a href="(.*?)">(.*?)</a>', r.text)
    pdf_url = ['http://papers.nips.cc' + x[0] + '.pdf' for x in all][1:]
    title = [x[1] + '.pdf' for x in all][1:]
    print(pdf_url)
    print(len(pdf_url))
    print(title)
    print(len(title))

    for i in range(len(pdf_url)):
        f = open('C:/Users/temp/Desktop/NIPS%s.sh' % year, 'a+', encoding='utf-8')
        file_title = title[i]
        file_title = file_title.replace(' ', '_').replace('(', '\(').replace(')', '\)').replace('\'', '\\\'')
        file_title = file_title.replace(':', '_').replace('&', '_').replace('?', '\?').replace('*', '\*')
        f.write('wget' + ' ' + pdf_url[i] + ' ' + '-O' + ' ' + file_title + ';' + '\n')
        f.close()


year = 2018
get_pdf(year)
