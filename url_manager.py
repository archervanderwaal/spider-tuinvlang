class UrlManager(object):

    def __init__(self):
        # 待爬取集合
        self.no_craw_urls = set()
        # 已爬取集合
        self.old_craw_urls = set()

    def add_craw_url(self, url):
        """添加url到待爬取url集合中"""
        if url is None:
            return
        if url not in self.no_craw_urls and url not in self.old_craw_urls:
            self.no_craw_urls.add(url)

    def has_no_craw_url(self):
        """判断待爬取集合是否还有"""
        return len(self.no_craw_urls) != 0

    def get_no_craw_url(self):
        """"获得一个待爬取的Url"""
        craw_url = self.no_craw_urls.pop()
        print(str(len(self.no_craw_urls)))
        self.old_craw_urls.add(craw_url)
        return craw_url

    def add_craw_urls(self, craw_urls):
        """添加urls到待爬取url集合中"""
        if craw_urls is None or len(craw_urls) == 0:
            return
        for craw_url in craw_urls:
            self.add_craw_url(craw_url)
