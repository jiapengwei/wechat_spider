# coding: utf-8
import os
import sys
from pprint import pprint
sys.path.append(os.getcwd())
from wechatarticles.ReadOutfile import Reader
from wechatarticles import ArticlesAPI

if __name__ == '__main__':
    official_cookie = "pgv_pvi=8721692672; RK=eE41JPwIHX; ptcz=7d0bb1b702f4d819d63b2cd8361f34419281233ef3e4b59e2e9134317a88c55a; ua_id=Q8hBsE5m4TFBuk6hAAAAAFbsyuFQz5bsug2diVDn9W8=; tvfe_boss_uuid=d1bdc2c81eeac198; pgv_pvid=7779098721; rewardsn=; wxtokenkey=777; pgv_si=s451068928; openid2ticket_o0YNqw5lH6lAL7XXGu2pY87cHhdM=bTSs0rM9Z/8dqZhY3QWlkB46uqqbujAmHpg05Z31zfo=; mm_lang=zh_CN; pgv_info=ssid=s5440213129; cert=ehmWUGFO9TefzK0JVmkiGT96na7hpZJw; sig=h0166ad7c77e8cbbae53f370f0295054a9b8443e24630aadd68a34e4125c4b9b2d0fa327ca9f476fb2c; master_key=/exV/mPf9gpV69wzzCdRmAwX/nxQHfhL+OINYyzMd60=; openid2ticket_oq8P1t9h_lQR6RPKcNMaVCkp0CDg=B8kuhYr4KFAK7YAeerkNzxlUMgi3lx9OBn6S1WwEz2U=; uuid=e2b5dc9870ad37a471859abb0cc1d6f7; rand_info=CAESIDJcGwN2hvX8ETW1PweF0wNrTIMIt/9GMpxtzWOTSnmZ; slave_bizuin=3086336939; data_bizuin=3086336939; bizuin=3086336939; data_ticket=RW+bihhmzAJRPCWaz1sd+tzfGPjbkns7Rpsrk9F63XI5Jrh4XuLz0ipkvaDz2xZq; slave_sid=SGJNc3ozcWNNd1psMWdIWDBHQldJenNTNTJWejQ4NWRfcGVaSjJMdkJWVENKVEFHZEs4QUhwd0RtOEtISDVXQmFfUUhlcEJLOVFyQUdtNDdiT0xXN1Y2cEs2WktmQlRVZUU1OFFyRnZHX1lmRG13UFliWllid2NHWWIxYWJZdWNLV2ZIVWdleFFsb0NZdFFt; slave_user=gh_b74b90425603; xid=156e920bb16374cfc5035e02f4ec552"
    token = "1395357689"
    appmsg_token = "1053_b4r%2B%2FZI69esVhynGWI5rk5JKfrwMUoMmbdxmf6TM-J3LDaAXj-SLi-Rs3VrrowYVI2u502pOf4Xf0ECv"
    wechat_cookie = "rewardsn=; wxtokenkey=777; wxuin=1571052916; devicetype=Windows10; version=62080079; lang=zh_CN; pass_ticket=DQjCGEzvqpriOSW8W1/h+yZUrW2i7pix+cBfM1DniEJE4UEImBC0CLG5E77Jw9ri; wap_sid2=CPS6ke0FElx3ZXc1N1o4c3BzdmVrM2xrNHNFQTM1U3ZTYlhEMURabks0OGd4dkRDLVl4OGtVdDV2LW5MM0U0UUY4Q2VrMU1GZ3BueWxzc2ozMkxxODd5b3Uyc1g5UjBFQUFBfjCegtbzBTgNQAE="

    nickname = "西安工业大学图书馆"

    # 手动输入所有参数
    test = ArticlesAPI(
        official_cookie=official_cookie,
        token=token,
        appmsg_token=appmsg_token,
        wechat_cookie=wechat_cookie)

    # 自定义爬取，每次爬取5篇以上
    data = test.complete_info(nickname=nickname, begin="0")
    print(data.__len__())
    pprint(data)