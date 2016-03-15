# coding=utf-8

import os



caselist = os.listdir("F:\\自动化脚本\\模块\\测试集\\test_case")
for a in caselist:
    s = a.split('.')[1]
    print(s)
    print(a)
    if s == 'py':
        #os.system( 'F:\\自动化脚本\\模块\\测试集\\test_case\\%s 1>>log.txt 2>&1 ' %a)
        os.system( 'F:\\自动化脚本\\模块\\测试集\\test_case\\%s' %a)
