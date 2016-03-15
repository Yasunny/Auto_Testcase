
# -*- coding: utf-8 -*-
import urllib,json
from urllib import urlencode
def main():
    #参数顺序：订单号，商品id，加油卡类型，充值数量，加油卡卡号，持卡人姓名，持卡人手机号码
    jiayouka = Jiayouka("jtest12340","64127500","1", "1", "10001132000099****", "董好帅", "1891351****")
    result = jiayouka.query()
    if result:
        error_code = result['error_code']
        if error_code == 0:
            """
                "cardnum": "100", /*充值金额*/
                "ordercash": "95.5", /*进货价格*/
                "cardname": "全国加油卡", /*充值名称*/
                "sporder_id": "S20141125221812330", /*商家订单号*/
                "game_userid": "100011320000991****", /*加油卡卡号*/
                "game_state": "0", /*充值状态:0充值中 1成功 9撤销*/
                "uorderid": "S2014111111115" /*商户自定的订单号*/
            """

            #以下充值成功后的业务逻辑请自行修改
            sporder_id = result['result']['sporder_id']
            ordercash = result['result']['ordercash']

            print("充值成功")
        else:
            print( result['reason'],"(",result['error_code'],")")
    else:
        print( "提交充值失败，请重试")

class Jiayouka:

    url = 'http://op.juhe.cn/ofpay/sinopec/onlineorder' #充值接口地址

    key = 'c5cf1fe0a8771c0d3f************' #申请的加油卡充值appkey

    openid = 'JH8d954266539f8af***********' #Openid，在个人中心查看

    orderid = '' #用户自定单号，8－32位字母、数字组合

    proid = '' #产品id:10000(中石化50元加油卡)、10001(中石化100元加油卡)、10003(中石化500元加油卡)、10004(中石化1000元加油卡)、10007(中石化任意金额充值)、10008(中石油任意金额充值)

    cardnum = '1' #充值数量 任意充 （整数（元）），其余面值固定值为1

    gameuserid = '' #加油卡卡号

    mobilephone = '' #持卡人手机号码

    realname = '' #持卡人姓名

    itype = '' #加油卡类型 （1:中石化、2:中石油；默认为1)

    def __init__(self,iorderid,icardid,itype,icardnum,igameuserid,irealname,imobilephone):
        self.orderid = iorderid
        self.cardid = icardid
        self.cardnum = icardnum
        self.gameuserid = igameuserid
        self.realname = irealname
        self.mobilephone = imobilephone
        self.type = itype

    def query(self):
        signsource = self.openid+self.key+self.proid+self.cardnum+self.gameuserid+self.orderid
        m = md5.new()
        m.update(signsource)
        sign = m.hexdigest()

        params = {"key":self.key,"orderid":self.orderid,"chargeType":self.type,"proid":self.proid,"cardnum":self.cardnum,"game_userid":self.gameuserid,"gasCardTel":self.mobilephone,"gasCardName":self.realname,"sign":sign}
        params = urlencode(params)
        print( params)

        fullurl = self.url+'?'+params

        wp = urllib.urlopen(fullurl)
        content = wp.read()
        res = json.loads(content)
        if res:
            return res
        else:
            return False

if __name__ == '__main__':
    main()