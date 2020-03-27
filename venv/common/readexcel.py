"""
功能描述：读取目标测试数据
解析：
    1-导入xlrd
    2-打开目标excel文件
    3-定位sheet页
    4-读取目标行
        #1-读取全部行数据(读取一行然后循环)
        #2-根据类名和方法名读取需要的数据
    5-返回
"""

# 1 - 导入xlrd
import os

import xlrd

class readExcel(object):

    def __init__(self):
        # 2 - 打开目标excel文件
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +"\\"+"testData" +"\\"+"data.xlsx"
        print(file_path,'path')
        workbook = xlrd.open_workbook(file_path,'r')
        self.data_list = []
        # 3 - 定位sheet页
        self.sheet = workbook.sheet_by_index(0)

    def read(self,classname,methodname):
        # 4 - 读取目标行
        for i in range(1,self.sheet.nrows):
            # # 1-读取全部行数据
            row_value = self.sheet.row_values(i)
            if row_value[1] == classname and row_value[2] == methodname:
                self.data_list.append(self.sheet.row_values(i)[3])
            # # 2-根据类名和方法名读取需要的数据
        # 5 - 返回
        return self.data_list
if __name__ == '__main__':
    re = readExcel()
    #print(re.read())
    print(re.read('HomeTest','test_sousuo2'))