
import requests
import re
import http_vlue as hv
print("物智学院CTF平台")
print("课程：漏洞扫描与安全审计")
print("阶段考1-py_dirb3")
port = input("请输入端口:")
url = f"http://10.68.6.202:{port}/product.php"
if hv.get_qx():
    response = requests.get(url)
    flag = re.search(r"Flag{.*}", response.text).group()
    print("这或许是你的答案:",flag)
    input("请按回车键继续...")
else:
    print("失败，原因：权限不足！")
    input("请按回车键继续...")
