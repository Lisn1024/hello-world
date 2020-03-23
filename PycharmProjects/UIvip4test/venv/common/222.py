'''
1.导入读取Excel包
2.打开目标文件
3.定位sheet页
4.定位行和列
5.读取数据
6.组装数据
7.return给需要数据的地方
'''
# 1.导入读取Excel包
import xlrd

class getExcelData(object):
    def __init__(self):

# 2.打开目标文件
        readbook = xlrd.open_workbook(r'D:\users\wb.lishengnan\PycharmProjects\vip4_interfaceTest\testData\data.xls')
        # print(readbook)
# 3.定位sheet页
        self.urlsheet = readbook.sheet_by_name('urlSheet')
        self.urlNum = self.urlsheet.nrows

        self.paramsheet = readbook.sheet_by_name('paramSheet')
        self.paramNum = self.paramsheet.nrows
        self.assertsheet = readbook.sheet_by_name('assertSheet')
        self.assertNum = self.assertsheet.nrows

# 4.循环定位所有的行或列的内容
# 5.读取数据
    def getSheetData(self,num,sheetName):
        data = []
        for i in range(1,num):
            sheetdata = sheetName.row_values(i)

            data.append(sheetdata)
        return data

# 6.组装数据
    def assembleData(self):
        urllist = self.getSheetData(self.urlNum,self.urlsheet)
        paramlist = self.getSheetData(self.paramNum,self.paramsheet)
        assertlist = self.getSheetData(self.assertNum,self.assertsheet)
        datalist = []
        for i in range(len(urllist)):
            new_urllist = urllist[i]
            new_paramlist = paramlist[i][1:]
            new_assertlist = assertlist[i][1:]
            new_urllist.append(new_paramlist)
            new_urllist.append(new_assertlist)
            # print(new_urllist)
            datalist.append(new_urllist)
        return datalist

if __name__ == '__main__':
    getData = getExcelData()
    print(getData.assembleData())




