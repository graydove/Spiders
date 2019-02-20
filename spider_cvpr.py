import requests
import re

'''
Reference URL:
http://openaccess.thecvf.com/content_cvpr_2015/papers/Chang_Propagated_Image_Filtering_2015_CVPR_paper.pdf
Papers of ICCV have the same way to be downloaded.
'''


def get_pdf(year):
    url = 'http://openaccess.thecvf.com/%s.py' % year
    r = requests.get(url)
    web = r.text
    url_pdf = re.findall(r'<a href=(.*?)>pdf</a>', web)
    for i in url_pdf:
        pdf = 'http://openaccess.thecvf.com/' + i.strip('"')
        f = open('C:/Users/temp/Desktop/%s.sh' % year, 'a+')
        f.write('wget' + ' ' + pdf + ';')
        f.close()


year = input('Please print a conference and a year:')
get_pdf(year)
