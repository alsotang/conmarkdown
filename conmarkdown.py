#! /usr/bin/env python
# coding=utf-8
'''
#=============================================================================
#     FileName: conmarkdown.py
#         Desc: convert HTML which is converted from markdown to markdown
#       Author: Alsotang
#        Email: alsotang@gmail.com
#     HomePage: http://tangzhan.li
#      Version: 0.0.1
#   LastChange: 2012-04-27 16:29:47
#      History:
#=============================================================================
'''

import re

from bs4 import BeautifulSoup


def case_tag(tag, contents):
    tag_name = tag.name
    if  tag_name == 'p':
        contents += '\n'
    elif tag_name == 'strong':
        contents = '**' + contents + '**'
    elif tag_name == 'em':
        contents = '*%s*' % contents
    elif re.match(r'h(\d)', tag_name):
        if tag.get('id'):
            contents = unicode(tag) + '\n'
        else:
            contents = int(tag_name[-1]) * '#' + contents + '\n'
    elif tag_name == 'li':
        contents = '* ' + contents
        if tag.parent.name == 'ul' and tag.parent.parent.name =='li':
            contents = '    ' + contents
    elif tag_name == 'a':
        contents = '[%s](%s)' % (contents, tag.get('href'))
    elif tag_name == 'pre':
        contents = re.sub(r'<(.*?)>(.*?)<\/\1>', r'\2', contents)
        contents = '\n'.join('    ' + line for line in contents.split('\n'))
    elif tag_name == 'code' and tag.parent.name != 'pre':
        contents = '`%s`' % (contents)
    elif tag_name == 'hr':
        contents = '* * *' + '\n'
    return contents

def convert(html_data):

    result_data = []

    for child in html_data.children:
        if not child:
            continue
        try:
            result_data.append(convert(child))
        except AttributeError:
            if len(html_data.contents) == 1:
                result_data.append(case_tag(html_data, unicode(child)))
                return ''.join(result_data)
            else:
                result_data.append(unicode(child))

    return case_tag(html_data, ''.join(result_data))
        

def conmarkdown(filename):
    FILENAME = filename or 'test'
    soup = BeautifulSoup(open(FILENAME + '.html'))
    soup = soup.body
    result = convert(soup)
    with open(FILENAME + '_converted.md', 'w') as wf:
        print >> wf, result.encode('utf-8')

if __name__ == '__main__':
    # 'test' is a HTML filename which would turn into 'test.html' later.  
    # and the result file named 'test_converted.md'.
    conmarkdown('test') 
