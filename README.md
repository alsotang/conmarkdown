#ConMarkdown

##Summary

将Markdown语法转换而来的HTML代码转换回去。

本项目使用Python编写，在Ubuntu 10.04, Python 2.6下测试通过。

项目依赖：BeautifulSoup4

This project is mean to 'Convert those HTML file which is converted from markdown to markdown', just like orther `html2markdown` project.

This project is written in Python 2.6, and it can run prefectly in Ubuntu 10.04.

##Howto Use

    :::python
    from conmarkdown import conmarkdown
    conmarkdown('the_name_of_the_HTML_file')

then you will get a converted .md file in the same dir of the HTML file.




