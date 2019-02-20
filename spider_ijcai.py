import requests
import re

'''
Reference URL:
https://www.ijcai.org/proceedings/2017/0001.pdf
https://www.ijcai.org/proceedings/2018/0001.pdf
'''


def get_pdf(year):
    r = requests.get('https://www.ijcai.org/proceedings/%s/' % year)
    title = re.findall('<p>(.*?)<br />', r.text)[1:]
    title = [x.split('/')[0].strip(' ') for x in title]
    url = re.findall('<a href="(.*?)">PDF</a>', r.text)
    pdf_url = ['https://www.ijcai.org/Proceedings/15/Papers/' + str(x.split('/')[-1]) for x in url]
    print(title)
    print(len(title))
    print(pdf_url)
    print(len(pdf_url))
    # for i in range(len(pdf_url)):
    #     print(i+1)
    #     print(pdf_url[i])

    for i in range(len(pdf_url)):
        f = open('C:/Users/temp/Desktop/IJCAI%s.sh' % year, 'a+', encoding='utf-8')
        file_title = str(title[i].split('/')[0]).strip(' ')
        file_title = file_title.replace(' ', '_').replace('(', '\(').replace(')', '\)').replace('\'', '\\\'')
        file_title = file_title.replace(':', '_').replace('&', '_')
        f.write('wget' + ' ' + pdf_url[i] + ' ' + '-O' + ' ' + file_title + '.pdf;' + '\n')
        f.close()


year = 2015
get_pdf(year)
