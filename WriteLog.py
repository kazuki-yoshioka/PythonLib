import os
from datetime import date, datetime
import time
import shutil
from typing import Text


class WriteLog():

    # ログのファイル名
    __FILE_NAME = 'app'

    # ログファイルの拡張子
    __FILE_EXTENSION = '.log'

    # ログを出力するディレクトリ
    __DIR_NAME = 'log'

    # 改行コード
    __NEWLINE_CODE = '\n'

    # 文字コード
    __CHAER_CODE = 'cp932'

    # ログのファイルパス
    __LOG_FILE_PATH = __DIR_NAME + '/' + __FILE_NAME + __FILE_EXTENSION

    def __init__(self):
        """[summary] 初期処理
        """
        if not os.path.exists(self.__DIR_NAME):
            # ディレクトリが存在しない場合、ディレクトリを作成する
            os.makedirs(self.__DIR_NAME)

        # 出力されているログファイルは本日出力されたものかチェック
        if not self.__isTodayLogFile():
            # ファイルをリネイム
            self.__renameLogFile()

        # ログファイルを出力
        if self.__isExistsLogFile() is False:
            # ログファイルを出力
            print('')

    def __isExistsLogFile(self):
        """[summary] ログファイルが存在しているのチェック

        Returns:
            [type]: [description]
        """
        if os.path.exists(self.__LOG_FILE_PATH):
            return True
        return False

    def __isTodayLogFile(self):
        """[summary] 出力されているログファイルは本日のものかチェック
        """
        # ログファイルが存在していない
        if self.__isExistsLogFile() is False:
            return False

        # ログファイルの更新日付を取得
        logDate = date(
            *time.localtime(os.path.getctime(self.__LOG_FILE_PATH))[:3])

        # 現在日付を取得
        today = self.getToday()

        # TODAYが後日付
        if self.comparisonDate(today, logDate) == 1:
            return False

        return True

    def __renameLogFile(self):
        """[summary] ファイルをリネイム
        """
        # ファイルが存在していない
        if self.__isExistsLogFile() is False:
            return

        # 更新日付を取得
        logDate = date(
            *time.localtime(os.path.getctime(self.__LOG_FILE_PATH))[:3])

        # リネイムするファイル名を設定
        renameLogFileName = self.__FILE_NAME + \
            + '_' + str(logDate) + self.__FILE_EXTENSION

        # リネイムしたファイルのパス
        renameLogFilePath = self.__DIR_NAME + renameLogFileName

        # ファイルをコピー
        shutil.rename(self.__LOG_FILE_PATH, renameLogFilePath)

    def getToday(self):
        return date.today()

    def getTime(self):
        now = datetime.today()

        hour = str(now.hour).zfill(2)
        minute = str(now.minute).zfill(2)
        second = str(now.second).zfill(2)

        return hour + '-' + minute + '-' + second

    def comparisonDate(self, date1, date2):
        """[summary] 日付を比較
        0: 同一日付
        1: date1が後日付
        2: date2が後日付
        -1: 異常終了

        Args:
            date1 ([type]): [description]
            date2 ([type]): [description]

        Returns:
            [type]: [description]
        """
        nDate1 = {}
        nDate2 = {}

        try:
            nDate1 = time.strptime(date1, '%d/%m/%Y')
            nDate2 = time.strptime(date2, '%d/%m/%Y')

        except Exception as e:
            print(e)
            return -1

        # 同一日付
        if nDate1 == nDate2:
            return 0

        # date1が後日付
        if nDate1 > nDate2:
            return 1

        return 2

    def makeFirstLogFile(self):
        open(self.__LOG_FILE_PATH,
             'w', newline="\n", encoding=self.__CHAER_CODE, errors='replace')

    def writeLog(self, mode='e', text=''):
        """[summary] ログファイルに書き込む

        Args:
            mode (str, optional): [description]. Defaults to 'e'.
            text (str, optional): [description]. Defaults to ''.
        """
        f = open(self.__LOG_FILE_PATH,
                 'a', newline="\n", encoding=self.__CHAER_CODE, errors='replace')

        try:
            # ファイルに書き込む
            f.write(self.__getWriteLogDateTime() + ' ***  ' +
                    self.__getTextByMode(mode=mode) + ' : ' + text + '\n')

        except Exception as e:
            print(e)
        finally:
            f.close

    def __getWriteLogDateTime(self):
        """[summary] ログに書き込む日時を取得

        Returns:
            [type]: [description]
        """
        today = self.getToday()
        time = self.getTime()

        return str(today) + ' : ' + str(time)

    def __getTextByMode(self, mode='e'):
        # エラーログの種類を返却
        if mode == 'e':
            return 'error'

        if mode == 'w':
            return 'warning'

        if mode == 'd':
            return 'debug'

        return 'None'


class ExeLog():
    @staticmethod
    def writeLog(mode='e', text=''):
        wl = WriteLog()
        wl.writeLog(mode=mode, text=text)


ExeLog().writeLog(mode='e', text='エラーログ')
ExeLog().writeLog(mode='w', text='ワーニングログ')
