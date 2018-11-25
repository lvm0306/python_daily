import requests
from bs4 import BeautifulSoup
import uuid
import requests
import time

import chardet

from utils.UserAgentSeed import getHeaders
from utils.GetEncoding import GetEncoding

ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}


class SpiderHtml():
    def __init__(self, url):
        self.url = url

    def getHtml(self):
        respone = requests.get(url=self.url, headers=getHeaders())
        respone.encoding = GetEncoding(self.url).get_encode1()
        return respone.text