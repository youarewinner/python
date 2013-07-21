# seach file 찾기 python 2github3rd-test
# -*- coding: utf-8 -*-
import urllib2
import re

text = '드림라인'
html_content = urllib2.urlopen('http://www.dreamline.kr/dreamline-blog').read()
matches = re.findall(text ,html_content)


if len(matches) == 0:
    print ' i did not find anything'
else:
    print 'My string is in the html'
    print text
