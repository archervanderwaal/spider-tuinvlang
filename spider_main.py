import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderTool(object):
    def __init__(self):
        # 初始化爬虫的管理器
        self.manager = url_manager.UrlManager()
        # 初始化输出器
        self.outputer = html_outputer.Outputer()
        # 初始化解析器
        self.parser = html_parser.Parser()
        # 初始化下载器
        self.downloader = html_downloader.Downloader()

    def start_work(self, root_url):

        index = 1
        # 调用url管理器加载待爬取的url
        self.manager.add_craw_url(root_url)
        # 判断是否有待爬取的url
        while self.manager.has_no_craw_url():
            if index >= 7:
                break
            try:
                # 获取一个待爬取的url
                craw_url = self.manager.get_no_craw_url()
                print("当前要爬的页面链接:" + craw_url)
                html_content = self.downloader.download(craw_url)

                # 解析爬到的html,返回符合要求的图片url,并且返回下一个
                result_img_urls, new_craw_url = self.parser.parse(html_content)
                # 添加下一个要爬取的页面链接
                print(new_craw_url)
                self.manager.add_craw_url(new_craw_url)
                # 收集数据
                self.outputer.collect_craw_data(result_img_urls=result_img_urls)
                print("第" + str(index) + "页爬取完毕，总共" + str(len(result_img_urls)) + "个图片.")
                index += 1
            except:
                print("craw failed!")
                continue

        self.outputer.output_html()

if __name__ == '__main__':
    root_url = 'http://www.dsqnw.com/tag/tuinvlang'
    spider = SpiderTool()
    spider.start_work(root_url)
