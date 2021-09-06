
class UtilityCheck():
    """[Utilityクラス]
    ・チェック処理を実施する
    """

    def __init__(self):
        print("チェック処理")

    @staticmethod
    def isNone(value):
        """[nullチェック]
        """
        if value is None:
            return True

        return False

    @staticmethod
    def typeIsStr(value):
        """[型チェック　string]
        """
        if UtilityCheck.isNone(value):
            return False

        if type(value) is str:
            return True

        return False

    @staticmethod
    def typeIsInt(value):
        """[型チェック　int]
        """
        if UtilityCheck.isNone(value):
            return False

        if type(value) is int:
            return True

        return False

    @staticmethod
    def isEmpty(_str):
        """[summary] 空文字チェック

        Args:
            _str ([type]): [description]

        Returns:
            [type]: [description]
        """
        if False is UtilityCheck.typeIsStr(_str):
            return False

        if len(_str) == 0:
            return False

        return True
