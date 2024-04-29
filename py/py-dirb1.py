import http_vlue as hv
import requests
import re


print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验3：py-dirb1目录扫描")

# 目标URL
url = 'http://10.68.6.202'
port = input('请输入端口：')
endpoint = "/get_dirb1_flag_xdijkhdjkfj.php"

if hv.get_qx():
    # 发送带有Payload的GET请求
    response = requests.get(f'{url}:{port}{endpoint}')

    # 使用正则表达式提取flag
    flag_pattern = r'Flag\{([\w-]+)\}'
    match = re.search(flag_pattern, response.text)

    # 检查是否匹配到flag
    if match:
        print("这个似乎是你的答案：", "Flag{"+match.group(1)+"}")
        input("请按回车键继续...")
    else:
        print("未找到Flag")
        input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")

