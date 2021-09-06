class FileRead():
    characterCode = ''

    # 読み込む際の取り除く文字列
    REMOVE_CHAR_LIST = ['"', '\n', '\r\n', '\t']

    # コンフィグファイルを読み込む際の取り除く文字列
    REMOVE_CHAR_LIST_CONFIG = ['"', '\n', '\r\n', '\t']

    # CSVのデータを区切る文字
    CSV_SPLIT_CHAR = '","'

    # configファイルを区切る文字
    CONFIG_SPLIT_CHAR = ' = '

    def __init__(self, _characterCode=None):
        """[summary] 初期処理

        Args:
            _characterCode ([type], optional): [description]. Defaults to None.
        """
        # 文字コードを設定
        if not(_characterCode is None):
            self.characterCode = _characterCode
        else:
            self.characterCode = 'shift_jis'

    def checkReadFile(self, _path=None, _fileName=None):
        """[summary] ファイルを読み込めるのかチェック

        Args:
            _path ([type], optional): [description]. Defaults to None.
            _fileName ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if _path is None:
            return False

        if _fileName is None:
            return False

        return True

    def readConfigFile(self):
        """[summary] configファイルを読み込む
        """
        _config = {}
        f = open('config/config.ini', 'r', encoding=self.characterCode)

        datalist = f.readlines()

        for readLine in datalist:
            if self.checkConfigFileLine(readLine) is False:
                continue

            char = readLine.split(self.CONFIG_SPLIT_CHAR)
            _config[self.removeConfigChar(
                char[0])] = self.removeConfigChar(char[1])
        f.close()

        return _config

    def readTextFile(self, _path=None, _fileName=None):
        """[summary] TXTファイルを読み込む

        Args:
            _path ([type], optional): [description]. Defaults to None.
            _fileName ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if self.checkReadFile(_path, _fileName) is False:
            return None

        readoPath = _fileName if _path is None else _path + '/' + _fileName

        # ファイルオープン
        f = open(readoPath, 'r', encoding=self.characterCode)

        datalist = f.readlines()
        itemList = []

        for readLine in datalist:
            itemList.append(readLine)

        return itemList

    def readCSVFile(self, _path=None, _fileName=None):
        """[summary] CSVファイルを読み込む

        Args:
            _path ([type], optional): [description]. Defaults to None.
            _fileName ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if self.checkReadFile(_path, _fileName) is False:
            return None

        readoPath = _fileName if _path is None else _path + '/' + _fileName

        # ファイルオープン
        f = open(readoPath, 'r', encoding=self.characterCode)

        headerFlg = True
        datalist = f.readlines()
        itemList = []

        for readLine in datalist:

            # ヘッダ
            if headerFlg:
                header = self.makeDictHeader(readLine)
                headerFlg = False
            # 明細行
            else:
                itemList.append(self.makeDictDetail(readLine, header))
        f.close()

        return itemList

    def makeDictHeader(self, readLine: str):
        """[summary] リストのヘッダを取得

        Args:
            readLine (str): [description]

        Returns:
            [type]: [description]
        """
        header = []

        if readLine is None:
            return

        rows = readLine.split('","')

        # ヘッダの文字列を取得
        for row in rows:
            header.append(self.removeChar(row))
        return header

    def makeDictDetail(self, readLine: str, _header):
        """[summary] CSVファイルの明細行のアイテムを作成

        Args:
            readLine (str): [description]
            _header ([type]): [description]

        Returns:
            [type]: [description]
        """
        if not _header:
            return

        if readLine is None:
            return

        rows = readLine.split(self.CSV_SPLIT_CHAR)

        i = 0
        item = {}
        for row in rows:
            item[_header[i]] = self.removeChar(row)
            i = i + 1

        return item

    def removeConfigChar(self, _str: str):
        """[summary] コンフィグファイルで不要な文字を取り除く

        Args:
            _str (str): [description]

        Returns:
            [type]: [description]
        """
        return self.removeChar(_str, self.REMOVE_CHAR_LIST_CONFIG)

    def removeChar(self, _str: str, _removeCharList=[]):
        """[summary] 対象の文字を取り除く

        Args:
            _str (str): [description]

        Returns:
            [type]: [description]
        """
        # 取り除く文字リストが空
        if not _removeCharList:
            _removeCharList = self.REMOVE_CHAR_LIST

        for removeChar in _removeCharList:
            _str = _str.replace(removeChar, '')

        return _str

    def checkConfigFileLine(self, _str: str):
        """[summary] 設定ファイルの設定情報かチェック

        Args:
            _str (str): [description]

        Returns:
            [type]: [description]
        """
        if _str is None:
            return False

        if len(_str) == 0:
            return False

        if _str[0] == '#':
            return False

        if not(' = ' in _str):
            return False

        return True
