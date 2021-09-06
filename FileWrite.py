class FileWrite():
    NEWLINE_CODE = '\n'

    CHAER_CODE = 'cp932'

    def writeFile(self, list, header, fileName):
        """[summary] 販売中止の商品をファイルに書き込む

        Args:
            list ([type]): [description]
        """
        f = open('file/' + fileName,
                 'w', newline="\n", encoding=self.CHAER_CODE, errors='replace')

        # ヘッダを書き込む
        self.writeHeader(f, header)

        for item in list:
            i = 1
            for key in item:
                if i == len(item):
                    self.writeStrFromat(f, item[key], True)

                else:
                    self.writeStrFromat(f, item[key], False)

                i = i + 1
        f.close()

    def writeHeader(self, f, header):

        i = 1
        for char in header:
            if i == len(header):
                self.writeStrFromat(f, char, True)

            else:
                self.writeStrFromat(f, char, False)

            i = i + 1

    def writeStrFromat(self, f, _str, endFlg=False):
        """[summary]  ファイルに書き込み際のフォーマット指定

        Args:
            f ([type]): [description]
            _str ([type]): [description]
            endFlg (bool, optional): [description]. Defaults to False.
        """
        f.write('"')
        f.write(_str)
        f.write('"')

        if endFlg is False:
            f.write(',')

        else:
            f.write(self.NEWLINE_CODE)
