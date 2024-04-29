import requests
import webbrowser
import http_vlue as hv

print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("header-level6")

url = 'http://10.68.6.202:'  # 此处应该补充具体的路径
port = input("请输入端口:")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "Chinese",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
if hv.get_qx():
    # 发送带有自定义头部的 GET 请求
    response = requests.get(url + port, headers=headers)
    # 获取响应头部中的密文和密钥
    flag = response.headers.get('ThisFlagIs')
    key = response.headers.get('KeyIs')


    print("密文:",flag)
    print("密钥:",key)
    print("网址:https://the-x.cn/cryptography/Sm4.aspx")
    print("请自行前往网站解密，祝你好运！")
    input("请按回车键继续...")
    #打开网址
    webbrowser.open("https://the-x.cn/cryptography/Sm4.aspx")



else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")