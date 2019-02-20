import requests
import re

'''
Reference URL:
http://proceedings.mlr.press/v70/jain17a/jain17a.pdf
Attention:
ICML2018 is v80
ICML2017 is v70
ICML2016 is v48
ICML2015 is v37
ICML2014 is v32
ICML2013 is v28
ICML2011 is v27
'''

url = 'http://proceedings.mlr.press/v28/'
website = requests.get(url).text
title_list = re.findall('<p class="title">(.*?)</p>', website)
pdf_list = re.findall('\[<a href="(.*?)">Download PDF</a>\]', website)
listnum = len(title_list)
print(title_list)
listpdf = len(pdf_list)
for i in range(listnum):
    title = title_list[i].replace(' ', '_')
    pdf = 'http' + re.findall('http(.*?)pdf', pdf_list[i])[0] + 'pdf'
    pdf_url = 'wget' + ' ' + pdf + ' ' + '-O' + ' ' + title + '.pdf;'
    f = open('C:/Users/temp/Desktop/ICML2013.json', 'a+', encoding='utf-8')
    f.write(pdf_url)
    f.close()
