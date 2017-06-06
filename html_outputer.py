class Outputer(object):
    def __init__(self):
        self.result_datas = []

    def collect_craw_data(self, result_img_urls):
        if result_img_urls is None or len(result_img_urls) == 0:
            return
        for img_url in result_img_urls:
            self.result_datas.append(img_url)

    def output_html(self):
        try:
            with open('output.html', 'w') as f_obj:
                f_obj.write("<html>")
                f_obj.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
                f_obj.write("<body>")
                f_obj.write("<table border='0'>")
                for img_url in self.result_datas:
                    f_obj.write("<tr>")
                    f_obj.write("<td align='center'>")
                    f_obj.write("<img src=" + img_url + "?width=700&height=470>")
                    f_obj.write("</td>")
                    f_obj.write("</tr>")
                f_obj.write("</table>")
                f_obj.write("</body>")
                f_obj.write("</html>")
        except:
            print("写入文件内容失败!")
            return False
        return True
