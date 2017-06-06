import re

import bs4 as bs4


class Parser(object):
    def parse(self, html_content):
        """解析html文档，获取img标签，src=.jpg的存储到data中，继续爬取下一页"""
        result_img_urls = []
        if html_content is None:
            return
        # 解析html文档
        soup = bs4.BeautifulSoup(html_content, 'html.parser', from_encoding='UTF-8 ')
        # 查询匹配的img标签
        imgs = soup.find_all('img', src=re.compile(r'[^\s]*.jpg'), width='408', height='280')
        for img in imgs:
            img_url = img['src'][2:img['src'].rfind('?')]
            result_img_urls.append("http://" + img_url)

        # 下一页的链接
        li = soup.find('li', class_='next-page')
        link = li.contents[0]
        new_craw_url = link['href'][2:]
        new_craw_url = "http://" + new_craw_url
        return result_img_urls, new_craw_url