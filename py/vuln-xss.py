import requests
import base64
import http_vlue as hv

print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("实验4：vuln-xss扫描 ")

url = "http://10.68.6.202:"
dk = input("请输入端口：")

if hv.get_qx():
    fs = requests.get(url + dk)
    flag = fs.headers.get('X-Powered-By')

    # Base64编码
    flag64 = base64.b64encode(flag.encode()).decode()
    if flag64:
        print("已经找到答案：Flag{" + flag64+"}")
        input("请按回车键继续...")
    else:
        print("未找到Flag")
        input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")
