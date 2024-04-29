import requests
import re
import http_vlue as hv

print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("header-level3")

url = 'http://10.68.6.202:'
port = input("请输入端口:")

headers = {
    'Content-Type': 'text/html; charset=utf-8',
	'X-Powered-By': 'Powered By Six-God'
}
if hv.get_qx():
    # 提交 POST 请求
    response = requests.post(url + port, headers=headers)
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