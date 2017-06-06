import requests


class Downloader(object):
    def download(self, craw_url):
        if craw_url is None:
            return None
        response = requests.get(craw_url)
        if response.status_code != 200:
            return None
        return response.text
