import requests
import re

'''
Reference URL: https://acl2018.org/programme/papers/

'''


r = requests.get('https://acl2018.org/programme/papers/')
title = re.findall('<i>(.*?)</i>', r.text)[1:]
url = re.findall('<p><a href="(.*?)">(.*?)</a>', r.text)[1:]
# pdf_url = ['http://www.aclweb.org/anthology/P/P%s/' % str(year)[-2:] + x[0] for x in url]

print title
	
