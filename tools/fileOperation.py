# -*- coding:utf-8 -*-


import os


def newFile(reportPath):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(reportPath)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(reportPath+'/'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(reportPath,lists[-1])
#    L=file_path.split('\\')
#    file_path='\\\\'.join(L)
    return file_path



def openFile(newPath):
    ret = True
    try:
        with open(newPath,'rb') as f :
            reportText = f.read().decode('utf-8')
            return reportText
    except:
        ret = False
        return ret






# file = newFile("/Users/chenhang/Desktop/pythonFile/python/untitled/practice/三角形判断/report")
# print(file)
#
# fileText = openFile(file)
# if fileText:
#     print(fileText)
# else:
#     print("文件读取错误")