import requests
import re
import http_vlue as hv
print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验4:XSS挑战 ")

url = 'http://10.68.6.202:'
port = input("请输入端口:")
uurl = '/flag/flag_fswerfadfdasiuadif132090'

headers = {
    'User-Agent': 'opera/1.0 (Windows NT 6.1; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
}
if hv.get_qx():
    # 提交 GET 请求
    response = requests.get(url + port+uurl, headers=headers)

    # 从响应文本中查找 Flag
    flag_match = re.search(r'Flag\{([\w-]+)\}', response.text)
    if flag_match:
        flag = flag_match.group(1).strip()
        print("这个似乎是答案：", "Flag{" + flag + "}")
        input("请按回车键继续...")
    else:
        print("未找到 Flag。")
        input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")