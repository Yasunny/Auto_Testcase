#coding=utf-8

import unittest
import BaiDuSearch,BaiDuYunPanLogin
#导入测试用例
testunit=unittest.TestSuite()#建立测试套件

testunit.addTest(unittest.makeSuite(BaiDuSearch.TestCase1))
testunit.addTest(unittest.makeSuite(BaiDuYunPanLogin.BaiDuYunPan))
#将测试用例添加到测试套件

runner=unittest.TextTestRunner()
runner.run(testunit)

#执行测试套件

#定义测试报告存放路径
'''filename='F:\\selenium_python\\report\\report.html'
fp=open(filename,"wb")

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'python search report',
    description=u'testcase relation')

runner.run(testunit)'''
