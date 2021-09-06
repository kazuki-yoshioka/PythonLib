import requests
import time

from bs4 import BeautifulSoup


class Scraping():

    # デフォルトのスリープ時間
    DEFAULT_SLEEP_TIME = 1

    soup = {}

    def __init__(self) -> None:
        self.soup = {}

    def close(self):
        """[summary] 実行時の終了処理
        """
        self.soup.clear()

    def setSoupByDriver(self, _driver=None):
        """[summary] スクレイピングするページをセット
        """
        if (_driver is None):
            _driver = self.driver

        self.soup = BeautifulSoup(_driver.page_source, "html.parser")

    def setSoupByUrl(self, _url):
        """[summary] スクレイピング対象のWEBページ情報を取得

        Args:
            _url ([type]): [description]
        """
        self.soup = {}
        if _url is None or len(_url) == 0:
            return False

        ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        headers = {'User-Agent': ua}
        _html = requests.get(_url, headers=headers)
        if _html is None:
            return False

        self.sleepTime()
        content_type_encoding = _html.encoding if _html.encoding != 'ISO-8859-1' else None
        self.soup = BeautifulSoup(
            _html.content, "html.parser", from_encoding=content_type_encoding)

        # self.sleepTime(1)
        _html.close

        if self.soup is None:
            return False

        return True

    def checkSoup(self):
        if self.soup is None:
            return False

        if not self.soup:
            return False

        return True

    def getElementById(self, _id):
        """[summary] 要素を取得する

        Args:
            _id ([type]): [description]

        Returns:
            [type]: [description]
        """
        if self.checkSoup() is False:
            return None

        # 要素を取得(ID)
        element = self.soup.select('#' + _id)

        return element

    def getElementByClassName(self, className):
        """[summary]　リストを取得（クラス指定）

        Args:
            className ([type]): [description]
            クラス名
        """
        if self.checkSoup() is False:
            return None

        element = self.soup.select('.' + className)

        # print(element)
        return element

    def getList(self, id=None, classFlg=False):
        """[summary] リストの要素を取得する

        Args:
            id ([type], optional): [description]. Defaults to None.  
            id、または、クラス名
            classFlg (bool, optional): [description]. Defaults to False.
            True: クラス名、 False: id
        """
        element = {}

        if classFlg is False:
            # IDで検索
            element = self.getElementById(id)

        else:
            # クラス名で検索
            element = self.getElementByClassName(id)

        if not element:
            return None

        form = element[0]

        if not form:
            return None

        return form.find_all('li')

    def sleepTime(self, _time=None):
        """[summary]  スリープ処理

        Args:
            _time ([type], optional): [description]. Defaults to None.
            スリープする指定時間
        """
        if _time is None:
            _time = self.DEFAULT_SLEEP_TIME

        time.sleep(_time)
