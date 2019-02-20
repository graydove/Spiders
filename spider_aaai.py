import requests
import re

'''
Reference URL:

'''


def get_pdf(year):
    r = requests.get('https://www.aaai.org/ocs/index.php/AAAI/AAAI%s/schedConf/presentations' % str(year)[-2:])
    title = re.findall('<a href="(.*?)">(.*?)</a>', r.text)
    title = [x[1] for x in title if x[1] != 'PDF'][43:]
    url = re.findall('href="(.*?)" class="file">PDF</a>', r.text)
    pdf_url = [x.replace('view', 'viewFile') for x in url]
    print(title)
    print(len(title))
    print(pdf_url)
    print(len(pdf_url))

    for i in range(len(pdf_url)):
        f = open('C:/Users/temp/Desktop/AAAI%s.sh' % year, 'a+', encoding='utf-8')
        file_title = title[i]
        file_title = file_title.replace(' ', '_').replace('(', '\(').replace(')', '\)').replace('\'', '\\\'')
        file_title = file_title.replace(':', '_').replace('&', '_').replace('?', '\?').replace('*', '\*')
        file_title = file_title.replace('’', '\'')
        f.write('wget' + ' ' + pdf_url[i] + ' ' + '-O' + ' ' + file_title + '.pdf;' + '\n')
        f.close()


year = 2014
get_pdf(year)