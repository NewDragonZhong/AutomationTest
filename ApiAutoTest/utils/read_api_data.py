import xlrd


class readExcel(object):
    def __init__(self, path):
        self.path = path

    @property
    def getSheet(self):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        return sheet

    @property
    def getRows(self):
        # 获取行数
        row = self.getSheet.nrows
        return row

    @property
    def getCol(self):
        # 获取列数
        col = self.getSheet.ncols
        return col

    # 以下是分别获取每一列的数值
    @property
    def getName(self):
        TestName = []
        for i in range(1, self.getRows):
            TestName.append(self.getSheet.cell_value(i, 0))
        return TestName

    @property
    def getData(self):
        TestData = []
        for i in range(1, self.getRows):
            TestData.append(self.getSheet.cell_value(i, 1))
        return TestData

    @property
    def getUrl(self):
        TestUrl = []
        for i in range(1, self.getRows):
            TestUrl.append(self.getSheet.cell_value(i, 2))
        return TestUrl

    @property
    def getMethod(self):
        TestMethod = []
        for i in range(1, self.getRows):
            TestMethod.append(self.getSheet.cell_value(i, 3))
        return TestMethod

    @property
    def getUid(self):
        TestUid = []
        for i in range(1, self.getRows):
            TestUid.append(self.getSheet.cell_value(i, 4))
        return TestUid

    @property
    def getCode(self):
        TestCode = []
        for i in range(1, self.getRows):
            TestCode.append(self.getSheet.cell_value(i, 5))
        return TestCode


if __name__ == '__main__':
    R = readExcel(r'F:\jingluoAPI\xl\add_thread_data.xlsx')
    print(type(eval(R.getData[0])))
