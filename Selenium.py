import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Selenium():

    # デフォルトのスリープ時間
    DEFAULT_SLEEP_TIME = 3

    driver = {}

    def initilize(self):
        """[summary] 実行時の初期処理
        """
        self.driver = webdriver.Chrome('driver/chromedriver.exe')
        self.driver.get(self.config['FIRST_URL'])

    def close(self):
        """[summary] 実行時の終了処理
        """
        if self.driver is None:
            return

        self.driver.close()

    def execute(self, _url):
        """[summary] 画面を立ち上げる

        Args:
            _url ([type]): [description]
        """
        self.driver = webdriver.Chrome('driver/chromedriver.exe')
        self.driver.get(_url)

    def getElement(self, id=None, className=None):
        """[summary] 要素を取得

        Args:
            id ([type], optional): [description]. Defaults to None.
            className ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        element = {}
        if not(id is None):
            element = self.driver.find_element_by_id(id)

        elif not(className is None):
            element = self.driver.find_element_by_class_name(className)

        return element

    def clickByClassName(self, className):
        """[summary] クリック処理（クラス指定）

        Args:
            className ([type]): [description]
            クラス名
        """
        return self.clickEvent(None, className)

    def clickById(self, id):
        """[summary] クリック処理（ID指定）

        Args:
            id ([type]): [description]
            IDの名称
        """
        return self.clickEvent(id, None)

    def clickEvent(self,  id=None, className=None):

        # 要素を取得
        element = self.getElement(id, className)

        if element is None:
            return False

        element.click()

        self.sleepTime()
        # print(element)

    def selectSelectBox(self, index=0, id=None, className=None):
        """[summary] セレクトボックスを選択

        Args:
            id ([type], optional): [description]. Defaults to None.
            IDの名称
            className ([type], optional): [description]. Defaults to None.
            クラスの名称
            index (int, optional): [description]. Defaults to 0.
            選択するインデックス
        """
        # ドロップリストの要素を取得
        dropdown = self.getElement(id, className)

        # 要素の取得に失敗
        if dropdown is None:
            return False

        # 対象の値を選択
        select = Select(dropdown)
        select.select_by_index(index)

        self.sleepTime()

        return True

    def sleepTime(self, _time=None):
        """[summary]  スリープ処理

        Args:
            _time ([type], optional): [description]. Defaults to None.
            スリープする指定時間
        """
        if _time is None:
            _time = self.DEFAULT_SLEEP_TIME

        time.sleep(_time)

    def getSouce(self):
        """[summary] ソースを取得

        Returns:
            [type]: [description]
        """
        if self.driver is None:
            return None

        return self.driver.page_source

    def capture(self, path='image', fileName='image.png'):
        """[summary] 現在のWebページをキャプチャする

        Args:
            path (str, optional): [description]. Defaults to 'image'.
            fileName (str, optional): [description]. Defaults to 'image.png'.

        Returns:
            [type]: [description]
        """
        filePath = path + '/' + fileName

        # ウィンドウを指定
        w = self.driver.execute_script("return document.body.scrollWidth;")
        h = self.driver.execute_script("return document.body.scrollHeight;")
        self.driver.set_window_size(w, h)

        self.sleepTime()

        # キャプチャ
        self.driver.save_screenshot(filePath)
