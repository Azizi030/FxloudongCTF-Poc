import requests
import re
import http_vlue as hv
print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("阶段考1-http-header-level6-Dynamic")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "Chinese",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
cookies = {
    "security_level": "0"
}
url = "http://10.68.6.202:"
port = input("请输入端口:")

if hv.get_qx():
    response = requests.get(url+port, headers=headers, cookies=cookies)

    #在响应头取出加密后的flag
    encrypted_flag = response.headers["ThisFlagIs"]

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://139.9.194.250:889",
        "Referer": "http://139.9.194.250:889/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    }
    url = "http://139.9.194.250:889/test.php"
    data = {
        "encrypted_content": f"{encrypted_flag}"
    }
    response = requests.post(url, headers=headers, data=data, verify=False)
    #使用正则表达式匹配flag
    flag = re.search(r"Flag{.*}", response.text).group()
    print("这似乎是你的答案：",flag)
    input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")