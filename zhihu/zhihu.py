#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass
import getHtml
import mybase
import gzip
from urllib import request
from urllib import parse


import mybase
import re

url = 'http://www.ebd.frank.eyebuy.direct/eyeglasses'
html = mybase.get_url_content(url)
ulInfo = re.compile('<ul class="products-list">.*?<li.*?>(.*?)</li></ul>', re.S)
strlist = re.findall(ulInfo, html)

# liInfo = re.compile('', re.S)
# liIn = re.findall(liInfo, strlist)
print(strlist[0])
# write_info('ebd.txt', strlist)


# 构造 Request headers
headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}

# 使用登录cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")


def get_xsrf():
    '''_xsrf 是一个动态变化的参数'''
    index_url = 'https://www.zhihu.com'
    # 获取登录时需要用到的_xsrf
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    # 这里的_xsrf 返回的是一个list
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]


# 获取验证码
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False


def login(secret, account):
    # 通过输入的用户名判断是否是手机号
    if re.match(r"^1\d{10}$", account):
        print("手机号登录 \n")
        post_url = 'https://www.zhihu.com/login/phone_num'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': secret,
            'remember_me': 'true',
            'phone_num': account,
        }
    else:
        if "@" in account:
            print("邮箱登录 \n")
        else:
            print("你的账号输入有问题，请重新登录")
            return 0
        post_url = 'https://www.zhihu.com/login/email'
        postdata = {
            '_xsrf': get_xsrf(),
            'password': secret,
            'remember_me': 'true',
            'email': account,
        }
    try:
        # 不需要验证码直接登录成功
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = login_page.text
        print(login_page.status_code)
        print(login_code)
    except:
        # 需要输入验证码后才能登录成功
        postdata["captcha"] = get_captcha()
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = eval(login_page.text)
        print(login_code['msg'])
    session.cookies.save()
def getOpener(head):
    # deal with the Cookies
    cj = cookielib.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data

try:
    input = raw_input
except:
    pass


if __name__ == '__main__':
    if isLogin():
        print('您已经登录')
    else:
        account = input('请输入你的用户名\n>  ')
        secret = input("请输入你的密码\n>  ")
        login(secret, account)

postDict={
    '_xsrf':get_xsrf(),
    'phone_num':'13955424735',
    'password':'940221',
    'remember_me':'true'
}
#给post数据编码
postDict["captcha"] = get_captcha()
postData=urllib.parse.urlencode(postDict).encode()

page = request.urlopen('https://www.zhihu.com/login/phone_num', postData).read()
page = page.decode('utf-8')
print(page)

url = 'https://www.zhihu.com'

r = session.get(url, headers = headers)
content = mybase.ungzip(r.content).decode('utf-8');
f = open('github.html', 'wt', encoding= 'utf-8')
f.write(content)
f.close()


'''
登录

对于需要用户登录的网站信息的爬取

'''
import urllib.request,gzip,re,http.cookiejar,urllib.parse
import sys
#解压缩函数
def ungzip(data):
    try:
        print("正在解压缩...")
        data = gzip.decompress(data)
        print("解压完毕...")
    except:
        print("未经压缩，无需解压...")
    return data

#构造文件头
def getOpener(header):
    #设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
    cookieJar = http.cookiejar.CookieJar()
    cp = urllib.request.HTTPCookieProcessor(cookieJar)
    opener = urllib.request.build_opener(cp)
    headers = []
    for key,value in header.items():
        elem = (key,value)
        headers.append(elem)
    opener.addheaders = headers
    return opener

#获取_xsrf
def getXsrf(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"',flags=0)
    strlist = cer.findall(data)
    return strlist[0]

#根据网站报头信息设置headers
headers = {
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate,br',
    'Host': 'www.zhihu.com',
    'DNT':'1'
}

url = "https://www.zhihu.com/"
req=urllib.request.Request(url,headers=headers)
res=urllib.request.urlopen(req)

#读取知乎首页内容，获得_xsrf
data = res.read()
_xsrf = getXsrf(data.decode('utf-8'))

opener = getOpener(headers)
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
url+='login/email'
name='**********'
passwd='*****'

#分析构造post数据
postDict={
    '_xsrf':_xsrf,
    'email':name,
    'password':passwd,
    'remember_me':'true'
}
#给post数据编码
postData=urllib.parse.urlencode(postDict).encode()

#构造请求
res=opener.open(url,postData)
data = res.read()
#解压缩
data = ungzip(data)
print(data.decode())